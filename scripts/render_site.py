#!/usr/bin/env python3
"""Render the normalized TikTok Ads contract pack as a static HTML site."""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest" / "contracts.json"
DOCS = ROOT / "docs"
ACTIONS_DIR = DOCS / "actions"
ASSETS_DIR = DOCS / "assets"
OFFICIAL_PERMISSION_URL = "https://business-api.tiktok.com/portal/docs?id=1753986142651394"
ZIP_PATH = ROOT / "downloads" / "tiktok-ads-yang-contract-pack-2026-08-30.zip"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def constraints(field: dict) -> str:
    values = field.get("constraints") or []
    return "<br>".join(esc(item) for item in values) if values else '<span class="muted">None documented</span>'


def action_filename(index: int, action: dict) -> str:
    short = action["tool_slug"].removeprefix("TIKTOK_ADS_").lower().replace("_", "-")
    return f"{index:03d}-{short}.html"


def page(title: str, body: str, prefix: str = ".", description: str = "TikTok Ads contract evidence") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)} · TikTok Ads contract kit</title>
  <link rel="stylesheet" href="{prefix}/assets/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{prefix}/index.html" aria-label="TikTok Ads contract kit home">
        <span class="brand-mark" aria-hidden="true">TA</span>
        <span>TikTok Ads contract kit</span>
      </a>
      <nav aria-label="Primary navigation">
        <a href="{prefix}/index.html">Actions</a>
        <a href="{prefix}/blocked.html">Blocked</a>
        <a href="{prefix}/sources.html">Sources</a>
        <a href="{prefix}/handoff.html">Yang handoff</a>
      </nav>
    </div>
  </header>
  <main id="main" class="page-shell">{body}</main>
  <footer>
    <p>Independent normalized evidence pack. Always re-check the linked official TikTok source before shipping.</p>
  </footer>
</body>
</html>"""


def field_table(fields: list[dict], request: bool) -> str:
    if request:
        head = "<tr><th>Field</th><th>Placement</th><th>Type</th><th>Requiredness</th><th>Constraints</th></tr>"
        rows = "".join(
            "<tr>"
            f"<td><code>{esc(field['path'])}</code></td>"
            f"<td><code>{esc(field.get('placement', 'unspecified'))}</code></td>"
            f"<td><code>{esc(field.get('type', 'unspecified'))}</code></td>"
            f"<td>{esc(field.get('requirement', 'unspecified'))}</td>"
            f"<td>{constraints(field)}</td>"
            "</tr>"
            for field in fields
        )
    else:
        head = "<tr><th>Field</th><th>Type</th><th>Presence</th><th>Constraints</th></tr>"
        rows = "".join(
            "<tr>"
            f"<td><code>{esc(field['path'])}</code></td>"
            f"<td><code>{esc(field.get('type', 'unspecified'))}</code></td>"
            f"<td>{esc(field.get('requirement', 'unspecified'))}</td>"
            f"<td>{constraints(field)}</td>"
            "</tr>"
            for field in fields
        )
    return f'<div class="table-wrap"><table>{head}{rows}</table></div>'


def badges(action: dict) -> str:
    method = action["method"]
    return (
        f'<span class="badge method-{method.lower()}">{esc(method)}</span>'
        f'<span class="badge">Scope {esc(action["parent_scope"])}</span>'
        f'<span class="badge">{esc(action["category"])}</span>'
    )


def contract_file_map() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((ROOT / "contracts").glob("*.md")):
        first = path.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ").strip()
        result[first] = path.name
    return result


def render_action_pages(actions: list[dict]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    markdown = contract_file_map()
    for index, action in enumerate(actions, 1):
        filename = action_filename(index, action)
        mapping[action["tool_slug"]] = filename
        previous_link = f'<a href="{action_filename(index - 1, actions[index - 2])}">← Previous</a>' if index > 1 else "<span></span>"
        next_link = f'<a href="{action_filename(index + 1, actions[index])}">Next →</a>' if index < len(actions) else "<span></span>"
        warning_items = action.get("warnings") or []
        warnings = "".join(f"<li>{esc(item)}</li>" for item in warning_items)
        if not warnings:
            warnings = '<li class="muted">No additional contradiction warning recorded.</li>'
        fixture_items = "".join(f"<li><code>{esc(item)}</code></li>" for item in action.get("required_fixture_inputs") or [])
        body = f"""
