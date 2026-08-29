# TIKTOK_ADS_LIST_BUSINESS_CENTER_ACCOUNT_COSTS

- Operation: Get the cost records of a BC and ad accounts
- Wire: `GET /bc/account/cost/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1829079287639041](https://business-api.tiktok.com/portal/docs?id=1829079287639041)
- Source content SHA-256: `bb95d3c90164dfde1451600a11b89db203800624a3d24d6fb7f00cab4a60a7d9`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.keyword` | `query` | `string` | `optional` | meaning: fuzzy match against advertiser ID or advertiser name |
| `filtering.start_date` | `query` | `string` | `optional` | rule: Query start date, in the format of YYYY-MM-DD (ad account time zone); rule: If you specify start_date and end_date simultaneously, the maximum time range is 365 days |
| `filtering.end_date` | `query` | `string` | `optional` | rule: Query end date, in the format of YYYY-MM-DD (ad account time zone); rule: If you specify start_date and end_date simultaneously, the maximum time range is 365 days |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥ 1; rule: Value range : ≥ 1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.cost_list` | `object[]` | - |
| `data.cost_list[].advertiser_id` | `string` | - |
| `data.cost_list[].advertiser_name` | `string` | - |
| `data.cost_list[].amount` | `number` | - |
| `data.cost_list[].cash_amount` | `number` | - |
| `data.cost_list[].grant_amount` | `number` | - |
| `data.cost_list[].tax_amount` | `number` | - |
| `data.cost_list[].currency` | `string` | - |
| `data.transaction_summary` | `object` | - |
| `data.transaction_summary.amount` | `number` | - |
| `data.transaction_summary.cash_amount` | `number` | - |
| `data.transaction_summary.grant_amount` | `number` | - |
| `data.transaction_summary.tax_amount` | `number` | - |
| `data.transaction_summary.currency` | `string` | - |
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
