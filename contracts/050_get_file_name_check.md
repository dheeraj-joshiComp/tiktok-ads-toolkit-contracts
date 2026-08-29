# TIKTOK_ADS_FILE_NAME_CHECK

- Operation: Check the names of files
- Wire: `GET /file/name/check/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1759130033155073](https://business-api.tiktok.com/portal/docs?id=1759130033155073)
- Source content SHA-256: `8cf8524f4c20e352dbe63042984da72f9d6a2b47d3faca25f47e3ac10427f725`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `query` | `string` | `required` | - |
| `files` | `query` | `object[]` | `conditional` | size: 20; rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |
| `files[].file_name` | `query` | `string` | `conditional` | condition: files is passed; rule: Required when files is passed |
| `files[].file_type` | `query` | `string` | `optional` | allowed: VIDEO, IMAGE; default: VIDEO |
| `file_name` | `query` | `string` | `conditional` | rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |
| `file_type` | `query` | `string` | `conditional` | allowed: VIDEO, IMAGE; default: VIDEO; rule: If you want to check whether a single file name has been used as video or image name, file_name and file_type are required; rule: If you want to check whether multiple file names have been used as video or image names, files is required |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.duplicate` | `boolean` | allowed: true, false |
| `data.duplicate_material_id` | `string` | - |
| `data.batch_results` | `object[]` | - |
| `data.batch_results[].file_name` | `string` | - |
| `data.batch_results[].duplicate` | `boolean` | allowed: true, false |
| `data.batch_results[].duplicate_material_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