<div class="breadcrumbs"><a href="../index.html">Actions</a><span>/</span><span>{index} of {len(actions)}</span></div>
<section class="hero compact">
  <p class="eyebrow">Normalized official contract</p>
  <h1>{esc(action['title'])}</h1>
  <p class="slug"><code>{esc(action['tool_slug'])}</code></p>
  <div class="badges">{badges(action)}</div>
</section>
<section class="metadata-grid" aria-label="Action metadata">
  <div><span>Wire endpoint</span><strong><code>{esc(action['method'])} {esc(action['path'])}</code></strong></div>
  <div><span>Encoding</span><strong>{esc(action.get('content_type') or ('query string' if action['method'] == 'GET' else 'application/json'))}</strong></div>
  <div><span>Ability hint</span><strong>{esc(action['ability_hint'])}</strong></div>
  <div><span>Permission evidence</span><strong>{esc(action['permission_evidence'])}</strong></div>
</section>
<section>
  <div class="section-heading"><div><p class="eyebrow">Input</p><h2>Request contract</h2></div><span>{len(action['request_fields'])} fields</span></div>
  {field_table(action['request_fields'], True)}
</section>
<section>
  <div class="section-heading"><div><p class="eyebrow">Output</p><h2>Response contract</h2></div><span>{len(action['response_fields'])} fields</span></div>
  <p class="callout">Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.</p>
  {field_table(action['response_fields'], False)}
</section>
<section class="split">
  <div>
    <p class="eyebrow">Runtime</p><h2>Fixture and live boundary</h2>
    <p><strong>Gate:</strong> {esc(action['product_gate_hint'])}</p>
    <p><strong>Live boundary:</strong> {esc(action['live_boundary'])}</p>
    <h3>Required fixture inputs</h3><ul class="compact-list">{fixture_items or '<li class="muted">None listed</li>'}</ul>
  </div>
  <div>
    <p class="eyebrow">Review</p><h2>Warnings</h2><ul>{warnings}</ul>
  </div>
</section>
<section class="source-panel">
  <div><p class="eyebrow">Provider evidence</p><h2>Official source</h2></div>
  <p><a class="button" href="{esc(action['doc_url'])}" rel="noreferrer" target="_blank">Open TikTok doc ↗</a></p>
  <dl>
    <div><dt>Document ID</dt><dd><code>{esc(action['doc_id'])}</code></dd></div>
    <div><dt>Source-content SHA-256</dt><dd><code class="hash">{esc(action['contract_sha256'])}</code></dd></div>
    <div><dt>Markdown contract</dt><dd><a href="../../contracts/{esc(markdown[action['tool_slug']])}">{esc(markdown[action['tool_slug']])}</a></dd></div>
  </dl>
</section>
<nav class="pager" aria-label="Action pagination">{previous_link}{next_link}</nav>
"""
        write(ACTIONS_DIR / filename, page(action["title"], body, "..", f"Normalized contract for {action['tool_slug']}"))
    return mapping


def parse_blocked_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in (ROOT / "evidence" / "blocked-paths.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `/"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4:
            continue
        selected, current, decision, evidence = cells
        link = re.search(r"\((https://[^)]+)\)", evidence)
        label = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", evidence)
        rows.append({
            "selected": selected.strip("`"),
            "current": current.strip("`"),
            "decision": decision.strip("`"),
            "evidence": label,
            "url": link.group(1) if link else "",
        })
    return rows


def render_index(actions: list[dict], mapping: dict[str, str], blocked_count: int) -> None:
    rows = "".join(
        f"""<tr data-action-row data-search="{esc(' '.join([a['tool_slug'], a['title'], a['path'], a['category']]).lower())}" data-method="{esc(a['method'])}" data-category="{esc(a['category'])}">
  <td><span class="badge method-{a['method'].lower()}">{esc(a['method'])}</span></td>
  <td><a href="actions/{esc(mapping[a['tool_slug']])}"><strong>{esc(a['title'])}</strong><br><code>{esc(a['tool_slug'])}</code></a></td>
  <td><code>{esc(a['path'])}</code></td>
  <td>{esc(a['category'])}</td>
  <td>{esc(a['parent_scope'])}</td>
