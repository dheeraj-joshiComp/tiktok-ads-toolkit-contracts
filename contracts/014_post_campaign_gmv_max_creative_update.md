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
