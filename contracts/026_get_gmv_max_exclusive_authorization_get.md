# TIKTOK_ADS_GMV_MAX_EXCLUSIVE_AUTHORIZATION_GET

- Operation: Get the TikTok Shop exclusive authorization status of an ad account
- Wire: `GET /gmv_max/exclusive_authorization/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001184635905](https://business-api.tiktok.com/portal/docs?id=1822001184635905)
- Source content SHA-256: `5e374d4fbc38767cb9d30d1a0409df85f01b69bdbd84b5a7c3388e94d5a2feb3`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |
| `advertiser_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.store_id` | `string` | - |
| `data.advertiser_id` | `string` | - |
| `data.authorization_status` | `string` | allowed: EFFECTIVE, INEFFECTIVE, UNAUTHORIZED |
| `data.advertiser_name` | `string` | - |
| `data.advertiser_status` | `string` | allowed: STATUS_ENABLE, STATUS_CONFIRM_FAIL, STATUS_PENDING_CONFIRM, STATUS_LIMIT, STATUS_CONTRACT_PENDING, STATUS_DISABLE, STATUS_PENDING_CONFIRM_MODIFY, STATUS_PENDING_VERIFIED, STATUS_SELF_SERVICE_UNAUDITED, STATUS_WA |
| `data.identity_id` | `string` | presence: present when an official TikTok account is set for the TikTok Shop |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
