# TikTok Ads Yang implementation prompts

Generated: `2026-08-30`
PR: [ComposioHQ/mercury#26271](https://github.com/ComposioHQ/mercury/pull/26271)
Pinned source: `9f35c86a6ec3d56fe442046282803b79206f97a5`
Evidence: live official TikTok v1.3 document tree and permission hierarchy.

## Verification verdict

Yes, after removing three provider-contract defects from the earlier result. The evidence pack contains **63 selected action candidates**. The prompts include each exact current v1.3 method/path, normalized parameter and response tables, official document ID/hash, and permission evidence chain.

`/bc/asset_group/update/` is excluded because TikTok publishes only generic `data: object` and an unrelated invoice example. Three Reporting Subscription replacements are also excluded from action prompts because they require developer secrets, separate auth/platform design, and a `REPORT_DATA_CHANGE` allowlist. The selected `/report/subscription/*` paths must not be implemented.

This does not certify provider behavior. Live QA still needs eligible advertiser, Business Center, Shop, creative, catalog, campaign, and cleanup fixtures. `/bc/asset_group/update/` remains blocked pending endpoint-specific response evidence.

## Evidence integrity

- Official API Reference doc: `1735713875563521`, SHA-256 `c61449f221ef72f249c26b35e7be531601d5d3004000587835eba2896988369c`
- Permission scope doc: `1753986142651394`, SHA-256 `e7d9a3e7f57d2f6c93ab126b4d485b7fa86a58913609c498185e1788412412aa`
- Provider-selected endpoint export: app `REDACTED_SELECTED_APP_ID`, SHA-256 `be6f8f814a87944973f4d1e511ef2ab76ac6135974ae5014184b2f88d38a2a45`. Each action below embeds its selected category.
- Official tree snapshot: 1200 documents, response SHA-256 `a6c8324a6c5ac58760bac0438420440f161ea20a36603f188870fc2dd1147e87`
- Parent-scope rule: a granted first-level permission authorizes its documented child endpoints.
- Selected category scopes used here: `1`, `2`, `4`, `6`, and `9`.
- Direct permission-table path mappings: 17. Provider-selected category plus inheritance mappings: 46.
- Empty parsed request tables: 0. Empty parsed response tables: 0.
- Constraint-bearing fields with no normalized fact: 0. The generator fails closed if one appears.
- External enum tables embedded: age groups, CTA values, operating regions, language values, creative pre-review locations, and Commercial Music Library genres.

## How to use this file

Send one prompt at a time. Wait for Yang to finish, push, and report the new SHA before sending the next prompt. Prompts P1 through P10 contain all 63 candidates.

## Prompt 1: P1 Ad Account GET actions

Actions in this prompt: **8**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this first batch: 9f35c86a6ec3d56fe442046282803b79206f97a5

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_GET_ASSET_BINDING_QUOTA` -> `GET /asset/bind/quota/`
- `TIKTOK_ADS_LIST_BUSINESS_CENTER_ACCOUNT_COSTS` -> `GET /bc/account/cost/get/`
- `TIKTOK_ADS_GET_BUSINESS_CENTER_ADVERTISER_ATTRIBUTES` -> `GET /bc/advertiser/attribute/`
- `TIKTOK_ADS_GET_ADVERTISER_QUALIFICATION` -> `GET /bc/advertiser/qualification/get/`
- `TIKTOK_ADS_CHECK_UNIONPAY_VERIFICATION_REQUIREMENT` -> `GET /bc/advertiser/unionpay_info/check/`
- `TIKTOK_ADS_LIST_ADVERTISER_ASSIGNED_TIKTOK_ACCOUNTS` -> `GET /bc/asset/advertiser/assigned/`
- `TIKTOK_ADS_GET_BID_PROTECTION_DETAILS` -> `GET /report/bid_protection/detail/get/`
- `TIKTOK_ADS_GET_BID_PROTECTION_STATUSES` -> `GET /report/bid_protection/status/get/`

Embedded provider contract manifest:

### `TIKTOK_ADS_GET_ASSET_BINDING_QUOTA`

- Operation: Get binding info of an asset
- Wire: `GET /asset/bind/quota/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1739659584022529`, [official page](https://business-api.tiktok.com/portal/docs?id=1739659584022529)
- Contract SHA-256: `3fcb3f397a3351613c0566e63bbaba7de3d32282637ff265239d1c57711673d8`
- Required live inputs from request contract: `advertiser_id`, `asset_id`, `asset_type`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `asset_id` | `query` | `string` | `required` | - |
| `asset_type` | `query` | `string` | `required` | allowed: IDENTITY |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.total_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.used_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.available_quota` | `number` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_LIST_BUSINESS_CENTER_ACCOUNT_COSTS`

- Operation: Get the cost records of a BC and ad accounts
- Wire: `GET /bc/account/cost/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1829079287639041`, [official page](https://business-api.tiktok.com/portal/docs?id=1829079287639041)
- Contract SHA-256: `bb95d3c90164dfde1451600a11b89db203800624a3d24d6fb7f00cab4a60a7d9`
- Required live inputs from request contract: `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.keyword` | `query` | `string` | `optional` | meaning: fuzzy match against advertiser ID or advertiser name |
| `filtering.start_date` | `query` | `string` | `optional` | rule: Query start date, in the format of YYYY-MM-DD (ad account time zone); rule: If you specify start_date and end_date simultaneously, the maximum time range is 365 days |
| `filtering.end_date` | `query` | `string` | `optional` | rule: Query end date, in the format of YYYY-MM-DD (ad account time zone); rule: If you specify start_date and end_date simultaneously, the maximum time range is 365 days |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥ 1; rule: Value range : ≥ 1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.cost_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].advertiser_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].cash_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].grant_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].tax_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.cost_list[].currency` | `string` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary` | `object` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary.amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary.cash_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary.grant_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary.tax_amount` | `number` | `provider-unspecified; model permissively` | - |
| `data.transaction_summary.currency` | `string` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `integer` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_GET_BUSINESS_CENTER_ADVERTISER_ATTRIBUTES`

- Operation: Get currencies and registration areas for ad accounts
- Wire: `GET /bc/advertiser/attribute/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1775752357139457`, [official page](https://business-api.tiktok.com/portal/docs?id=1775752357139457)
- Contract SHA-256: `6e5ee0ef6fec74745469193703d3fe1e480a4dd85994c777178bbbe224eb3765`
- Required live inputs from request contract: `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.currencies` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.region_codes` | `string[]` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_GET_ADVERTISER_QUALIFICATION`

- Operation: Get qualifications within a Business Center
- Wire: `GET /bc/advertiser/qualification/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1770118680584194`, [official page](https://business-api.tiktok.com/portal/docs?id=1770118680584194)
- Contract SHA-256: `c696bff72c963c956e3fa3f1b16b3a22044fee8fa930ec4275312e61a177c8e2`
- Required live inputs from request contract: `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.verified` | `query` | `boolean` | `optional` | - |
| `page` | `query` | `int` | `optional` | default: 1; range: ≥ 1; rule: Value range : ≥ 1 |
| `page_size` | `query` | `int` | `optional` | default: 10; range: 1-100; rule: Value range: 1-100 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.qualifications` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.qualifications[].qualification_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.qualifications[].company_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.qualifications[].status` | `string` | `provider-unspecified; model permissively` | allowed: VERIFIED, UNVERIFIED |
| `data.qualifications[].owner_advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.qualifications[].linked_advertiser_count` | `int` | `provider-unspecified; model permissively` | - |
| `data.qualifications[].region_code` | `string` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CHECK_UNIONPAY_VERIFICATION_REQUIREMENT`

- Operation: Check the UnionPay verification requirement for a business license
- Wire: `GET /bc/advertiser/unionpay_info/check/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1813772238056449`, [official page](https://business-api.tiktok.com/portal/docs?id=1813772238056449)
- Contract SHA-256: `9aa9453f4ca7342bccd5118164e4ff74a4d25f47e821603ee6ee891b2075d1a2`
- Required live inputs from request contract: `license_no`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `license_no` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.unionpay_verification_required` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false; any-of: true: required. || false: not required.; rule: Whether UnionPay verification is required for the business license; rule: Supported values: true: required |

### `TIKTOK_ADS_LIST_ADVERTISER_ASSIGNED_TIKTOK_ACCOUNTS`

- Operation: Get ad accounts linked to a TikTok account in Business Center
- Wire: `GET /bc/asset/advertiser/assigned/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1855027294743554`, [official page](https://business-api.tiktok.com/portal/docs?id=1855027294743554)
- Contract SHA-256: `78ccb6a44226bf235871b3fbc6ab01bbd7fd4810e5dcb7db3a8ffe1ff60d7bb5`
- Required live inputs from request contract: `asset_id`, `asset_type`, `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `asset_id` | `query` | `string` | `required` | - |
| `asset_type` | `query` | `string` | `required` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].advertiser_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_GET_BID_PROTECTION_DETAILS`

- Operation: Get bid protection history
- Wire: `GET /report/bid_protection/detail/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1874392516418561`, [official page](https://business-api.tiktok.com/portal/docs?id=1874392516418561)
- Contract SHA-256: `a1424d681dc7fa60f809838d01eb0bd5ac73c3b4dcdfc9c984a86b3229b4cbb4`
- Required live inputs from request contract: `advertiser_id`, `data_level`, `end_date`, `query_ids`, `start_date`
- Product/fixture gate: Eligible campaign with bid-protection history
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `data_level` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `query_ids` | `query` | `string[]` | `required` | cross-field: when start_date to 2026-08-01 and end_date to 2026-08-11 (a 10-day range), the maximum number of IDs you can specify in query_ids is 20 (200 divided by 10); rule: The maximum allowed size is 200 divided by the time range you define using start_date and end_date; rule: For example, if you set start_date to 2026-08-01 and end_date to 2026-08-11 (a 10-day range), the maximum number of IDs you can specify in query_ids is 20 (200 divided by 10); rule: All IDs must belong to the same advertiser |
| `start_date` | `query` | `string` | `required` | rule: The start date for your bid protection history query, in the format of YYYY-MM-DD (ad account timezone); rule: Ensure the start date is within the past 60 days and is earlier than or equal to your end_date |
| `end_date` | `query` | `string` | `required` | rule: The end date for your bid protection history query, in the format of YYYY-MM-DD (ad account timezone); rule: Ensure the end date is within 60 days after your start_date and is later than or equal to the start_date |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.bid_protection_records` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.bid_protection_records[].data_level` | `string` | `provider-unspecified; model permissively` | allowed: CAMPAIGN, ADGROUP |
| `data.bid_protection_records[].query_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.bid_protection_records[].record_date` | `string` | `provider-unspecified; model permissively` | rule: The date when the record was generated, in the format of YYYY-MM-DD (ad account timezone) |
| `data.bid_protection_records[].bid_protection_daily_status` | `string` | `provider-unspecified; model permissively` | allowed: UNDER_PROTECTION, INELIGIBLE, CONFIRMING, PAYMENT_COMPLETE, TARGET_MET |
| `data.bid_protection_records[].status_detail` | `string` | `provider-unspecified; model permissively` | - |
| `data.bid_protection_records[].credit_amount` | `string` | `provider-unspecified; model permissively` | - |
| `data.bid_protection_records[].currency` | `string` | `provider-unspecified; model permissively` | rule: The currency for the ad credits amount, in the format of ISO 4217 currency code |

### `TIKTOK_ADS_GET_BID_PROTECTION_STATUSES`

- Operation: Get bid protection statuses
- Wire: `GET /report/bid_protection/status/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1874392512912449`, [official page](https://business-api.tiktok.com/portal/docs?id=1874392512912449)
- Contract SHA-256: `ed5e55d9c8199fd5781e3b047ede949fda63237bb7c41d821c7e911ae0d5cc62`
- Required live inputs from request contract: `advertiser_id`, `data_level`, `query_ids`
- Product/fixture gate: Eligible campaign with bid-protection history
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `data_level` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `query_ids` | `query` | `string[]` | `required` | size: 200; rule: All IDs must belong to the same advertiser |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].data_level` | `string` | `provider-unspecified; model permissively` | allowed: CAMPAIGN, ADGROUP |
| `data.list[].query_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].bid_protection_status` | `string` | `provider-unspecified; model permissively` | allowed: ACTIVE, INVALID, INACTIVE; rule: INVALID: Bid protection is temporarily ineligible for the campaign or ad group because the campaign or ad group was paused or deleted within the first 3 days after creation |
| `data.list[].compensation_category` | `string` | `provider-unspecified; model permissively` | allowed: FULL_LIFE_CYCLE, THREE_DAY |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 2: P2 Ad Account POST actions

Actions in this prompt: **4**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_DISABLE_BUSINESS_CENTER_ADVERTISER` -> `POST /bc/advertiser/disable/`
- `TIKTOK_ADS_ASSIGN_TIKTOK_ACCOUNT_TO_ADVERTISER` -> `POST /bc/asset/advertiser/assign/`
- `TIKTOK_ADS_UNASSIGN_TIKTOK_ACCOUNT_FROM_ADVERTISER` -> `POST /bc/asset/advertiser/unassign/`
- `TIKTOK_ADS_CREATE_BUSINESS_CENTER_ORGANIZATION_ACCOUNT` -> `POST /bc/oa/create/`

Embedded provider contract manifest:

### `TIKTOK_ADS_DISABLE_BUSINESS_CENTER_ADVERTISER`

- Operation: Disable an ad account
- Wire: `POST /bc/advertiser/disable/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1752349244331009`, [official page](https://business-api.tiktok.com/portal/docs?id=1752349244331009)
- Contract SHA-256: `74d802fe5befc9bffbe400e6aa3d829a47780eb8ca0b07e0d1c6daeadeb675f8`
- Required live inputs from request contract: `advertiser_ids`, `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `advertiser_ids` | `json_body` | `string[]` | `required` | size: 1 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.disabled_advertiser_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.failed_infos` | `map` | `provider-unspecified; model permissively` | allowed: DELIVERING, UNPAID_BILL, SUSPENDED, UNFINISHED_TRANSFER, AUTOPAY_UNBILLED; rule: Enum values: DELIVERING: The ad account has ads that are being delivered within 3 days |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_ASSIGN_TIKTOK_ACCOUNT_TO_ADVERTISER`

- Operation: Link a TikTok account to an ad account in Business Center
- Wire: `POST /bc/asset/advertiser/assign/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `updates`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1846868953025538`, [official page](https://business-api.tiktok.com/portal/docs?id=1846868953025538)
- Contract SHA-256: `9d5688fc93f8886ebff538627510616da9010fd22a71ed365089135562ef2faf`
- Required live inputs from request contract: `advertiser_id`, `asset_id`, `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `asset_type` | `json_body` | `string` | `optional` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT; default: TT_ACCOUNT |
| `asset_id` | `json_body` | `string` | `required` | - |
| `advertiser_id` | `json_body` | `string` | `required` | rule: The ID of an ad account within the same Business Center to link the TikTok account to |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_UNASSIGN_TIKTOK_ACCOUNT_FROM_ADVERTISER`

- Operation: Unlink a TikTok account from an ad account in Business Center
- Wire: `POST /bc/asset/advertiser/unassign/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1855027260369921`, [official page](https://business-api.tiktok.com/portal/docs?id=1855027260369921)
- Contract SHA-256: `144f681a3297baaada563d9d5eda0f8bca818907b32033bff88779f898ac3b80`
- Required live inputs from request contract: `advertiser_id`, `asset_id`, `asset_type`, `bc_id`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `asset_id` | `json_body` | `string` | `required` | - |
| `asset_type` | `json_body` | `string` | `required` | allowed: TT_ACCOUNT, MANAGED_BUSINESS_ACCOUNT |
| `advertiser_id` | `json_body` | `string` | `required` | rule: The ID of an ad account within the same Business Center to unlink the TikTok account from |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CREATE_BUSINESS_CENTER_ORGANIZATION_ACCOUNT`

- Operation: Create an Organization Account in a Business Center
- Wire: `POST /bc/oa/create/` on the existing v1.3 base URL
- Request encoding: `multipart/form-data`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ad Account Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1855027199571138`, [official page](https://business-api.tiktok.com/portal/docs?id=1855027199571138)
- Contract SHA-256: `389a68abe879bb1eff17310de35eab0f38306a46d45cf39c87c87acca88c838f`
- Required live inputs from request contract: `bc_id`, `display_name`, `operating_region_code`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `multipart_form` | `string` | `required` | - |
| `display_name` | `multipart_form` | `string` | `required` | length: 30 characters; rule: Length limit: 30 characters |
| `handle` | `multipart_form` | `string` | `optional` | length: 24 characters; rule: Length limit: 24 characters; rule: The handle cannot consist solely of numbers |
| `profile_image` | `multipart_form` | `file` | `optional` | multipart encoding: binary file part |
| `operating_region_code` | `multipart_form` | `string` | `required` | rule: Note : If your business is based in the Chinese mainland, you must select an operating region other than China when creating an Organization Account, as CN is not an available option for operating_reg; allowed: AR, AU, AT, BD, BE, BR, BG, KH, CA, CL, CO, HR, CY, CZ, DK, EC, EG, EE, FI, FR, DE, GR, HU, ID, IQ, IE, IL, IT, JP, JO, KZ, KW, LV, LT, LU, MY, MX, MA, NL, NZ, NO, PK, PE, PH, PL, PT, RO, SA, SG, SK, SI, ZA, KR, ES, SE, CH, TW, TH, TR, AE, GB, US, VN |
| `qualification_info` | `multipart_form` | `object` | `conditional` | condition: the type of your Business Center is AGENCY or SELF_SERVICE_AGENCY; rule: Required when the type of your Business Center is AGENCY or SELF_SERVICE_AGENCY; multipart encoding: JSON-serialized string form part |
| `qualification_info.qualification_id` | `multipart_form` | `string` | `optional` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.asset_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.asset_name` | `string` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 3: P3 GMV Max GET actions

Actions in this prompt: **8**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_GET` -> `GET /campaign/gmv_max/session/get/`
- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_LIST` -> `GET /campaign/gmv_max/session/list/`
- `TIKTOK_ADS_GMV_MAX_EXCLUSIVE_AUTHORIZATION_GET` -> `GET /gmv_max/exclusive_authorization/get/`
- `TIKTOK_ADS_GMV_MAX_IDENTITY_GET` -> `GET /gmv_max/identity/get/`
- `TIKTOK_ADS_GMV_MAX_OCCUPIED_CUSTOM_SHOP_ADS_LIST` -> `GET /gmv_max/occupied_custom_shop_ads/list/`
- `TIKTOK_ADS_GMV_MAX_STORE_LIST` -> `GET /gmv_max/store/list/`
- `TIKTOK_ADS_GMV_MAX_STORE_SHOP_AD_USAGE_CHECK` -> `GET /gmv_max/store/shop_ad_usage_check/`
- `TIKTOK_ADS_GMV_MAX_VIDEO_GET` -> `GET /gmv_max/video/get/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_GET`

- Operation: Get details of max delivery or creative boost sessions
- Wire: `GET /campaign/gmv_max/session/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1835247031331842`, [official page](https://business-api.tiktok.com/portal/docs?id=1835247031331842)
- Contract SHA-256: `961501f7635a62eee76b4a9ec9e95a793b1dd9bb5a1de53b610791f8462bb20a`
- Required live inputs from request contract: `advertiser_id`, `session_ids`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `session_ids` | `query` | `string[]` | `required` | size: 20 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.session_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.session_list[].campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].bid_type` | `string` | `provider-unspecified; model permissively` | allowed: NO_BID, CREATIVE_NO_BID |
| `data.session_list[].session_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].budget` | `float` | `provider-unspecified; model permissively` | rule: Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget |
| `data.session_list[].product_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.session_list[].product_list[].spu_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].schedule_type` | `string` | `provider-unspecified; model permissively` | rule: SCHEDULE_FROM_NOW: To enable the max delivery or creative boost mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `data.session_list[].schedule_start_time` | `string` | `provider-unspecified; model permissively` | rule: The start time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].schedule_end_time` | `string` | `provider-unspecified; model permissively` | rule: The end time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].item_id` | `string` | `provider-unspecified; model permissively` | presence: present when bid_type is CREATIVE_NO_BID |

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_LIST`

- Operation: Get max delivery or creative boost sessions within a campaign
- Wire: `GET /campaign/gmv_max/session/list/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1835246996436162`, [official page](https://business-api.tiktok.com/portal/docs?id=1835246996436162)
- Contract SHA-256: `998acd282c3928c7d14832003656d9ad53e315cee1431a3930af9c08886d65a4`
- Required live inputs from request contract: `advertiser_id`, `campaign_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `campaign_id` | `query` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.session_list` | `object[]` | `provider-unspecified; model permissively` | rule: The list of max delivery sessions for products or creative boost sessions for videos within the Product GMV Max Campaign |
| `data.session_list[].campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].bid_type` | `string` | `provider-unspecified; model permissively` | allowed: NO_BID, CREATIVE_NO_BID |
| `data.session_list[].session_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].budget` | `float` | `provider-unspecified; model permissively` | rule: Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget |
| `data.session_list[].product_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.session_list[].product_list[].spu_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.session_list[].schedule_type` | `string` | `provider-unspecified; model permissively` | rule: SCHEDULE_FROM_NOW: To enable the max delivery or creative boost mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `data.session_list[].schedule_start_time` | `string` | `provider-unspecified; model permissively` | rule: The start time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.session_list[].schedule_end_time` | `string` | `provider-unspecified; model permissively` | rule: The end time for the max delivery or creative boost mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |

### `TIKTOK_ADS_GMV_MAX_EXCLUSIVE_AUTHORIZATION_GET`

- Operation: Get the TikTok Shop exclusive authorization status of an ad account
- Wire: `GET /gmv_max/exclusive_authorization/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001184635905`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001184635905)
- Contract SHA-256: `5e374d4fbc38767cb9d30d1a0409df85f01b69bdbd84b5a7c3388e94d5a2feb3`
- Required live inputs from request contract: `advertiser_id`, `store_authorized_bc_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |
| `advertiser_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.store_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.authorization_status` | `string` | `provider-unspecified; model permissively` | allowed: EFFECTIVE, INEFFECTIVE, UNAUTHORIZED |
| `data.advertiser_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.advertiser_status` | `string` | `provider-unspecified; model permissively` | allowed: STATUS_ENABLE, STATUS_CONFIRM_FAIL, STATUS_PENDING_CONFIRM, STATUS_LIMIT, STATUS_CONTRACT_PENDING, STATUS_DISABLE, STATUS_PENDING_CONFIRM_MODIFY, STATUS_PENDING_VERIFIED, STATUS_SELF_SERVICE_UNAUDITED, STATUS_WA |
| `data.identity_id` | `string` | `provider-unspecified; model permissively` | presence: present when an official TikTok account is set for the TikTok Shop |

### `TIKTOK_ADS_GMV_MAX_IDENTITY_GET`

- Operation: Get identities for GMV Max Campaigns
- Wire: `GET /gmv_max/identity/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001101474882`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001101474882)
- Contract SHA-256: `dfa82f27673dc8e08fc532f1b72dd7f6d9c53474e520356f24a5a34e7db46479`
- Required live inputs from request contract: `advertiser_id`, `store_authorized_bc_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.identity_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.identity_list[].identity_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.identity_list[].identity_type` | `string` | `provider-unspecified; model permissively` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.identity_list[].identity_authorized_bc_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is BC_AUTH_TT |
| `data.identity_list[].identity_authorized_shop_id` | `string` | `provider-unspecified; model permissively` | presence: Returned for some BC_AUTH_TT identities |
| `data.identity_list[].store_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is TTS_TT |
| `data.identity_list[].profile_image` | `string` | `provider-unspecified; model permissively` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.identity_list[].display_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.identity_list[].user_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.identity_list[].is_running_custom_shop_ads` | `bool` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.identity_list[].product_gmv_max_available` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.identity_list[].live_gmv_max_available` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.identity_list[].unavailable_reason` | `string` | `provider-unspecified; model permissively` | allowed: OCCUPIED, UNAUTHORIZED; presence: present when live_gmv_max_available is false |

