# TIKTOK_ADS_SHOWCASE_IDENTITY_GET

- Operation: Get identities with Showcase permission under an ad account
- Wire: `GET /showcase/identity/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1759233549899778](https://business-api.tiktok.com/portal/docs?id=1759233549899778)
- Source content SHA-256: `d508b8237854da58393fd458aa976cea01333713220ca87f0aabb789548033cb`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `identity_id` | `string` | - |
| `identity_type` | `string` | allowed: TT_USER, BC_AUTH_TT |
| `identity_authorized_bc_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
