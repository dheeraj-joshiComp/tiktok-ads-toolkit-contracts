# TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_GET

- Operation: Download asynchronous catalog product diagnostic information
- Wire: `GET /diagnostic/catalog/product/task/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1771117294731266](https://business-api.tiktok.com/portal/docs?id=1771117294731266)
- Source content SHA-256: `f24df2e0e8cb2a7c0570010cb7eb5d1cc377dd52ab923e29c7c44a59e9101622`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `catalog_id` | `query` | `string` | `required` | - |
| `bc_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.status` | `string` | allowed: SUCCEED, PROCESSING, FAILED |
| `data.diagnostic_file_url` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
