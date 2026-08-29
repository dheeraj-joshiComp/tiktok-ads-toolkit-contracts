# TIKTOK_ADS_GMV_MAX_IDENTITY_GET

- Operation: Get identities for GMV Max Campaigns
- Wire: `GET /gmv_max/identity/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001101474882](https://business-api.tiktok.com/portal/docs?id=1822001101474882)
- Source content SHA-256: `dfa82f27673dc8e08fc532f1b72dd7f6d9c53474e520356f24a5a34e7db46479`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.identity_list` | `object[]` | - |
| `data.identity_list[].identity_id` | `string` | - |
| `data.identity_list[].identity_type` | `string` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.identity_list[].identity_authorized_bc_id` | `string` | presence: present when identity_type is BC_AUTH_TT |
| `data.identity_list[].identity_authorized_shop_id` | `string` | presence: Returned for some BC_AUTH_TT identities |
| `data.identity_list[].store_id` | `string` | presence: present when identity_type is TTS_TT |
| `data.identity_list[].profile_image` | `string` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.identity_list[].display_name` | `string` | - |
| `data.identity_list[].user_name` | `string` | - |
| `data.identity_list[].is_running_custom_shop_ads` | `bool` | allowed: true, false |
| `data.identity_list[].product_gmv_max_available` | `boolean` | allowed: true, false |
| `data.identity_list[].live_gmv_max_available` | `boolean` | allowed: true, false |
| `data.identity_list[].unavailable_reason` | `string` | allowed: OCCUPIED, UNAUTHORIZED; presence: present when live_gmv_max_available is false |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