### `TIKTOK_ADS_GMV_MAX_OCCUPIED_CUSTOM_SHOP_ADS_LIST`

- Operation: Check the occupancy of identities or products in Shopping Ads
- Wire: `GET /gmv_max/occupied_custom_shop_ads/list/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001136924674`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001136924674)
- Contract SHA-256: `633ec0ed19c4175cd4a83e4957ea797eecf2468dfc920537ab88561f5601a0c3`
- Required live inputs from request contract: `advertiser_id`, `asset_ids`, `occupied_asset_type`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `occupied_asset_type` | `query` | `string` | `required` | allowed: IDENTITY_TT_USER, IDENTITY_BC_AUTH_TT, IDENTITY_TTS_TT, SPU |
| `asset_ids` | `query` | `string[]` | `required` | size: 1; rule: When occupied_asset_type is SPU, specify the SPU ID of a product within the TikTok Shop via this field |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads[].advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads[].campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads[].adgroup_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads[].ad_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.occupied_custom_shop_ads[].create_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the ad group or ad was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |

### `TIKTOK_ADS_GMV_MAX_STORE_LIST`

- Operation: Get TikTok Shops for GMV Max Campaigns
- Wire: `GET /gmv_max/store/list/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001044479041`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001044479041)
- Contract SHA-256: `5fd083b5cf4fe023c7e1f1a95985c205115aa39f0990b84223acfb74610f8081`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.store_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].is_gmv_max_available` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.store_list[].store_authorized_bc_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].is_owner_bc` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.store_list[].store_authorized_bc_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_authorized_bc_info.bc_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_authorized_bc_info.bc_profile_image` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_authorized_bc_info.bc_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_authorized_bc_info.user_role` | `string` | `provider-unspecified; model permissively` | allowed: ADMIN, STANDARD; rule: The role of the user (member) within the Business Center |
| `data.store_list[].thumbnail_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_code` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].targeting_region_codes` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.store_list[].store_status` | `string` | `provider-unspecified; model permissively` | allowed: ACTIVE, INACTIVE, NEW_CREATE |
| `data.store_list[].store_role` | `string` | `provider-unspecified; model permissively` | allowed: AD_PROMOTION, MANAGER, UNSET |
| `data.store_list[].exclusive_authorized_advertiser_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.store_list[].exclusive_authorized_advertiser_info.advertiser_status` | `string` | `provider-unspecified; model permissively` | allowed: STATUS_ENABLE, STATUS_CONFIRM_FAIL, STATUS_PENDING_CONFIRM, STATUS_LIMIT, STATUS_CONTRACT_PENDING, STATUS_DISABLE, STATUS_PENDING_CONFIRM_MODIFY, STATUS_PENDING_VERIFIED, STATUS_SELF_SERVICE_UNAUDITED, STATUS_WA |

### `TIKTOK_ADS_GMV_MAX_STORE_SHOP_AD_USAGE_CHECK`

- Operation: Check the availability of a TikTok Shop for Product GMV Max Campaigns
- Wire: `GET /gmv_max/store/shop_ad_usage_check/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001084174338`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001084174338)
- Contract SHA-256: `a21b20096df419e79a25f3a4d0cbc4e0fdcafa27aeb41a45dbd7fb34c8a40c5c`
- Required live inputs from request contract: `advertiser_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.promote_all_products_allowed` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.is_running_custom_shop_ads` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |

### `TIKTOK_ADS_GMV_MAX_VIDEO_GET`

- Operation: Get posts for a Product GMV Max Campaign
- Wire: `GET /gmv_max/video/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822001168512129`, [official page](https://business-api.tiktok.com/portal/docs?id=1822001168512129)
- Contract SHA-256: `206057c962ca308160135fbcb9eb43f9411f3b4322c0f755f8103f75b937245a`
- Required live inputs from request contract: `advertiser_id`, `store_authorized_bc_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `store_id` | `query` | `string` | `required` | - |
| `store_authorized_bc_id` | `query` | `string` | `required` | - |
| `spu_id_list` | `query` | `string[]` | `optional` | size rule: When custom_posts_eligible is false or not specified: 50.; size rule: When custom_posts_eligible is true: 1. |
| `custom_posts_eligible` | `query` | `boolean` | `optional` | allowed: true, false; default: false; cross-field: when true, spu_id_list must contain exactly 1 product |
| `sort_field` | `query` | `string` | `optional` | allowed: GMV, POST_TIME, VIDEO_VIEWS, VIDEO_LIKES, CLICK_THROUGH_RATE, PRODUCT_CLICKS; default: GMV; rule: Valid only when custom_posts_eligible is false or not provided |
| `sort_type` | `query` | `string` | `optional` | allowed: ASC, DESC; default: DESC; cross-field: for authorized-post sorting, provide sort_field and sort_type together |
| `keyword` | `query` | `string` | `optional` | rule: To search by post ID (item_id), provide a numeric string with at least 19 characters |
| `need_auth_code_video` | `query` | `boolean` | `optional` | allowed: true, false; default: false; result rule: when need_auth_code_video is false or omitted and identity_list is omitted, item_list is empty |
| `identity_list` | `query` | `object[]` | `optional` | size: 20; result rule: when need_auth_code_video is false or omitted and identity_list is omitted, item_list is empty |
| `identity_list[].identity_id` | `query` | `string` | `optional` | - |
| `identity_list[].identity_type` | `query` | `string` | `optional` | allowed: TT_USER, BC_AUTH_TT, TTS_TT |
| `identity_list[].identity_authorized_bc_id` | `query` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |
| `identity_list[].identity_authorized_shop_id` | `query` | `string` | `conditional` | condition: required for BC_AUTH_TT only when /gmv_max/identity/get returns identity_authorized_shop_id for that identity |
| `identity_list[].store_id` | `query` | `string` | `conditional` | condition: identity_type is TTS_TT; rule: Required when identity_type is TTS_TT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.item_list[].item_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].text` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].spu_id_list` | `string[]` | `provider-unspecified; model permissively` | presence: absent for videos without a product anchor |
| `data.item_list[].can_change_anchor` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false; rule: false: You cannot use the video to create a customized post; rule: Note : If can_change_anchor is false, you cannot pass the video to custom_anchor_video_list or item_list in /campaign/gmv_max/create/ or /campaign/gmv_max/update/ to create customized posts |
| `data.item_list[].identity_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list[].identity_info.identity_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].identity_info.identity_type` | `string` | `provider-unspecified; model permissively` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.item_list[].identity_info.identity_authorized_bc_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is BC_AUTH_TT |
| `data.item_list[].identity_info.identity_authorized_shop_id` | `string` | `provider-unspecified; model permissively` | presence: Returned for some BC_AUTH_TT identities |
| `data.item_list[].identity_info.store_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is TTS_TT |
| `data.item_list[].identity_info.profile_image` | `string` | `provider-unspecified; model permissively` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds; temporary URL: approximately 48 hours |
| `data.item_list[].identity_info.display_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.video_cover_url` | `string` | `provider-unspecified; model permissively` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds; temporary URL: approximately 24 hours |
| `data.item_list[].video_info.preview_url` | `string` | `provider-unspecified; model permissively` | temporary URL: 6 hours |
| `data.item_list[].video_info.height` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.width` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.bit_rate` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.duration` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.size` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.signature` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.format` | `string` | `provider-unspecified; model permissively` | rule: The format of the video |
| `data.item_list[].video_info.definition` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.fps` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 4: P4 GMV Max POST actions

