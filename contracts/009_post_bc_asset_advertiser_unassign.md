# TIKTOK_ADS_UNASSIGN_TIKTOK_ACCOUNT_FROM_ADVERTISER

- Operation: Unlink a TikTok account from an ad account in Business Center
- Wire: `POST /bc/asset/advertiser/unassign/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1855027260369921](https://business-api.tiktok.com/portal/docs?id=1855027260369921)
- Source content SHA-256: `144f681a3297baaada563d9d5eda0f8bca818907b32033bff88779f898ac3b80`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `asset_id` | `json_body` | `string` | `required` | - |
| `asset_type` | `json_body` | `string` | `required` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT |
| `advertiser_id` | `json_body` | `string` | `required` | rule: The ID of an ad account within the same Business Center to unlink the TikTok account from |

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
