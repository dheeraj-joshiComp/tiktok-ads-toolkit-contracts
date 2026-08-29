# TIKTOK_ADS_CREATIVE_ASSET_DELETE

- Operation: Delete creative assets
- Wire: `POST /creative/asset/delete/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1797202997456897](https://business-api.tiktok.com/portal/docs?id=1797202997456897)
- Source content SHA-256: `0bd58a90ee28e07e62569743faa2a8525013424eae95c0171ead81ca7565619c`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `video_ids` | `json_body` | `string[]` | `optional` | rule: At most 50 IDs can be included in the list; max items: 50 |
| `image_ids` | `json_body` | `string[]` | `optional` | rule: At most 50 IDs can be included in the list; max items: 50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.failed_video_ids` | `string[]` | - |
| `data.failed_image_ids` | `string[]` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