Actions in this prompt: **6**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_CREATIVE_UPDATE` -> `POST /campaign/gmv_max/creative/update/`
- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_CREATE` -> `POST /campaign/gmv_max/session/create/`
- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_DELETE` -> `POST /campaign/gmv_max/session/delete/`
- `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_UPDATE` -> `POST /campaign/gmv_max/session/update/`
- `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_DELETE` -> `POST /gmv_max/creation/custom_anchor_video_list/delete/`
- `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_GET` -> `POST /gmv_max/creation/custom_anchor_video_list/get/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_CREATIVE_UPDATE`

- Operation: Remove or add back creatives in a GMV Max Campaign
- Wire: `POST /campaign/gmv_max/creative/update/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `updates`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1861260625563202`, [official page](https://business-api.tiktok.com/portal/docs?id=1861260625563202)
- Contract SHA-256: `9d077f9afc9adc49cb4969945311060291576b4bf3b709d8e5a4a5506d6acdf0`
- Required live inputs from request contract: `action`, `advertiser_id`, `campaign_id`, `item_list`, `item_list[].item_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: Note : The campaign must be in an active status; rule: If the campaign is a Product GMV Max Campaign, the product_video_specific_type of the campaign must be AUTO_SELECTION |
| `action` | `json_body` | `string` | `required` | allowed: REMOVE, ADD; rule: Note : Once the action is performed, wait 20 minutes before verifying the updated statuses using /gmv_max/report/get/ |
| `item_list` | `json_body` | `object[]` | `required` | size: 400; rule: Note : This endpoint allows for the removal of up to 10,000 posts from a GMV Max Campaign, with a limit of 400 posts per request |
| `item_list[].item_id` | `json_body` | `string` | `required` | - |
| `item_list[].spu_id_list` | `json_body` | `string[]` | `conditional` | rule: Required for a Product GMV Max Campaign |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_CREATE`

- Operation: Create a max delivery or creative boost session
- Wire: `POST /campaign/gmv_max/session/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1835246967275522`, [official page](https://business-api.tiktok.com/portal/docs?id=1835246967275522)
- Contract SHA-256: `3eccc89ae52262794735982b3019865576fd5462805dbe9f22efbb6bae3d83b3`
- Required live inputs from request contract: `advertiser_id`, `campaign_id`, `session`, `session.bid_type`, `session.budget`, `session.item_id`, `session.product_list`, `session.product_list[].spu_id`, `session.schedule_type`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

Variant: `Parameters for creating a max delivery session`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.bid_type` | `json_body` | `string` | `required` | allowed: NO_BID; default: NO_BID |
| `session.product_list` | `json_body` | `object[]` | `required` | size: 1 |
| `session.product_list[].spu_id` | `json_body` | `string` | `required` | - |
| `session.budget` | `json_body` | `float` | `required` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; default: SCHEDULE_FROM_NOW; rule: Enum values: SCHEDULE_FROM_NOW: To enable the max delivery mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `session.schedule_start_time` | `json_body` | `string` | `optional` | rule: The start time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The start time cannot be earlier than the current time |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |

Variant: `Parameters for creating a creative boost session`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.bid_type` | `json_body` | `string` | `required` | allowed: CREATIVE_NO_BID |
| `session.product_list` | `json_body` | `object[]` | `required` | size: 1 |
| `session.product_list[].spu_id` | `json_body` | `string` | `required` | - |
| `session.item_id` | `json_body` | `string` | `required` | - |
| `session.budget` | `json_body` | `float` | `required` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `required` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; default: SCHEDULE_FROM_NOW; rule: Enum values: SCHEDULE_FROM_NOW: To enable creative boost for the product continuously after the current time, until the campaign scheduled end time |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for creative boost, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.session_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_DELETE`

- Operation: Delete a max delivery or creative boost session
- Wire: `POST /campaign/gmv_max/session/delete/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1835246983475217`, [official page](https://business-api.tiktok.com/portal/docs?id=1835246983475217)
- Contract SHA-256: `787506a4cf488f817f2dceef7b33fa6c0297c73ea56b596fb9a58c10f479ff75`
- Required live inputs from request contract: `advertiser_id`, `session_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_UPDATE`

- Operation: Update a max delivery or creative boost session
- Wire: `POST /campaign/gmv_max/session/update/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `updates`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1835247009119233`, [official page](https://business-api.tiktok.com/portal/docs?id=1835247009119233)
- Contract SHA-256: `159adc3e85e3aaf75bb562f78d5c581bff3e985e5129d353e9e069a1b69663b8`
- Required live inputs from request contract: `advertiser_id`, `campaign_id`, `session`, `session_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

Variant: `Parameters for updating a max delivery session`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.budget` | `json_body` | `float` | `optional` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; rule: Enum values: SCHEDULE_FROM_NOW: To enable the max delivery mode for the product continuously after the schedule_start_time, until the campaign scheduled end time |
| `session.schedule_start_time` | `json_body` | `string` | `optional` | rule: The start time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The start time cannot be earlier than the current time + 5 minutes |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for the max delivery mode, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |

Variant: `Parameters for updating a creative boost session`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_id` | `json_body` | `string` | `required` | rule: To filter existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `store_id` | `json_body` | `string` | `required` | - |
| `session_id` | `json_body` | `string` | `required` | - |
| `session` | `json_body` | `object` | `required` | - |
| `session.budget` | `json_body` | `float` | `optional` | range: ≥ 10 (USD); rule: Value range: ≥ 10 (USD) |
| `session.schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_FROM_NOW, SCHEDULE_START_END; default: SCHEDULE_FROM_NOW; rule: Enum values: SCHEDULE_FROM_NOW: To enable creative boost for the product continuously after the current time, until the campaign scheduled end time |
| `session.schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: The end time for creative boost, in the format of YYYY-MM-DD HH:MM:SS (UTC+0); rule: Note : The end time cannot be earlier than the current time |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_DELETE`

- Operation: Delete customized TikTok posts
- Wire: `POST /gmv_max/creation/custom_anchor_video_list/delete/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1866513159202306`, [official page](https://business-api.tiktok.com/portal/docs?id=1866513159202306)
- Contract SHA-256: `9e47aea82633f962e1b1aa351069ee60a70379158b2feec99946da4aa4c5572b`
- Required live inputs from request contract: `advertiser_id`, `custom_anchor_video_list`, `custom_anchor_video_list[].item_id`, `custom_anchor_video_list[].spu_id_list`, `store_authorized_bc_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `store_id` | `json_body` | `string` | `required` | - |
| `store_authorized_bc_id` | `json_body` | `string` | `required` | - |
| `custom_anchor_video_list` | `json_body` | `object[]` | `required` | size: 200 |
| `custom_anchor_video_list[].item_id` | `json_body` | `string` | `required` | - |
| `custom_anchor_video_list[].spu_id_list` | `json_body` | `string[]` | `required` | - |
| `campaign_id` | `json_body` | `string` | `conditional` | condition: the specified TikTok videos (item_id) have been used in a campaign to create campaign-level customized posts; rule: Required when the specified TikTok videos (item_id) have been used in a campaign to create campaign-level customized posts; rule: To retrieve existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_GET`

- Operation: Get customized TikTok posts
- Wire: `POST /gmv_max/creation/custom_anchor_video_list/get/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1866513156712449`, [official page](https://business-api.tiktok.com/portal/docs?id=1866513156712449)
- Contract SHA-256: `aaa6a9a44e867cf77c783ad28377f465162f02a8c955cffe7ce0617a51db15dc`
- Required live inputs from request contract: `advertiser_id`, `creative_source`, `store_authorized_bc_id`, `store_id`
- Product/fixture gate: Eligible TikTok Shop, owning or authorized Business Center, advertiser, and GMV Max resources
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `store_id` | `json_body` | `string` | `required` | - |
| `store_authorized_bc_id` | `json_body` | `string` | `required` | - |
| `creative_source` | `json_body` | `string` | `required` | allowed: CUSTOMIZED |
| `spu_id_list` | `json_body` | `string[]` | `optional` | - |
| `sort_field` | `json_body` | `string` | `optional` | allowed: GMV, POST_TIME, VIDEO_VIEWS, VIDEO_LIKES, CLICK_THROUGH_RATE, PRODUCT_CLICKS; default: GMV |
| `sort_type` | `json_body` | `string` | `optional` | allowed: ASC, DESC |
| `keyword` | `json_body` | `string` | `optional` | rule: To search by post ID (item_id), provide a numeric string with at least 19 characters |
| `need_auth_code_video` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |
| `identity_list` | `json_body` | `object[]` | `optional` | size: 20 |
| `identity_list[].identity_id` | `json_body` | `string` | `optional` | - |
| `identity_list[].identity_type` | `json_body` | `string` | `optional` | allowed: TT_USER, BC_AUTH_TT, TTS_TT |
| `identity_list[].identity_authorized_bc_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is BC_AUTH_TT |
| `identity_list[].identity_authorized_shop_id` | `json_body` | `string` | `optional` | rule: Required only when dentity_type is BC_AUTH_TT and identity_authorized_shop_id is returned for the identity from /gmv_max/identity/get/ |
| `identity_list[].store_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is TTS_TT |
| `campaign_id` | `json_body` | `string` | `optional` | rule: To retrieve existing Product GMV Max Campaigns within your ad account, use /gmv_max/campaign/get/ and set filtering to {"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]} |
| `page` | `json_body` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `json_body` | `number` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.item_list[].item_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].text` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].spu_id_list` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.item_list[].can_change_anchor` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false; rule: false: You cannot use the video to create a customized post; rule: Note : If can_change_anchor is false, you cannot pass the video to custom_anchor_video_list or item_list in /campaign/gmv_max/create/ or /campaign/gmv_max/update/ to create customized posts |
| `data.item_list[].identity_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list[].identity_info.identity_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].identity_info.identity_type` | `string` | `provider-unspecified; model permissively` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT, TTS_TT |
| `data.item_list[].identity_info.identity_authorized_bc_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is BC_AUTH_TT |
| `data.item_list[].identity_info.identity_authorized_shop_id` | `string` | `provider-unspecified; model permissively` | presence: Returned for some BC_AUTH_TT identities |
| `data.item_list[].identity_info.store_id` | `string` | `provider-unspecified; model permissively` | presence: present when identity_type is TTS_TT |
| `data.item_list[].identity_info.profile_image` | `string` | `provider-unspecified; model permissively` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.item_list[].identity_info.display_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.video_cover_url` | `string` | `provider-unspecified; model permissively` | rule: The expiration time is included in the URL after the x-expires parameter, in the format of an Epoch/Unix timestamp in seconds |
| `data.item_list[].video_info.preview_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.height` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.width` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.bit_rate` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.duration` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.size` | `number` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.signature` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.format` | `string` | `provider-unspecified; model permissively` | rule: The format of the video |
| `data.item_list[].video_info.definition` | `string` | `provider-unspecified; model permissively` | - |
| `data.item_list[].video_info.fps` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 5: P5 Other Ads GET actions

Actions in this prompt: **9**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CAMPAIGN_QUOTA_INFO` -> `GET /campaign/quota/info/`
- `TIKTOK_ADS_CAMPAIGN_LABEL_GET` -> `GET /campaign_label/get/`
- `TIKTOK_ADS_CHANGELOG_GET` -> `GET /changelog/get/`
- `TIKTOK_ADS_CHANGELOG_TASK_DOWNLOAD` -> `GET /changelog/task/download/`
- `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_GET` -> `GET /search_ad/negative_keyword/get/`
- `TIKTOK_ADS_SHOWCASE_IDENTITY_GET` -> `GET /showcase/identity/get/`
- `TIKTOK_ADS_SHOWCASE_PRODUCT_GET` -> `GET /showcase/product/get/`
- `TIKTOK_ADS_SHOWCASE_REGION_GET` -> `GET /showcase/region/get/`
- `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CHECK` -> `GET /smart_plus/campaign/copy/task/check/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CAMPAIGN_QUOTA_INFO`

- Operation: Get the quota for a SKAN Dedicated Campaign per ad network
- Wire: `GET /campaign/quota/info/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1752256376677378`, [official page](https://business-api.tiktok.com/portal/docs?id=1752256376677378)
- Contract SHA-256: `1cd0ea930fb7ab3202ef283c684c53e3b973dbdb166efa49740b50dfd4a96032`
- Required live inputs from request contract: `advertiser_id`, `app_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `app_id` | `query` | `string` | `required` | - |
| `campaign_id` | `query` | `string` | `optional` | - |
| `adgroup_id` | `query` | `string` | `optional` | rule: ID of an ad group within a SKAN 4; rule: Note : If the ID is not the ID of an ad group within a SKAN 4 |
| `has_advertiser_quota` | `query` | `boolean` | `optional` | default: false |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota` | `object` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota.max_test_number` | `number` | `provider-unspecified; model permissively` | rule: Maximum test group number in one split-test |
| `data.split_test_quota.available_test_group` | `number` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota.used_test_group` | `number` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota.releasing_test_group` | `number` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota.used_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.split_test_quota.releasing_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.total_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.used_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.releasing_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.available_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.used_campaign_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.releasing_campaign_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].used_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].releasing_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.total_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.used_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.releasing_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.available_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.used_campaign_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.releasing_campaign_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].used_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].releasing_campaign_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].advertiser_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.adgroup_quota_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.adgroup_quota_info.total_adgroup_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.adgroup_quota_info.used_adgroup_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.adgroup_quota_info.available_adgroup_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.adgroup_quota_info.placements` | `string[]` | `provider-unspecified; model permissively` | rule: You cannot create ad groups with placements that are not listed here |
| `data.adgroup_quota_info.campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.ad_quota_info` | `object` | `provider-unspecified; model permissively` | cross-field: when a SKAN 4.0 App ID (app_id) without specifying campaign_id and adgroup_id in the request, this field will represent the default ad quota for a regular SKAN 4; rule: Ad quota under an ad group within a SKAN 4; rule: Note : If the specified ad group (adgroup_id) is not within a SKAN 4 |
| `data.ad_quota_info.total_ad_quota` | `number` | `provider-unspecified; model permissively` | rule: For ad groups within regular SKAN 4 |
| `data.ad_quota_info.used_ad_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.ad_quota_info.available_ad_quota` | `number` | `provider-unspecified; model permissively` | - |
| `data.ad_quota_info.adgroup_id` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CAMPAIGN_LABEL_GET`

- Operation: Get the campaign labels of an ad account
- Wire: `GET /campaign_label/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1851286489283585`, [official page](https://business-api.tiktok.com/portal/docs?id=1851286489283585)
- Contract SHA-256: `0bde24742221001cfd5a8d482415fe1bd4cd055c3b5b7e200619c398e24579ab`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `campaign_label_ids` | `query` | `string[]` | `optional` | size: 50; rule: Each label ID must be a 19-digit numeric string; rule: Note : This filter is only supported in synchronous basic reports |
| `campaign_label_names` | `query` | `string[]` | `optional` | size: 10 |
| `campaign_label_types` | `query` | `string[]` | `optional` | allowed: GENERAL, MARKETING_EVENT |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-1,000; rule: Value range: 1-1,000 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | rule: Details of the campaign labels within an ad account |
| `data.list[].campaign_label_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].campaign_label_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].campaign_label_type` | `string` | `provider-unspecified; model permissively` | allowed: GENERAL, MARKETING_EVENT |
| `data.list[].campaign_label_color` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].create_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the campaign label was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CHANGELOG_GET`

- Operation: Get the activity log of a Business Center
- Wire: `GET /changelog/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1820767460168705`, [official page](https://business-api.tiktok.com/portal/docs?id=1820767460168705)
- Contract SHA-256: `d962772a9cea251318e89d38e28f17d0363bc3defeb0fa35ece67676e1ab8b07`
- Required live inputs from request contract: `bc_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.start_date` | `query` | `string` | `optional` | rule: Query start date, in the format of YYYY-MM-DD (UTC+0); rule: Recommended date range: six months |
| `filtering.end_date` | `query` | `string` | `optional` | rule: Query end date, in the format of YYYY-MM-DD (UTC+0); rule: Recommended date range: six months |
| `filtering.activity_type` | `query` | `string` | `optional` | allowed: ALL, USER, ACCOUNT, ASSET, BUSINESS; default: ALL |
| `lang` | `query` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `sort_field` | `query` | `string` | `optional` | allowed: operation_time; default: operation_time; rule: Enum value: operation_time: To sort by the time when the activity occurred, which corresponds to the time parameter within the returned object array changelog_list |
| `sort_type` | `query` | `string` | `optional` | allowed: DESC, ASC; default: DESC |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.changelog_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.changelog_list[].time` | `string` | `provider-unspecified; model permissively` | rule: The time of the activity, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.changelog_list[].activity_type` | `string` | `provider-unspecified; model permissively` | allowed: USER, ACCOUNT, ASSET, BUSINESS |
| `data.changelog_list[].operator_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.changelog_list[].activity_log` | `string` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CHANGELOG_TASK_DOWNLOAD`

- Operation: Get the downloaded file
- Wire: `GET /changelog/task/download/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1739924165710849`, [official page](https://business-api.tiktok.com/portal/docs?id=1739924165710849)
- Contract SHA-256: `956a76be30cb405032c42d583c2d99dbeea9403ad84ef03e2080f475f08d6d0a`
- Required live inputs from request contract: `advertiser_id`, `task_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.status` | `string` | `provider-unspecified; model permissively` | allowed: PROCESSING, SUCCESS, FAILED |
| `data.changelog` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_GET`

- Operation: Get negative keywords
- Wire: `GET /search_ad/negative_keyword/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1775104887052289`, [official page](https://business-api.tiktok.com/portal/docs?id=1775104887052289)
- Contract SHA-256: `cb6c5ab08776ac8d0e6f1a3471c2f26408bf11dc1745e6a42f74a30867155d86`
- Required live inputs from request contract: `advertiser_id`, `object_id`, `object_type`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `object_type` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_id` | `query` | `string` | `required` | - |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: [1,50]; rule: Value range: [1,50] |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.keywords` | `object[]` | `provider-unspecified; model permissively` | size: 1,000 |
| `data.keywords[].keyword_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.keywords[].name` | `string` | `provider-unspecified; model permissively` | - |
| `data.keywords[].match_type` | `string` | `provider-unspecified; model permissively` | allowed: PRECISE_WORD, PHRASE_WORD, BROAD_WORD |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SHOWCASE_IDENTITY_GET`

- Operation: Get identities with Showcase permission under an ad account
- Wire: `GET /showcase/identity/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1759233549899778`, [official page](https://business-api.tiktok.com/portal/docs?id=1759233549899778)
- Contract SHA-256: `d508b8237854da58393fd458aa976cea01333713220ca87f0aabb789548033cb`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `identity_id` | `string` | `provider-unspecified; model permissively` | - |
| `identity_type` | `string` | `provider-unspecified; model permissively` | allowed: TT_USER, BC_AUTH_TT |
| `identity_authorized_bc_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SHOWCASE_PRODUCT_GET`

- Operation: Get the available products in a Showcase
- Wire: `GET /showcase/product/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1759233576199169`, [official page](https://business-api.tiktok.com/portal/docs?id=1759233576199169)
- Contract SHA-256: `e7036d54deb4ebca33282e6eecded98c7eae258c236dbb4a56929471bb6c517f`
- Required live inputs from request contract: `advertiser_id`, `identity_id`, `identity_type`, `region_codes`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
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


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.showcase_products` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].item_group_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].title` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].product_image_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].min_price` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].max_price` | `string` | `provider-unspecified; model permissively` | rule: The maximum price of the product |
| `data.showcase_products[].currency` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].category` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].status` | `string` | `provider-unspecified; model permissively` | allowed: AVAILABLE, NOT_AVAILABLE |
| `data.showcase_products[].catalog_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.showcase_products[].store_id` | `string` | `provider-unspecified; model permissively` | rule: Note that the only supported store type is TikTok Shop |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SHOWCASE_REGION_GET`

