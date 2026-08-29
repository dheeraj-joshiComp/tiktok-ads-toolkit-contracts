# TIKTOK_ADS_GET_ASSET_BINDING_QUOTA

- Operation: Get binding info of an asset
- Wire: `GET /asset/bind/quota/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ad Account Management`
- Source: [doc 1739659584022529](https://business-api.tiktok.com/portal/docs?id=1739659584022529)
- Source content SHA-256: `3fcb3f397a3351613c0566e63bbaba7de3d32282637ff265239d1c57711673d8`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `asset_id` | `query` | `string` | `required` | - |
| `asset_type` | `query` | `string` | `required` | allowed: IDENTITY |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.total_quota` | `number` | - |
| `data.used_quota` | `number` | - |
| `data.available_quota` | `number` | - |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
