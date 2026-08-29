# TIKTOK_ADS_CHANGELOG_GET

- Operation: Get the activity log of a Business Center
- Wire: `GET /changelog/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1820767460168705](https://business-api.tiktok.com/portal/docs?id=1820767460168705)
- Source content SHA-256: `d962772a9cea251318e89d38e28f17d0363bc3defeb0fa35ece67676e1ab8b07`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.start_date` | `query` | `string` | `optional` | rule: Query start date, in the format of YYYY-MM-DD (UTC+0); rule: Recommended date range: six months |
| `filtering.end_date` | `query` | `string` | `optional` | rule: Query end date, in the format of YYYY-MM-DD (UTC+0); rule: Recommended date range: six months |
| `filtering.activity_type` | `query` | `string` | `optional` | allowed: ALL, USER, ACCOUNT, ASSET, BUSINESS; default: ALL |
| `lang` | `query` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `sort_field` | `query` | `string` | `optional` | allowed: operation_time; default: operation_time; rule: Enum value: operation_time: To sort by the time when the activity occurred, which corresponds to the time parameter within the returned object array changelog_list |
| `sort_type` | `query` | `string` | `optional` | allowed: DESC, ASC; default: DESC |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.changelog_list` | `object[]` | - |
| `data.changelog_list[].time` | `string` | rule: The time of the activity, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.changelog_list[].activity_type` | `string` | allowed: USER, ACCOUNT, ASSET, BUSINESS |
| `data.changelog_list[].operator_id` | `string` | - |
| `data.changelog_list[].activity_log` | `string` | - |
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
