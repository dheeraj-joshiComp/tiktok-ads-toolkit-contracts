# TIKTOK_ADS_CHECK_UNIONPAY_VERIFICATION_REQUIREMENT

- Operation: Check the UnionPay verification requirement for a business license
- Wire: `GET /bc/advertiser/unionpay_info/check/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1813772238056449](https://business-api.tiktok.com/portal/docs?id=1813772238056449)
- Source content SHA-256: `9aa9453f4ca7342bccd5118164e4ff74a4d25f47e821603ee6ee891b2075d1a2`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `license_no` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.unionpay_verification_required` | `boolean` | allowed: true, false; any-of: true: required. || false: not required.; rule: Whether UnionPay verification is required for the business license; rule: Supported values: true: required |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
