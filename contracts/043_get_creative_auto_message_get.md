# TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_GET

- Operation: Get welcome messages within an ad account
- Wire: `GET /creative/auto_message/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1822106498804738](https://business-api.tiktok.com/portal/docs?id=1822106498804738)
- Source content SHA-256: `07038c4d2be4473295ad139d763c403bdfc1d2973599d0452795c9fb3c9ebcf2`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `auto_message_type` | `query` | `string` | `required` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `auto_message_id` | `query` | `string` | `optional` | - |
| `page` | `query` | `number` | `optional` | default: 1; range: ≥ 1; rule: Value range: ≥ 1 |
| `page_size` | `query` | `number` | `optional` | default: 10; range: 1-100; rule: Value range: 1-100 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | rule: The list of automatic messages within the ad account |
| `data.list[].auto_message_id` | `string` | - |
| `data.list[].auto_message_type` | `string` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `data.list[].welcome_message` | `string` | - |
| `data.list[].welcome_message.title` | `string` | rule: You can use the name to distinguish between different welcome messages within the welcome message library of your ad account |
| `data.list[].welcome_message.content` | `string` | rule: The greeting within the welcome message |
| `data.list[].welcome_message.suggested_questions` | `object[]` | - |
| `data.list[].welcome_message.suggested_questions[].question` | `string` | - |
| `data.list[].welcome_message.suggested_questions[].answer` | `string` | - |
| `data.list[].audit_status` | `string` | allowed: AUDITING, PASS, REJECTED |
| `data.list[].create_time` | `string` | rule: The time when the automatic message was created, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
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
