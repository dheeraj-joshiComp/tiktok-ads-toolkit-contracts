# TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_GET

- Operation: Get negative keywords
- Wire: `GET /search_ad/negative_keyword/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1775104887052289](https://business-api.tiktok.com/portal/docs?id=1775104887052289)
- Source content SHA-256: `cb6c5ab08776ac8d0e6f1a3471c2f26408bf11dc1745e6a42f74a30867155d86`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `object_type` | `query` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_id` | `query` | `string` | `required` | - |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: [1,50]; rule: Value range: [1,50] |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.keywords` | `object[]` | size: 1,000 |
| `data.keywords[].keyword_id` | `string` | - |
| `data.keywords[].name` | `string` | - |
| `data.keywords[].match_type` | `string` | allowed: PRECISE_WORD, PHRASE_WORD, BROAD_WORD |
| `data.page_info` | `object` | - |
| `data.page_info.page` | `number` | - |
| `data.page_info.page_size` | `number` | - |
| `data.page_info.total_number` | `number` | - |
| `data.page_info.total_page` | `number` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
