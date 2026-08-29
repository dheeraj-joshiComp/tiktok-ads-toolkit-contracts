# TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CHECK

- Operation: Get the results of an asynchronous copy task for an Upgraded Smart+ Campaign
- Wire: `GET /smart_plus/campaign/copy/task/check/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1866529943741441](https://business-api.tiktok.com/portal/docs?id=1866529943741441)
- Source content SHA-256: `690f7bf9b4a7792726096bccc67c80047e2b336d6513ac6d3d6cb27619f28702`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.task_status` | `string` | allowed: RUNNING, SUCCESS, FAILURE |
| `data.task_info` | `object` | - |
| `data.task_info.total_ad_count` | `number` | - |
| `data.task_info.success_ad_count` | `number` | - |
| `data.task_result` | `object` | - |
| `data.task_result.campaign_id` | `string` | - |
| `data.task_result.campaign_name` | `string` | - |
| `data.task_result.campaign_error_infos` | `string[]` | - |
| `data.task_result.adgroup_result_list` | `object[]` | - |
| `data.task_result.adgroup_result_list[].adgroup_id` | `string` | - |
| `data.task_result.adgroup_result_list[].adgroup_name` | `string` | - |
| `data.task_result.adgroup_result_list[].total_ad_count` | `number` | - |
| `data.task_result.adgroup_result_list[].success_ad_count` | `number` | - |
| `data.task_result.adgroup_result_list[].adgroup_error_list` | `string[]` | - |
| `data.task_result.adgroup_result_list[].ad_status` | `string` | allowed: ALL_SUCCESS, PARTIAL_SUCCESS |
| `data.task_result.adgroup_result_list[].ad_result_list` | `object[]` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].is_success` | `boolean` | allowed: true, false |
| `data.task_result.adgroup_result_list[].ad_result_list[].smart_plus_ad_id` | `string` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].ad_name` | `string` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].ad_error_list` | `string[]` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
