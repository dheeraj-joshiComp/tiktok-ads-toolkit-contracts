# TIKTOK_ADS_CREATE_BUSINESS_CENTER_ORGANIZATION_ACCOUNT

- Operation: Create an Organization Account in a Business Center
- Wire: `POST /bc/oa/create/`
- Request encoding: `multipart/form-data`
- Ability hint: `creates-or-starts-job`
- Parent scope: `1`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ad Account Management`
- Source: [doc 1855027199571138](https://business-api.tiktok.com/portal/docs?id=1855027199571138)
- Source content SHA-256: `389a68abe879bb1eff17310de35eab0f38306a46d45cf39c87c87acca88c838f`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `multipart_form` | `string` | `required` | - |
| `display_name` | `multipart_form` | `string` | `required` | length: 30 characters; rule: Length limit: 30 characters |
| `handle` | `multipart_form` | `string` | `optional` | length: 24 characters; rule: Length limit: 24 characters; rule: The handle cannot consist solely of numbers |
| `profile_image` | `multipart_form` | `file` | `optional` | multipart encoding: binary file part |
| `operating_region_code` | `multipart_form` | `string` | `required` | rule: Note : If your business is based in the Chinese mainland, you must select an operating region other than China when creating an Organization Account, as CN is not an available option for operating_reg; allowed: AR, AU, AT, BD, BE, BR, BG, KH, CA, CL, CO, HR, CY, CZ, DK, EC, EG, EE, FI, FR, DE, GR, HU, ID, IQ, IE, IL, IT, JP, JO, KZ, KW, LV, LT, LU, MY, MX, MA, NL, NZ, NO, PK, PE, PH, PL, PT, RO, SA, SG, SK, SI, ZA, KR, ES, SE, CH, TW, TH, TR, AE, GB, US, VN |
| `qualification_info` | `multipart_form` | `object` | `conditional` | condition: the type of your Business Center is AGENCY or SELF_SERVICE_AGENCY; rule: Required when the type of your Business Center is AGENCY or SELF_SERVICE_AGENCY; multipart encoding: JSON-serialized string form part |
| `qualification_info.qualification_id` | `multipart_form` | `string` | `optional` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.asset_id` | `string` | - |
| `data.asset_name` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
