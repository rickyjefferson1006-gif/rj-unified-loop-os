#!/usr/bin/env python3
"""Downstream website, application, CRM, content, legal, and search build loop."""

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


PHASES = (
    "handoff-validation",
    "brand-ux",
    "information-architecture",
    "search-strategy",
    "content-system",
    "legal-compliance",
    "site-app-crm",
    "search-implementation",
    "integrations",
    "experience-verification",
    "launch-package",
)

ARTIFACTS = {
    "handoff-validation": ["handoff-validation.json"],
    "brand-ux": ["brand-system.json"],
    "information-architecture": ["site-map.json"],
    "search-strategy": ["search-strategy.json"],
    "content-system": ["content-system.json", "editorial-plan.md"],
    "legal-compliance": ["legal-matrix.json"],
    "site-app-crm": ["implementation-report.json"],
    "search-implementation": ["search-manifest.json"],
    "integrations": ["integrations.json"],
    "experience-verification": ["verification.json"],
    "launch-package": ["launch-report.md"],
}

AGENTS = {
    "handoff-validation": "xp-strategist",
    "brand-ux": "xp-designer",
    "information-architecture": "xp-strategist",
    "search-strategy": "xp-search",
    "content-system": "xp-content",
    "legal-compliance": "xp-legal",
    "site-app-crm": "xp-builder",
    "search-implementation": "xp-search",
    "integrations": "xp-builder",
    "experience-verification": "xp-qa",
    "launch-package": "xp-qa",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def control_path(project: Path) -> Path:
    return project / ".experience-build"


def validate_handoff(project: Path) -> list[str]:
    path = control_path(project) / "handoff.json"
    if not path.exists():
        return ["Missing .experience-build/handoff.json"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "READY":
        reasons.append("Handoff status is not READY")
    if payload.get("target_stage") != "experience-build":
        reasons.append("Handoff target is not experience-build")
    for item in payload.get("artifacts", []):
        artifact = project / item.get("path", "")
        if not artifact.exists():
            reasons.append(f"Missing handoff artifact: {item.get('path')}")
        elif digest(artifact) != item.get("sha256"):
            reasons.append(f"Handoff artifact changed after approval: {item.get('path')}")
    return reasons


def validate_page_inventory(control: Path) -> list[str]:
    path = control / "site-map.json"
    if not path.exists():
        return ["Missing site-map.json"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "COMPLETE":
        reasons.append("site-map.json status is not COMPLETE")
    pages = payload.get("pages", [])
    if not pages:
        reasons.append("Site map contains no pages")
    seen_paths: set[str] = set()
    required = ("id", "path", "purpose", "audience", "page_type", "primary_query", "intent", "title", "description", "canonical", "indexing", "schema_types", "internal_links", "primary_cta")
    for index, page in enumerate(pages):
        missing = [field for field in required if page.get(field) in (None, "", [])]
        if missing:
            reasons.append(f"Page {page.get('id', index)} missing: {', '.join(missing)}")
        route = page.get("path")
        if route in seen_paths:
            reasons.append(f"Duplicate page path: {route}")
        seen_paths.add(route)
    page_ids = {page.get("id") for page in pages}
    for page in pages:
        for target in page.get("internal_links", []):
            if target not in page_ids:
                reasons.append(f"Page {page.get('id')} links to unknown page ID {target}")
    return reasons


def validate_search_manifest(control: Path) -> list[str]:
    path = control / "search-manifest.json"
    if not path.exists():
        return ["Missing search-manifest.json"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "COMPLETE":
        reasons.append("search-manifest.json status is not COMPLETE")
    pages = payload.get("pages", [])
    required = ("path", "title", "description", "canonical", "robots", "og", "social_card", "json_ld", "headings", "answer_blocks", "entity_ids", "internal_links")
    titles: set[str] = set()
    descriptions: set[str] = set()
    for index, page in enumerate(pages):
        missing = [field for field in required if page.get(field) in (None, "", [])]
        if missing:
            reasons.append(f"Search page {page.get('path', index)} missing: {', '.join(missing)}")
        title = page.get("title")
        description = page.get("description")
        if title in titles:
            reasons.append(f"Duplicate title: {title}")
        if description in descriptions:
            reasons.append(f"Duplicate description: {description}")
        titles.add(title)
        descriptions.add(description)
    for field in ("robots_txt", "sitemap", "redirect_map", "entity_graph", "indexnow"):
        if field not in payload or payload.get(field) is None:
            reasons.append(f"Search manifest missing {field}")
    return reasons


def validate_legal(control: Path, policy: dict[str, Any]) -> list[str]:
    path = control / "legal-matrix.json"
    if not path.exists():
        return ["Missing legal-matrix.json"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "COMPLETE":
        reasons.append("Legal matrix is not COMPLETE")
    for fact in ("business_identity", "jurisdictions", "data_inventory", "processing_purposes"):
        if not payload.get(fact):
            reasons.append(f"Legal matrix missing verified {fact}")
    if "cookies_and_trackers" not in payload or not isinstance(payload.get("cookies_and_trackers"), list):
        reasons.append("Legal matrix missing verified cookies_and_trackers inventory")
    required_types = {"terms", "privacy", "accessibility", "general_disclaimer"}
    page_types = {item.get("type") for item in payload.get("pages", [])}
    for required in required_types:
        if required not in page_types:
            reasons.append(f"Missing required legal page: {required}")
    for page in payload.get("pages", []):
        if page.get("applicable") and page.get("status") != "approved":
            reasons.append(f"Applicable legal page is not approved: {page.get('type')}")
        if page.get("unresolved_placeholders"):
            reasons.append(f"Legal page contains unresolved placeholders: {page.get('type')}")
    return reasons


def validate_verification(control: Path, policy: dict[str, Any]) -> list[str]:
    path = control / "verification.json"
    if not path.exists():
        return ["Missing verification.json"]
    payload = read_json(path)
    reasons: list[str] = []
    if payload.get("status") != "COMPLETE":
        reasons.append("Experience verification is not COMPLETE")
    gates = {gate.get("id"): gate for gate in payload.get("gates", []) if isinstance(gate, dict)}
    for gate_id in policy["verification"].get("required_gates", []):
        gate = gates.get(gate_id)
        if not gate:
            reasons.append(f"Missing verification gate: {gate_id}")
        elif gate.get("status") != "passed":
            reasons.append(f"Verification gate failed: {gate_id}")
        elif not gate.get("evidence"):
            reasons.append(f"Verification gate lacks evidence: {gate_id}")
    if payload.get("blocking_findings"):
        reasons.append(f"Verification has {len(payload['blocking_findings'])} blocking finding(s)")
    links = payload.get("link_results", {})
    if links.get("internal_dead", 0) > policy["verification"].get("maximum_internal_dead_links", 0):
        reasons.append("Internal dead-link threshold exceeded")
    if links.get("external_dead", 0) > policy["verification"].get("maximum_external_dead_links", 0):
        reasons.append("External dead-link threshold exceeded")
    return reasons


def validate_phase(control: Path, phase: str, policy: dict[str, Any]) -> list[str]:
    reasons = [f"Missing artifact: {name}" for name in ARTIFACTS[phase] if not (control / name).exists()]
    if reasons:
        return reasons
    for name in ARTIFACTS[phase]:
        if not name.endswith(".json"):
            continue
        payload = read_json(control / name)
        if payload.get("status") != "COMPLETE":
            reasons.append(f"{name} status is not COMPLETE")
    if phase == "handoff-validation":
        reasons.extend(validate_handoff(control.parent))
    elif phase == "information-architecture":
        reasons.extend(validate_page_inventory(control))
    elif phase == "legal-compliance":
        reasons.extend(validate_legal(control, policy))
    elif phase == "search-implementation":
        reasons.extend(validate_search_manifest(control))
    elif phase == "experience-verification":
        reasons.extend(validate_verification(control, policy))
    return sorted(set(reasons))


def prompt(project: Path, phase: str) -> str:
    outputs = ", ".join(ARTIFACTS[phase])
    return f"""
Execute only ExperienceBuild phase: {phase}.
Project root: {project}
Required outputs beneath .experience-build: {outputs}.

Read AGENTS.md, BUILD_SPEC.md, research-build-policy.json, experience-build-policy.json, the signed .experience-build/handoff.json, every approved Stage 1 artifact, and completed ExperienceBuild artifacts. Use the experience-build Skill. Do not invent company facts, legal applicability, search performance, test results, or URLs. Do not create low-value scaled content. Do not deploy to production. Write BLOCKED artifacts with precise reasons when required evidence, business facts, approvals, credentials, or verification are missing.
""".strip()


def run_agent(project: Path, phase: str, policy: dict[str, Any], log: Path) -> int:
    executable = shutil.which(policy["automation"].get("vibe_command", "vibe"))
    if not executable:
        raise RuntimeError("Vibe executable was not found")
    args = [executable, "--trust", "--workdir", str(project), "--agent", AGENTS[phase], "--prompt", prompt(project, phase)]
    with log.open("w", encoding="utf-8", newline="\n") as handle:
        return subprocess.run(args, cwd=project, stdout=handle, stderr=subprocess.STDOUT, text=True, check=False).returncode


def run(project: Path, policy: dict[str, Any], selected_phase: str) -> int:
    control = control_path(project)
    control.mkdir(parents=True, exist_ok=True)
    state_path = control / "state.json"
    state = read_json(state_path) if state_path.exists() else {
        "version": 1,
        "status": "initialized",
        "created_at": now(),
        "phases": {phase: {"status": "pending", "attempts": 0} for phase in PHASES},
    }
    selected = PHASES if selected_phase == "all" else (selected_phase,)
    maximum = int(policy["automation"].get("maximum_phase_attempts", 3))
    for phase in selected:
        unmet = [prior for prior in PHASES[:PHASES.index(phase)] if state["phases"][prior]["status"] != "passed"]
        if unmet:
            print(json.dumps({"status": "BLOCKED", "phase": phase, "reasons": [f"Prerequisite phase has not passed: {item}" for item in unmet]}, indent=2))
            return 2
        phase_state = state["phases"][phase]
        if phase_state["status"] == "passed":
            continue
        while phase_state["attempts"] < maximum:
            phase_state["attempts"] += 1
            phase_state["status"] = "running"
            write_json(state_path, state)
            log = control / f"{phase}-attempt-{phase_state['attempts']}.log"
            code = run_agent(project, phase, policy, log)
            reasons = validate_phase(control, phase, policy)
            if code != 0:
                reasons.append(f"Vibe exited with code {code}; inspect {log.name}")
            if not reasons:
                phase_state["status"] = "passed"
                phase_state["completed_at"] = now()
                write_json(state_path, state)
                break
            phase_state["status"] = "blocked"
            phase_state["reasons"] = reasons
            write_json(state_path, state)
        if phase_state["status"] != "passed":
            print(json.dumps({"status": "BLOCKED", "phase": phase, "reasons": phase_state.get("reasons", [])}, indent=2))
            return 2
    if selected_phase != "all":
        print(json.dumps({"status": "PHASE_COMPLETE", "phase": selected_phase}, indent=2))
        return 0
    all_reasons: list[str] = []
    for phase in PHASES:
        all_reasons.extend(validate_phase(control, phase, policy))
    state["status"] = "COMPLETE" if not all_reasons else "BLOCKED"
    state["completed_at"] = now()
    state["reasons"] = sorted(set(all_reasons))
    write_json(state_path, state)
    print(json.dumps({"status": state["status"], "reasons": state["reasons"]}, indent=2))
    return 0 if state["status"] == "COMPLETE" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("run", "verify"))
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--phase", choices=("all",) + PHASES, default="all")
    args = parser.parse_args()
    project = args.project.resolve()
    policy = read_json(args.policy.resolve() if args.policy else project / "experience-build-policy.json")
    if args.command == "run":
        return run(project, policy, args.phase)
    reasons: list[str] = []
    control = control_path(project)
    for phase in PHASES:
        reasons.extend(validate_phase(control, phase, policy))
    print(json.dumps({"status": "COMPLETE" if not reasons else "BLOCKED", "reasons": sorted(set(reasons))}, indent=2))
    return 0 if not reasons else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(1)