</tr>"""
        for a in actions
    )
    categories = "".join(f'<option value="{esc(category)}">{esc(category)}</option>' for category in sorted({a["category"] for a in actions}))
    body = f"""
<section class="hero">
  <p class="eyebrow">Frozen evidence · 2026-08-30</p>
  <h1>Build the missing TikTok Ads actions from contracts, not guesses.</h1>
  <p class="lede">A private implementation kit for the provider-selected v2.0 ceiling. Every candidate below has a normalized request and response contract, permission trail, official source, and explicit live-test boundary.</p>
  <div class="hero-actions"><a class="button" href="handoff.html">Open Yang handoff</a><a class="text-link" href="../downloads/tiktok-ads-yang-contract-pack-2026-08-30.zip">Download offline pack</a></div>
</section>
<section class="stats" aria-label="Coverage summary">
  <div><strong>160</strong><span>selected endpoints</span></div>
  <div><strong>44</strong><span>already represented</span></div>
  <div><strong>{len(actions)}</strong><span>contract-complete gaps</span></div>
  <div><strong>{blocked_count}</strong><span>blocked gaps</span></div>
</section>
<section>
  <div class="section-heading"><div><p class="eyebrow">Implementation set</p><h2>63 action contracts</h2></div><span id="result-count" aria-live="polite">{len(actions)} shown</span></div>
  <div class="filters">
    <label>Search actions<input id="action-search" type="search" placeholder="Slug, title, path, or category" autocomplete="off"></label>
    <label>Method<select id="method-filter"><option value="">All methods</option><option value="GET">GET</option><option value="POST">POST</option></select></label>
    <label>Category<select id="category-filter"><option value="">All categories</option>{categories}</select></label>
  </div>
  <div class="table-wrap"><table id="action-table"><thead><tr><th>Method</th><th>Action</th><th>Endpoint</th><th>Category</th><th>Scope</th></tr></thead><tbody>{rows}</tbody></table></div>
  <div id="empty-state" class="empty-state" hidden>No actions match these filters.</div>
</section>
<section class="boundary">
  <div><p class="eyebrow">What this proves</p><h2>Implementation-grade contract evidence</h2><p>Field placement, types, requiredness, constraints, response paths, permission evidence, and exact source provenance.</p></div>
  <div><p class="eyebrow">What remains</p><h2>Provider-account certification</h2><p>OAuth approval, account roles, product eligibility, allowlists, real fixtures, and reversible live execution.</p></div>
</section>
<script src="assets/app.js" defer></script>
"""
    write(DOCS / "index.html", page("Actions", body, ".", "Search 63 TikTok Ads action contracts"))


def render_blocked(rows: list[dict[str, str]]) -> None:
    counts = Counter(row["decision"] for row in rows)
    count_list = "".join(f"<li><code>{esc(key)}</code><span>{value}</span></li>" for key, value in sorted(counts.items()))
    table_rows = "".join(
        "<tr>"
        f"<td><code>{esc(row['selected'])}</code></td>"
        f"<td><code>{esc(row['current'])}</code></td>"
        f"<td><span class=" + '"badge blocked"' + f">{esc(row['decision'])}</span></td>"
        f"<td>{f'<a href={chr(34)}{esc(row["url"])}{chr(34)} target={chr(34)}_blank{chr(34)} rel={chr(34)}noreferrer{chr(34)}>{esc(row["evidence"])} ↗</a>' if row['url'] else esc(row['evidence'])}</td>"
        "</tr>"
        for row in rows
    )
    body = f"""
