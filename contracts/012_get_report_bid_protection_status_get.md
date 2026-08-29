# TIKTOK_ADS_GET_BID_PROTECTION_STATUSES

- Operation: Get bid protection statuses
- Wire: `GET /report/bid_protection/status/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1874392512912449](https://business-api.tiktok.com/portal/docs?id=1874392512912449)
- Source content SHA-256: `ed5e55d9c8199fd5781e3b047ede949fda63237bb7c41d821c7e911ae0d5cc62`
- Product/fixture gate: Eligible campaign with bid-protection history
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `data_level` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `query_ids` | `query` | `string[]` | `required` | size: 200; rule: All IDs must belong to the same advertiser |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | - |
| `data.list[].data_level` | `string` | allowed: CAMPAIGN, ADGROUP |
| `data.list[].query_id` | `string` | - |
| `data.list[].bid_protection_status` | `string` | allowed: ACTIVE, INVALID, INACTIVE; rule: INVALID: Bid protection is temporarily ineligible for the campaign or ad group because the campaign or ad group was paused or deleted within the first 3 days after creation |
| `data.list[].compensation_category` | `string` | allowed: FULL_LIFE_CYCLE, THREE_DAY |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
