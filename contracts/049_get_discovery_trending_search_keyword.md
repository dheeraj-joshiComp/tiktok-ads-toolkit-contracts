# TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH_KEYWORD

- Operation: Get recommended search keywords
- Wire: `GET /discovery/trending/search/keyword/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1832798361818114](https://business-api.tiktok.com/portal/docs?id=1832798361818114)
- Source content SHA-256: `7b1912a7b62cba22088556317127d488e00a1e9dfaf798778b395ba1f6cc84d9`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `query` | `query` | `string` | `required` | length: 255 characters; rule: Length limit: 255 characters |
| `is_personalized` | `query` | `boolean` | `optional` | default: false |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.search_keywords` | `string[]` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
