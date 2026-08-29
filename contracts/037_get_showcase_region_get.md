# TIKTOK_ADS_SHOWCASE_REGION_GET

- Operation: Get the available regions for a Showcase via identity
- Wire: `GET /showcase/region/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1759233561597954](https://business-api.tiktok.com/portal/docs?id=1759233561597954)
- Source content SHA-256: `ff69b373cb153d23621c00fc0e22da3ab46ffb08d9bcf10906f0b295044def07`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `identity_id` | `query` | `string` | `required` | - |
| `identity_type` | `query` | `string` | `required` | allowed: TT_USER, BC_AUTH_TT |
| `identity_authorized_bc_id` | `query` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.region_codes` | `string[]` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
