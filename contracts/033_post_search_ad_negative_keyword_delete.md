# TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_DELETE

- Operation: Delete negative keywords
- Wire: `POST /search_ad/negative_keyword/delete/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1775104910010369](https://business-api.tiktok.com/portal/docs?id=1775104910010369)
- Source content SHA-256: `477bd35e4df4aa8de417a7b2f3740783a67d386e74a77010656021bb503278f1`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `object_type` | `json_body` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_id` | `json_body` | `string` | `required` | - |
| `keyword_ids` | `json_body` | `string[]` | `required` | size: 1,000 |

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
