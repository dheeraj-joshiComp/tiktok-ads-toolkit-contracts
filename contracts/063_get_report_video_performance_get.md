# TIKTOK_ADS_REPORT_VIDEO_PERFORMANCE_GET

- Operation: Get in-second performance
- Wire: `GET /report/video_performance/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `4`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Reporting`
- Source: [doc 1738825259075586](https://business-api.tiktok.com/portal/docs?id=1738825259075586)
- Source content SHA-256: `69b9e6a3040ca5480e586ea2cf04e90846b9de5be21ff6162240cc2cedc632f3`
- Product/fixture gate: Advertiser with non-empty delivered-campaign reporting data
- Live boundary: Read-only call permitted after fixture discovery
- Warning: Provider enum is documented as sort_type ASC or DES, not DESC. Preserve DES unless live evidence proves a typo. The response table types data.list as object while the example is an array; model it defensively as a collection and metrics as dynamic string-to-list[number] keys.

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `report_type` | `query` | `string` | `optional` | allowed: AD, VIDEO; default: AD |
| `metrics_fields` | `query` | `string[]` | `optional` | - |
| `filtering` | `query` | `object` | `required` | - |
| `filtering.ad_ids` | `query` | `string[]` | `conditional` | rule: Note : Currently, the limit of the ad_ids you pass is 200 |
| `filtering.adgroup_ids` | `query` | `string[]` | `conditional` | - |
| `filtering.campaign_ids` | `query` | `string[]` | `conditional` | - |
| `filtering.material_ids` | `query` | `string[]` | `conditional` | size: 1 |
| `filtering.video_ids` | `query` | `string[]` | `conditional` | size: 1 |
| `filtering.start_time` | `query` | `string` | `optional` | cross-field: Valid only when report_type is set to VIDEO; rule: If you want to specify a time range for Video Insights data, you need to pass in both start_time and end_time, and specify lifetime as false; rule: Query start time (closed interval) in the format of YYYY-MM-DD hh:mm:ss (UTC+0 Time) |
| `filtering.end_time` | `query` | `string` | `optional` | cross-field: Valid only when report_type is set to VIDEO; rule: If you want to specify a time range for Video Insights data, you need to pass in both start_time and end_time, and specify lifetime as false; rule: Query end time (closed interval) in the format of YYYY-MM-DD hh:mm:ss(UTC+0 Time) |
| `filtering.lifetime` | `query` | `boolean` | `optional` | default: true; cross-field: Valid only when report_type is set to VIDEO; rule: If you want to specify a time range for Video Insights data, you need to pass in both start_time and end_time, and specify lifetime as false |
| `sort_field` | `query` | `string` | `optional` | - |
| `sort_type` | `query` | `string` | `optional` | allowed: ASC, DES |
| `page` | `query` | `number` | `optional` | default: 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-500; rule: Value range: 1-500 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object` | - |
| `data.list.info` | `object` | - |
| `data.list.info.ad_id` | `string` | - |
| `data.list.info.video_id` | `string` | - |
| `data.list.info.duration` | `number` | - |
| `data.list.metrics` | `object` | - |
| `data.list.metrics.metric_name` | `number[]` | - |
| `data.page_info` | `object` | - |
| `data.page_info.page` | `number` | - |
| `data.page_info.total_page` | `number` | - |
| `data.page_info.page_size` | `number` | - |
| `data.page_info.total_number` | `number` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
