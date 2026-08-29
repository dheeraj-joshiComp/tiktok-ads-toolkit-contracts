# TikTok Ads toolkit contract kit

Private, evidence-first handoff for expanding the Composio `tiktok_ads` toolkit without inventing provider contracts.

The provider-selected export contains 160 endpoints. At the pinned audit point, 44 of those were already represented, 63 missing endpoints had complete official contracts, and 53 missing endpoints remained blocked. This repository packages the 63 contract-complete candidates as 40 GET actions and 23 POST actions.

## Start here

1. Read [`YANG_START_HERE.md`](YANG_START_HERE.md).
2. Run only Prompt 1 from [`yang/implementation-prompts.md`](yang/implementation-prompts.md).
3. Use [`manifest/contracts.json`](manifest/contracts.json) as the machine-readable source of truth.
4. Do not implement anything in [`evidence/blocked-paths.md`](evidence/blocked-paths.md).
5. Open [`docs/index.html`](docs/index.html) for the searchable offline HTML reference.

## What is included

| Path | Purpose |
|---|---|
| `contracts/` | One normalized Markdown contract per candidate action |
| `manifest/contracts.json` | Complete request, response, constraint, permission, fixture, and live-boundary manifest |
| `yang/implementation-prompts.md` | Ten sequential implementation batches |
| `yang/two-endpoint-manifest.md` | Standalone contracts for the two endpoints Yang requested explicitly |
| `evidence/selected-endpoints.json` | Provider-selected v2.0 endpoint export with the developer app ID redacted |
| `evidence/permission-evidence.*` | Action-to-category-to-parent-scope mapping |
| `evidence/blocked-paths.md` | Fifty-three paths that must not be fabricated from current evidence |
| `evidence/source-index.csv` | Exact official URL, document ID, and source-content fingerprint for every candidate |
| `evidence/gated-doc-audit.md` | Recovery decisions and known provider contradictions |
| `evidence/us-runtime-eligibility.md` | US applicability and fixture/allowlist boundaries |
| `docs/` | Searchable static HTML reference with one page per action |
| `downloads/` | Sanitized offline ZIP for direct handoff |

## Evidence boundary

- Every candidate has request fields, placement, types, requiredness, constraints, response fields, an official TikTok URL, and a SHA-256 provenance fingerprint.
- The fingerprints identify the official source content observed during the audit. The original authenticated portal snapshots are deliberately not redistributed here.
- This repository contains normalized schema facts, not a mirror of TikTok's gated portal, HARs, cookies, screenshots, or credentials.
- Contract completeness supports implementation and mocked contract tests. It does not prove that a customer account is entitled to execute an endpoint.
- Live certification still depends on OAuth approval, advertiser/Business Center roles, product eligibility, allowlists, real fixtures, and safe cleanup for mutations.

## Rebuild and verify

Requires Python 3 and no third-party packages.

```bash
python3 scripts/render_site.py
python3 scripts/verify_pack.py
python3 -m http.server 8000 --directory docs
```

Then open `http://localhost:8000`.

## Frozen target

- Mercury PR: `ComposioHQ/mercury#26271`
- Audited SHA: `9f35c86a6ec3d56fe442046282803b79206f97a5`
- Evidence date: `2026-08-30`

Before implementation, compare the current PR head with the audited SHA. If it moved, review the diff first. Mercury was not modified while assembling this repository.
