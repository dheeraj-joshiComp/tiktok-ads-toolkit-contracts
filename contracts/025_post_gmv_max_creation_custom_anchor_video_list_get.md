# TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_GET

- Operation: Get customized TikTok posts
- Wire: `POST /gmv_max/creation/custom_anchor_video_list/get/`
- Request encoding: `application/json`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1866513156712449](https://business-api.tiktok.com/portal/docs?id=1866513156712449)
- Source content SHA-256: `aaa6a9a44e867cf77c783ad28377f465162f02a8c955cffe7ce0617a51db15dc`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `store_id` | `json_body` | `string` | `required` | - |
| `store_authorized_bc_id` | `json_body` | `string` | `required` | - |
| `creative_source` | `json_body` | `string` | `required` | allowed: CUSTOMIZED |
| `spu_id_list` | `json_body` | `string[]` | `optional` | - |
| `sort_field` | `json_body` | `string` | `optional` | allowed: GMV, POST_TIME, VIDEO_VIEWS, VIDEO_LIKES, CLICK_THROUGH_RATE, PRODUCT_CLICKS; default: GMV |
| `sort_type` | `json_body` | `string` | `optional` | allowed: ASC, DESC |
| `keyword` | `json_body` | `string` | `optional` | rule: To search by post ID (item_id), provide a numeric string with at least 19 characters |
| `need_auth_code_video` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |
| `identity_list` | `json_body` | `object[]` | `optional` | size: 20 |
| `identity_list[].identity_id` | `json_body` | `string` | `optional` | - |
| `identity_list[].identity_type` | `json_body` | `string` | `optional` | allowed: TT_USER, BC_AUTH_TT, TTS_TT |
| `identity_list[].identity_authorized_bc_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is BC_AUTH_TT |
| `identity_list[].identity_authorized_shop_id` | `json_body` | `string` | `optional` | rule: Required only when dentity_type is BC_AUTH_TT and identity_authorized_shop_id is returned for the identity from /gmv_max/identity/get/ |
| `identity_list[].store_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is TTS_TT |
| `campaign_id` | `json_body` | `string` | `optional` | rule: To retrieve existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `page` | `json_body` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `json_body` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.item_list` | `object[]` | - |
| `data.item_list[].item_id` | `string` | - |
| `data.item_list[].text` | `string` | - |
| `data.item_list[].spu_id_list` | `string[]` | - |
| `data.item_list[].can_change_anchor` | `boolean` | allowed: true, false; rule: false: You cannot use the video to create a customized post; rule: Note : If can_change_anchor is false, you cannot pass the video to custom_anchor_video_list or item_list in /campaign/gmv_max/create/ or /campaign/gmv_max/update/ to create customized posts |
| `data.item_list[].identity_info` | `object` | - |
| `data.item_list[].identity_info.identity_id` | `string` | - |
| `data.item_list[].identity_info.identity_type` | `string` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.item_list[].identity_info.identity_authorized_bc_id` | `string` | presence: present when identity_type is BC_AUTH_TT |
| `data.item_list[].identity_info.identity_authorized_shop_id` | `string` | presence: Returned for some BC_AUTH_TT identities |
| `data.item_list[].identity_info.store_id` | `string` | presence: present when identity_type is TTS_TT |
| `data.item_list[].identity_info.profile_image` | `string` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.item_list[].identity_info.display_name` | `string` | - |
| `data.item_list[].video_info` | `object` | - |
| `data.item_list[].video_info.video_id` | `string` | - |
| `data.item_list[].video_info.video_cover_url` | `string` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.item_list[].video_info.preview_url` | `string` | - |
| `data.item_list[].video_info.height` | `number` | - |
| `data.item_list[].video_info.width` | `number` | - |
| `data.item_list[].video_info.bit_rate` | `number` | - |
| `data.item_list[].video_info.duration` | `number` | - |
| `data.item_list[].video_info.size` | `number` | - |
| `data.item_list[].video_info.signature` | `string` | - |
| `data.item_list[].video_info.format` | `string` | rule: The format of the video |
| `data.item_list[].video_info.definition` | `string` | - |
| `data.item_list[].video_info.fps` | `number` | - |
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
