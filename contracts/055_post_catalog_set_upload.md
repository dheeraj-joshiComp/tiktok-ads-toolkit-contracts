# TIKTOK_ADS_CATALOG_SET_UPLOAD

- Operation: Create a product set by file
- Wire: `POST /catalog/set/upload/`
- Request encoding: `multipart/form-data`
- Ability hint: `creates-or-starts-job`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1846770644217858](https://business-api.tiktok.com/portal/docs?id=1846770644217858)
- Source content SHA-256: `44256152228005bc37ef2d50e1b041953edde9575866321a3b5c6127153bbcd9`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `multipart_form` | `string` | `required` | - |
| `catalog_id` | `multipart_form` | `string` | `required` | rule: To retrieve the list of E-commerce catalogs within a Business Center, use /catalog/get/ |
| `product_set_name` | `multipart_form` | `string` | `required` | length: 28 characters; rule: Length limit: 28 characters; rule: Note : Duplicate product set names are not supported |
| `file` | `multipart_form` | `file` | `required` | max rows: 5,000; file format: .csv only; rule: Recommended settings： Maximum row count: 5,000 |
| `file_signature` | `multipart_form` | `string` | `required` | meaning: MD5 hash of the uploaded file for integrity verification |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.product_set_id` | `string` | - |
| `data.product_set_name` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
