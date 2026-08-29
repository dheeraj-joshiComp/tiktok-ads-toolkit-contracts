# TIKTOK_ADS_CREATIVE_FATIGUE_GET

- Operation: Get Creative Fatigue Detection results
- Wire: `GET /creative_fatigue/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `4`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Reporting`
- Source: [doc 1767568466842626](https://business-api.tiktok.com/portal/docs?id=1767568466842626)
- Source content SHA-256: `6117eb0c814fc85b57770a4508d8f82d508f335ab64f8e43a02b65bbdc7b4672`
- Product/fixture gate: Creative Fatigue allowlist and delivered-ad history
- Live boundary: Read-only call permitted after fixture discovery
- Allowlist: `CREATIVE_FATIGUE`

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `ad_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `required` | - |
| `filtering.start_date` | `query` | `string` | `required` | rule: Query start date (closed interval), in the format of YYYY-MM-DD (advertiser account time zone); rule: You can only specify a date within the last 60 days |
| `filtering.end_date` | `query` | `string` | `required` | rule: Query end date (open interval), in the format of YYYY-MM-DD (advertiser account time zone); rule: You can only specify a date within the last 60 days |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: [1, 500]; rule: Value range: [1, 500] |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | - |
| `data.list[].adgroup_id` | `string` | - |
| `data.list[].ad_id` | `string` | - |
| `data.list[].date` | `string` | - |
| `data.list[].metrics` | `object` | - |
| `data.list[].metrics.has_fatigue` | `boolean` | - |
| `data.list[].metrics.fatigue_index` | `number` | - |
| `data.list[].metrics.dnu` | `number` | - |
| `data.list[].metrics.dnu_ratio` | `number` | rule: This metric is calculated by dividing the number of daily new users attracted by the ad on a specific date by the maximum number of daily new users that the ad attracted in the last 60 days |
| `data.list[].metrics.spend` | `number` | - |
| `data.list[].metrics.cost_per_conversion` | `number` | rule: This metric returns actual value when the ad is within a non-iOS 14 Dedicated Campaign, and returns 0; rule: 0 when the ad is within an iOS 14 Dedicated Campaign |
| `data.list[].metrics.skan_cost_per_conversion` | `number` | rule: This metric returns actual value when the ad is within an iOS 14 Dedicated Campaign, and returns 0; rule: 0 when the ad is within a non-iOS 14 Dedicated Campaign |
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
