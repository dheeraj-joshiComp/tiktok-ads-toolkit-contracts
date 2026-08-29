# TIKTOK_ADS_BUSINESS_SPARK_AD_CREATE

- Operation: Create a campaign, an ad group, and a Spark Ad in one step
- Wire: `POST /business/spark_ad/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1829744071179330](https://business-api.tiktok.com/portal/docs?id=1829744071179330)
- Source content SHA-256: `e79299d9800b72d9552be44b3ef51c2755550987aec87225d8e739c18028a3d2`
- Product/fixture gate: Authorized TikTok identity/post and a disposable non-delivering campaign fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST
- Additional enum source: [doc 1737174886619138](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `objective_type` | `json_body` | `string` | `optional` | allowed: REACH, TRAFFIC, VIDEO_VIEWS, ENGAGEMENT |
| `adgroup_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `saved_audience_id` | `json_body` | `string` | `optional` | rule: Either saved_audience_id or location_ids is required; rule: Before using this field, call /dmp/saved_audience/create/ to create a Saved Audience and get the Saved Audience ID in response |
| `location_ids` | `json_body` | `string[]` | `optional` | size: 3,000; rule: Either saved_audience_id or location_ids is required |
| `gender` | `json_body` | `string` | `optional` | allowed: GENDER_FEMALE, GENDER_MALE, GENDER_UNLIMITED |
| `age_groups` | `json_body` | `string[]` | `optional` | allowed: AGE_13_17, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45_54, AGE_55_100 |
| `budget_mode` | `json_body` | `string` | `optional` | allowed: BUDGET_MODE_TOTAL, BUDGET_MODE_DAY; rule: If this field is set to BUDGET_MODE_TOTAL, then schedule_type must be SCHEDULE_START_END, which requires an end date (schedule_end_time) |
| `budget` | `json_body` | `float` | `optional` | - |
| `schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_START_END, SCHEDULE_FROM_NOW; rule: If budget_mode is BUDGET_MODE_TOTAL, this field must be set to SCHEDULE_START_END; rule: SCHEDULE_FROM_NOW: To run the campaign continuously after the scheduled start time |
| `schedule_start_time` | `json_body` | `string` | `optional` | rule: Schedule start time (UTC+0), in the format of YYYY-MM-DD HH:MM:SS; rule: The start time can be up to 12 hours earlier than the current time, but cannot be later than 2028-01-01 00:00:00 |
| `schedule_end_time` | `json_body` | `string` | `optional` | rule: Required when schedule_type is SCHEDULE_START_END; rule: Schedule end time (UTC+0), in the format of YYYY-MM-DD HH:MM:SS; rule: The end time cannot be later than 2038-01-01 00:00:00 |
| `optimization_goal` | `json_body` | `string` | `optional` | mapping: REACH=>REACH; TRAFFIC=>CLICK|TRAFFIC_LANDING_PAGE_VIEW; VIDEO_VIEWS=>ENGAGED_VIEW; ENGAGEMENT=>FOLLOWERS|PAGE_VISIT |
| `frequency` | `json_body` | `number` | `optional` | all-of: frequency range: 1–1,000. || frequency_schedule: 1–30 (days).; rule: Required when objective_type is REACH; rule: Frequency, the maximum number of times a user can see your ad within a given period; rule: The following conditions should be both met: frequency range: 1–1,000; rule: For instance, frequency = 2 and frequency_schedule = 3 ensure ads are shown no more than twice every three days |
| `frequency_schedule` | `json_body` | `number` | `optional` | all-of: frequency range: 1–1,000. || frequency_schedule: 1–30 (days).; rule: Required when objective_type is REACH; rule: The following conditions should be both met: frequency range: 1–1,000; rule: For instance, frequency = 2 and frequency_schedule = 3 ensure ads are shown no more than twice every three days |
| `bid_type` | `json_body` | `string` | `optional` | allowed: BID_TYPE_CUSTOM, BID_TYPE_NO_BID; default: BID_TYPE_NO_BID; rule: BID_TYPE_NO_BID: Maximum Delivery |
| `bid_price` | `json_body` | `number` | `optional` | all-of: optimization_goal is REACH, CLICK, PAGE_VISIT, or ENGAGED_VIEW. || bid_type is BID_TYPE_CUSTOM.; rule: Required when the following conditions are both met: optimization_goal is REACH, CLICK, PAGE_VISIT, or ENGAGED_VIEW |
| `conversion_bid_price` | `json_body` | `float` | `optional` | all-of: optimization_goal is TRAFFIC_LANDING_PAGE_VIEW, or FOLLOWERS. || bid_type is BID_TYPE_CUSTOM.; rule: Required when the following conditions are both met: optimization_goal is TRAFFIC_LANDING_PAGE_VIEW, or FOLLOWERS |
| `ad_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: The format of the auto-generated ad name is ad ID (ad_id); rule: Length limit: 512 characters; rule: Emojis are not supported |
| `identity_type` | `json_body` | `string` | `optional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT |
| `identity_id` | `json_body` | `string` | `optional` | - |
| `identity_authorized_bc_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is BC_AUTH_TT |
| `tiktok_item_id` | `json_body` | `string` | `optional` | - |
| `call_to_action` | `json_body` | `string` | `optional` | rule: Required when optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `landing_page_url` | `json_body` | `string` | `optional` | any-of: optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT. || optimization_goal is REACH or ENGAGED_VIEW and call_to_action is specified.; rule: Required in any of the following conditions: optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT; rule: Not supported when optimization_goal is FOLLOWERS or PAGE_VISIT |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.campaign_id` | `string` | - |
| `data.adgroup_id` | `string` | rule: The ID of the ad group created within the campaign |
| `data.ad_id` | `string` | rule: The ID of the Spark Ad created within the ad group |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
