# TIKTOK_ADS_SMART_PLUS_ADGROUP_BUDGET_UPDATE

- Operation: Update the budgets of Upgraded Smart+ Ad Groups
- Wire: `POST /smart_plus/adgroup/budget/update/`
- Request encoding: `application/json`
- Ability hint: `updates`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1843314914438466](https://business-api.tiktok.com/portal/docs?id=1843314914438466)
- Source content SHA-256: `6517dfda5ef0e0d349247f1f7b72f59b7e26b785cdf9af729e8b5e7843e1b8f6`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `budget` | `json_body` | `object[]` | `conditional` | size: 20 |
| `budget[].adgroup_id` | `json_body` | `string` | `conditional` | condition: the object array budget is specified; rule: Required when the object array budget is specified |
| `budget[].budget` | `json_body` | `float` | `conditional` | condition: the object array budget is specified; rule: Required when the object array budget is specified |
| `scheduled_budget` | `json_body` | `object[]` | `conditional` | size: 20 |
| `scheduled_budget[].adgroup_id` | `json_body` | `string` | `conditional` | condition: the object array scheduled_budget is specified; any-of: If the ad group (adgroup_id) is part of a CBO campaign (where budget_optimize_on istrue), a min_budget or max_budget or both must be configured. || No prerequisites apply for ad groups within non-CBO campaigns (w; rule: Required when the object array scheduled_budget is specified; rule: Note : If the ad group (adgroup_id) is part of a CBO campaign (where budget_optimize_on istrue), a min_budget or max_budget or both must be configured |
| `scheduled_budget[].scheduled_budget` | `json_body` | `float` | `conditional` | condition: the object array scheduled_budget is specified; any-of: For an ad group in a CBO campaign (where budget_optimize_on is true), a min_budget or max_budget or both must be configured. This field will set the maximum daily budget control fo || For an ad group in a non-CBO; rule: Required when the object array scheduled_budget is specified; rule: The maximum budget control or the new budget for the ad group (adgroup_id); rule: This field will set the maximum daily budget control for the ad group |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
