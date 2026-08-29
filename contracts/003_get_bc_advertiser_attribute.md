# TIKTOK_ADS_GET_BUSINESS_CENTER_ADVERTISER_ATTRIBUTES

- Operation: Get currencies and registration areas for ad accounts
- Wire: `GET /bc/advertiser/attribute/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1775752357139457](https://business-api.tiktok.com/portal/docs?id=1775752357139457)
- Source content SHA-256: `6e5ee0ef6fec74745469193703d3fe1e480a4dd85994c777178bbbe224eb3765`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.currencies` | `string[]` | - |
| `data.region_codes` | `string[]` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