<section class="hero compact"><p class="eyebrow">Stop list</p><h1>Blocked selected endpoints</h1><p class="lede">These {len(rows)} gaps do not have enough safe, current provider evidence for implementation. Do not turn them into actions by inference.</p></section>
<section class="split"><div><h2>Decision breakdown</h2><ul class="count-list">{count_list}</ul></div><div><h2>Unblock rule</h2><p>Require a complete current provider contract, correct auth design, and a test plan with an eligible fixture and cleanup. A permission-table row alone is not a request/response contract.</p></div></section>
<section><div class="table-wrap"><table><thead><tr><th>Selected path</th><th>Current path</th><th>Decision</th><th>Evidence</th></tr></thead><tbody>{table_rows}</tbody></table></div></section>
"""
    write(DOCS / "blocked.html", page("Blocked paths", body))


def render_sources(actions: list[dict], mapping: dict[str, str]) -> None:
    rows = "".join(
        f"<tr><td><a href=" + f'"actions/{esc(mapping[a["tool_slug"]])}"><code>{esc(a["tool_slug"])}</code></a></td>'
        f"<td><a href=\"{esc(a['doc_url'])}\" target=\"_blank\" rel=\"noreferrer\">Doc {esc(a['doc_id'])} ↗</a></td>"
        f"<td><code class=\"hash\">{esc(a['contract_sha256'])}</code></td></tr>"
        for a in actions
    )
    body = f"""
<section class="hero compact"><p class="eyebrow">Provenance</p><h1>Official source index</h1><p class="lede">Each hash is a fingerprint of the official source content observed during the audit. It is not a claim that the gated source snapshot is redistributed in this repository.</p></section>
<section><div class="table-wrap"><table><thead><tr><th>Action</th><th>Official TikTok page</th><th>Source-content SHA-256</th></tr></thead><tbody>{rows}</tbody></table></div></section>
"""
    write(DOCS / "sources.html", page("Sources", body))


def render_handoff(manifest: dict) -> None:
    batch_rows = "".join(
        f"<tr><td>{esc(name.split()[0])}</td><td>{esc(' '.join(name.split()[1:]))}</td><td>{len(slugs)}</td><td>{'<br>'.join(f'<code>{esc(slug)}</code>' for slug in slugs)}</td></tr>"
        for name, slugs in manifest["batches"].items()
    )
    body = f"""
<section class="hero compact"><p class="eyebrow">Implementation handoff</p><h1>Yang execution order</h1><p class="lede">Use one batch at a time in the existing Mercury PR. Stop after each accepted SHA so independent review can catch drift before the next batch compounds it.</p></section>
<section class="steps"><ol><li>Compare the current PR head with audited SHA <code>{esc(manifest['metadata']['mercury_sha'])}</code>.</li><li>Read the machine manifest and permission map.</li><li>Run Prompt 1 only.</li><li>Return the accepted SHA and focused test evidence.</li><li>Insert that SHA into the next prompt's placeholder.</li><li>Do not merge; hand back the final SHA for preview QA.</li></ol></section>
<section><div class="section-heading"><div><p class="eyebrow">Ten checkpoints</p><h2>Batch map</h2></div><a href="../yang/implementation-prompts.md">Open full prompts</a></div><div class="table-wrap"><table><thead><tr><th>Batch</th><th>Family</th><th>Actions</th><th>Tool slugs</th></tr></thead><tbody>{batch_rows}</tbody></table></div></section>
<section class="callout"><strong>Stop boundary:</strong> implement only the 63 manifest entries. The blocked ledger is not permission to infer the missing contracts.</section>
"""
    write(DOCS / "handoff.html", page("Yang handoff", body))


def write_permission_evidence(actions: list[dict], metadata: dict) -> None:
    entries = [
        {
            "tool_slug": action["tool_slug"],
            "method": action["method"],
            "path": action["path"],
            "selected_category": action["category"],
            "parent_scope": action["parent_scope"],
            "evidence_type": action["permission_evidence"],
            "official_permission_url": OFFICIAL_PERMISSION_URL,
            "endpoint_doc_url": action["doc_url"],
            "endpoint_contract_sha256": action["contract_sha256"],
        }
        for action in actions
    ]
    payload = {
        "metadata": {
            "generated_at": metadata["generated_at"],
            "selected_export_sha256": metadata["selected_export_sha256"],
            "direct_permission_mappings": sum(item["evidence_type"] == "direct_permission_table_mapping" for item in entries),
            "category_inheritance_mappings": sum(item["evidence_type"] == "selected_export_category_plus_first_level_inheritance" for item in entries),
            "note": "Developer app ID is redacted. Source hashes are provenance fingerprints; authenticated source snapshots are not bundled.",
        },
        "entries": entries,
    }
    write(ROOT / "evidence" / "permission-evidence.json", json.dumps(payload, indent=2, ensure_ascii=False))
    rows = "\n".join(
        f"| `{item['tool_slug']}` | `{item['method']} {item['path']}` | {item['selected_category']} | `{item['parent_scope']}` | `{item['evidence_type']}` | [endpoint]({item['endpoint_doc_url']}) |"
        for item in entries
    )
    md = f"""# Permission evidence map

