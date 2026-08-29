# TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_CREATE

- Operation: Create an asynchronous download task for catalog product diagnostic information
- Wire: `POST /diagnostic/catalog/product/task/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1771117279175682](https://business-api.tiktok.com/portal/docs?id=1771117279175682)
- Source content SHA-256: `e607f404d890626f71027c07f1289b6a15c3ee5c7df8693c65938477b2e74c90`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `catalog_id` | `json_body` | `string` | `required` | - |
| `bc_id` | `json_body` | `string` | `required` | - |
| `feed_id` | `json_body` | `string` | `optional` | - |
| `lang` | `json_body` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `issue_id` | `json_body` | `string` | `optional` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.task_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
