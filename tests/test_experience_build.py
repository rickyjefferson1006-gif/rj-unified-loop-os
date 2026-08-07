import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import experience_build


class ExperienceBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.project = Path(self.temp.name)
        self.control = self.project / ".experience-build"
        self.control.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def write(self, relative, payload):
        path = self.project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(payload, dict):
            path.write_text(json.dumps(payload), encoding="utf-8")
        else:
            path.write_text(payload, encoding="utf-8")
        return path

    def test_handoff_detects_changed_approved_artifact(self):
        artifact = self.write(".research-build/evidence.json", "approved")
        self.write(".experience-build/handoff.json", {
            "status": "READY",
            "target_stage": "experience-build",
            "artifacts": [{"path": ".research-build/evidence.json", "sha256": experience_build.digest(artifact)}]
        })
        artifact.write_text("changed", encoding="utf-8")
        reasons = experience_build.validate_handoff(self.project)
        self.assertTrue(any("changed after approval" in reason for reason in reasons))

    def test_site_map_rejects_unknown_internal_page(self):
        self.write(".experience-build/site-map.json", {
            "status": "COMPLETE",
            "pages": [{
                "id": "PAGE-001", "path": "/", "purpose": "Home", "audience": ["buyer"],
                "page_type": "home", "primary_query": "service", "intent": "commercial",
                "title": "Service", "description": "Description", "canonical": "https://example.com/",
                "indexing": "index", "schema_types": ["WebPage"], "internal_links": ["PAGE-999"],
                "primary_cta": "Start"
            }]
        })
        reasons = experience_build.validate_page_inventory(self.control)
        self.assertTrue(any("unknown page ID" in reason for reason in reasons))

    def test_search_manifest_rejects_duplicate_titles(self):
        base = {
            "title": "Duplicate", "description": "One", "canonical": "https://example.com/a",
            "robots": "index,follow", "og": {"title": "A"}, "social_card": {"card": "summary"},
            "json_ld": [{"@type": "WebPage"}], "headings": ["A"], "answer_blocks": ["Answer"],
            "entity_ids": ["ORG-1"], "internal_links": ["/b"]
        }
        second = dict(base, path="/b", description="Two", canonical="https://example.com/b")
        first = dict(base, path="/a")
        self.write(".experience-build/search-manifest.json", {
            "status": "COMPLETE", "pages": [first, second], "robots_txt": {"path": "/robots.txt"},
            "sitemap": {"path": "/sitemap.xml"}, "redirect_map": [], "entity_graph": {"nodes": []},
            "indexnow": {"enabled": True}
        })
        reasons = experience_build.validate_search_manifest(self.control)
        self.assertTrue(any("Duplicate title" in reason for reason in reasons))


if __name__ == "__main__":
    unittest.main()