- Operation: Get the available regions for a Showcase via identity
- Wire: `GET /showcase/region/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1759233561597954`, [official page](https://business-api.tiktok.com/portal/docs?id=1759233561597954)
- Contract SHA-256: `ff69b373cb153d23621c00fc0e22da3ab46ffb08d9bcf10906f0b295044def07`
- Required live inputs from request contract: `advertiser_id`, `identity_id`, `identity_type`
- Product/fixture gate: Advertiser with Showcase identity, region, and product access
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `identity_id` | `query` | `string` | `required` | - |
| `identity_type` | `query` | `string` | `required` | allowed: TT_USER, BC_AUTH_TT |
| `identity_authorized_bc_id` | `query` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.region_codes` | `string[]` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CHECK`

- Operation: Get the results of an asynchronous copy task for an Upgraded Smart+ Campaign
- Wire: `GET /smart_plus/campaign/copy/task/check/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1866529943741441`, [official page](https://business-api.tiktok.com/portal/docs?id=1866529943741441)
- Contract SHA-256: `690f7bf9b4a7792726096bccc67c80047e2b336d6513ac6d3d6cb27619f28702`
- Required live inputs from request contract: `advertiser_id`, `task_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_status` | `string` | `provider-unspecified; model permissively` | allowed: RUNNING, SUCCESS, FAILURE |
| `data.task_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_info.total_ad_count` | `number` | `provider-unspecified; model permissively` | - |
| `data.task_info.success_ad_count` | `number` | `provider-unspecified; model permissively` | - |
| `data.task_result` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_result.campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.campaign_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.campaign_error_infos` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].adgroup_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].adgroup_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].total_ad_count` | `number` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].success_ad_count` | `number` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].adgroup_error_list` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].ad_status` | `string` | `provider-unspecified; model permissively` | allowed: ALL_SUCCESS, PARTIAL_SUCCESS |
| `data.task_result.adgroup_result_list[].ad_result_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].is_success` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.task_result.adgroup_result_list[].ad_result_list[].smart_plus_ad_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].ad_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.task_result.adgroup_result_list[].ad_result_list[].ad_error_list` | `string[]` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 6: P6 Other Ads POST actions

Actions in this prompt: **5**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_BUSINESS_SPARK_AD_CREATE` -> `POST /business/spark_ad/create/`
- `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_ADD` -> `POST /search_ad/negative_keyword/add/`
- `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_DELETE` -> `POST /search_ad/negative_keyword/delete/`
- `TIKTOK_ADS_SMART_PLUS_ADGROUP_BUDGET_UPDATE` -> `POST /smart_plus/adgroup/budget/update/`
- `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CREATE` -> `POST /smart_plus/campaign/copy/task/create/`

Embedded provider contract manifest:

### `TIKTOK_ADS_BUSINESS_SPARK_AD_CREATE`

- Operation: Create a campaign, an ad group, and a Spark Ad in one step
- Wire: `POST /business/spark_ad/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1829744071179330`, [official page](https://business-api.tiktok.com/portal/docs?id=1829744071179330)
- Contract SHA-256: `e79299d9800b72d9552be44b3ef51c2755550987aec87225d8e739c18028a3d2`
- Additional enum evidence: doc `1737174886619138`, [official page](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Authorized TikTok identity/post and a disposable non-delivering campaign fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `campaign_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `objective_type` | `json_body` | `string` | `optional` | allowed: REACH, TRAFFIC, VIDEO_VIEWS, ENGAGEMENT |
| `adgroup_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `saved_audience_id` | `json_body` | `string` | `optional` | rule: Either saved_audience_id or location_ids is required; rule: Before using this field, call /dmp/saved_audience/create/ to create a Saved Audience and get the Saved Audience ID in response |
| `location_ids` | `json_body` | `string[]` | `optional` | size: 3,000; rule: Either saved_audience_id or location_ids is required |
| `gender` | `json_body` | `string` | `optional` | allowed: GENDER_FEMALE, GENDER_MALE, GENDER_UNLIMITED |
| `age_groups` | `json_body` | `string[]` | `optional` | allowed: AGE_13_17, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45_54, AGE_55_100 |
| `budget_mode` | `json_body` | `string` | `optional` | allowed: BUDGET_MODE_TOTAL, BUDGET_MODE_DAY; rule: If this field is set to BUDGET_MODE_TOTAL, then schedule_type must be SCHEDULE_START_END, which requires an end date (schedule_end_time) |
| `budget` | `json_body` | `float` | `optional` | - |
| `schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_START_END, SCHEDULE_FROM_NOW; rule: If budget_mode is BUDGET_MODE_TOTAL, this field must be set to SCHEDULE_START_END; rule: SCHEDULE_FROM_NOW: To run the campaign continuously after the scheduled start time |
| `schedule_start_time` | `json_body` | `string` | `optional` | rule: Schedule start time (UTC+0), in the format of YYYY-MM-DD HH:MM:SS; rule: The start time can be up to 12 hours earlier than the current time, but cannot be later than 2028-01-01 00:00:00 |
| `schedule_end_time` | `json_body` | `string` | `optional` | rule: Required when schedule_type is SCHEDULE_START_END; rule: Schedule end time (UTC+0), in the format of YYYY-MM-DD HH:MM:SS; rule: The end time cannot be later than 2038-01-01 00:00:00 |
| `optimization_goal` | `json_body` | `string` | `optional` | mapping: REACH=>REACH; TRAFFIC=>CLICK|TRAFFIC_LANDING_PAGE_VIEW; VIDEO_VIEWS=>ENGAGED_VIEW; ENGAGEMENT=>FOLLOWERS|PAGE_VISIT |
| `frequency` | `json_body` | `number` | `optional` | all-of: frequency range: 1–1,000. || frequency_schedule: 1–30 (days).; rule: Required when objective_type is REACH; rule: Frequency, the maximum number of times a user can see your ad within a given period; rule: The following conditions should be both met: frequency range: 1–1,000; rule: For instance, frequency = 2 and frequency_schedule = 3 ensure ads are shown no more than twice every three days |
| `frequency_schedule` | `json_body` | `number` | `optional` | all-of: frequency range: 1–1,000. || frequency_schedule: 1–30 (days).; rule: Required when objective_type is REACH; rule: The following conditions should be both met: frequency range: 1–1,000; rule: For instance, frequency = 2 and frequency_schedule = 3 ensure ads are shown no more than twice every three days |
| `bid_type` | `json_body` | `string` | `optional` | allowed: BID_TYPE_CUSTOM, BID_TYPE_NO_BID; default: BID_TYPE_NO_BID; rule: BID_TYPE_NO_BID: Maximum Delivery |
| `bid_price` | `json_body` | `number` | `optional` | all-of: optimization_goal is REACH, CLICK, PAGE_VISIT, or ENGAGED_VIEW. || bid_type is BID_TYPE_CUSTOM.; rule: Required when the following conditions are both met: optimization_goal is REACH, CLICK, PAGE_VISIT, or ENGAGED_VIEW |
| `conversion_bid_price` | `json_body` | `float` | `optional` | all-of: optimization_goal is TRAFFIC_LANDING_PAGE_VIEW, or FOLLOWERS. || bid_type is BID_TYPE_CUSTOM.; rule: Required when the following conditions are both met: optimization_goal is TRAFFIC_LANDING_PAGE_VIEW, or FOLLOWERS |
| `ad_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: The format of the auto-generated ad name is ad ID (ad_id); rule: Length limit: 512 characters; rule: Emojis are not supported |
| `identity_type` | `json_body` | `string` | `optional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT |
| `identity_id` | `json_body` | `string` | `optional` | - |
| `identity_authorized_bc_id` | `json_body` | `string` | `optional` | rule: Required when identity_type is BC_AUTH_TT |
| `tiktok_item_id` | `json_body` | `string` | `optional` | - |
| `call_to_action` | `json_body` | `string` | `optional` | rule: Required when optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `landing_page_url` | `json_body` | `string` | `optional` | any-of: optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT. || optimization_goal is REACH or ENGAGED_VIEW and call_to_action is specified.; rule: Required in any of the following conditions: optimization_goal is CLICK, TRAFFIC_LANDING_PAGE_VIEW, or PAGE_VISIT; rule: Not supported when optimization_goal is FOLLOWERS or PAGE_VISIT |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.campaign_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.adgroup_id` | `string` | `provider-unspecified; model permissively` | rule: The ID of the ad group created within the campaign |
| `data.ad_id` | `string` | `provider-unspecified; model permissively` | rule: The ID of the Spark Ad created within the ad group |

### `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_ADD`

- Operation: Create negative keywords
- Wire: `POST /search_ad/negative_keyword/add/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1775104895291393`, [official page](https://business-api.tiktok.com/portal/docs?id=1775104895291393)
- Contract SHA-256: `c2676d4825e315a97398d6ad00e1c14ada161436e9cd7c755c7a639064b519a1`
- Required live inputs from request contract: `advertiser_id`, `keywords`, `keywords[].name`, `object_ids`, `object_type`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `object_type` | `json_body` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_ids` | `json_body` | `string[]` | `required` | size: 50 |
| `replace` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |
| `keywords` | `json_body` | `object[]` | `required` | size: 1,000; rule: Note : For each ad group, you can configure a maximum of 10,000 negative keywords |
| `keywords[].name` | `json_body` | `string` | `required` | length: 80 characters; rule: Length limit: 80 characters |
| `keywords[].match_type` | `json_body` | `string` | `optional` | allowed: PRECISE_WORD, PHRASE_WORD, BROAD_WORD; default: BROAD_WORD |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_DELETE`

- Operation: Delete negative keywords
- Wire: `POST /search_ad/negative_keyword/delete/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1775104910010369`, [official page](https://business-api.tiktok.com/portal/docs?id=1775104910010369)
- Contract SHA-256: `477bd35e4df4aa8de417a7b2f3740783a67d386e74a77010656021bb503278f1`
- Required live inputs from request contract: `advertiser_id`, `keyword_ids`, `object_id`, `object_type`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `object_type` | `json_body` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_id` | `json_body` | `string` | `required` | - |
| `keyword_ids` | `json_body` | `string[]` | `required` | size: 1,000 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SMART_PLUS_ADGROUP_BUDGET_UPDATE`

- Operation: Update the budgets of Upgraded Smart+ Ad Groups
- Wire: `POST /smart_plus/adgroup/budget/update/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `updates`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1843314914438466`, [official page](https://business-api.tiktok.com/portal/docs?id=1843314914438466)
- Contract SHA-256: `6517dfda5ef0e0d349247f1f7b72f59b7e26b785cdf9af729e8b5e7843e1b8f6`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `budget` | `json_body` | `object[]` | `conditional` | size: 20 |
| `budget[].adgroup_id` | `json_body` | `string` | `conditional` | condition: the object array budget is specified; rule: Required when the object array budget is specified |
| `budget[].budget` | `json_body` | `float` | `conditional` | condition: the object array budget is specified; rule: Required when the object array budget is specified |
| `scheduled_budget` | `json_body` | `object[]` | `conditional` | size: 20 |
| `scheduled_budget[].adgroup_id` | `json_body` | `string` | `conditional` | condition: the object array scheduled_budget is specified; any-of: If the ad group (adgroup_id) is part of a CBO campaign (where budget_optimize_on istrue), a min_budget or max_budget or both must be configured. || No prerequisites apply for ad groups within non-CBO campaigns (w; rule: Required when the object array scheduled_budget is specified; rule: Note : If the ad group (adgroup_id) is part of a CBO campaign (where budget_optimize_on istrue), a min_budget or max_budget or both must be configured |
| `scheduled_budget[].scheduled_budget` | `json_body` | `float` | `conditional` | condition: the object array scheduled_budget is specified; any-of: For an ad group in a CBO campaign (where budget_optimize_on is true), a min_budget or max_budget or both must be configured. This field will set the maximum daily budget control fo || For an ad group in a non-CBO; rule: Required when the object array scheduled_budget is specified; rule: The maximum budget control or the new budget for the ad group (adgroup_id); rule: This field will set the maximum daily budget control for the ad group |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CREATE`

