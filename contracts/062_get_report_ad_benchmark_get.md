# TIKTOK_ADS_REPORT_AD_BENCHMARK_GET

- Operation: Get ad benchmarks
- Wire: `GET /report/ad_benchmark/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `4`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Reporting`
- Source: [doc 1738824501176321](https://business-api.tiktok.com/portal/docs?id=1738824501176321)
- Source content SHA-256: `fb0cdb7cde507263ec2c08973f297e9632a75f48deeed608376a8c2c97c4115f`
- Product/fixture gate: Advertiser with non-empty delivered-campaign reporting data
- Live boundary: Read-only call permitted after fixture discovery
- Warning: Provider contradiction: the response table types data.list as object, while the success example is an array. Model list defensively as a collection and metrics as dynamic string-to-number keys; add regression tests for the documented table and example shapes.

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `compare_time_window` | `query` | `string` | `optional` | - |
| `dimensions` | `query` | `string[]` | `required` | - |
| `metrics_fields` | `query` | `string[]` | `optional` | - |
| `filtering` | `query` | `object` | `required` | rule: You must specify one and only one out of the three conditions allowed |
| `filtering.ad_ids` | `query` | `string[]` | `optional` | - |
| `filtering.adgroup_ids` | `query` | `string[]` | `optional` | - |
| `filtering.campaign_ids` | `query` | `string[]` | `optional` | - |
| `sort_field` | `query` | `string` | `optional` | - |
| `sort_type` | `query` | `string` | `optional` | - |
| `page` | `query` | `number` | `optional` | - |
| `page_size` | `query` | `number` | `optional` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.compare_date` | `string` | - |
| `data.list` | `object` | rule: Note : If an ad accumulates fewer than 1,000 impressions within the comparison window (compare_time_window), the benchmark metric data will be empty |
| `data.list.info` | `object` | - |
| `data.list.info.ad_id` | `string` | - |
| `data.list.info.location` | `string` | - |
| `data.list.info.placement` | `string` | - |
| `data.list.info.ad_category` | `number` | - |
| `data.list.info.external_action` | `string` | - |
| `data.list.metrics` | `object` | - |
| `data.list.metrics.metric_name` | `number` | rule: After the metric name, you can see a number with one decimal place, in the value range of [0 |
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
