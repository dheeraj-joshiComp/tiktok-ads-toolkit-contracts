# TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH

- Operation: Get trending search keywords
- Wire: `GET /discovery/trending/search/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1832798345014338](https://business-api.tiktok.com/portal/docs?id=1832798345014338)
- Source content SHA-256: `1372cc3165cff55d0688cf5dbd3587b78b35f261b325abb0e0eb8348ba71c199`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
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
