#!/usr/bin/env python3
"""Policy-driven multi-domain loop orchestrator for Mistral Vibe Code."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AGENT_BY_PROFILE = {
    "research": "rb-researcher",
    "software": "rb-builder",
    "experience": "xp-builder",
    "compliance": "lo-compliance",
    "finance": "lo-compliance",
    "growth": "lo-growth",
    "operations": "lo-operator",
    "ai": "lo-ai",
}

VERIFICATION_WORDS = {"verify", "verification", "audit", "review", "approve", "approval", "qa", "test", "reconcile"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def load_catalog(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    reasons = validate_catalog(payload)
    if reasons:
        raise ValueError("Invalid loop catalog: " + "; ".join(reasons))
    return payload


def validate_catalog(catalog: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    loops = catalog.get("loops", [])
    identifiers = [item.get("id") for item in loops]
    duplicates = sorted({item for item in identifiers if item and identifiers.count(item) > 1})
    if duplicates:
        reasons.append("Duplicate loop IDs: " + ", ".join(duplicates))
    known = set(identifiers)
    allowed_risks = {"low", "medium", "high", "critical"}
    for item in loops:
        loop_id = item.get("id", "<missing>")
        required = ("name", "domain", "purpose", "trigger", "cadence", "risk", "profile", "stages")
        missing = [field for field in required if item.get(field) in (None, "", [])]
        if missing:
            reasons.append(f"{loop_id} missing: {', '.join(missing)}")
        if item.get("risk") not in allowed_risks:
            reasons.append(f"{loop_id} has invalid risk")
        if item.get("profile") not in AGENT_BY_PROFILE:
            reasons.append(f"{loop_id} has unknown profile")
        stages = item.get("stages", [])
        if len(stages) < 3 or len(stages) != len(set(stages)):
            reasons.append(f"{loop_id} needs at least three unique stages")
        for target in item.get("handoff_to", []):
            if target not in known:
                reasons.append(f"{loop_id} has unknown handoff target {target}")
    return reasons


def select_agent(loop: dict[str, Any], stage: str) -> str:
    words = set(stage.replace("-", " ").split())
    if words & VERIFICATION_WORDS:
        return "lo-verifier"
    return AGENT_BY_PROFILE[loop["profile"]]


def run_root(project: Path, loop_id: str, run_id: str) -> Path:
    return project / ".loop-os" / loop_id / run_id


def stage_path(root: Path, order: int, stage: str) -> Path:
    return root / "stages" / f"{order:02d}-{stage}.json"


def approval_status(root: Path) -> dict[str, Any]:
    path = root / "approvals.json"
    return read_json(path) if path.exists() else {"approvals": []}


def validate_stage(path: Path, loop: dict[str, Any], stage: str, policy: dict[str, Any]) -> list[str]:
    if not path.exists():
        return [f"Missing stage artifact: {path.name}"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "COMPLETE":
        reasons.append(f"{stage} status is not COMPLETE")
    required = policy["completion"]["required_stage_fields"]
    for field in required:
        if field not in payload or (field != "next_stage" and payload.get(field) in (None, "", [])):
            reasons.append(f"{stage} missing {field}")
    if payload.get("loop_id") != loop["id"] or payload.get("stage") != stage:
        reasons.append(f"{stage} identity does not match requested loop")
    failed = [gate.get("id", "unknown") for gate in payload.get("gates", []) if gate.get("status") != "passed"]
    reasons.extend(f"{stage} gate did not pass: {gate}" for gate in failed)
    if payload.get("unresolved_blockers"):
        reasons.append(f"{stage} contains unresolved blockers")
    return reasons


def validate_run(root: Path, loop: dict[str, Any], policy: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    for order, stage in enumerate(loop["stages"], 1):
        reasons.extend(validate_stage(stage_path(root, order, stage), loop, stage, policy))
    approvals = {item.get("id"): item.get("status") for item in approval_status(root).get("approvals", [])}
    for required in loop.get("human_approvals", []):
        if approvals.get(required) != "approved":
            reasons.append(f"Required human approval is missing: {required}")
    if loop["risk"] in policy["approval"]["risk_levels_requiring_final_approval"]:
        if approvals.get("final-release") != "approved":
            reasons.append("Required human approval is missing: final-release")
    return sorted(set(reasons))


def create_run(project: Path, loop: dict[str, Any], inputs: Path | None) -> tuple[str, Path]:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    root = run_root(project, loop["id"], run_id)
    root.mkdir(parents=True, exist_ok=False)
    input_record: dict[str, Any] | None = None
    if inputs:
        target = root / "inputs" / inputs.name
        target.parent.mkdir(parents=True)
        shutil.copy2(inputs, target)
        input_record = {"path": str(target.relative_to(project)), "sha256": sha256(target)}
    write_json(root / "run.json", {
        "version": 1,
        "run_id": run_id,
        "loop_id": loop["id"],
        "status": "initialized",
        "created_at": now(),
        "input": input_record,
        "stages": {stage: {"status": "pending", "attempts": 0} for stage in loop["stages"]},
    })
    write_json(root / "approvals.json", {"approvals": []})
    return run_id, root


def latest_run(project: Path, loop_id: str) -> Path:
    parent = project / ".loop-os" / loop_id
    candidates = sorted((item for item in parent.iterdir() if item.is_dir()), reverse=True) if parent.exists() else []
    if not candidates:
        raise ValueError(f"No runs exist for {loop_id}")
    return candidates[0]


def build_prompt(project: Path, root: Path, loop: dict[str, Any], stage: str, order: int) -> str:
    output = stage_path(root, order, stage)
    return f"""Execute Loop OS stage `{stage}` for loop `{loop['id']}`.
