# Evidence notes

- `selected-endpoints.json` is the v2.0 provider-selected endpoint export with the developer app ID redacted. Its endpoint/category structure is preserved.
- `permission-evidence.json` and `.md` are derived from the normalized contract manifest. They make the 17 direct permission mappings and 46 category-inheritance mappings explicit.
- `source-index.csv` points to the official provider pages. `contract_sha256` is a provenance fingerprint of the provider content observed during the audit; the gated source snapshot is not bundled.
- `blocked-paths.md` is a stop list, not a backlog of contracts that may be guessed.
- `gated-doc-audit.md` and `us-runtime-eligibility.md` separate implementation evidence from provider-account runtime eligibility.
