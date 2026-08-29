# TIKTOK_ADS_CATALOG_VIDEO_GET

- Operation: Get the uploaded catalog videos within a catalog
- Wire: `GET /catalog/video/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1803655082498050](https://business-api.tiktok.com/portal/docs?id=1803655082498050)
- Source content SHA-256: `181c80df54aa42247a05dd7a9c44760421e304353af40355f7ae98e59148e9e7`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `catalog_id` | `query` | `string` | `required` | - |
| `catalog_video_ids` | `query` | `string[]` | `optional` | size: 50 |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.videos` | `object[]` | - |
| `data.videos[].catalog_video_id` | `string` | - |
| `data.videos[].video_name` | `string` | - |
| `data.videos[].video_link` | `string` | - |
| `data.videos[].sku_id_list` | `string[]` | - |
| `data.videos[].category` | `string` | - |
| `data.videos[].brand` | `string` | - |
| `data.videos[].creator` | `string` | - |
| `data.videos[].video_type` | `string` | - |
| `data.videos[].description` | `string` | - |
| `data.videos[].landing_page_url` | `string` | - |
| `data.videos[].custom_label_0` | `string` | - |
| `data.videos[].custom_label_1` | `string` | - |
| `data.videos[].custom_label_2` | `string` | - |
| `data.videos[].custom_label_3` | `string` | - |
| `data.videos[].custom_label_4` | `string` | - |
| `data.videos[].video_id` | `string` | rule: The video ID generated after the video extraction is complete |
| `data.videos[].video_signature` | `string` | - |
| `data.videos[].status` | `string` | allowed: PENDING, SUCCESS, FAILED |
| `data.videos[].create_time` | `string` | rule: The time when the video upload was completed, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.videos[].active_status` | `string` | allowed: ACTIVATED, DEACTIVATED; rule: DEACTIVATED: The video is deactivated and cannot be used for ad delivery |
| `data.videos[].preview_url` | `string` | presence: present when status is SUCCESS; rule: The video preview link, which is valid for six hours and needs to be re-acquired after expiration |
| `data.page_info` | `object` | - |
| `data.page_info.page` | `integer` | - |
| `data.page_info.page_size` | `integer` | - |
| `data.page_info.total_number` | `integer` | - |
| `data.page_info.total_page` | `integer` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
