# TIKTOK_ADS_GMV_MAX_STORE_SHOP_AD_USAGE_CHECK

- Operation: Check the availability of a TikTok Shop for Product GMV Max Campaigns
- Wire: `GET /gmv_max/store/shop_ad_usage_check/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1822001084174338](https://business-api.tiktok.com/portal/docs?id=1822001084174338)
- Source content SHA-256: `a21b20096df419e79a25f3a4d0cbc4e0fdcafa27aeb41a45dbd7fb34c8a40c5c`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.promote_all_products_allowed` | `boolean` | allowed: true, false |
| `data.is_running_custom_shop_ads` | `boolean` | allowed: true, false |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
