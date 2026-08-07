#!/usr/bin/env python3
"""Fail-closed research-to-production orchestration for Mistral Vibe Code."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PHASES = (
    "intake",
    "research",
    "requirements",
    "architecture",
    "threat-model",
    "implementation",
    "verification",
    "delivery",
)

PHASE_ARTIFACTS = {
    "intake": ["intake.json"],
    "research": ["evidence.json", "research-report.md"],
    "requirements": ["requirements.json"],
    "architecture": ["architecture.json"],
    "threat-model": ["threat-model.json"],
    "implementation": ["implementation-report.json"],
    "verification": ["verification.json"],
    "delivery": ["delivery-report.md"],
}

HANDOFF_INPUTS = tuple(
    artifact
    for phase in PHASES
    for artifact in PHASE_ARTIFACTS[phase]
)

PHASE_AGENTS = {
    "intake": "rb-planner",
    "research": "rb-researcher",
    "requirements": "rb-planner",
    "architecture": "rb-architect",
    "threat-model": "rb-security",
    "implementation": "rb-builder",
    "verification": "rb-verifier",
    "delivery": "rb-verifier",
}


@dataclass
class GateResult:
    passed: bool
    reasons: list[str]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    temporary.replace(path)


def project_paths(project: Path) -> tuple[Path, Path]:
    control = project / ".research-build"
    return control, control / "state.json"


def initialize(project: Path, spec: Path | None, kit_root: Path) -> None:
    project.mkdir(parents=True, exist_ok=True)
    control, state_path = project_paths(project)
    control.mkdir(parents=True, exist_ok=True)

    for name in (".vibe", "AGENTS.md"):
        source = kit_root / name
        target = project / name
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        elif not target.exists():
            shutil.copy2(source, target)

    policy_target = project / "research-build-policy.json"
    if not policy_target.exists():
        shutil.copy2(kit_root / "policy.example.json", policy_target)

    experience_policy = project / "experience-build-policy.json"
    if not experience_policy.exists():
        shutil.copy2(kit_root / "experience-policy.example.json", experience_policy)

    experience_runner = project / "experience_build.py"
    if not experience_runner.exists():
        shutil.copy2(kit_root / "experience_build.py", experience_runner)

    for source_name, target_name in (
        ("loop_os.py", "loop_os.py"),
        ("loop-catalog.json", "loop-catalog.json"),
        ("loop-policy.example.json", "loop-policy.json"),
        ("loop-schedules.example.json", "loop-schedules.json"),
    ):
        target = project / target_name
        if not target.exists():
            shutil.copy2(kit_root / source_name, target)

    target_templates = project / "templates"
    target_templates.mkdir(exist_ok=True)
    for name in ("PAGE_INVENTORY_GUIDE.md", "LEGAL_FACT_INTAKE.md", "SEARCH_BUILD_MATRIX.md", "LOOP_PORTFOLIO.md"):
        shutil.copy2(kit_root / "templates" / name, target_templates / name)

    spec_target = project / "BUILD_SPEC.md"
    if spec:
        shutil.copy2(spec.resolve(), spec_target)
    elif not spec_target.exists():
        shutil.copy2(kit_root / "templates" / "BUILD_SPEC.md", spec_target)

    state = {
        "version": 1,
        "status": "initialized",
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "spec_sha256": sha256(spec_target),
        "phases": {phase: {"status": "pending", "attempts": 0} for phase in PHASES},
    }
    write_json(state_path, state)
    print(f"Initialized ResearchBuild Loop in {project}")


def phase_prompt(project: Path, phase: str) -> str:
    artifacts = ", ".join(PHASE_ARTIFACTS[phase])
    return f"""
Execute only the ResearchBuild phase: {phase}.

Project root: {project}
Read AGENTS.md, BUILD_SPEC.md, research-build-policy.json, and all completed artifacts in .research-build before acting.
Required outputs for this phase: {artifacts}.

