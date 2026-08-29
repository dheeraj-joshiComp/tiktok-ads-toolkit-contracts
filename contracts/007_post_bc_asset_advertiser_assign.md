# TIKTOK_ADS_ASSIGN_TIKTOK_ACCOUNT_TO_ADVERTISER

- Operation: Link a TikTok account to an ad account in Business Center
- Wire: `POST /bc/asset/advertiser/assign/`
- Request encoding: `application/json`
- Ability hint: `updates`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1846868953025538](https://business-api.tiktok.com/portal/docs?id=1846868953025538)
- Source content SHA-256: `9d5688fc93f8886ebff538627510616da9010fd22a71ed365089135562ef2faf`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `asset_type` | `json_body` | `string` | `optional` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT; default: TT_ACCOUNT |
| `asset_id` | `json_body` | `string` | `required` | - |
| `advertiser_id` | `json_body` | `string` | `required` | rule: The ID of an ad account within the same Business Center to link the TikTok account to |

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
