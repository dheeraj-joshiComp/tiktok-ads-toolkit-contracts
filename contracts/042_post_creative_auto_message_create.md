# TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_CREATE

- Operation: Create a welcome message within an ad account
- Wire: `POST /creative/auto_message/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1822106113771521](https://business-api.tiktok.com/portal/docs?id=1822106113771521)
- Source content SHA-256: `69793b0c21b4049a85a1a165528cfe9c8ba214224eb7b773acef344c1e605e54`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `auto_message_type` | `json_body` | `string` | `required` | allowed: WELCOME_MESSAGE; rule: A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad |
| `welcome_message` | `json_body` | `object` | `conditional` | condition: auto_message_type is WELCOME_MESSAGE; rule: Required when auto_message_type is WELCOME_MESSAGE |
| `welcome_message.title` | `json_body` | `string` | `conditional` | condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: You can specify a unique name to distinguish between different welcome messages within the welcome message library of your ad account |
| `welcome_message.content` | `json_body` | `string` | `conditional` | length: 200 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: The greeting within the welcome message; rule: Length limit: 200 characters |
| `welcome_message.suggested_questions` | `json_body` | `object[]` | `conditional` | size: 1-3; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Size range: 1-3 |
| `welcome_message.suggested_questions[].question` | `json_body` | `string` | `conditional` | length: 70 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Length limit: 70 characters |
| `welcome_message.suggested_questions[].answer` | `json_body` | `string` | `conditional` | length: 500 characters; condition: welcome_message is passed; rule: Required when welcome_message is passed; rule: Length limit: 500 characters |

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
