# TIKTOK_ADS_CAMPAIGN_LABEL_GET

- Operation: Get the campaign labels of an ad account
- Wire: `GET /campaign_label/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1851286489283585](https://business-api.tiktok.com/portal/docs?id=1851286489283585)
- Source content SHA-256: `0bde24742221001cfd5a8d482415fe1bd4cd055c3b5b7e200619c398e24579ab`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `campaign_label_ids` | `query` | `string[]` | `optional` | size: 50; rule: Each label ID must be a 19-digit numeric string; rule: Note : This filter is only supported in synchronous basic reports |
| `campaign_label_names` | `query` | `string[]` | `optional` | size: 10 |
| `campaign_label_types` | `query` | `string[]` | `optional` | allowed: GENERAL, MARKETING_EVENT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-1,000; rule: Value range: 1-1,000 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | rule: Details of the campaign labels within an ad account |
| `data.list[].campaign_label_id` | `string` | - |
| `data.list[].campaign_label_name` | `string` | - |
| `data.list[].campaign_label_type` | `string` | allowed: GENERAL, MARKETING_EVENT |
| `data.list[].campaign_label_color` | `string` | - |
| `data.list[].create_time` | `string` | rule: The time when the campaign label was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
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
