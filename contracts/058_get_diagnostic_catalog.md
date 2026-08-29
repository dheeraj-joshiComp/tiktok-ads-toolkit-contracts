# TIKTOK_ADS_DIAGNOSTIC_CATALOG

- Operation: Get synchronous catalog product diagnostic information
- Wire: `GET /diagnostic/catalog/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `9`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `DPA Catalog Management`
- Source: [doc 1771117232728066](https://business-api.tiktok.com/portal/docs?id=1771117232728066)
- Source content SHA-256: `fba7db5edd98934e15bf79dfbde0b1370b854ea5b5ec62f0f679f53f93e2d50c`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `catalog_id` | `query` | `string` | `required` | - |
| `bc_id` | `query` | `string` | `required` | - |
| `feed_id` | `query` | `string` | `optional` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.issue_level` | `query` | `string` | `optional` | allowed: CRITICAL, WARNING |
| `filtering.issue_category` | `query` | `string` | `optional` | allowed: PRODUCT_ATTRIBUTES, PRODUCT_REVIEW, CATALOG, PIXEL_OR_EVENT, FILE_UPLOAD_OR_FEED |
| `lang` | `query` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: [1, 20]; rule: Value range: [1, 20] |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.diagnostic_date` | `string` | rule: The date (UTC +0 Time) when the diagnostic information was generated, in the format of "YYYY-MM-DD" |
| `data.issues` | `object[]` | - |
| `data.issues[].issue_id` | `string` | - |
| `data.issues[].issue_title` | `string` | - |
| `data.issues[].reason_and_suggestion` | `string` | - |
| `data.issues[].issue_level` | `string` | allowed: CRITICAL, WARNING |
| `data.issues[].issue_category` | `string` | allowed: PRODUCT_ATTRIBUTES, PRODUCT_REVIEW, CATALOG, PIXEL_OR_EVENT, FILE_UPLOAD_OR_FEED |
| `data.issues[].issue_product_field` | `string` | - |
| `data.issues[].affected_product_count` | `integer` | - |
| `data.issues[].affected_product_percentage` | `number` | range: [0,100]; rule: Value range: [0,100] |
| `data.issues[].example_affected_products` | `object[]` | - |
| `data.page_info` | `object` | - |
| `data.page_info.page` | `number` | - |
| `data.page_info.page_size` | `number` | - |
| `data.page_info.total_number` | `number` | - |
| `data.page_info.total_page` | `number` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
