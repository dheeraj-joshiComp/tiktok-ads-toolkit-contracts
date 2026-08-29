# TIKTOK_ADS_CATALOG_INSIGHT_PRODUCT_GET

- Operation: Get trending catalog products
- Wire: `GET /catalog/insight/product/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1805640886872066](https://business-api.tiktok.com/portal/docs?id=1805640886872066)
- Source content SHA-256: `8d997a4bf89661ceb30c794a08020d416827c69e0399669f18f79972d20f784e`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `catalog_id` | `query` | `string` | `required` | rule: The catalog needs to be an E-commerce catalog that contains at least 20 products; rule: To verify that the catalog contains at least 20 products, use /catalog/overview/ and check whether the sum of the values of the returned approved, rejected, and processing fields is equal to or greate |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.category_ids` | `query` | `string[]` | `conditional` | size: 50; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |
| `filtering.brands` | `query` | `string[]` | `conditional` | size: 50; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |
| `filtering.availabilities` | `query` | `string[]` | `conditional` | allowed: IN_STOCK, AVAILABLE_FOR_ORDER, PREORDER, OUT_OF_STOCK, DISCONTINUED; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.product_insights` | `object[]` | rule: The list of up to 50 trending products within the E-commerce catalog, sorted in descending order by popularity |
| `data.product_insights[].product_id` | `string` | - |
| `data.product_insights[].image_url` | `string` | - |
| `data.product_insights[].title` | `string` | - |
| `data.product_insights[].description` | `string` | - |
| `data.product_insights[].sku_id` | `string` | - |
| `data.product_insights[].category_info` | `object` | - |
| `data.product_insights[].category_info.category_id` | `string` | rule: The TikTok product category ID assigned to the product, consisting of three levels separated by the number sign (#), in the format of "level_id_1#level_id_2#level_id_3" |
| `data.product_insights[].category_info.level_info` | `object` | - |
| `data.product_insights[].category_info.level_info.level_id_1` | `string` | - |
| `data.product_insights[].category_info.level_info.level_name_1` | `string` | - |
| `data.product_insights[].category_info.level_info.level_id_2` | `string` | - |
| `data.product_insights[].category_info.level_info.level_name_2` | `string` | - |
| `data.product_insights[].category_info.level_info.level_id_3` | `string` | - |
| `data.product_insights[].category_info.level_info.level_name_3` | `string` | - |
| `data.product_insights[].brand` | `string` | - |
| `data.product_insights[].price` | `object` | - |
| `data.product_insights[].price.price` | `float` | - |
| `data.product_insights[].price.currency` | `string` | - |
| `data.product_insights[].price.sale_price` | `float` | - |
| `data.product_insights[].price.sale_price_effective_date` | `string[]` | - |
| `data.product_insights[].availability` | `string` | allowed: IN_STOCK, AVAILABLE_FOR_ORDER, PREORDER, OUT_OF_STOCK, DISCONTINUED |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
