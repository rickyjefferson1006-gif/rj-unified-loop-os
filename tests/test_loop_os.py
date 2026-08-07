import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import loop_os


class LoopOSTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.project = Path(self.temp.name)
        self.loop = {
            "id": "example-loop",
            "name": "Example",
            "domain": "software",
            "purpose": "Test the engine",
            "trigger": "test",
            "cadence": "on demand",
            "risk": "high",
            "profile": "software",
            "stages": ["intake", "build", "verify"],
            "handoff_to": [],
            "human_approvals": ["scope"]
        }
        self.policy = {
            "completion": {
                "required_stage_fields": ["objective", "inputs_used", "evidence", "decisions", "outputs", "gates", "metrics", "risks", "next_stage", "handoff"]
            },
            "approval": {"risk_levels_requiring_final_approval": ["high", "critical"]},
            "automation": {"maximum_stage_attempts": 3}
        }

    def tearDown(self):
        self.temp.cleanup()

    def complete_stage(self, root, order, stage, next_stage):
        loop_os.write_json(loop_os.stage_path(root, order, stage), {
            "version": 1,
            "loop_id": self.loop["id"],
            "stage": stage,
            "status": "COMPLETE",
            "completed_at": loop_os.now(),
            "objective": "Complete stage",
            "inputs_used": ["input"],
            "evidence": ["evidence"],
            "decisions": ["decision"],
            "outputs": ["output"],
            "gates": [{"id": "quality", "status": "passed", "evidence": "test"}],
            "metrics": [{"name": "pass", "value": 1}],
            "risks": [{"risk": "none observed"}],
            "unresolved_blockers": [],
            "next_stage": next_stage,
            "handoff": {"status": "ready"}
        })

    def test_catalog_is_valid(self):
        catalog = json.loads((Path(__file__).resolve().parents[1] / "loop-catalog.json").read_text(encoding="utf-8"))
        self.assertEqual([], loop_os.validate_catalog(catalog))
        self.assertGreaterEqual(len(catalog["loops"]), 35)

    def test_create_run_hashes_immutable_input(self):
        source = self.project / "input.json"
        source.write_text('{"approved": true}', encoding="utf-8")
        _, root = loop_os.create_run(self.project, self.loop, source)
        state = loop_os.read_json(root / "run.json")
        copied = self.project / state["input"]["path"]
        self.assertEqual(loop_os.sha256(copied), state["input"]["sha256"])

    def test_schedule_references_known_loops(self):
        root = Path(__file__).resolve().parents[1]
        catalog = json.loads((root / "loop-catalog.json").read_text(encoding="utf-8"))
        schedules = json.loads((root / "loop-schedules.example.json").read_text(encoding="utf-8"))
        known = {item["id"] for item in catalog["loops"]}
        referenced = {item["loop_id"] for item in schedules["schedules"] + schedules["event_triggers"]}
        self.assertEqual(set(), referenced - known)

    def test_high_risk_run_requires_named_and_final_approvals(self):
        _, root = loop_os.create_run(self.project, self.loop, None)
        for order, stage in enumerate(self.loop["stages"], 1):
            next_stage = self.loop["stages"][order] if order < len(self.loop["stages"]) else None
            self.complete_stage(root, order, stage, next_stage)
        reasons = loop_os.validate_run(root, self.loop, self.policy)
        self.assertIn("Required human approval is missing: scope", reasons)
        self.assertIn("Required human approval is missing: final-release", reasons)

    def test_verification_stage_uses_independent_verifier(self):
        self.assertEqual("lo-verifier", loop_os.select_agent(self.loop, "independent-verification"))


if __name__ == "__main__":
    unittest.main()
