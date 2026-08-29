# TIKTOK_ADS_SHOWCASE_PRODUCT_GET

- Operation: Get the available products in a Showcase
- Wire: `GET /showcase/product/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1759233576199169](https://business-api.tiktok.com/portal/docs?id=1759233576199169)
- Source content SHA-256: `e7036d54deb4ebca33282e6eecded98c7eae258c236dbb4a56929471bb6c517f`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `identity_id` | `query` | `string` | `required` | - |
| `identity_type` | `query` | `string` | `required` | allowed: TT_USER, BC_AUTH_TT |
| `identity_authorized_bc_id` | `query` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |
| `region_codes` | `query` | `string[]` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.item_group_ids` | `query` | `string[]` | `optional` | size: 10 |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: [1, 1000]; rule: Value range: [1, 1000] |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.showcase_products` | `object[]` | - |
| `data.showcase_products[].item_group_id` | `string` | - |
| `data.showcase_products[].title` | `string` | - |
| `data.showcase_products[].product_image_url` | `string` | - |
| `data.showcase_products[].min_price` | `string` | - |
| `data.showcase_products[].max_price` | `string` | rule: The maximum price of the product |
| `data.showcase_products[].currency` | `string` | - |
| `data.showcase_products[].category` | `string` | - |
| `data.showcase_products[].status` | `string` | allowed: AVAILABLE, NOT_AVAILABLE |
| `data.showcase_products[].catalog_id` | `string` | - |
| `data.showcase_products[].store_id` | `string` | rule: Note that the only supported store type is TikTok Shop |
| `data.page_info` | `object` | - |
| `data.page_info.page` | `number` | - |
| `data.page_info.page_size` | `number` | - |
| `data.page_info.total_number` | `number` | - |
| `data.page_info.total_page` | `number` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
