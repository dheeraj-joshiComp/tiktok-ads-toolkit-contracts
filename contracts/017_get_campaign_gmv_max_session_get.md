# TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_GET

- Operation: Get details of max delivery or creative boost sessions
- Wire: `GET /campaign/gmv_max/session/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1835247031331842](https://business-api.tiktok.com/portal/docs?id=1835247031331842)
- Source content SHA-256: `961501f7635a62eee76b4a9ec9e95a793b1dd9bb5a1de53b610791f8462bb20a`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `session_ids` | `query` | `string[]` | `required` | size: 20 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.session_list` | `object[]` | - |
| `data.session_list[].campaign_id` | `string` | - |
| `data.session_list[].bid_type` | `string` | allowed: NO_BID, CREATIVE_NO_BID |
| `data.session_list[].session_id` | `string` | - |
| `data.session_list[].budget` | `float` | rule: Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget |
| `data.session_list[].product_list` | `object[]` | - |
| `data.session_list[].product_list[].spu_id` | `string` | - |
| `data.session_list[].schedule_type` | `string` | rule: SCHEDULE_FROM_NOW: To enable the max delivery or creative boost mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `data.session_list[].schedule_start_time` | `string` | rule: The start time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].schedule_end_time` | `string` | rule: The end time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].item_id` | `string` | presence: present when bid_type is CREATIVE_NO_BID |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
