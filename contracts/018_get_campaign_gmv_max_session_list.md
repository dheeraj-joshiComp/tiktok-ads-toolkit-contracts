# TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_LIST

- Operation: Get max delivery or creative boost sessions within a campaign
- Wire: `GET /campaign/gmv_max/session/list/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1835246996436162](https://business-api.tiktok.com/portal/docs?id=1835246996436162)
- Source content SHA-256: `998acd282c3928c7d14832003656d9ad53e315cee1431a3930af9c08886d65a4`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `campaign_id` | `query` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.session_list` | `object[]` | rule: The list of max delivery sessions for products or creative boost sessions for videos within the Product GMV Max Campaign |
| `data.session_list[].campaign_id` | `string` | - |
| `data.session_list[].bid_type` | `string` | allowed: NO_BID, CREATIVE_NO_BID |
| `data.session_list[].session_id` | `string` | - |
| `data.session_list[].budget` | `float` | rule: Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget |
| `data.session_list[].product_list` | `object[]` | - |
| `data.session_list[].product_list[].spu_id` | `string` | - |
| `data.session_list[].schedule_type` | `string` | rule: SCHEDULE_FROM_NOW: To enable the max delivery or creative boost mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `data.session_list[].schedule_start_time` | `string` | rule: The start time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].schedule_end_time` | `string` | rule: The end time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