Use the research-build Skill. Follow the required schemas and phase gates. Inspect actual sources and actual command results. Do not fabricate evidence or results. Do not perform production deployment or destructive operations. If required information is unavailable or a gate cannot pass, still write the phase artifact with status BLOCKED and explicit blocking reasons. Never claim COMPLETE unless the evidence and checks support it.
""".strip()


def run_vibe(project: Path, phase: str, policy: dict[str, Any], log_path: Path) -> int:
    command = policy["automation"].get("vibe_command", "vibe")
    executable = shutil.which(command)
    if not executable:
        raise RuntimeError(f"Vibe executable not found: {command}")
    args = [
        executable,
        "--trust",
        "--workdir",
        str(project),
        "--agent",
        PHASE_AGENTS[phase],
        "--prompt",
        phase_prompt(project, phase),
    ]
    with log_path.open("w", encoding="utf-8", newline="\n") as log:
        process = subprocess.run(args, cwd=project, stdout=log, stderr=subprocess.STDOUT, text=True, check=False)
    return process.returncode


def validate_evidence(control: Path, policy: dict[str, Any]) -> GateResult:
    reasons: list[str] = []
    path = control / "evidence.json"
    if not path.exists():
        return GateResult(False, ["Missing evidence.json"])
    try:
        payload = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return GateResult(False, [f"Invalid evidence.json: {exc}"])
    sources = payload.get("sources", []) if isinstance(payload, dict) else []
    if payload.get("status") != "COMPLETE":
        reasons.append("Evidence phase status is not COMPLETE")
    if not isinstance(sources, list):
        return GateResult(False, ["evidence.json sources must be an array"])
    counts = {"official": 0, "paper": 0, "repository": 0, "standard": 0}
    seen_urls: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            reasons.append(f"Evidence item {index} is not an object")
            continue
        missing = [field for field in ("id", "title", "url", "source_type", "accessed_at", "claims") if not source.get(field)]
        if missing:
            reasons.append(f"Evidence item {index} missing: {', '.join(missing)}")
        url = source.get("url", "")
        if url in seen_urls:
            reasons.append(f"Duplicate evidence URL: {url}")
        seen_urls.add(url)
        source_type = source.get("source_type")
        if source_type in counts:
            counts[source_type] += 1
        if not isinstance(source.get("claims"), list) or not source.get("claims"):
            reasons.append(f"Evidence item {index} has no supported claims")
    settings = policy["research"]
    minimums = {
        "total": (len(sources), settings["minimum_total_sources"]),
        "official": (counts["official"], settings["minimum_official_sources"]),
        "paper": (counts["paper"], settings["minimum_papers"]),
        "repository": (counts["repository"], settings["minimum_repositories"]),
        "standard": (counts["standard"], settings["minimum_standards"]),
    }
    for label, (actual, required) in minimums.items():
        if actual < required:
            reasons.append(f"Insufficient {label} evidence: {actual} < {required}")
    return GateResult(not reasons, reasons)


def validate_requirements(control: Path) -> GateResult:
    reasons: list[str] = []
    evidence_ids: set[str] = set()
    evidence_path = control / "evidence.json"
    if evidence_path.exists():
        evidence_ids = {item.get("id") for item in load_json(evidence_path).get("sources", []) if isinstance(item, dict)}
    path = control / "requirements.json"
    if not path.exists():
        return GateResult(False, ["Missing requirements.json"])
    try:
        payload = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return GateResult(False, [f"Invalid requirements.json: {exc}"])
    requirements = payload.get("requirements", []) if isinstance(payload, dict) else []
    if payload.get("status") != "COMPLETE":
        reasons.append("Requirements phase status is not COMPLETE")
    if not requirements:
        reasons.append("No requirements recorded")
    ids: set[str] = set()
    for index, item in enumerate(requirements):
        if not isinstance(item, dict):
            reasons.append(f"Requirement {index} is not an object")
            continue
        requirement_id = item.get("id")
        if not requirement_id:
            reasons.append(f"Requirement {index} has no ID")
        elif requirement_id in ids:
            reasons.append(f"Duplicate requirement ID: {requirement_id}")
        ids.add(requirement_id)
        for field in ("statement", "acceptance_criteria", "test_ids", "evidence_ids", "risk"):
            if not item.get(field):
                reasons.append(f"Requirement {requirement_id or index} missing {field}")
        for evidence_id in item.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                reasons.append(f"Requirement {requirement_id} references unknown evidence {evidence_id}")
    return GateResult(not reasons, reasons)


def scan_placeholders(project: Path, policy: dict[str, Any]) -> list[str]:
    if not policy["completion"].get("forbid_placeholder_markers", True):
        return []
    markers = tuple(marker.lower() for marker in policy["completion"].get("placeholder_markers", []))
    findings: list[str] = []
    ignored = {"node_modules", ".git", ".research-build", "dist", "build", ".next", "coverage", ".venv", "vendor"}
    for relative in policy["completion"].get("production_paths", []):
        root = project / relative
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or any(part in ignored for part in path.parts):
                continue
            try:
                content = path.read_text(encoding="utf-8", errors="ignore").lower()
            except OSError:
                continue
            for marker in markers:
                if marker in content:
                    findings.append(f"Placeholder marker {marker!r} in {path.relative_to(project)}")
    return findings


def run_quality_commands(project: Path, policy: dict[str, Any], control: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    log_dir = control / "quality-logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    for index, command in enumerate(policy.get("quality_commands", []), start=1):
        log_path = log_dir / f"{index:02d}.log"
        completed = subprocess.run(command, cwd=project, shell=True, capture_output=True, text=True, check=False)
        log_path.write_text((completed.stdout or "") + (completed.stderr or ""), encoding="utf-8")
        results.append({"command": command, "exit_code": completed.returncode, "log": str(log_path.relative_to(project))})
    return results


def validate_phase_json_status(control: Path) -> list[str]:
    reasons: list[str] = []
    for name in ("intake.json", "architecture.json", "threat-model.json", "implementation-report.json", "verification.json"):
        path = control / name
        if not path.exists():
            continue
        try:
            payload = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            reasons.append(f"Invalid {name}: {exc}")
            continue
        if not isinstance(payload, dict) or payload.get("status") != "COMPLETE":
            reasons.append(f"{name} status is not COMPLETE")
    return reasons


def validate_verification_gates(control: Path, policy: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    path = control / "verification.json"
    if not path.exists():
        return reasons
    payload = load_json(path)
    gates = payload.get("quality_gates", [])
    gate_map = {gate.get("id"): gate for gate in gates if isinstance(gate, dict) and gate.get("id")}
    for required in policy["completion"].get("required_verification_gates", []):
        gate = gate_map.get(required)
        if not gate:
            reasons.append(f"Missing required verification gate: {required}")
        elif gate.get("status") != "passed":
            reasons.append(f"Verification gate did not pass: {required}")
    blocking = payload.get("blocking_findings", [])
    if blocking:
        reasons.append(f"Verification contains {len(blocking)} blocking finding(s)")
    return reasons


def verify_project(project: Path, policy: dict[str, Any]) -> GateResult:
    control, _ = project_paths(project)
    reasons: list[str] = []
    for phase, artifacts in PHASE_ARTIFACTS.items():
        for artifact in artifacts:
            if not (control / artifact).exists():
                reasons.append(f"Missing {phase} artifact: {artifact}")
    reasons.extend(validate_evidence(control, policy).reasons)
    reasons.extend(validate_requirements(control).reasons)
    reasons.extend(validate_phase_json_status(control))
    reasons.extend(validate_verification_gates(control, policy))
    reasons.extend(scan_placeholders(project, policy))
    if policy["completion"].get("require_nonempty_quality_commands", True) and not policy.get("quality_commands"):
        reasons.append("No independent quality commands configured")
    quality = run_quality_commands(project, policy, control)
    failed = [result for result in quality if result["exit_code"] != 0]
    reasons.extend(f"Quality command failed: {result['command']}" for result in failed)
    result = GateResult(not reasons, sorted(set(reasons)))
    write_json(control / "independent-verification.json", {
        "status": "COMPLETE" if result.passed else "BLOCKED",
        "verified_at": utc_now(),
        "reasons": result.reasons,
        "quality_commands": quality,
    })
    return result


def create_handoff(project: Path) -> Path:
    control, _ = project_paths(project)
    artifacts: list[dict[str, str]] = []
    missing: list[str] = []
    for name in HANDOFF_INPUTS:
        path = control / name
        if not path.exists():
            missing.append(name)
            continue
        artifacts.append({
            "path": str(path.relative_to(project)).replace("\\", "/"),
            "sha256": sha256(path),
        })
    independent = control / "independent-verification.json"
    if not independent.exists() or load_json(independent).get("status") != "COMPLETE":
        missing.append("passing independent-verification.json")
    if missing:
        raise RuntimeError(f"Cannot create handoff; missing or incomplete: {', '.join(missing)}")
    handoff = {
        "version": 1,
        "status": "READY",
        "created_at": utc_now(),
        "source_stage": "research-build",
        "target_stage": "experience-build",
        "artifacts": artifacts,
        "required_downstream_outcomes": [
            "brand and design system",
            "website information architecture and internal linking",
            "public website and authenticated application surfaces",
            "CRM, forms, consent, and communication integrations",
            "technical SEO, GEO, AEO, and AI-search readiness",
            "structured data, Open Graph, and social metadata",
            "people-first content and editorial governance",
            "applicable legal and policy pages based on verified facts",
            "accessibility, performance, security, and link integrity",
            "deployment, monitoring, rollback, and operations package"
        ]
    }
    output = project / ".experience-build" / "handoff.json"
    write_json(output, handoff)
    return output


def run_phases(project: Path, phase: str, policy: dict[str, Any]) -> int:
    control, state_path = project_paths(project)
    if not state_path.exists():
        raise RuntimeError("Project is not initialized. Run the init command first.")
    state = load_json(state_path)
    selected = PHASES if phase == "all" else (phase,)
    maximum_attempts = int(policy["automation"].get("maximum_phase_attempts", 3))

    for current in selected:
        current_index = PHASES.index(current)
        unmet = [prior for prior in PHASES[:current_index] if state["phases"][prior].get("status") != "passed"]
        if unmet:
            print(json.dumps({"status": "BLOCKED", "phase": current, "reasons": [f"Prerequisite phase has not passed: {item}" for item in unmet]}, indent=2))
            return 2
        phase_state = state["phases"][current]
        if phase_state.get("status") == "passed":
            continue
        passed = False
        while phase_state.get("attempts", 0) < maximum_attempts and not passed:
            phase_state["attempts"] = phase_state.get("attempts", 0) + 1
            phase_state["status"] = "running"
            phase_state["started_at"] = utc_now()
            state["updated_at"] = utc_now()
            write_json(state_path, state)
            log_path = control / f"{current}-attempt-{phase_state['attempts']}.log"
            return_code = run_vibe(project, current, policy, log_path)
            missing = [name for name in PHASE_ARTIFACTS[current] if not (control / name).exists()]
            if current == "research":
                gate = validate_evidence(control, policy)
            elif current == "requirements":
                gate = validate_requirements(control)
            else:
                gate = GateResult(not missing and return_code == 0, [f"Missing artifact: {item}" for item in missing])
                if return_code != 0:
                    gate.reasons.append(f"Vibe exited with code {return_code}; inspect {log_path.name}")
            passed = gate.passed
            phase_state["status"] = "passed" if passed else "blocked"
            phase_state["completed_at"] = utc_now()
            phase_state["reasons"] = gate.reasons
            state["updated_at"] = utc_now()
            write_json(state_path, state)
        if not passed:
            print(json.dumps({"status": "BLOCKED", "phase": current, "reasons": phase_state.get("reasons", [])}, indent=2))
            return 2

    if phase != "all":
        print(json.dumps({"status": "PHASE_COMPLETE", "phase": phase}, indent=2))
        return 0

    final = verify_project(project, policy)
    state["status"] = "COMPLETE" if final.passed else "BLOCKED"
    state["updated_at"] = utc_now()
    state["blocking_reasons"] = final.reasons
    write_json(state_path, state)
    if final.passed:
        create_handoff(project)
    print(json.dumps({"status": state["status"], "reasons": final.reasons}, indent=2))
    return 0 if final.passed else 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--project", required=True, type=Path)
    init_parser.add_argument("--spec", type=Path)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--project", required=True, type=Path)
    run_parser.add_argument("--policy", type=Path)
    run_parser.add_argument("--phase", choices=("all",) + PHASES, default="all")
    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("--project", required=True, type=Path)
    verify_parser.add_argument("--policy", type=Path)
    handoff_parser = subparsers.add_parser("handoff")
    handoff_parser.add_argument("--project", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    kit_root = Path(__file__).resolve().parent
    project = args.project.resolve()
    if args.command == "init":
        initialize(project, args.spec, kit_root)
        return 0
    if args.command == "handoff":
        output = create_handoff(project)
        print(json.dumps({"status": "READY", "handoff": str(output)}, indent=2))
        return 0
    policy_path = args.policy.resolve() if args.policy else project / "research-build-policy.json"
    policy = load_json(policy_path)
    if args.command == "run":
        return run_phases(project, args.phase, policy)
    result = verify_project(project, policy)
    print(json.dumps({"status": "COMPLETE" if result.passed else "BLOCKED", "reasons": result.reasons}, indent=2))
    return 0 if result.passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "ERROR", "error": str(error)}, indent=2), file=sys.stderr)
        raise SystemExit(1)