Official permission reference: {OFFICIAL_PERMISSION_URL}

- Direct endpoint-to-permission mappings: **{payload['metadata']['direct_permission_mappings']}**
- Selected-category plus official first-level inheritance mappings: **{payload['metadata']['category_inheritance_mappings']}**
- Selected export SHA-256 before app-ID redaction: `{metadata['selected_export_sha256']}`

The developer app ID is intentionally redacted. The category assignment is preserved in `selected-endpoints.json`. Feature allowlists and product eligibility remain separate runtime gates.

| Tool | Wire | Selected category | Parent scope | Evidence type | Official endpoint |
|---|---|---|---:|---|---|
{rows}
"""
    write(ROOT / "evidence" / "permission-evidence.md", md)


def write_assets() -> None:
    css = r"""
:root {
  color-scheme: light;
  --bg: #f4f6f3;
  --surface: #ffffff;
  --surface-2: #e9efed;
  --ink: #16211f;
  --muted: #5c6a67;
  --line: #cbd6d2;
  --accent: #006d68;
  --accent-dark: #004b47;
  --post: #9b3d20;
  --blocked: #7c2d2d;
  --focus: #005fcc;
  --radius: 0.45rem;
  --max: 92rem;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 16px/1.55 ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
a { color: var(--accent-dark); text-underline-offset: 0.18em; }
a:hover { color: var(--accent); }
a:focus-visible, input:focus-visible, select:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
code { font: 0.86em/1.55 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; overflow-wrap: anywhere; }
h1, h2, h3 { line-height: 1.16; letter-spacing: -0.025em; }
h1 { max-width: 22ch; font-size: clamp(2.1rem, 5vw, 4.5rem); margin: 0.3rem 0 1rem; }
h2 { font-size: clamp(1.45rem, 2.4vw, 2.25rem); margin: 0.2rem 0 0.8rem; }
h3 { font-size: 1rem; margin: 1.35rem 0 0.45rem; }
p { max-width: 78ch; }
.skip-link { position: fixed; left: 1rem; top: -5rem; z-index: 20; padding: 0.7rem 1rem; background: var(--ink); color: white; }
.skip-link:focus { top: 1rem; }
.site-header { position: sticky; top: 0; z-index: 10; border-bottom: 1px solid var(--line); background: rgba(244, 246, 243, 0.96); backdrop-filter: blur(12px); }
.header-inner { max-width: var(--max); margin: auto; padding: 0.75rem 1.25rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.brand { display: inline-flex; align-items: center; gap: 0.65rem; color: var(--ink); font-weight: 760; text-decoration: none; }
.brand-mark { display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 50%; background: var(--ink); color: white; font-size: 0.72rem; letter-spacing: 0.08em; }
nav { display: flex; flex-wrap: wrap; gap: 0.9rem; }
nav a { font-weight: 650; text-decoration: none; }
.page-shell { max-width: var(--max); margin: auto; padding: 1rem 1.25rem 5rem; }
section { margin-top: 3.5rem; }
.hero { padding: clamp(2.5rem, 7vw, 7rem) 0 clamp(2rem, 5vw, 5rem); border-bottom: 1px solid var(--line); }
.hero.compact { padding: clamp(2rem, 5vw, 4.5rem) 0 2.5rem; }
.hero.compact h1 { font-size: clamp(2rem, 4vw, 3.5rem); }
.eyebrow { margin: 0; color: var(--accent-dark); font-size: 0.78rem; font-weight: 800; letter-spacing: 0.11em; text-transform: uppercase; }
.lede { color: var(--muted); font-size: clamp(1.05rem, 1.8vw, 1.3rem); max-width: 70ch; }
.hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin-top: 1.75rem; }
.button { display: inline-block; padding: 0.72rem 1rem; border: 1px solid var(--accent-dark); border-radius: var(--radius); background: var(--accent-dark); color: white; font-weight: 720; text-decoration: none; }
.button:hover { background: var(--accent); color: white; }
.text-link { font-weight: 720; }
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; border: 1px solid var(--line); background: var(--line); }
.stats div { padding: 1.25rem; background: var(--surface); }
.stats strong { display: block; font-size: clamp(2rem, 4vw, 3.25rem); line-height: 1; }
.stats span { display: block; color: var(--muted); margin-top: 0.5rem; }
.section-heading { display: flex; align-items: end; justify-content: space-between; gap: 1rem; margin-bottom: 1rem; }
.filters { display: grid; grid-template-columns: minmax(15rem, 2fr) 1fr 1fr; gap: 0.75rem; margin-bottom: 1rem; }
label { color: var(--muted); font-size: 0.8rem; font-weight: 720; }
input, select { width: 100%; min-height: 2.7rem; margin-top: 0.3rem; border: 1px solid var(--line); border-radius: var(--radius); background: var(--surface); color: var(--ink); padding: 0.55rem 0.7rem; font: inherit; }
.table-wrap { overflow-x: auto; border: 1px solid var(--line); background: var(--surface); }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 0.78rem 0.85rem; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { position: sticky; top: 3.55rem; background: var(--surface-2); color: #33423f; font-size: 0.75rem; letter-spacing: 0.06em; text-transform: uppercase; }
tbody tr:last-child td { border-bottom: 0; }
tbody tr:hover { background: #f8faf9; }
.badge { display: inline-flex; align-items: center; min-height: 1.65rem; padding: 0.18rem 0.48rem; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); color: var(--ink); font-size: 0.72rem; font-weight: 780; white-space: nowrap; }
.method-get { border-color: #78aaa5; color: #005b56; background: #edf8f6; }
.method-post { border-color: #d69c82; color: #783018; background: #fff2ec; }
.blocked { border-color: #d09a9a; color: var(--blocked); background: #fff2f2; }
.badges { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.slug { font-size: 1.05rem; }
.metadata-grid { display: grid; grid-template-columns: repeat(4, 1fr); border: 1px solid var(--line); background: var(--surface); }
.metadata-grid div { min-width: 0; padding: 1rem; border-right: 1px solid var(--line); }
.metadata-grid div:last-child { border-right: 0; }
.metadata-grid span { display: block; color: var(--muted); font-size: 0.75rem; font-weight: 720; text-transform: uppercase; letter-spacing: 0.06em; }
.metadata-grid strong { display: block; margin-top: 0.35rem; }
.split, .boundary { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; border: 1px solid var(--line); background: var(--line); }
.split > div, .boundary > div { padding: 1.5rem; background: var(--surface); }
.callout { padding: 1rem; border-left: 4px solid var(--accent); background: #eaf4f2; }
.source-panel { padding: 1.5rem; border: 1px solid var(--line); background: var(--surface); }
.source-panel dl { display: grid; grid-template-columns: 1fr 2fr 2fr; gap: 1rem; margin-top: 1.5rem; }
dt { color: var(--muted); font-size: 0.75rem; font-weight: 720; text-transform: uppercase; }
dd { margin: 0.25rem 0 0; }
.hash { word-break: break-all; }
.muted { color: var(--muted); }
.breadcrumbs { display: flex; gap: 0.55rem; color: var(--muted); margin-top: 1.2rem; font-size: 0.88rem; }
.pager { justify-content: space-between; margin-top: 2.5rem; }
.empty-state { padding: 2rem; border: 1px dashed var(--line); text-align: center; color: var(--muted); }
.compact-list { columns: 2; }
.count-list { list-style: none; padding: 0; }
.count-list li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.45rem 0; border-bottom: 1px solid var(--line); }
.steps { padding: 1.5rem; border: 1px solid var(--line); background: var(--surface); }
.steps li { margin: 0.65rem 0; }
footer { border-top: 1px solid var(--line); padding: 1.5rem; color: var(--muted); }
footer p { max-width: var(--max); margin: auto; }
@media (max-width: 900px) {
  .stats, .metadata-grid { grid-template-columns: 1fr 1fr; }
  .metadata-grid div:nth-child(2) { border-right: 0; }
  .metadata-grid div:nth-child(-n+2) { border-bottom: 1px solid var(--line); }
  .filters { grid-template-columns: 1fr 1fr; }
  .filters label:first-child { grid-column: 1 / -1; }
  .source-panel dl { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .header-inner { align-items: flex-start; flex-direction: column; }
  .site-header { position: static; }
  th { position: static; }
  .stats, .metadata-grid, .split, .boundary, .filters { grid-template-columns: 1fr; }
  .metadata-grid div { border-right: 0; border-bottom: 1px solid var(--line); }
  .metadata-grid div:last-child { border-bottom: 0; }
  .filters label:first-child { grid-column: auto; }
  .compact-list { columns: 1; }
  th, td { padding: 0.65rem; }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
"""
    js = r"""
(() => {
  const rows = [...document.querySelectorAll('[data-action-row]')];
  const search = document.querySelector('#action-search');
  const method = document.querySelector('#method-filter');
  const category = document.querySelector('#category-filter');
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  if (!rows.length || !search || !method || !category || !count || !empty) return;
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    rows.forEach((row) => {
      const show = (!query || row.dataset.search.includes(query)) &&
        (!method.value || row.dataset.method === method.value) &&
        (!category.value || row.dataset.category === category.value);
      row.hidden = !show;
      if (show) visible += 1;
    });
    count.textContent = `${visible} shown`;
    empty.hidden = visible !== 0;
  };
  [search, method, category].forEach((control) => control.addEventListener('input', update));
})();
"""
    write(ASSETS_DIR / "styles.css", css)
    write(ASSETS_DIR / "app.js", js)
    write(DOCS / ".nojekyll", "")


def validate_source_urls(actions: list[dict]) -> None:
    for action in actions:
        parsed = urlparse(action["doc_url"])
        if parsed.scheme != "https" or parsed.netloc != "business-api.tiktok.com":
            raise ValueError(f"Unexpected source domain for {action['tool_slug']}: {action['doc_url']}")


def build_zip() -> None:
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(ROOT.rglob("*")):
            if (
                not path.is_file()
                or ".git" in path.parts
                or "downloads" in path.parts
                or "__pycache__" in path.parts
                or path.suffix == ".pyc"
                or path.name in {"SHA256SUMS", ".DS_Store"}
            ):
                continue
            archive.write(path, Path("tiktok-ads-toolkit-contracts") / path.relative_to(ROOT))


def write_checksums() -> None:
    rows = []
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
            or path.name in {"SHA256SUMS", ".DS_Store"}
        ):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    write(ROOT / "SHA256SUMS", "\n".join(rows))


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    actions = manifest["actions"]
    if len(actions) != 63 or Counter(action["method"] for action in actions) != Counter({"GET": 40, "POST": 23}):
        raise ValueError("Manifest count drift: expected 63 actions (40 GET, 23 POST)")
    if len({action["tool_slug"] for action in actions}) != len(actions):
        raise ValueError("Duplicate tool slugs")
    validate_source_urls(actions)
    blocked = parse_blocked_rows()
    if len(blocked) != 53:
        raise ValueError(f"Blocked ledger drift: expected 53, found {len(blocked)}")
    if DOCS.exists():
        shutil.rmtree(DOCS)
    ACTIONS_DIR.mkdir(parents=True)
    ASSETS_DIR.mkdir(parents=True)
    write_permission_evidence(actions, manifest["metadata"])
    write_assets()
    mapping = render_action_pages(actions)
    render_index(actions, mapping, len(blocked))
    render_blocked(blocked)
    render_sources(actions, mapping)
    render_handoff(manifest)
    build_zip()
    write_checksums()
    print(f"Rendered {len(actions)} action pages, {len(blocked)} blocked rows, and {ZIP_PATH.name}")


if __name__ == "__main__":
    main()
