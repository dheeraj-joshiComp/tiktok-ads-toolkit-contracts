# TIKTOK_ADS_GMV_MAX_OCCUPIED_CUSTOM_SHOP_ADS_LIST

- Operation: Check the occupancy of identities or products in Shopping Ads
- Wire: `GET /gmv_max/occupied_custom_shop_ads/list/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001136924674](https://business-api.tiktok.com/portal/docs?id=1822001136924674)
- Source content SHA-256: `633ec0ed19c4175cd4a83e4957ea797eecf2468dfc920537ab88561f5601a0c3`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `occupied_asset_type` | `query` | `string` | `required` | allowed: IDENTITY_TT_USER, IDENTITY_BC_AUTH_TT, IDENTITY_TTS_TT, SPU |
| `asset_ids` | `query` | `string[]` | `required` | size: 1; rule: When occupied_asset_type is SPU, specify the SPU ID of a product within the TikTok Shop via this field |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.occupied_custom_shop_ads` | `object[]` | - |
| `data.occupied_custom_shop_ads[].advertiser_id` | `string` | - |
| `data.occupied_custom_shop_ads[].campaign_id` | `string` | - |
| `data.occupied_custom_shop_ads[].adgroup_id` | `string` | - |
| `data.occupied_custom_shop_ads[].ad_id` | `string` | - |
| `data.occupied_custom_shop_ads[].create_time` | `string` | rule: The time when the ad group or ad was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