- Operation: Create an asynchronous copy task for an Upgraded Smart+ Campaign
- Wire: `POST /smart_plus/campaign/copy/task/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Ads Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1866528879472641`, [official page](https://business-api.tiktok.com/portal/docs?id=1866528879472641)
- Contract SHA-256: `92e9dd7c171d932434ac0ebff41040a392df3bf2be9de61d8b7d96ab99073a6c`
- Additional enum evidence: doc `1737174886619138`, [official page](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`
- Required live inputs from request contract: `advertiser_id`, `campaign_id`, `request_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `request_id` | `json_body` | `string` | `required` | rule: If you retry requests with the same request ID multiple times within the 10-second cache time, then only one request will succeed; rule: If a duplicate request with the expired request ID is received after the cache time, the server will treat it as a new request and process it accordingly |
| `campaign_id` | `json_body` | `string` | `required` | rule: To retrieve Upgraded Smart+ Campaigns within your ad account, use /smart_plus/campaign/get/; rule: Note : The source campaign must use one of these advertising objectives: APP_PROMOTION, LEAD_GENERATION, WEB_CONVERSIONS; rule: The source campaign must not be deleted; rule: The source campaign must contain at least 1 undeleted ad group, which must contain at least 1 undeleted ad; rule: The source campaign must satisfy all per-level limits, and the total copied assets must also not exceed the global new campaign limits: On the source campaign: you may have a maximum of 10 undeleted a |
| `operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: DISABLE; rule: If you want to update the status of the campaign after creation, use /smart_plus/campaign/status/update/ |
| `campaign_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `budget` | `json_body` | `number` | `optional` | rule: The budget for the new campaign or the budget limit for all ad groups under the new campaign; rule: To retrieve the current campaign budget, use /smart_plus/campaign/get/ after the copy task is completed and check the returned current_budget; rule: When budget_optimize_on of the source campaign is false, this field represents the budget limit for all ad groups under the new campaign; rule: When budget_mode is BUDGET_MODE_DAY, this field represents the daily limit for all ad groups under the new campaign; rule: When budget_mode is BUDGET_MODE_TOTAL, this field represents the total limit for all ad groups under the new campaign |
| `schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_START_END, SCHEDULE_FROM_NOW; rule: You need to pass both schedule_start_time and schedule_end_time at the same time |
| `schedule_start_time` | `json_body` | `string` | `conditional` | condition: schedule_type is passed; rule: Required when schedule_type is passed; rule: Schedule start time (UTC+0) for all new ad groups, in the format of YYYY-MM-DD HH:MM:SS; rule: The start time can be up to 12 hours earlier than the current time, but cannot be later than 2028-01-01 00:00:00 |
| `schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: Schedule end time (UTC+0) for all new ad groups, in the format of YYYY-MM-DD HH:MM:SS; rule: The end time cannot be later than 2038-01-01 00:00:00 |
| `dayparting` | `json_body` | `string` | `optional` | rule: Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters |
| `deep_copy_mode` | `json_body` | `string` | `optional` | allowed: DEFAULT, CUSTOM; default: DEFAULT; rule: You can copy a maximum of 20 ads per ad group, across a maximum of 30 ad groups |
| `adgroup_list` | `json_body` | `object[]` | `optional` | size: 10; rule: When deep_copy_mode is set to CUSTOM, this field is required |
| `adgroup_list[].adgroup_id` | `json_body` | `string` | `conditional` | condition: adgroup_list is passed; rule: Required when adgroup_list is passed |
| `adgroup_list[].operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: ENABLE; rule: If you want to update the status of the ad group after creation, use /smart_plus/adgroup/status/update/ |
| `adgroup_list[].adgroup_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `adgroup_list[].budget` | `json_body` | `number` | `optional` | rule: To retrieve the current ad group budget, use /smart_plus/adgroup/get/ after the copy task is completed and check the returned current_budget |
| `adgroup_list[].min_budget` | `json_body` | `number` | `optional` | all-of: At the campaign level:budget_optimize_on is truebudget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET || At the ad group level:bid_type is BID_TYPE_NO_BID; rule: Valid only when the following conditions are all met: At the campaign level: budget_optimize_on is true; rule: The system will aim to spend at least this amount, but it is not guaranteed |
| `adgroup_list[].targeting_spec` | `json_body` | `object` | `optional` | - |
| `adgroup_list[].targeting_spec.location_ids` | `json_body` | `string[]` | `optional` | rule: Note : If you add the US as your target location, then you can not remove the US after ad group creation |
| `adgroup_list[].targeting_spec.zipcode_ids` | `json_body` | `string[]` | `optional` | size: 3,000; rule: If you provide both location_ids and zipcode_ids, the combined total of location IDs, zip code IDs, and postal code IDs cannot exceed 3,000 per ad group; rule: Note : Zip code targeting is currently only supported for the US and postal code targeting is currently only supported for Canada, Brazil, Indonesia, Thailand, and Vietnam; rule: You cannot use zip code targeting or postal code targeting in campaigns that have enabled special ad categories (special_industries); rule: Overlapping targeted locations are not supported; rule: For instance, you cannot target the US and the state of California at the same time |
| `adgroup_list[].targeting_spec.excluded_audience_ids` | `json_body` | `string[]` | `optional` | rule: Note : When at the campaign level rta_id is specified, this field is not supported |
| `adgroup_list[].targeting_spec.audience_ids` | `json_body` | `string[]` | `optional` | rule: Note : When at the campaign level rta_id is specified, this field is not supported |
| `adgroup_list[].targeting_spec.saved_audience_id` | `json_body` | `string` | `optional` | all-of: The targeting_optimization_mode of the source ad group is MANUAL. || The category of Housing, Employment, or Credit (specical_industries) is NOT specified in your campaign. || TikTok placement is selected in your; rule: Before using this field, call /dmp/saved_audience/create/ to create a Saved Audience and get the Saved Audience ID in response; rule: If you use saved_audience_id to create an ad group, we will return both the Saved Audience ID and the targeting options that are included within your Saved Audience in response; rule: However, be aware that if you are creating an ad group based on a Saved Audience, it’s essential to avoid setting both the saved_audience_id and targeting options (such as gender) defined within your ; rule: Make sure that the age targeting setting is allowed before you use the Saved Audience (saved_audience_id ) in the ad group |
| `adgroup_list[].ad_list` | `json_body` | `object[]` | `conditional` | size: 30; rule: When deep_copy_mode is set to CUSTOM, this field is required; rule: Note : The maximum number of ads that you can specify in the new campaign is 200 |
| `adgroup_list[].ad_list[].smart_plus_ad_id` | `json_body` | `string` | `conditional` | condition: ad_list is passed; rule: Required when ad_list is passed |
| `adgroup_list[].ad_list[].operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: ENABLE; rule: If you want to update the status of the ad after creation, use /smart_plus/ad/status/update/ |
| `adgroup_list[].ad_list[].ad_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `adgroup_list[].ad_list[].creative_list` | `json_body` | `object[]` | `optional` | size: 1-50; rule: Size range: 1-50; rule: The maximum number of creatives that you can specify in the new campaign is 1,000 |
| `adgroup_list[].ad_list[].creative_list[].creative_info` | `json_body` | `object` | `conditional` | condition: creative_list is specified; rule: Required when creative_list is specified |
| `adgroup_list[].ad_list[].creative_list[].creative_info.ad_format` | `json_body` | `string` | `conditional` | condition: creative_info is specified; any-of: SINGLE_VIDEO: Single Video.To use this format, specify any of the following:a video through video_id and a video cover through web_uria TikTok video post through tiktok_item_id. || CAROUSEL_ADS: Standard Carousel; rule: Required when creative_info is specified; rule: The ad format; rule: To use this format, specify any of the following: a video through video_id and a video cover through web_uri; rule: To use this format, specify any of the following: carousel images through web_uri and a piece of music through music_id |
| `adgroup_list[].ad_list[].creative_list[].creative_info.video_info` | `json_body` | `object` | `conditional` | rule: Required for Spark Ads Single Video ads through Spark Ads Push |
| `video_id` | `json_body` | `string` | `conditional` | condition: video_info is specified; rule: Required when video_info is specified; rule: To search for videos within your ad account, use /file/video/ad/search/ |
| `file_name` | `json_body` | `string` | `optional` | - |
| `adgroup_list[].ad_list[].creative_list[].creative_info.image_info` | `json_body` | `object[]` | `conditional` | any-of: Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. || Spark Ads Standard Carousel ads through Spark Ads Push. You need to specify one to 35 carousel images. || Catalog Carousel ; rule: Required for the following types of ads: Spark Ads Single Video ads through Spark Ads Push; rule: Not supported for Catalog Carousel ads in Upgraded Smart+ Web Ads |
| `web_uri` | `json_body` | `string` | `conditional` | condition: image_info is specified; rule: Required when image_info is specified; rule: To search for images within your ad account, use /file/image/ad/search/ |
| `adgroup_list[].ad_list[].creative_list[].creative_info.music_info` | `json_body` | `object` | `conditional` | any-of: When you create Standard Carousel Ads, including:Spark Ads Standard Carousel ads through Spark Ads PushSpark Ads Standard Carousel ads through Spark Ads Pull || When objective_type is WEB_CONVERSIONS or LEAD_GENE; rule: Required for the following scenarios: When you create Standard Carousel Ads, including: Spark Ads Standard Carousel ads through Spark Ads Push |
| `music_id` | `json_body` | `string` | `conditional` | condition: music_info is specified; rule: Required when music_info is specified |
| `adgroup_list[].ad_list[].creative_list[].creative_info.aigc_disclosure_type` | `json_body` | `string` | `optional` | allowed: SELF_DISCLOSURE, NOT_DECLARED; default: NOT_DECLARED; rule: After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full |
| `adgroup_list[].ad_list[].creative_list[].creative_info.tiktok_item_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; any-of: Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. || Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post.; rule: Required when you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; rule: Not supported when catalog_creative_toggle is true |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_type` | `json_body` | `string` | `conditional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT; condition: you create Spark Ads; rule: Required when you create Spark Ads |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads; rule: Required when you create Spark Ads |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |
| `adgroup_list[].ad_list[].ad_text_list` | `json_body` | `object[]` | `conditional` | size: 5; condition: tiktok_item_id is not specified; rule: Required when tiktok_item_id is not specified |
| `adgroup_list[].ad_list[].ad_text_list[].ad_text` | `json_body` | `string` | `conditional` | condition: ad_text_list is specified; rule: Required when ad_text_list is specified |
| `adgroup_list[].ad_list[].call_to_action_list` | `json_body` | `object[]` | `conditional` | size: 3; rule: Note : This field is not supported in any of the following scenarios and you need to use call_to_action_id instead; rule: At the ad level, identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE |
| `adgroup_list[].ad_list[].call_to_action_list[].call_to_action` | `json_body` | `string` | `conditional` | condition: call_to_action_list is specified; rule: Required when call_to_action_list is specified; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `adgroup_list[].ad_list[].landing_page_url_list` | `json_body` | `object[]` | `optional` | size: 0-1; rule: Size range: 0-1 |
| `adgroup_list[].ad_list[].landing_page_url_list[].landing_page_url` | `json_body` | `string` | `conditional` | condition: landing_page_url_list is specified; rule: Required when landing_page_url_list is specified |
| `adgroup_list[].ad_list[].ad_configuration` | `json_body` | `object` | `optional` | - |
| `adgroup_list[].ad_list[].ad_configuration.utm_params` | `json_body` | `object[]` | `optional` | size: 14; cross-field: when landing_page_url to a URL that already includes URL parameters, you can optionally pass utm_params at the same time to store the URL parameters used in the URL. In such cases,; rule: If you set landing_page_url to a URL that already includes URL parameters, you can optionally pass utm_params at the same time to store the URL parameters used in the URL |
| `adgroup_list[].ad_list[].ad_configuration.utm_params[].key` | `json_body` | `string` | `optional` | rule: Length limit when you specify a custom parameter: 100 characters |
| `adgroup_list[].ad_list[].ad_configuration.utm_params[].value` | `json_body` | `string` | `optional` | rule: Length limit when you specify a custom value: 600 characters |
| `adgroup_list[].ad_list[].ad_configuration.call_to_action_id` | `json_body` | `string` | `optional` | rule: At the ad level, identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.adgroup_error_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.adgroup_error_list[].adgroup_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.adgroup_error_list[].error_message` | `string` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 7: P7 Creative GET actions

Actions in this prompt: **8**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_GET` -> `GET /creative/auto_message/get/`
- `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_GET` -> `GET /creative/pre_review/task/get/`
- `TIKTOK_ADS_DISCOVERY_CML_TRENDING_LIST` -> `GET /discovery/cml/trending_list/`
- `TIKTOK_ADS_DISCOVERY_CML_VIDEO_LIST` -> `GET /discovery/cml/video_list/`
- `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH` -> `GET /discovery/trending/search/`
- `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH_KEYWORD` -> `GET /discovery/trending/search/keyword/`
- `TIKTOK_ADS_FILE_NAME_CHECK` -> `GET /file/name/check/`
- `TIKTOK_ADS_VIDEO_FIX_TASK_GET` -> `GET /video/fix/task/get/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_GET`

- Operation: Get welcome messages within an ad account
- Wire: `GET /creative/auto_message/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822106498804738`, [official page](https://business-api.tiktok.com/portal/docs?id=1822106498804738)
- Contract SHA-256: `07038c4d2be4473295ad139d763c403bdfc1d2973599d0452795c9fb3c9ebcf2`
- Required live inputs from request contract: `advertiser_id`, `auto_message_type`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `auto_message_type` | `query` | `string` | `required` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `auto_message_id` | `query` | `string` | `optional` | - |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-100; rule: Value range: 1-100 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | rule: The list of automatic messages within the ad account |
| `data.list[].auto_message_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].auto_message_type` | `string` | `provider-unspecified; model permissively` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `data.list[].welcome_message` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].welcome_message.title` | `string` | `provider-unspecified; model permissively` | rule: You can use the name to distinguish between different welcome messages within the welcome message library of your ad account |
| `data.list[].welcome_message.content` | `string` | `provider-unspecified; model permissively` | rule: The greeting within the welcome message |
| `data.list[].welcome_message.suggested_questions` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].welcome_message.suggested_questions[].question` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].welcome_message.suggested_questions[].answer` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].audit_status` | `string` | `provider-unspecified; model permissively` | allowed: AUDITING, PASS, REJECTED |
| `data.list[].create_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the automatic message was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_GET`

- Operation: Get the result of a creative pre-review task
- Wire: `GET /creative/pre_review/task/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1874110636550082`, [official page](https://business-api.tiktok.com/portal/docs?id=1874110636550082)
- Contract SHA-256: `18d77a2b51c4b2ee97866a07bb7bf52f9bfc34ca433563b31991b01a77447ca2`
- Required live inputs from request contract: `advertiser_id`, `task_id`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_status` | `string` | `provider-unspecified; model permissively` | allowed: PROCESSING, SUCCESS |
| `data.pre_review_result_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.pre_review_result_list[].pre_review_status` | `string` | `provider-unspecified; model permissively` | allowed: APPROVED, REJECTED, UNSURE, UNAVAILABLE; rule: UNSURE: Result cannot be determined |
| `data.pre_review_result_list[].material_type` | `string` | `provider-unspecified; model permissively` | allowed: VIDEO, IMAGE, AD_TEXT, LANDING_PAGE_URL |
| `data.pre_review_result_list[].material_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.pre_review_result_list[].result_creation_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the pre-review result was generated, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.pre_review_result_list[].result_expiration_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the pre-review result will expire, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.pre_review_result_list[].location_code` | `string` | `provider-unspecified; model permissively` | allowed: AD, AE, AG, AI, AL, AO, AR, AT, AU, AW, AZ, BA, BB, BD, BE, BG, BH, BL, BM, BO, BQ, BR, BS, BY, BZ, CA, CD, CH, CL, CO, CR, CU, CV, CW, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, ER, ES, FI, FO, FR, GB, GD, GE, GF, GG, GI, GL, GN, GP, GQ, GR, GT, GW, HK, HN, HR, HT, HU, ID, IE, IL, IM, IN, IQ, IS, IT, JE, JM, JO, JP, KE, KH, KM, KN, KR, KW, KY, KZ, LB, LC, LI, LK, LT, LU, LV, LY, MA, MC, MD, ME, MF, MK, MM, MO, MQ, MR, MS, MT, MX, MY, MZ, NG, NI, NL, NO, NP, NZ, OM, PA, PE, PF, PH, PK, PL, PM, PR, PS, PT, PY, QA, RO, RS, RU, SA, SD, SE, SG, SI, SJ, SK, SM, SO, SS, ST, SV, SX, SY, TC, TD, TF, TH, TN, TR, TT, TW, UA, US, UY, UZ, VC, VE, VG, VI, VN, YE, ZA |
| `data.pre_review_result_list[].is_ecommerce` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.pre_review_result_list[].reject_info_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.pre_review_result_list[].reject_info_list[].reason` | `string` | `provider-unspecified; model permissively` | - |
| `data.pre_review_result_list[].reject_info_list[].suggestion` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DISCOVERY_CML_TRENDING_LIST`

