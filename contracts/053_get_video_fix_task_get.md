# TIKTOK_ADS_VIDEO_FIX_TASK_GET

- Operation: Get the results of a Smart Fix task
- Wire: `GET /video/fix/task/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Creative Management`
- Source: [doc 1741469487859714](https://business-api.tiktok.com/portal/docs?id=1741469487859714)
- Source content SHA-256: `db0ece5e9ada2fb7dffa2ef2a12ac49b9852160ab2da0718f020ae2f4fdee2a8`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `task_id` | `query` | `string` | `required` | - |
| `advertiser_id` | `query` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.status` | `string` | allowed: PROCESSING, FAILED, SUCCESS |
| `data.error_msg` | `string` | presence: present when the status is FAILED |
| `data.videos` | `object[]` | size: 3; presence: present when the status is SUCCESS |
| `data.videos[].video_id` | `string` | - |
| `data.videos[].video_url` | `string` | rule: Valid only for 7 days |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
