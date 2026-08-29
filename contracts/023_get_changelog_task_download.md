# TIKTOK_ADS_CHANGELOG_TASK_DOWNLOAD

- Operation: Get the downloaded file
- Wire: `GET /changelog/task/download/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `2`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ads Management`
- Source: [doc 1739924165710849](https://business-api.tiktok.com/portal/docs?id=1739924165710849)
- Source content SHA-256: `956a76be30cb405032c42d583c2d99dbeea9403ad84ef03e2080f475f08d6d0a`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `task_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.status` | `string` | allowed: PROCESSING, SUCCESS, FAILED |
| `data.changelog` | `string` | - |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