- Operation: Get popular tracks from the Commercial Music Library
- Wire: `GET /discovery/cml/trending_list/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1825119063013505`, [official page](https://business-api.tiktok.com/portal/docs?id=1825119063013505)
- Contract SHA-256: `fd021b078d09ea4c05a81fd64f59b01208f0759c602faf5deda715359fdec8dc`
- Required live inputs from request contract: `business_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `genre` | `query` | `string` | `optional` | default: ALL; allowed: ALL, ROCK, POP, LATIN, METAL, ELECTRONIC, HIP_HOP/RAP, ALTERNATIVE/INDIE, FOLK, R&B/SOUL, COUNTRY, CLASSICAL, JAZZ, REGGAE, CHILDHOOD, BLUES, EASY_LISTENING, NEW_AGE, WORLD_MUSIC, EXPERIMENTAL, DEVOTIONAL, CHINESE_TRADITION, 8_BIT, A_CAPPELLA, AFRO-POP, ALTERNATIVE_HIP_HOP, ALTERNATIVE_ROCK, AMBIENT, ARABIC_POP, BASS_HOUSE, BGM, BOOMBAP, BOSSA_NOVA, BRAZILIAN_FUNK_STYLE, BUDDHIST_MUSIC, CANTOPOP, CELTIC_POP, CHAMBER_MUSIC, CHILL_BEATS, CHILLOUT, CHINESE_FOLK, CHINESE_OPERA, CHINESE_POP, CHINESE_STYLE, CHINOISERIE_ELECTRONIC, CHINOISERIE_RAP, CHRISTIAN_MUSIC, CONTEMPORARY_R&B, COUNTRY_POP, DANCE_POP, DISCO, DJ, DRUM&BASS, DUBSTEP, EDM, EDM_TRAP, ELECTRO_POP, EPIC, FOLK_POP, FUNK, FUTURE_BASS, GOSPEL, GUFENG_MUSIC, HARD_ROCK, HIP_HOUSE, HOLIDAY_MUSIC, HOUSE, INDIAN_POP, INDIE_FOLK, INDIE_POP, INDIE_ROCK, INSTRUMENTAL_HIP_HOP, INSTRUMENTAL_ROCK, IRISH_FOLK, J_ROCK, JAPANESE_TRADITIONAL_MUSIC, JAZZ_FUSION, JAZZ_HIP_HOP, JAZZ_POP, J-POP, K-POP, LATIN_POP, LO-FI, MC, NOISE, OLD_SCHOOL, OTHERS, POP_RAP, POP_ROCK, POP_SOUL, PSYCHEDELIC_ROCK, PUNK, R&B_RAP, REGGAETON, RUSSIAN_POP, SERTANEJO, SON_CUBANO, SOUL, SOUNDTRACK, SYMPHONY, SYNTH_POP, TANGO, TECHNO, TEEN_POP, TRADITIONAL_CHINESE_FOLK, TRANCE, TRAP_RAP, TRIP_HOP, TROPICAL_HOUSE, TURKISH_POP |
| `country_code` | `query` | `string` | `optional` | default: US |
| `date_range` | `query` | `string` | `optional` | allowed: 1DAY, 7DAY, 30DAY, 90DAY; default: 7DAY |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].commercial_music_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].commercial_music_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].duration` | `integer` | `provider-unspecified; model permissively` | - |
| `data.list[].thumbnail_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].artist` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].preview_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].genres` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.list[].rank_position` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_history` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_history[].date` | `string` | `provider-unspecified; model permissively` | rule: Date, in the format of YYYY-MM-DD |
| `data.list[].trending_history[].rank_position_daily` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].full_duration_song_clip` | `object` | `provider-unspecified; model permissively` | - |
| `data.list[].full_duration_song_clip.preview_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].full_duration_song_clip.duration` | `integer` | `provider-unspecified; model permissively` | - |
| `data.list[].full_duration_song_clip.song_clip_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_song_clip` | `object` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_song_clip.preview_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_song_clip.duration` | `integer` | `provider-unspecified; model permissively` | - |
| `data.list[].trending_song_clip.song_clip_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DISCOVERY_CML_VIDEO_LIST`

