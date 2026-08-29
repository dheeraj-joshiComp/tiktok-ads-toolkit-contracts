# TIKTOK_ADS_DISABLE_BUSINESS_CENTER_ADVERTISER

- Operation: Disable an ad account
- Wire: `POST /bc/advertiser/disable/`
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`
- Parent scope: `1`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ad Account Management`
- Source: [doc 1752349244331009](https://business-api.tiktok.com/portal/docs?id=1752349244331009)
- Source content SHA-256: `74d802fe5befc9bffbe400e6aa3d829a47780eb8ca0b07e0d1c6daeadeb675f8`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `advertiser_ids` | `json_body` | `string[]` | `required` | size: 1 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.disabled_advertiser_ids` | `string[]` | - |
| `data.failed_infos` | `map` | allowed: DELIVERING, UNPAID_BILL, SUSPENDED, UNFINISHED_TRANSFER, AUTOPAY_UNBILLED; rule: Enum values: DELIVERING: The ad account has ads that are being delivered within 3 days |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
