# TIKTOK_ADS_LIST_ADVERTISER_ASSIGNED_TIKTOK_ACCOUNTS

- Operation: Get ad accounts linked to a TikTok account in Business Center
- Wire: `GET /bc/asset/advertiser/assigned/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1855027294743554](https://business-api.tiktok.com/portal/docs?id=1855027294743554)
- Source content SHA-256: `78ccb6a44226bf235871b3fbc6ab01bbd7fd4810e5dcb7db3a8ffe1ff60d7bb5`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `asset_id` | `query` | `string` | `required` | - |
| `asset_type` | `query` | `string` | `required` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | - |
| `data.list[].advertiser_id` | `string` | - |
| `data.list[].advertiser_name` | `string` | - |
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