- Operation: Get trending videos related to tracks
- Wire: `GET /discovery/cml/video_list/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1825119068941314`, [official page](https://business-api.tiktok.com/portal/docs?id=1825119068941314)
- Contract SHA-256: `23d62c742a1f6621e05c6dc9561503e6e565765d8b179727a258b812d29a0d45`
- Required live inputs from request contract: `business_id`, `commercial_music_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `commercial_music_id` | `query` | `string` | `required` | - |
| `country_code` | `query` | `string` | `optional` | default: US |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.commercial_music_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.commercial_music_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.top_video_list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.top_video_list[].video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.top_video_list[].embed_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.top_video_list[].share_url` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH`

- Operation: Get trending search keywords
- Wire: `GET /discovery/trending/search/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1832798345014338`, [official page](https://business-api.tiktok.com/portal/docs?id=1832798345014338)
- Contract SHA-256: `1372cc3165cff55d0688cf5dbd3587b78b35f261b325abb0e0eb8348ba71c199`
- Required live inputs from request contract: `business_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `is_personalized` | `query` | `boolean` | `optional` | default: false |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.search_keywords` | `string[]` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH_KEYWORD`

- Operation: Get recommended search keywords
- Wire: `GET /discovery/trending/search/keyword/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1832798361818114`, [official page](https://business-api.tiktok.com/portal/docs?id=1832798361818114)
- Contract SHA-256: `7b1912a7b62cba22088556317127d488e00a1e9dfaf798778b395ba1f6cc84d9`
- Required live inputs from request contract: `business_id`, `query`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `query` | `query` | `string` | `required` | length: 255 characters; rule: Length limit: 255 characters |
| `is_personalized` | `query` | `boolean` | `optional` | default: false |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.search_keywords` | `string[]` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_FILE_NAME_CHECK`

- Operation: Check the names of files
- Wire: `GET /file/name/check/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1759130033155073`, [official page](https://business-api.tiktok.com/portal/docs?id=1759130033155073)
- Contract SHA-256: `8cf8524f4c20e352dbe63042984da72f9d6a2b47d3faca25f47e3ac10427f725`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `files` | `query` | `object[]` | `conditional` | size: 20; rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |
| `files[].file_name` | `query` | `string` | `conditional` | condition: files is passed; rule: Required when files is passed |
| `files[].file_type` | `query` | `string` | `optional` | allowed: VIDEO, IMAGE; default: VIDEO |
| `file_name` | `query` | `string` | `conditional` | rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |
| `file_type` | `query` | `string` | `conditional` | allowed: VIDEO, IMAGE; default: VIDEO; rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.duplicate` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.duplicate_material_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.batch_results` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.batch_results[].file_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.batch_results[].duplicate` | `boolean` | `provider-unspecified; model permissively` | allowed: true, false |
| `data.batch_results[].duplicate_material_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_VIDEO_FIX_TASK_GET`

- Operation: Get the results of a Smart Fix task
- Wire: `GET /video/fix/task/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1741469487859714`, [official page](https://business-api.tiktok.com/portal/docs?id=1741469487859714)
- Contract SHA-256: `db0ece5e9ada2fb7dffa2ef2a12ac49b9852160ab2da0718f020ae2f4fdee2a8`
- Required live inputs from request contract: `advertiser_id`, `task_id`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `task_id` | `query` | `string` | `required` | - |
| `advertiser_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.status` | `string` | `provider-unspecified; model permissively` | allowed: PROCESSING, FAILED, SUCCESS |
| `data.error_msg` | `string` | `provider-unspecified; model permissively` | presence: present when the status is FAILED |
| `data.videos` | `object[]` | `provider-unspecified; model permissively` | size: 3; presence: present when the status is SUCCESS |
| `data.videos[].video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].video_url` | `string` | `provider-unspecified; model permissively` | rule: Valid only for 7 days |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 8: P8 Creative POST actions

Actions in this prompt: **5**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CREATIVE_ASSET_DELETE` -> `POST /creative/asset/delete/`
- `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_CREATE` -> `POST /creative/auto_message/create/`
- `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_CREATE` -> `POST /creative/pre_review/task/create/`
- `TIKTOK_ADS_SMART_PLUS_AD_PREVIEW` -> `POST /smart_plus/ad/preview/`
- `TIKTOK_ADS_VIDEO_FIX_TASK_CREATE` -> `POST /video/fix/task/create/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CREATIVE_ASSET_DELETE`

- Operation: Delete creative assets
- Wire: `POST /creative/asset/delete/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `destructive-or-status-changing`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1797202997456897`, [official page](https://business-api.tiktok.com/portal/docs?id=1797202997456897)
- Contract SHA-256: `0bd58a90ee28e07e62569743faa2a8525013424eae95c0171ead81ca7565619c`
- Required live inputs from request contract: `advertiser_id`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `video_ids` | `json_body` | `string[]` | `optional` | rule: At most 50 IDs can be included in the list; max items: 50 |
| `image_ids` | `json_body` | `string[]` | `optional` | rule: At most 50 IDs can be included in the list; max items: 50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.failed_video_ids` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.failed_image_ids` | `string[]` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_CREATE`

- Operation: Create a welcome message within an ad account
- Wire: `POST /creative/auto_message/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1822106113771521`, [official page](https://business-api.tiktok.com/portal/docs?id=1822106113771521)
- Contract SHA-256: `69793b0c21b4049a85a1a165528cfe9c8ba214224eb7b773acef344c1e605e54`
- Required live inputs from request contract: `advertiser_id`, `auto_message_type`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `auto_message_type` | `json_body` | `string` | `required` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `welcome_message` | `json_body` | `object` | `conditional` | condition: auto_message_type is WELCOME_MESSAGE; rule: Required when auto_message_type is WELCOME_MESSAGE |
| `welcome_message.title` | `json_body` | `string` | `conditional` | condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: You can specify a unique name to distinguish between different welcome messages within the welcome message library of your ad account |
| `welcome_message.content` | `json_body` | `string` | `conditional` | length: 200 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: The greeting within the welcome message; rule: Length limit: 200 characters |
| `welcome_message.suggested_questions` | `json_body` | `object[]` | `conditional` | size: 1-3; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Size range: 1-3 |
| `welcome_message.suggested_questions[].question` | `json_body` | `string` | `conditional` | length: 70 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Length limit: 70 characters |
| `welcome_message.suggested_questions[].answer` | `json_body` | `string` | `conditional` | length: 500 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Length limit: 500 characters |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_CREATE`

- Operation: Create a creative pre-review task
- Wire: `POST /creative/pre_review/task/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1874110632584577`, [official page](https://business-api.tiktok.com/portal/docs?id=1874110632584577)
- Contract SHA-256: `329b6d2fdb16acc3c146a1fdddba0294a5a57021d4debb19def06659a1a22723`
- Required live inputs from request contract: `advertiser_id`, `location_codes`, `material_list`, `material_list[].material_id`, `material_list[].material_type`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `material_list` | `json_body` | `object[]` | `required` | size: 1-5; rule: Size range: 1-5 |
| `material_list[].material_type` | `json_body` | `string` | `required` | allowed: VIDEO, IMAGE, AD_TEXT, LANDING_PAGE_URL |
| `material_list[].material_id` | `json_body` | `string` | `required` | rule: To search for video IDs within your ad account, use /file/video/ad/search/ and check the returned video_id; rule: To search for image IDs within your ad account, use /file/image/ad/search/ and check the returned image_id |
| `location_codes` | `json_body` | `string[]` | `required` | size: 1; allowed: AD, AE, AG, AI, AL, AO, AR, AT, AU, AW, AZ, BA, BB, BD, BE, BG, BH, BL, BM, BO, BQ, BR, BS, BY, BZ, CA, CD, CH, CL, CO, CR, CU, CV, CW, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, ER, ES, FI, FO, FR, GB, GD, GE, GF, GG, GI, GL, GN, GP, GQ, GR, GT, GW, HK, HN, HR, HT, HU, ID, IE, IL, IM, IN, IQ, IS, IT, JE, JM, JO, JP, KE, KH, KM, KN, KR, KW, KY, KZ, LB, LC, LI, LK, LT, LU, LV, LY, MA, MC, MD, ME, MF, MK, MM, MO, MQ, MR, MS, MT, MX, MY, MZ, NG, NI, NL, NO, NP, NZ, OM, PA, PE, PF, PH, PK, PL, PM, PR, PS, PT, PY, QA, RO, RS, RU, SA, SD, SE, SG, SI, SJ, SK, SM, SO, SS, ST, SV, SX, SY, TC, TD, TF, TH, TN, TR, TT, TW, UA, US, UY, UZ, VC, VE, VG, VI, VN, YE, ZA |
| `is_ecommerce` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.pre_review_task_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_SMART_PLUS_AD_PREVIEW`

- Operation: Preview Upgraded Smart+ Ads
- Wire: `POST /smart_plus/ad/preview/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1843317445798914`, [official page](https://business-api.tiktok.com/portal/docs?id=1843317445798914)
- Contract SHA-256: `a2e1f35b5c18fb30fef25b223d714209f509f2cbfb6ed9a48835615e28d7882f`
- Additional enum evidence: doc `1737174886619138`, [official page](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`
- Required live inputs from request contract: `advertiser_id`, `creative_list`, `creative_list[].creative_info`, `preview_type`, `smart_plus_ad_id`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

Variant: `Preview ads that you plan to create`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `preview_type` | `json_body` | `string` | `required` | allowed: ADS_CREATION |
| `catalog_enabled` | `json_body` | `boolean` | `optional` | allowed: true, false |
| `catalog_id` | `json_body` | `string` | `conditional` | condition: catalog_enabled is true; rule: Required when catalog_enabled is true; rule: To retrieve the catalogs within your Business Center, use /catalog/get/ |
| `catalog_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: catalog_enabled is true; rule: Required when catalog_enabled is true |
| `creative_list` | `json_body` | `object[]` | `required` | size: 1- 31; rule: Size range: 1- 31 |
| `creative_list[].creative_info` | `json_body` | `object` | `required` | - |
| `creative_list[].creative_info.video_info` | `json_body` | `object` | `conditional` | any-of: Non-Spark Ads Single Video ads. || Spark Ads Single Video ads through Spark Ads Push.; rule: Required for the following types of ads: Non-Spark Ads Single Video ads |
| `creative_list[].creative_info.video_info.video_id` | `json_body` | `string` | `conditional` | condition: video_info is specified; rule: Required when video_info is specified; rule: To search for videos within your ad account, use /file/video/ad/search/ |
| `creative_list[].creative_info.image_info` | `json_body` | `object[]` | `conditional` | any-of: Non-Spark Ads Single Video ads. You need to specify a video cover. || Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. || Non-Spark Ads Standard Carousel ads. You need to spec; rule: Required for the following types of ads: Non-Spark Ads Single Video ads; rule: Not supported for Catalog Carousel ads |
| `creative_list[].creative_info.image_info[].web_uri` | `json_body` | `string` | `conditional` | condition: image_info is specified; rule: Required when image_info is specified; rule: To search for images within your ad account, use /file/image/ad/search/ |
| `creative_list[].creative_info.music_info` | `json_body` | `object` | `conditional` | any-of: When you create Standard Carousel Ads, including:Non-Spark Ads Standard Carousel adsSpark Ads Standard Carousel ads through Spark Ads PushSpark Ads Standard Carousel ads through Sp || When objective_type is WEB_C; rule: Required for the following scenarios: When you create Standard Carousel Ads, including: Non-Spark Ads Standard Carousel ads |
| `creative_list[].creative_info.music_info.music_id` | `json_body` | `string` | `conditional` | condition: music_info is specified; rule: Required when music_info is specified |
| `creative_list[].creative_info.tiktok_item_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; any-of: Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. || Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post.; rule: Required when you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; rule: Not supported when catalog_creative_toggle is true |
| `creative_list[].creative_info.identity_type` | `json_body` | `string` | `conditional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT; condition: you create Spark Ads without using catalog creatives; all-of: At the campaign level, objective_type is APP_PROMOTION or WEB_CONVERSIONS. || At the ad group level, placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK, or placement_type is PLACEMEN; rule: Required when you create Spark Ads without using catalog creatives; rule: Note : If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the identity_type and identity_id within ad_configuration |
| `creative_list[].creative_info.identity_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads without using catalog creatives; rule: Required when you create Spark Ads without using catalog creatives; rule: Note : If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the identity_type and identity_id within ad_configuration |
| `creative_list[].creative_info.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type within creative_info is BC_AUTH_TT; rule: Required when identity_type within creative_info is BC_AUTH_TT |
| `ad_text_list` | `json_body` | `object[]` | `conditional` | size: 5; condition: tiktok_item_id is not specified; rule: Required when tiktok_item_id is not specified |
| `ad_text_list[].ad_text` | `json_body` | `string` | `conditional` | condition: ad_text_list is specified; rule: Required when ad_text_list is specified |
| `call_to_action_list` | `json_body` | `object[]` | `optional` | size: 3; rule: Note : This field is not supported for Upgraded Smart+ Lead Generation Campaigns; rule: call_to_action_list and call_to_action_id cannot be set at the same time |
| `call_to_action_list[].call_to_action` | `json_body` | `string` | `conditional` | condition: call_to_action_list is specified; rule: Required when call_to_action_list is specified; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `ad_configuration` | `json_body` | `object` | `optional` | - |
| `ad_configuration.identity_type` | `json_body` | `string` | `conditional` | allowed: CUSTOMIZED_USER, TT_USER, BC_AUTH_TT; any-of: You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. || You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more; rule: Required in any of the following scenarios: You are creating non-Spark Ads on non-TikTok placements |
| `ad_configuration.identity_id` | `json_body` | `string` | `conditional` | any-of: You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. || You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more; rule: Required in any of the following scenarios: You are creating non-Spark Ads on non-TikTok placements |
| `ad_configuration.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type within ad_configuration is BC_AUTH_TT; rule: Required when identity_type within ad_configuration is BC_AUTH_TT |
| `ad_configuration.product_specific_type` | `json_body` | `string` | `conditional` | allowed: ALL, PRODUCT_SET, CUSTOMIZED_PRODUCTS; condition: catalog_enabled is true at the campaign level; any-of: ALL: Allow TikTok to dynamically choose from all products. || PRODUCT_SET: Specify a product set. TikTok will dynamically choose products from this set. || CUSTOMIZED_PRODUCTS: Specify a customized number of prod; rule: Required when catalog_enabled is true at the campaign level; rule: If this field is set to CUSTOMIZED_PRODUCTS, product_ids is required |
| `ad_configuration.product_set_id` | `json_body` | `string` | `conditional` | condition: product_specific_type is PRODUCT_SET; any-of: To retrieve the product sets within your ad account, use /catalog/set/get/. || To create a product set, use /catalog/set/create/.; rule: Required when product_specific_type is PRODUCT_SET |
| `ad_configuration.product_ids` | `json_body` | `string[]` | `conditional` | size: 20; condition: product_specific_type is CUSTOMIZED_PRODUCTS; rule: Required when product_specific_type is CUSTOMIZED_PRODUCTS |
| `ad_configuration.catalog_creative_toggle` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false; cross-field: Valid only when catalog_enabled is true.; ; Whether to enable auto-selection of creatives from your catalog.; ; Supported values: true, false.; Default value: false.; ; If you set  |
| `ad_configuration.catalog_creative_info` | `json_body` | `object` | `optional` | any-of: The ad is an Upgraded Smart+ E-commerce Catalog Ad or Upgraded Smart+ Streaming Ad. || catalog_creative_toggle is true.; rule: Valid only when the following conditions are met: The ad is an Upgraded Smart+ E-commerce Catalog Ad or Upgraded Smart+ Streaming Ad |
| `ad_configuration.catalog_creative_info.catalog_media_settings` | `json_body` | `string[]` | `optional` | rule: If you include this value in catalog_media_settings, you can optionally specify catalog_template_video_id at the same time; rule: If you include this value in catalog_media_settings, you cannot specify catalog_template_video_id at the same time; rule: Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library |
| `ad_configuration.catalog_creative_info.catalog_template_video_id` | `json_body` | `string` | `optional` | any-of: The ad is an Upgraded Smart+ Streaming Ad. || TEMPLATE_VIDEO is included in catalog_media_settings.; rule: Valid only when the following conditions are met: The ad is an Upgraded Smart+ Streaming Ad |
| `ad_configuration.call_to_action_id` | `json_body` | `string` | `optional` | rule: Note : call_to_action_list and call_to_action_id cannot be set at the same time |

Variant: `Preview existing ads`

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `preview_type` | `json_body` | `string` | `required` | allowed: AD |
| `smart_plus_ad_id` | `json_body` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.preview_link` | `string` | `provider-unspecified; model permissively` | - |
| `data.iframe` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_VIDEO_FIX_TASK_CREATE`

- Operation: Create a Smart Fix task
- Wire: `POST /video/fix/task/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `6`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Creative Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1741468875279361`, [official page](https://business-api.tiktok.com/portal/docs?id=1741468875279361)
- Contract SHA-256: `b7189d9b691d363e2d02f9b396d592fc899ad1aefc90976994a6fce15c39819d`
- Required live inputs from request contract: `advertiser_id`, `tasks[].video_id`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `tasks` | `json_body` | `object[]` | `optional` | size: 10 |
| `tasks[].video_id` | `json_body` | `string` | `required` | - |
| `tasks[].auto_bind_enabled` | `json_body` | `boolean` | `optional` | default: False |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.tasks` | `object[]` | `provider-unspecified; model permissively` | size: 10 |
| `data.tasks[].video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.tasks[].fix_task_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.tasks[].flaw_types` | `string[]` | `provider-unspecified; model permissively` | allowed: LOW_RESOLUTION, ILLEGAL_VIDEO_SIZE, NO_BGM, BLACK_EDGE |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 9: P9 Reporting and Catalog GET actions

Actions in this prompt: **7**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CATALOG_INSIGHT_PRODUCT_GET` -> `GET /catalog/insight/product/get/`
- `TIKTOK_ADS_CATALOG_VIDEO_GET` -> `GET /catalog/video/get/`
- `TIKTOK_ADS_CREATIVE_FATIGUE_GET` -> `GET /creative_fatigue/get/`
- `TIKTOK_ADS_DIAGNOSTIC_CATALOG` -> `GET /diagnostic/catalog/`
- `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_GET` -> `GET /diagnostic/catalog/product/task/get/`
- `TIKTOK_ADS_REPORT_AD_BENCHMARK_GET` -> `GET /report/ad_benchmark/get/`
- `TIKTOK_ADS_REPORT_VIDEO_PERFORMANCE_GET` -> `GET /report/video_performance/get/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CATALOG_INSIGHT_PRODUCT_GET`

- Operation: Get trending catalog products
- Wire: `GET /catalog/insight/product/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1805640886872066`, [official page](https://business-api.tiktok.com/portal/docs?id=1805640886872066)
- Contract SHA-256: `8d997a4bf89661ceb30c794a08020d416827c69e0399669f18f79972d20f784e`
- Required live inputs from request contract: `bc_id`, `catalog_id`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `catalog_id` | `query` | `string` | `required` | rule: The catalog needs to be an E-commerce catalog that contains at least 20 products; rule: To verify that the catalog contains at least 20 products, use /catalog/overview/ and check whether the sum of the values of the returned approved, rejected, and processing fields is equal to or greate |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.category_ids` | `query` | `string[]` | `conditional` | size: 50; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |
| `filtering.brands` | `query` | `string[]` | `conditional` | size: 50; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |
| `filtering.availabilities` | `query` | `string[]` | `conditional` | allowed: IN_STOCK, AVAILABLE_FOR_ORDER, PREORDER, OUT_OF_STOCK, DISCONTINUED; rule: When filtering is specified, you need to provide at least one of category_ids, brands, and availabilities |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.product_insights` | `object[]` | `provider-unspecified; model permissively` | rule: The list of up to 50 trending products within the E-commerce catalog, sorted in descending order by popularity |
| `data.product_insights[].product_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].image_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].title` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].description` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].sku_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.category_id` | `string` | `provider-unspecified; model permissively` | rule: The TikTok product category ID assigned to the product, consisting of three levels separated by the number sign (#), in the format of "level_id_1#level_id_2#level_id_3" |
| `data.product_insights[].category_info.level_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_id_1` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_name_1` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_id_2` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_name_2` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_id_3` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].category_info.level_info.level_name_3` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].brand` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].price` | `object` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].price.price` | `float` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].price.currency` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].price.sale_price` | `float` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].price.sale_price_effective_date` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.product_insights[].availability` | `string` | `provider-unspecified; model permissively` | allowed: IN_STOCK, AVAILABLE_FOR_ORDER, PREORDER, OUT_OF_STOCK, DISCONTINUED |

### `TIKTOK_ADS_CATALOG_VIDEO_GET`

- Operation: Get the uploaded catalog videos within a catalog
- Wire: `GET /catalog/video/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1803655082498050`, [official page](https://business-api.tiktok.com/portal/docs?id=1803655082498050)
- Contract SHA-256: `181c80df54aa42247a05dd7a9c44760421e304353af40355f7ae98e59148e9e7`
- Required live inputs from request contract: `bc_id`, `catalog_id`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `catalog_id` | `query` | `string` | `required` | - |
| `catalog_video_ids` | `query` | `string[]` | `optional` | size: 50 |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: 1-50; rule: Value range: 1-50 |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.videos` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.videos[].catalog_video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].video_name` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].video_link` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].sku_id_list` | `string[]` | `provider-unspecified; model permissively` | - |
| `data.videos[].category` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].brand` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].creator` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].video_type` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].description` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].landing_page_url` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].custom_label_0` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].custom_label_1` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].custom_label_2` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].custom_label_3` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].custom_label_4` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].video_id` | `string` | `provider-unspecified; model permissively` | rule: The video ID generated after the video extraction is complete |
| `data.videos[].video_signature` | `string` | `provider-unspecified; model permissively` | - |
| `data.videos[].status` | `string` | `provider-unspecified; model permissively` | allowed: PENDING, SUCCESS, FAILED |
| `data.videos[].create_time` | `string` | `provider-unspecified; model permissively` | rule: The time when the video upload was completed, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.videos[].active_status` | `string` | `provider-unspecified; model permissively` | allowed: ACTIVATED, DEACTIVATED; rule: DEACTIVATED: The video is deactivated and cannot be used for ad delivery |
| `data.videos[].preview_url` | `string` | `provider-unspecified; model permissively` | presence: present when status is SUCCESS; rule: The video preview link, which is valid for six hours and needs to be re-acquired after expiration |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `integer` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `integer` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CREATIVE_FATIGUE_GET`

- Operation: Get Creative Fatigue Detection results
- Wire: `GET /creative_fatigue/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `4`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Reporting` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1767568466842626`, [official page](https://business-api.tiktok.com/portal/docs?id=1767568466842626)
- Contract SHA-256: `6117eb0c814fc85b57770a4508d8f82d508f335ab64f8e43a02b65bbdc7b4672`
- Provider gate: `CREATIVE_FATIGUE` allowlist
- Required live inputs from request contract: `ad_id`, `advertiser_id`, `filtering`, `filtering.end_date`, `filtering.start_date`
- Product/fixture gate: Creative Fatigue allowlist and delivered-ad history
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `ad_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `required` | - |
| `filtering.start_date` | `query` | `string` | `required` | rule: Query start date (closed interval), in the format of YYYY-MM-DD (advertiser account time zone); rule: You can only specify a date within the last 60 days |
| `filtering.end_date` | `query` | `string` | `required` | rule: Query end date (open interval), in the format of YYYY-MM-DD (advertiser account time zone); rule: You can only specify a date within the last 60 days |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: [1, 500]; rule: Value range: [1, 500] |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.list[].adgroup_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].ad_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].date` | `string` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics` | `object` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics.has_fatigue` | `boolean` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics.fatigue_index` | `number` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics.dnu` | `number` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics.dnu_ratio` | `number` | `provider-unspecified; model permissively` | rule: This metric is calculated by dividing the number of daily new users attracted by the ad on a specific date by the maximum number of daily new users that the ad attracted in the last 60 days |
| `data.list[].metrics.spend` | `number` | `provider-unspecified; model permissively` | - |
| `data.list[].metrics.cost_per_conversion` | `number` | `provider-unspecified; model permissively` | rule: This metric returns actual value when the ad is within a non-iOS 14 Dedicated Campaign, and returns 0; rule: 0 when the ad is within an iOS 14 Dedicated Campaign |
| `data.list[].metrics.skan_cost_per_conversion` | `number` | `provider-unspecified; model permissively` | rule: This metric returns actual value when the ad is within an iOS 14 Dedicated Campaign, and returns 0; rule: 0 when the ad is within a non-iOS 14 Dedicated Campaign |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DIAGNOSTIC_CATALOG`

- Operation: Get synchronous catalog product diagnostic information
- Wire: `GET /diagnostic/catalog/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1771117232728066`, [official page](https://business-api.tiktok.com/portal/docs?id=1771117232728066)
- Contract SHA-256: `fba7db5edd98934e15bf79dfbde0b1370b854ea5b5ec62f0f679f53f93e2d50c`
- Required live inputs from request contract: `bc_id`, `catalog_id`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `catalog_id` | `query` | `string` | `required` | - |
| `bc_id` | `query` | `string` | `required` | - |
| `feed_id` | `query` | `string` | `optional` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.issue_level` | `query` | `string` | `optional` | allowed: CRITICAL, WARNING |
| `filtering.issue_category` | `query` | `string` | `optional` | allowed: PRODUCT_ATTRIBUTES, PRODUCT_REVIEW, CATALOG, PIXEL_OR_EVENT, FILE_UPLOAD_OR_FEED |
| `lang` | `query` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `page` | `query` | `integer` | `optional` | default: 1; range: ≥1; rule: Value range: ≥1 |
| `page_size` | `query` | `integer` | `optional` | default: 10; range: [1, 20]; rule: Value range: [1, 20] |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.diagnostic_date` | `string` | `provider-unspecified; model permissively` | rule: The date (UTC +0 Time) when the diagnostic information was generated, in the format of "YYYY-MM-DD" |
| `data.issues` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.issues[].issue_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.issues[].issue_title` | `string` | `provider-unspecified; model permissively` | - |
| `data.issues[].reason_and_suggestion` | `string` | `provider-unspecified; model permissively` | - |
| `data.issues[].issue_level` | `string` | `provider-unspecified; model permissively` | allowed: CRITICAL, WARNING |
| `data.issues[].issue_category` | `string` | `provider-unspecified; model permissively` | allowed: PRODUCT_ATTRIBUTES, PRODUCT_REVIEW, CATALOG, PIXEL_OR_EVENT, FILE_UPLOAD_OR_FEED |
| `data.issues[].issue_product_field` | `string` | `provider-unspecified; model permissively` | - |
| `data.issues[].affected_product_count` | `integer` | `provider-unspecified; model permissively` | - |
| `data.issues[].affected_product_percentage` | `number` | `provider-unspecified; model permissively` | range: [0,100]; rule: Value range: [0,100] |
| `data.issues[].example_affected_products` | `object[]` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_GET`

- Operation: Download asynchronous catalog product diagnostic information
- Wire: `GET /diagnostic/catalog/product/task/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1771117294731266`, [official page](https://business-api.tiktok.com/portal/docs?id=1771117294731266)
- Contract SHA-256: `f24df2e0e8cb2a7c0570010cb7eb5d1cc377dd52ab923e29c7c44a59e9101622`
- Required live inputs from request contract: `bc_id`, `catalog_id`, `task_id`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `catalog_id` | `query` | `string` | `required` | - |
| `bc_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.status` | `string` | `provider-unspecified; model permissively` | allowed: SUCCEED, PROCESSING, FAILED |
| `data.diagnostic_file_url` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_REPORT_AD_BENCHMARK_GET`

- Operation: Get ad benchmarks
- Wire: `GET /report/ad_benchmark/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `4`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Reporting` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1738824501176321`, [official page](https://business-api.tiktok.com/portal/docs?id=1738824501176321)
- Contract SHA-256: `fb0cdb7cde507263ec2c08973f297e9632a75f48deeed608376a8c2c97c4115f`
- Warning: Provider contradiction: the response table types data.list as object, while the success example is an array. Model list defensively as a collection and metrics as dynamic string-to-number keys; add regression tests for the documented table and example shapes.
- Required live inputs from request contract: `advertiser_id`, `dimensions`, `filtering`
- Product/fixture gate: Advertiser with non-empty delivered-campaign reporting data
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
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


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.compare_date` | `string` | `provider-unspecified; model permissively` | - |
| `data.list` | `object` | `provider-unspecified; model permissively` | rule: Note : If an ad accumulates fewer than 1,000 impressions within the comparison window (compare_time_window), the benchmark metric data will be empty |
| `data.list.info` | `object` | `provider-unspecified; model permissively` | - |
| `data.list.info.ad_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.info.location` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.info.placement` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.info.ad_category` | `number` | `provider-unspecified; model permissively` | - |
| `data.list.info.external_action` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.metrics` | `object` | `provider-unspecified; model permissively` | - |
| `data.list.metrics.metric_name` | `number` | `provider-unspecified; model permissively` | rule: After the metric name, you can see a number with one decimal place, in the value range of [0 |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_REPORT_VIDEO_PERFORMANCE_GET`

- Operation: Get in-second performance
- Wire: `GET /report/video_performance/get/` on the existing v1.3 base URL
- Request encoding: `query string`
- Ability hint: `reads`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `4`
- Permission evidence: `direct_permission_table_mapping`
- Provider-selected category: `Reporting` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1738825259075586`, [official page](https://business-api.tiktok.com/portal/docs?id=1738825259075586)
- Contract SHA-256: `69b9e6a3040ca5480e586ea2cf04e90846b9de5be21ff6162240cc2cedc632f3`
- Warning: Provider enum is documented as sort_type ASC or DES, not DESC. Preserve DES unless live evidence proves a typo. The response table types data.list as object while the example is an array; model it defensively as a collection and metrics as dynamic string-to-list[number] keys.
- Required live inputs from request contract: `advertiser_id`, `filtering`
- Product/fixture gate: Advertiser with non-empty delivered-campaign reporting data
- Live boundary: Read-only call permitted after fixture discovery

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
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


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.list` | `object` | `provider-unspecified; model permissively` | - |
| `data.list.info` | `object` | `provider-unspecified; model permissively` | - |
| `data.list.info.ad_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.info.video_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.list.info.duration` | `number` | `provider-unspecified; model permissively` | - |
| `data.list.metrics` | `object` | `provider-unspecified; model permissively` | - |
| `data.list.metrics.metric_name` | `number[]` | `provider-unspecified; model permissively` | - |
| `data.page_info` | `object` | `provider-unspecified; model permissively` | - |
| `data.page_info.page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_page` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.page_size` | `number` | `provider-unspecified; model permissively` | - |
| `data.page_info.total_number` | `number` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Prompt 10: P10 Catalog POST actions

Actions in this prompt: **3**

````text
Yang, continue the TikTok Ads toolkit from the exact pinned state below. This prompt is self-contained because the TikTok documentation portal may be inaccessible in your environment.

Required starting SHA for this batch: <PREVIOUS_ACCEPTED_BATCH_SHA>. Replace this placeholder with the final SHA from the preceding accepted batch before sending the prompt.

Repository: ComposioHQ/mercury
PR: #26271
Starting SHA: supplied at the top of this prompt
Toolkit: apps/tiktok_ads
Base URL: https://business-api.tiktok.com/open_api/v1.3

Before editing, verify PR head still equals the supplied starting SHA. If it moved, inspect the delta and report conflicts instead of overwriting newer work.

Implementation rules:
1. Implement only the actions in this prompt. Do not add any of the 53 blocked paths.
2. Use declarative Python actions and the existing tiktok_ads utilities, provider envelope handling, error map, JSON-query encoder, and grant_requirements style.
3. Use the embedded contract manifest as the field-level provider evidence. The links and document hashes are provenance. Do not invent fields, enums, defaults, limits, nullability, replacements, or endpoint behavior. If the provider table and example conflict, use a defensive permissive shape, add a contradiction test/note, or stop that action.
4. Inject Access-Token through auth. Never expose access tokens, app secrets, or client secrets as normal tool inputs.
5. Follow the per-field placement in the embedded manifest. GET list/object query values use the existing JSON-query encoder. POST actions may be JSON or multipart; `/bc/oa/create/` and `/catalog/set/upload/` are multipart/form-data and must not use JSON. Add an exact serialization test for every action.
6. Request requiredness follows the manifest. For responses, provider nullability is not guaranteed. Model documented fields permissively unless current live evidence proves a field is always present.
7. Choose ability from the operation's semantic effect, not the HTTP verb. A POST preview/get/report task may still be a read. Deletes, disables, assignments, and persistent creates need the corresponding destructive/create/update hint.
8. Add focused tests for request schema, exact wire placement, conditional validation, constraints, response shaping, empty data, nested data, provider-envelope errors, wildcard HTTP errors, and documented pagination defaults/bounds. Never invent a page-size default above 10.
9. Do not live-call destructive, file-upload, developer-secret, irreversible, or spend-affecting operations in this batch. Other writes require a disposable fixture, read-back assertion, and exact cleanup; otherwise mark them fixture-blocked, not passed.
10. Keep each action's source= citation on its exact official doc URL. For `direct_permission_table_mapping`, the permission page names the path. For `selected_export_category_plus_first_level_inheritance`, the evidence chain is the provider-supplied selected-endpoint category export plus TikTok's official first-level inheritance rule. Do not claim the permission table directly names those paths.
11. Update the selected endpoint ledger for these actions. Do not claim live verification from unit tests.
12. Run the focused tiktok_ads tests, app checks, compile checks, Ruff, and mypy for the changed diff. Commit and push only this batch. Do not merge.

Required actions in this batch:

- `TIKTOK_ADS_CATALOG_SET_UPLOAD` -> `POST /catalog/set/upload/`
- `TIKTOK_ADS_CATALOG_VIDEO_FILE` -> `POST /catalog/video/file/`
- `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_CREATE` -> `POST /diagnostic/catalog/product/task/create/`

Embedded provider contract manifest:

### `TIKTOK_ADS_CATALOG_SET_UPLOAD`

- Operation: Create a product set by file
- Wire: `POST /catalog/set/upload/` on the existing v1.3 base URL
- Request encoding: `multipart/form-data`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1846770644217858`, [official page](https://business-api.tiktok.com/portal/docs?id=1846770644217858)
- Contract SHA-256: `44256152228005bc37ef2d50e1b041953edde9575866321a3b5c6127153bbcd9`
- Required live inputs from request contract: `bc_id`, `catalog_id`, `file`, `file_signature`, `product_set_name`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `multipart_form` | `string` | `required` | - |
| `catalog_id` | `multipart_form` | `string` | `required` | rule: To retrieve the list of E-commerce catalogs within a Business Center, use /catalog/get/ |
| `product_set_name` | `multipart_form` | `string` | `required` | length: 28 characters; rule: Length limit: 28 characters; rule: Note : Duplicate product set names are not supported |
| `file` | `multipart_form` | `file` | `required` | max rows: 5,000; file format: .csv only; rule: Recommended settings： Maximum row count: 5,000 |
| `file_signature` | `multipart_form` | `string` | `required` | meaning: MD5 hash of the uploaded file for integrity verification |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.product_set_id` | `string` | `provider-unspecified; model permissively` | - |
| `data.product_set_name` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_CATALOG_VIDEO_FILE`

- Operation: Upload catalog videos via a file URL
- Wire: `POST /catalog/video/file/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1803655037415489`, [official page](https://business-api.tiktok.com/portal/docs?id=1803655037415489)
- Contract SHA-256: `56f110b548398f7257469a4e67eb172d068c9d5c6107f53278bc13af79740227`
- Required live inputs from request contract: `bc_id`, `catalog_id`, `file_url`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `catalog_id` | `json_body` | `string` | `required` | - |
| `file_url` | `json_body` | `string` | `required` | - |
| `advertiser_ids` | `json_body` | `string[]` | `optional` | size: 100; rule: The ad account and the catalog (catalog_id) must be within the same Business Center (bc_id) and you need to have Admin or Operator permission for the ad account |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.feed_log_id` | `string` | `provider-unspecified; model permissively` | - |

### `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_CREATE`

- Operation: Create an asynchronous download task for catalog product diagnostic information
- Wire: `POST /diagnostic/catalog/product/task/create/` on the existing v1.3 base URL
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`. Verify semantic side effects before finalizing `ability=`.
- Grant: first-level parent scope `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Provider-selected category: `DPA Catalog Management` for app `REDACTED_SELECTED_APP_ID`
- Provider evidence: doc `1771117279175682`, [official page](https://business-api.tiktok.com/portal/docs?id=1771117279175682)
- Contract SHA-256: `e607f404d890626f71027c07f1289b6a15c3ee5c7df8693c65938477b2e74c90`
- Required live inputs from request contract: `bc_id`, `catalog_id`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

Request fields:

| Wire path | Placement | Type | Requiredness | Documented constraints |
|---|---|---|---|---|
| `catalog_id` | `json_body` | `string` | `required` | - |
| `bc_id` | `json_body` | `string` | `required` | - |
| `feed_id` | `json_body` | `string` | `optional` | - |
| `lang` | `json_body` | `string` | `optional` | default: en; allowed: ar, cs-CZ, de, en, es, fil, fr, id, it, ja, ko, ms, pl-PL, pt, ru, sv-SE, th, tr, vi, zh |
| `issue_id` | `json_body` | `string` | `optional` | - |


Response fields:

| Response path | Type | Requiredness policy | Documented constraints |
|---|---|---|---|
| `code` | `number` | `provider-unspecified; model permissively` | - |
| `message` | `string` | `provider-unspecified; model permissively` | - |
| `request_id` | `string` | `provider-unspecified; model permissively` | - |
| `data` | `object` | `provider-unspecified; model permissively` | - |
| `data.task_id` | `string` | `provider-unspecified; model permissively` | - |

Delivery report required from Yang:
- Starting SHA and final SHA
- Action files and tests added
- Exact commands and counts
- Any manifest contradiction or provider-doc defect
- Live-tested, fixture-blocked, provider-gated, and not-run actions listed separately
- Confirmation that no other endpoint family was changed
````

## Stop list

Do not ask Yang to implement the remaining 53 selected paths from this evidence pack. They are absent, deprecated, permission-only, unsafe, contradictory, have a provider-doc defect, or belong in auth/connection design. The three `/subscription/*` replacements require the developer secret and an allowlist.

- [Gated-doc Markdown audit](../evidence/gated-doc-audit.md)
- [Structured contract manifest](../manifest/contracts.json)
