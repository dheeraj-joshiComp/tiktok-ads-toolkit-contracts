# TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_DELETE

- Operation: Delete customized TikTok posts
- Wire: `POST /gmv_max/creation/custom_anchor_video_list/delete/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1866513159202306](https://business-api.tiktok.com/portal/docs?id=1866513159202306)
- Source content SHA-256: `9e47aea82633f962e1b1aa351069ee60a70379158b2feec99946da4aa4c5572b`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `store_id` | `json_body` | `string` | `required` | - |
| `store_authorized_bc_id` | `json_body` | `string` | `required` | - |
| `custom_anchor_video_list` | `json_body` | `object[]` | `required` | size: 200 |
| `custom_anchor_video_list[].item_id` | `json_body` | `string` | `required` | - |
| `custom_anchor_video_list[].spu_id_list` | `json_body` | `string[]` | `required` | - |
| `campaign_id` | `json_body` | `string` | `conditional` | condition: the specified TikTok videos (item_id) have been used in a campaign to create campaign-level customized posts; rule: Required when the specified TikTok videos (item_id) have been used in a campaign to create campaign-level customized posts; rule: To retrieve existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |

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
