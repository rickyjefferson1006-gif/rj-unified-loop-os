#!/usr/bin/env python3
"""Collect arXiv and GitHub candidates without treating discovery as verified evidence."""

from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


USER_AGENT = "ResearchBuildLoop/1.0"


def request(url: str, headers: dict[str, str] | None = None) -> bytes:
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    with urllib.request.urlopen(urllib.request.Request(url, headers=merged), timeout=30) as response:
        return response.read()


def arxiv(query: str, limit: int) -> list[dict[str, Any]]:
    encoded = urllib.parse.urlencode({"search_query": f"all:{query}", "start": 0, "max_results": limit, "sortBy": "submittedDate", "sortOrder": "descending"})
    root = ET.fromstring(request(f"https://export.arxiv.org/api/query?{encoded}"))
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    results = []
    for entry in root.findall("atom:entry", namespace):
        authors = [node.findtext("atom:name", default="", namespaces=namespace) for node in entry.findall("atom:author", namespace)]
        results.append({
            "source_type": "paper",
            "title": " ".join((entry.findtext("atom:title", default="", namespaces=namespace)).split()),
            "url": entry.findtext("atom:id", default="", namespaces=namespace),
            "published_at": entry.findtext("atom:published", default="", namespaces=namespace),
            "updated_at": entry.findtext("atom:updated", default="", namespaces=namespace),
            "authors": authors,
            "summary": " ".join((entry.findtext("atom:summary", default="", namespaces=namespace)).split()),
            "verification_status": "candidate"
        })
    return results


def github(query: str, limit: int) -> list[dict[str, Any]]:
    encoded = urllib.parse.urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": min(limit, 100)})
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    payload = json.loads(request(f"https://api.github.com/search/repositories?{encoded}", headers))
    return [{
        "source_type": "repository",
        "title": item["full_name"],
        "url": item["html_url"],
        "description": item.get("description"),
        "default_branch": item.get("default_branch"),
        "license": (item.get("license") or {}).get("spdx_id"),
        "stars": item.get("stargazers_count"),
        "open_issues": item.get("open_issues_count"),
        "updated_at": item.get("updated_at"),
        "archived": item.get("archived"),
        "verification_status": "candidate"
    } for item in payload.get("items", [])]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    errors: list[str] = []
    papers: list[dict[str, Any]] = []
    repositories: list[dict[str, Any]] = []
    try:
        papers = arxiv(args.query, args.limit)
    except Exception as exc:  # network and upstream errors are recorded, never hidden
        errors.append(f"arXiv collection failed: {exc}")
    try:
        repositories = github(args.query, args.limit)
    except Exception as exc:
        errors.append(f"GitHub collection failed: {exc}")
    payload = {
        "query": args.query,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "warning": "Discovery candidates are not verified evidence. Inspect every source before acceptance.",
        "papers": papers,
        "repositories": repositories,
        "errors": errors,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"papers": len(papers), "repositories": len(repositories), "errors": errors}, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())

