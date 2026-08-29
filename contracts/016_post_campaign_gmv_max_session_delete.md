# TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_DELETE

- Operation: Delete a max delivery or creative boost session
- Wire: `POST /campaign/gmv_max/session/delete/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1835246983475217](https://business-api.tiktok.com/portal/docs?id=1835246983475217)
- Source content SHA-256: `787506a4cf488f817f2dceef7b33fa6c0297c73ea56b596fb9a58c10f479ff75`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |

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
