#!/usr/bin/env python3
"""Fail closed when the shareable handoff loses integrity or leaks sensitive data."""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.has_main = False
        self.has_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        if tag == "main":
            self.has_main = True
        if tag == "h1":
            self.has_h1 = True


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def verify_local_links() -> None:
    for path in sorted((ROOT / "docs").rglob("*.html")):
        parser = Parser()
        parser.feed(path.read_text(encoding="utf-8"))
        if not parser.has_main or not parser.has_h1:
            fail(f"Missing semantic main/h1 in {path.relative_to(ROOT)}")
        for href in parser.hrefs:
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (path.parent / href.split("#", 1)[0]).resolve()
            if not target.exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {href}")


def verify_checksums() -> None:
    checksum_path = ROOT / "SHA256SUMS"
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        path = ROOT / relative
        if not path.is_file():
            fail(f"Checksum target missing: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            fail(f"Checksum mismatch: {relative}")


def verify_no_sensitive_material() -> None:
    forbidden = {
        "local user path": "/Users/" + "dheeraj",
        "preview env key name": "PREVIEW_" + "COMPOSIO_API_KEY",
    }
    secret_patterns = {
        "unredacted provider app_id": re.compile(r'"app_id"\s*:\s*"[0-9]{10,}"'),
        "unredacted provider app reference": re.compile(r"\bapp\s+`[0-9]{10,}`", re.IGNORECASE),
        "GitHub token": re.compile(r"gh[opsu]_[A-Za-z0-9]{20,}"),
        "OpenAI-style secret": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    }
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix == ".zip":
            continue
        data = path.read_text(encoding="utf-8", errors="ignore")
        for label, needle in forbidden.items():
            if needle in data:
                fail(f"{label} found in {path.relative_to(ROOT)}")
        for label, pattern in secret_patterns.items():
            if pattern.search(data):
                fail(f"{label} pattern found in {path.relative_to(ROOT)}")


def main() -> None:
    manifest = json.loads((ROOT / "manifest" / "contracts.json").read_text(encoding="utf-8"))
    actions = manifest["actions"]
    if len(actions) != 63:
        fail(f"Expected 63 actions, found {len(actions)}")
    if Counter(action["method"] for action in actions) != Counter({"GET": 40, "POST": 23}):
        fail("Method split is not 40 GET and 23 POST")
    if len({action["tool_slug"] for action in actions}) != 63:
        fail("Tool slugs are not unique")
    if len({(action["method"], action["path"]) for action in actions}) != 63:
        fail("Method/path pairs are not unique")
    if len(list((ROOT / "contracts").glob("*.md"))) != 63:
        fail("Expected 63 Markdown contracts")
    if len(list((ROOT / "docs" / "actions").glob("*.html"))) != 63:
        fail("Expected 63 HTML action pages")
    for action in actions:
        if not action["request_fields"] or not action["response_fields"]:
            fail(f"Empty contract table: {action['tool_slug']}")
        parsed = urlparse(action["doc_url"])
        if parsed.scheme != "https" or parsed.netloc != "business-api.tiktok.com":
            fail(f"Non-official source: {action['tool_slug']}")
        if not re.fullmatch(r"[0-9a-f]{64}", action["contract_sha256"]):
            fail(f"Invalid source fingerprint: {action['tool_slug']}")
    permission = json.loads((ROOT / "evidence" / "permission-evidence.json").read_text(encoding="utf-8"))
    if permission["metadata"]["direct_permission_mappings"] != 17 or permission["metadata"]["category_inheritance_mappings"] != 46:
        fail("Permission evidence split drifted")
    selected = json.loads((ROOT / "evidence" / "selected-endpoints.json").read_text(encoding="utf-8"))
    if selected["app_id"] != "REDACTED_SELECTED_APP_ID" or selected["total_endpoints_displayed"] != 160:
        fail("Selected endpoint evidence is not redacted or count drifted")
    blocked_rows = sum(1 for line in (ROOT / "evidence" / "blocked-paths.md").read_text(encoding="utf-8").splitlines() if line.startswith("| `/"))
    if blocked_rows != 53:
        fail(f"Expected 53 blocked paths, found {blocked_rows}")
    verify_no_sensitive_material()
    verify_local_links()
    verify_checksums()
    with zipfile.ZipFile(ROOT / "downloads" / "tiktok-ads-yang-contract-pack-2026-08-30.zip") as archive:
        if archive.testzip() is not None:
            fail("ZIP integrity check failed")
    print("PASS: 63 contracts (40 GET, 23 POST), 53 blocked paths, sources, links, redaction, checksums, and ZIP integrity")


if __name__ == "__main__":
    main()
