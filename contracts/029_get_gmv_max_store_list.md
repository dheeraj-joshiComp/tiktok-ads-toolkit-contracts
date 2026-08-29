# TIKTOK_ADS_GMV_MAX_STORE_LIST

- Operation: Get TikTok Shops for GMV Max Campaigns
- Wire: `GET /gmv_max/store/list/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001044479041](https://business-api.tiktok.com/portal/docs?id=1822001044479041)
- Source content SHA-256: `5fd083b5cf4fe023c7e1f1a95985c205115aa39f0990b84223acfb74610f8081`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
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
| `data.store_list` | `object[]` | - |
| `data.store_list[].store_id` | `string` | - |
| `data.store_list[].is_gmv_max_available` | `boolean` | allowed: true, false |
| `data.store_list[].store_authorized_bc_id` | `string` | - |
| `data.store_list[].is_owner_bc` | `boolean` | allowed: true, false |
| `data.store_list[].store_authorized_bc_info` | `object` | - |
| `data.store_list[].store_authorized_bc_info.bc_id` | `string` | - |
| `data.store_list[].store_authorized_bc_info.bc_profile_image` | `string` | - |
| `data.store_list[].store_authorized_bc_info.bc_name` | `string` | - |
| `data.store_list[].store_authorized_bc_info.user_role` | `string` | allowed: ADMIN, STANDARD; rule: The role of the user (member) within the Business Center |
| `data.store_list[].thumbnail_url` | `string` | - |
| `data.store_list[].store_name` | `string` | - |
| `data.store_list[].store_code` | `string` | - |
| `data.store_list[].targeting_region_codes` | `string[]` | - |
| `data.store_list[].store_status` | `string` | allowed: ACTIVE, INACTIVE, NEW_CREATE |
| `data.store_list[].store_role` | `string` | allowed: AD_PROMOTION, MANAGER, UNSET |
| `data.store_list[].exclusive_authorized_advertiser_info` | `object` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_id` | `string` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_name` | `string` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_status` | `string` | allowed: STATUS_ENABLE, STATUS_CONFIRM_FAIL, STATUS_PENDING_CONFIRM, STATUS_LIMIT, STATUS_CONTRACT_PENDING, STATUS_DISABLE, STATUS_PENDING_CONFIRM_MODIFY, STATUS_PENDING_VERIFIED, STATUS_SELF_SERVICE_UNAUDITED, STATUS_WA |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
