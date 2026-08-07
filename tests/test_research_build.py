import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import research_build
import experience_build


class ResearchBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.project = Path(self.temp.name)
        self.control = self.project / ".research-build"
        self.control.mkdir()
        self.policy = {
            "research": {
                "minimum_total_sources": 2,
                "minimum_official_sources": 1,
                "minimum_papers": 1,
                "minimum_repositories": 0,
                "minimum_standards": 0,
            },
            "completion": {
                "forbid_placeholder_markers": True,
                "placeholder_markers": ["TODO"],
                "production_paths": ["src"],
                "require_nonempty_quality_commands": False,
                "required_verification_gates": [],
            },
            "quality_commands": [],
        }

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, name, payload):
        (self.control / name).write_text(json.dumps(payload), encoding="utf-8")

    def test_evidence_gate_passes_valid_diverse_sources(self):
        self.write_json("evidence.json", {"status": "COMPLETE", "sources": [
            {"id": "E-001", "title": "Docs", "url": "https://example.com/docs", "source_type": "official", "accessed_at": "2026-08-03T00:00:00Z", "claims": ["A"]},
            {"id": "E-002", "title": "Paper", "url": "https://arxiv.org/abs/1", "source_type": "paper", "accessed_at": "2026-08-03T00:00:00Z", "claims": ["B"]},
        ]})
        result = research_build.validate_evidence(self.control, self.policy)
        self.assertTrue(result.passed, result.reasons)

    def test_requirements_gate_rejects_unknown_evidence(self):
        self.write_json("evidence.json", {"status": "COMPLETE", "sources": []})
        self.write_json("requirements.json", {"status": "COMPLETE", "requirements": [{
            "id": "FR-001",
            "statement": "Do work",
            "acceptance_criteria": ["Works"],
            "test_ids": ["T-001"],
            "evidence_ids": ["E-999"],
            "risk": "medium",
        }]})
        result = research_build.validate_requirements(self.control)
        self.assertFalse(result.passed)
        self.assertTrue(any("unknown evidence" in reason for reason in result.reasons))

    def test_placeholder_scan_finds_production_marker(self):
        source = self.project / "src"
        source.mkdir()
        (source / "app.py").write_text("# TODO implement", encoding="utf-8")
        findings = research_build.scan_placeholders(self.project, self.policy)
        self.assertEqual(len(findings), 1)

    def test_handoff_hashes_every_approved_artifact(self):
        for name in research_build.HANDOFF_INPUTS:
            path = self.control / name
            if path.suffix == ".json":
                path.write_text(json.dumps({"status": "COMPLETE"}), encoding="utf-8")
            else:
                path.write_text("complete\n", encoding="utf-8")
        self.write_json("independent-verification.json", {"status": "COMPLETE"})

        handoff_path = research_build.create_handoff(self.project)
        handoff = json.loads(handoff_path.read_text(encoding="utf-8"))

        self.assertEqual(handoff["status"], "READY")
        self.assertEqual(len(handoff["artifacts"]), len(research_build.HANDOFF_INPUTS))
        self.assertEqual([], experience_build.validate_handoff(self.project))


if __name__ == "__main__":
    unittest.main()
