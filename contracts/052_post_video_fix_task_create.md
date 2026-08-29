# TIKTOK_ADS_VIDEO_FIX_TASK_CREATE

- Operation: Create a Smart Fix task
- Wire: `POST /video/fix/task/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `6`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Creative Management`
- Source: [doc 1741468875279361](https://business-api.tiktok.com/portal/docs?id=1741468875279361)
- Source content SHA-256: `b7189d9b691d363e2d02f9b396d592fc899ad1aefc90976994a6fce15c39819d`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `tasks` | `json_body` | `object[]` | `optional` | size: 10 |
| `tasks[].video_id` | `json_body` | `string` | `required` | - |
| `tasks[].auto_bind_enabled` | `json_body` | `boolean` | `optional` | default: False |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.tasks` | `object[]` | size: 10 |
| `data.tasks[].video_id` | `string` | - |
| `data.tasks[].fix_task_id` | `string` | - |
| `data.tasks[].flaw_types` | `string[]` | allowed: LOW_RESOLUTION, ILLEGAL_VIDEO_SIZE, NO_BGM, BLACK_EDGE |
| `request_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
