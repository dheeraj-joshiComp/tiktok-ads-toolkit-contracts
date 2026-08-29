# TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_GET

- Operation: Get the result of a creative pre-review task
- Wire: `GET /creative/pre_review/task/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1874110636550082](https://business-api.tiktok.com/portal/docs?id=1874110636550082)
- Source content SHA-256: `18d77a2b51c4b2ee97866a07bb7bf52f9bfc34ca433563b31991b01a77447ca2`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
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
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.task_status` | `string` | allowed: PROCESSING, SUCCESS |
| `data.pre_review_result_list` | `object[]` | - |
| `data.pre_review_result_list[].pre_review_status` | `string` | allowed: APPROVED, REJECTED, UNSURE, UNAVAILABLE; rule: UNSURE: Result cannot be determined |
| `data.pre_review_result_list[].material_type` | `string` | allowed: VIDEO, IMAGE, AD_TEXT, LANDING_PAGE_URL |
| `data.pre_review_result_list[].material_id` | `string` | - |
| `data.pre_review_result_list[].result_creation_time` | `string` | rule: The time when the pre-review result was generated, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.pre_review_result_list[].result_expiration_time` | `string` | rule: The time when the pre-review result will expire, in the format of YYYY-MM-DD HH:MM:SS (UTC+0) |
| `data.pre_review_result_list[].location_code` | `string` | allowed: AD, AE, AG, AI, AL, AO, AR, AT, AU, AW, AZ, BA, BB, BD, BE, BG, BH, BL, BM, BO, BQ, BR, BS, BY, BZ, CA, CD, CH, CL, CO, CR, CU, CV, CW, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, ER, ES, FI, FO, FR, GB, GD, GE, GF, GG, GI, GL, GN, GP, GQ, GR, GT, GW, HK, HN, HR, HT, HU, ID, IE, IL, IM, IN, IQ, IS, IT, JE, JM, JO, JP, KE, KH, KM, KN, KR, KW, KY, KZ, LB, LC, LI, LK, LT, LU, LV, LY, MA, MC, MD, ME, MF, MK, MM, MO, MQ, MR, MS, MT, MX, MY, MZ, NG, NI, NL, NO, NP, NZ, OM, PA, PE, PF, PH, PK, PL, PM, PR, PS, PT, PY, QA, RO, RS, RU, SA, SD, SE, SG, SI, SJ, SK, SM, SO, SS, ST, SV, SX, SY, TC, TD, TF, TH, TN, TR, TT, TW, UA, US, UY, UZ, VC, VE, VG, VI, VN, YE, ZA |
| `data.pre_review_result_list[].is_ecommerce` | `boolean` | allowed: true, false |
| `data.pre_review_result_list[].reject_info_list` | `object[]` | - |
| `data.pre_review_result_list[].reject_info_list[].reason` | `string` | - |
| `data.pre_review_result_list[].reject_info_list[].suggestion` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
