# TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_UPDATE

- Operation: Update a max delivery or creative boost session
- Wire: `POST /campaign/gmv_max/session/update/`
- Request encoding: `application/json`
- Ability hint: `updates`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1835247009119233](https://business-api.tiktok.com/portal/docs?id=1835247009119233)
- Source content SHA-256: `159adc3e85e3aaf75bb562f78d5c581bff3e985e5129d353e9e069a1b69663b8`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

### Variant: Parameters for updating a max delivery session

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.budget` | `json_body` | `float` | `optional` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; rule: Enum values: SCHEDULE_FROM_NOW: To enable the max delivery mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `session.schedule_start_time` | `json_body` | `string` | `optional` | rule: The start time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The start time cannot be earlier than the current time + 5 minutes |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |

### Variant: Parameters for updating a creative boost session

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.budget` | `json_body` | `float` | `optional` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; default: SCHEDULE_FROM_NOW; rule: Enum values: SCHEDULE_FROM_NOW: To enable creative boost for the product continuously after the current time, until the campaign scheduled end time |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for creative boost, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
