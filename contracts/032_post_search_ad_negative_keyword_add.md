# TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_ADD

- Operation: Create negative keywords
- Wire: `POST /search_ad/negative_keyword/add/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1775104895291393](https://business-api.tiktok.com/portal/docs?id=1775104895291393)
- Source content SHA-256: `c2676d4825e315a97398d6ad00e1c14ada161436e9cd7c755c7a639064b519a1`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `object_type` | `json_body` | `string` | `required` | allowed: CAMPAIGN, ADGROUP |
| `object_ids` | `json_body` | `string[]` | `required` | size: 50 |
| `replace` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |
| `keywords` | `json_body` | `object[]` | `required` | size: 1,000; rule: Note : For each ad group, you can configure a maximum of 10,000 negative keywords |
| `keywords[].name` | `json_body` | `string` | `required` | length: 80 characters; rule: Length limit: 80 characters |
| `keywords[].match_type` | `json_body` | `string` | `optional` | allowed: PRECISE_WORD, PHRASE_WORD, BROAD_WORD; default: BROAD_WORD |

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
