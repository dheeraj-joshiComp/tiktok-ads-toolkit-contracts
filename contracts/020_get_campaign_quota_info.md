# TIKTOK_ADS_CAMPAIGN_QUOTA_INFO

- Operation: Get the quota for a SKAN Dedicated Campaign per ad network
- Wire: `GET /campaign/quota/info/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1752256376677378](https://business-api.tiktok.com/portal/docs?id=1752256376677378)
- Source content SHA-256: `1cd0ea930fb7ab3202ef283c684c53e3b973dbdb166efa49740b50dfd4a96032`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `app_id` | `query` | `string` | `required` | - |
| `campaign_id` | `query` | `string` | `optional` | - |
| `adgroup_id` | `query` | `string` | `optional` | rule: ID of an ad group within a SKAN 4; rule: Note : If the ID is not the ID of an ad group within a SKAN 4 |
| `has_advertiser_quota` | `query` | `boolean` | `optional` | default: false |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.split_test_quota` | `object` | - |
| `data.split_test_quota.max_test_number` | `number` | rule: Maximum test group number in one split-test |
| `data.split_test_quota.available_test_group` | `number` | - |
| `data.split_test_quota.used_test_group` | `number` | - |
| `data.split_test_quota.releasing_test_group` | `number` | - |
| `data.split_test_quota.used_quota` | `number` | - |
| `data.split_test_quota.releasing_quota` | `number` | - |
| `data.campaign_quota_info` | `object` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info` | `object` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info` | `object` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.total_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.used_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.releasing_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.available_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.used_campaign_ids` | `string[]` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.total_campaign_quota_info.releasing_campaign_ids` | `string[]` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv` | `object[]` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].used_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].releasing_campaign_quota` | `number` | - |
| `data.campaign_quota_info.tiktok_campaign_quota_info.campaign_quota_by_adv[].advertiser_id` | `string` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info` | `object` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info` | `object` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.total_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.used_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.releasing_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.available_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.used_campaign_ids` | `string[]` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.total_campaign_quota_info.releasing_campaign_ids` | `string[]` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv` | `object[]` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].used_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].releasing_campaign_quota` | `number` | - |
| `data.campaign_quota_info.pangle_campaign_quota_info.campaign_quota_by_adv[].advertiser_id` | `string` | - |
| `data.adgroup_quota_info` | `object` | - |
| `data.adgroup_quota_info.total_adgroup_quota` | `number` | - |
| `data.adgroup_quota_info.used_adgroup_quota` | `number` | - |
| `data.adgroup_quota_info.available_adgroup_quota` | `number` | - |
| `data.adgroup_quota_info.placements` | `string[]` | rule: You cannot create ad groups with placements that are not listed here |
| `data.adgroup_quota_info.campaign_id` | `string` | - |
| `data.ad_quota_info` | `object` | cross-field: when a SKAN 4.0 App ID (app_id) without specifying campaign_id and adgroup_id in the request, this field will represent the default ad quota for a regular SKAN 4; rule: Ad quota under an ad group within a SKAN 4; rule: Note : If the specified ad group (adgroup_id) is not within a SKAN 4 |
| `data.ad_quota_info.total_ad_quota` | `number` | rule: For ad groups within regular SKAN 4 |
| `data.ad_quota_info.used_ad_quota` | `number` | - |
| `data.ad_quota_info.available_ad_quota` | `number` | - |
| `data.ad_quota_info.adgroup_id` | `string` | - |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