Purpose: {loop['purpose']}
Risk: {loop['risk']}
Project: {project}
Run directory: {root}
Required output: {output}

Read AGENTS.md, .vibe/skills/loop-os/SKILL.md, the loop catalog entry, run.json, immutable inputs, prior stage artifacts, and applicable approved ResearchBuild and ExperienceBuild artifacts. Research material claims from primary sources when needed. Never invent evidence, legal applicability, credit-report facts, client consent, test results, financial qualification, credentials, or deployment status.

Write one JSON object containing: version, loop_id, stage, status, completed_at, objective, inputs_used, evidence, decisions, outputs, gates, metrics, risks, unresolved_blockers, next_stage, and handoff. Every gate must have id, status, and evidence. Use status BLOCKED with precise unresolved_blockers whenever facts, permission, approval, credentials, evidence, or tests are missing. Do not perform production deployment, transmit disputes or legal notices, apply for credit, submit grants, send marketing messages, move money, delete data, or contact third parties without the required human approval.
"""


def call_agent(project: Path, root: Path, loop: dict[str, Any], stage: str, order: int, policy: dict[str, Any], attempt: int) -> int:
    executable = shutil.which(policy["automation"].get("vibe_command", "vibe"))
    if not executable:
        raise RuntimeError("Vibe executable was not found")
    agent = select_agent(loop, stage)
    log = root / "logs" / f"{order:02d}-{stage}-attempt-{attempt}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    args = [executable, "--trust", "--workdir", str(project), "--agent", agent, "--prompt", build_prompt(project, root, loop, stage, order)]
    with log.open("w", encoding="utf-8", newline="\n") as handle:
        return subprocess.run(args, cwd=project, stdout=handle, stderr=subprocess.STDOUT, text=True, check=False).returncode


def execute(project: Path, root: Path, loop: dict[str, Any], policy: dict[str, Any], selected_stage: str) -> int:
    state_path = root / "run.json"
    state = read_json(state_path)
    stages = loop["stages"] if selected_stage == "all" else [selected_stage]
    maximum = int(policy["automation"].get("maximum_stage_attempts", 3))
    for stage in stages:
        order = loop["stages"].index(stage) + 1
        prior = loop["stages"][: order - 1]
        incomplete = [item for item in prior if state["stages"][item]["status"] != "passed"]
        if incomplete:
            print(json.dumps({"status": "BLOCKED", "stage": stage, "reasons": [f"Prerequisite has not passed: {item}" for item in incomplete]}, indent=2))
            return 2
        current = state["stages"][stage]
        while current["attempts"] < maximum and current["status"] != "passed":
            current["attempts"] += 1
            current["status"] = "running"
            write_json(state_path, state)
            code = call_agent(project, root, loop, stage, order, policy, current["attempts"])
            reasons = validate_stage(stage_path(root, order, stage), loop, stage, policy)
            if code != 0:
                reasons.append(f"Vibe exited with code {code}")
            current["status"] = "passed" if not reasons else "blocked"
            current["reasons"] = reasons
            current["completed_at"] = now()
            write_json(state_path, state)
        if current["status"] != "passed":
            print(json.dumps({"status": "BLOCKED", "stage": stage, "reasons": current.get("reasons", [])}, indent=2))
            return 2
    reasons = validate_run(root, loop, policy) if selected_stage == "all" else []
    state["status"] = "COMPLETE" if selected_stage == "all" and not reasons else ("BLOCKED" if reasons else "IN_PROGRESS")
    state["reasons"] = reasons
    state["updated_at"] = now()
    write_json(state_path, state)
    print(json.dumps({"status": state["status"], "loop_id": loop["id"], "run_id": state["run_id"], "reasons": reasons}, indent=2))
    return 0 if not reasons else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "describe", "init", "approve", "run", "verify"))
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--loop")
    parser.add_argument("--run-id")
    parser.add_argument("--stage", default="all")
    parser.add_argument("--inputs", type=Path)
    parser.add_argument("--approval")
    parser.add_argument("--approver")
    parser.add_argument("--note")
    args = parser.parse_args()
    project = args.project.resolve()
    catalog_path = args.catalog.resolve() if args.catalog else project / "loop-catalog.json"
    policy_path = args.policy.resolve() if args.policy else project / "loop-policy.json"
    catalog = load_catalog(catalog_path)
    loops = {item["id"]: item for item in catalog["loops"]}
    if args.command == "list":
        print(json.dumps({"loops": [{key: item[key] for key in ("id", "name", "domain", "purpose", "trigger", "cadence", "risk")} for item in catalog["loops"]]}, indent=2))
        return 0
    if not args.loop or args.loop not in loops:
        raise ValueError("--loop must name a loop from the catalog")
    loop = loops[args.loop]
    if args.command == "describe":
        print(json.dumps(loop, indent=2))
        return 0
    policy = read_json(policy_path)
    if args.command == "init":
        run_id, root = create_run(project, loop, args.inputs.resolve() if args.inputs else None)
        print(json.dumps({"status": "INITIALIZED", "loop_id": loop["id"], "run_id": run_id, "path": str(root)}, indent=2))
        return 0
    root = run_root(project, loop["id"], args.run_id) if args.run_id else latest_run(project, loop["id"])
    if args.command == "approve":
        if not args.approval or not args.approver:
            raise ValueError("approve requires --approval and --approver")
        payload = approval_status(root)
        payload["approvals"] = [item for item in payload.get("approvals", []) if item.get("id") != args.approval]
        payload["approvals"].append({
            "id": args.approval,
            "status": "approved",
            "approver": args.approver,
            "approved_at": now(),
            "note": args.note or "",
        })
        write_json(root / "approvals.json", payload)
        print(json.dumps({"status": "APPROVED", "loop_id": loop["id"], "approval": args.approval, "approver": args.approver}, indent=2))
        return 0
    if args.command == "verify":
        reasons = validate_run(root, loop, policy)
        print(json.dumps({"status": "COMPLETE" if not reasons else "BLOCKED", "reasons": reasons}, indent=2))
        return 0 if not reasons else 2
    if args.stage != "all" and args.stage not in loop["stages"]:
        raise ValueError("--stage must be all or a stage from the selected loop")
    return execute(project, root, loop, policy, args.stage)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(1)
