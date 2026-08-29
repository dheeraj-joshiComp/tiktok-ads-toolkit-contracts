# Two endpoint manifest requested by Yang

# TIKTOK_ADS_CAMPAIGN_GMV_MAX_CREATIVE_UPDATE

- Operation: Remove or add back creatives in a GMV Max Campaign
- Wire: `POST /campaign/gmv_max/creative/update/`
- Request encoding: `application/json`
- Ability hint: `updates`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1861260625563202](https://business-api.tiktok.com/portal/docs?id=1861260625563202)
- Source content SHA-256: `9d077f9afc9adc49cb4969945311060291576b4bf3b709d8e5a4a5506d6acdf0`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: Note : The campaign must be in an active status; rule: If the campaign is a Product GMV Max Campaign, the product_video_specific_type of the campaign must be AUTO_SELECTION |
| `action` | `json_body` | `string` | `required` | allowed: REMOVE, ADD; rule: Note : Once the action is performed, wait 20 minutes before verifying the updated statuses using /gmv_max/report/get/ |
| `item_list` | `json_body` | `object[]` | `required` | size: 400; rule: Note : This endpoint allows for the removal of up to 10,000 posts from a GMV Max Campaign, with a limit of 400 posts per request |
| `item_list[].item_id` | `json_body` | `string` | `required` | - |
| `item_list[].spu_id_list` | `json_body` | `string[]` | `conditional` | rule: Required for a Product GMV Max Campaign |

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


# TIKTOK_ADS_GMV_MAX_VIDEO_GET

- Operation: Get posts for a Product GMV Max Campaign
- Wire: `GET /gmv_max/video/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001168512129](https://business-api.tiktok.com/portal/docs?id=1822001168512129)
- Source content SHA-256: `206057c962ca308160135fbcb9eb43f9411f3b4322c0f755f8103f75b937245a`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |
| `spu_id_list` | `query` | `string[]` | `optional` | size rule: When custom_posts_eligible is false or not specified: 50.; size rule: When custom_posts_eligible is true: 1. |
| `custom_posts_eligible` | `query` | `boolean` | `optional` | allowed: true, false; default: false; cross-field: when true, spu_id_list must contain exactly 1 product |
| `sort_field` | `query` | `string` | `optional` | allowed: GMV, POST_TIME, VIDEO_VIEWS, VIDEO_LIKES, CLICK_THROUGH_RATE, PRODUCT_CLICKS; default: GMV; rule: Valid only when custom_posts_eligible is false or not provided |
| `sort_type` | `query` | `string` | `optional` | allowed: ASC, DESC; default: DESC; cross-field: for authorized-post sorting, provide sort_field and sort_type together |
| `keyword` | `query` | `string` | `optional` | rule: To search by post ID (item_id), provide a numeric string with at least 19 characters |
| `need_auth_code_video` | `query` | `boolean` | `optional` | allowed: true, false; default: false; result rule: when need_auth_code_video is false or omitted and identity_list is omitted, item_list is empty |
| `identity_list` | `query` | `object[]` | `optional` | size: 20; result rule: when need_auth_code_video is false or omitted and identity_list is omitted, item_list is empty |
| `identity_list[].identity_id` | `query` | `string` | `optional` | - |
| `identity_list[].identity_type` | `query` | `string` | `optional` | allowed: TT_USER, BC_AUTH_TT, TTS_TT |
| `identity_list[].identity_authorized_bc_id` | `query` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |
| `identity_list[].identity_authorized_shop_id` | `query` | `string` | `conditional` | condition: required for BC_AUTH_TT only when /gmv_max/identity/get returns identity_authorized_shop_id for that identity |
| `identity_list[].store_id` | `query` | `string` | `conditional` | condition: identity_type is TTS_TT; rule: Required when identity_type is TTS_TT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

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
| `data.item_list[].spu_id_list` | `string[]` | presence: absent for videos without a product anchor |
| `data.item_list[].can_change_anchor` | `boolean` | allowed: true, false; rule: false: You cannot use the video to create a customized post; rule: Note : If can_change_anchor is false, you cannot pass the video to custom_anchor_video_list or item_list in /campaign/gmv_max/create/ or /campaign/gmv_max/update/ to create customized posts |
| `data.item_list[].identity_info` | `object` | - |
| `data.item_list[].identity_info.identity_id` | `string` | - |
| `data.item_list[].identity_info.identity_type` | `string` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.item_list[].identity_info.identity_authorized_bc_id` | `string` | presence: present when identity_type is BC_AUTH_TT |
| `data.item_list[].identity_info.identity_authorized_shop_id` | `string` | presence: Returned for some BC_AUTH_TT identities |
| `data.item_list[].identity_info.store_id` | `string` | presence: present when identity_type is TTS_TT |
| `data.item_list[].identity_info.profile_image` | `string` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds; temporary URL: approximately 48 hours |
| `data.item_list[].identity_info.display_name` | `string` | - |
| `data.item_list[].video_info` | `object` | - |
| `data.item_list[].video_info.video_id` | `string` | - |
| `data.item_list[].video_info.video_cover_url` | `string` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds; temporary URL: approximately 24 hours |
| `data.item_list[].video_info.preview_url` | `string` | temporary URL: 6 hours |
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
