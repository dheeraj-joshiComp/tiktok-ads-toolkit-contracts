# Yang: start here

## Goal

Add the 63 contract-complete TikTok Ads actions to the existing toolkit in the same Mercury PR. Do not restart the toolkit and do not open a second PR.

## Required order

1. Confirm the current head of `ComposioHQ/mercury#26271` and compare it with audited SHA `9f35c86a6ec3d56fe442046282803b79206f97a5`.
2. Read `manifest/contracts.json` and `evidence/permission-evidence.md`.
3. Execute Prompt 1 from `yang/implementation-prompts.md` only.
4. Return the final accepted batch SHA and test evidence.
5. For Prompt 2 onward, replace `<PREVIOUS_ACCEPTED_BATCH_SHA>` with the preceding accepted SHA.
6. Stop after each batch for independent review.

## Non-negotiable boundaries

- Implement only the 63 manifest entries.
- Do not implement the 53 entries in `evidence/blocked-paths.md`.
- Do not infer undocumented fields, response shapes, scopes, defaults, enums, or nullability.
- Keep Access-Token and developer secrets in auth. Never expose them as action inputs.
- Preserve the documented query, JSON, or multipart placement exactly.
- A POST method is not automatically safe. Classify ability and cleanup before any live call.
- Mocked tests prove serialization and shaping only. Report live status separately.
- Do not merge. Hand back the final SHA for independent preview QA.

## Why 63, not 116

The audit recovered full official contracts for 63 of 116 selected-endpoint gaps. The other 53 are blocked by missing contracts, provider contradictions, obsolete routes, separate auth designs, human connection flows, allowlists, or unsafe no-rollback behavior. Building those now would require fabrication or an unapproved live mutation.

## Source priority

1. `manifest/contracts.json`
2. Matching file in `contracts/`
3. Exact official TikTok URL and source fingerprint in `evidence/source-index.csv`
4. `evidence/gated-doc-audit.md` for contradiction notes

If these disagree, stop and report the exact action and fields. Do not choose one silently.
