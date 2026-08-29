# TIKTOK_ADS_DISCOVERY_CML_VIDEO_LIST

- Operation: Get trending videos related to tracks
- Wire: `GET /discovery/cml/video_list/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1825119068941314](https://business-api.tiktok.com/portal/docs?id=1825119068941314)
- Source content SHA-256: `23d62c742a1f6621e05c6dc9561503e6e565765d8b179727a258b812d29a0d45`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `commercial_music_id` | `query` | `string` | `required` | - |
| `country_code` | `query` | `string` | `optional` | default: US |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.commercial_music_id` | `string` | - |
| `data.commercial_music_name` | `string` | - |
| `data.top_video_list` | `object[]` | - |
| `data.top_video_list[].video_id` | `string` | - |
| `data.top_video_list[].embed_url` | `string` | - |
| `data.top_video_list[].share_url` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
