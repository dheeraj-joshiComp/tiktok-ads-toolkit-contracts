# TIKTOK_ADS_GET_BID_PROTECTION_DETAILS

- Operation: Get bid protection history
- Wire: `GET /report/bid_protection/detail/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1874392516418561](https://business-api.tiktok.com/portal/docs?id=1874392516418561)
- Source content SHA-256: `a1424d681dc7fa60f809838d01eb0bd5ac73c3b4dcdfc9c984a86b3229b4cbb4`
- Product/fixture gate: Eligible campaign with bid-protection history
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `data_level` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `query_ids` | `query` | `string[]` | `required` | cross-field: when start_date to 2026-08-01 and end_date to 2026-08-11 (a 10-day range), the maximum number of IDs you can specify in query_ids is 20 (200 divided by 10); rule: The maximum allowed size is 200 divided by the time range you define using start_date and end_date; rule: For example, if you set start_date to 2026-08-01 and end_date to 2026-08-11 (a 10-day range), the maximum number of IDs you can specify in query_ids is 20 (200 divided by 10); rule: All IDs must belong to the same advertiser |
| `start_date` | `query` | `string` | `required` | rule: The start date for your bid protection history query, in the format of YYYY-MM-DD (ad account timezone); rule: Ensure the start date is within the past 60 days and is earlier than or equal to your end_date |
| `end_date` | `query` | `string` | `required` | rule: The end date for your bid protection history query, in the format of YYYY-MM-DD (ad account timezone); rule: Ensure the end date is within 60 days after your start_date and is later than or equal to the start_date |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.bid_protection_records` | `object[]` | - |
| `data.bid_protection_records[].data_level` | `string` | allowed: CAMPAIGN, ADGROUP |
| `data.bid_protection_records[].query_id` | `string` | - |
| `data.bid_protection_records[].record_date` | `string` | rule: The date when the record was generated, in the format of YYYY-MM-DD (ad account timezone) |
| `data.bid_protection_records[].bid_protection_daily_status` | `string` | allowed: UNDER_PROTECTION, INELIGIBLE, CONFIRMING, PAYMENT_COMPLETE, TARGET_MET |
| `data.bid_protection_records[].status_detail` | `string` | - |
| `data.bid_protection_records[].credit_amount` | `string` | - |
| `data.bid_protection_records[].currency` | `string` | rule: The currency for the ad credits amount, in the format of ISO 4217 currency code |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
