# TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_CREATE

- Operation: Create a creative pre-review task
- Wire: `POST /creative/pre_review/task/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1874110632584577](https://business-api.tiktok.com/portal/docs?id=1874110632584577)
- Source content SHA-256: `329b6d2fdb16acc3c146a1fdddba0294a5a57021d4debb19def06659a1a22723`
- Product/fixture gate: Advertiser-owned disposable creative/video/file fixture
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `material_list` | `json_body` | `object[]` | `required` | size: 1-5; rule: Size range: 1-5 |
| `material_list[].material_type` | `json_body` | `string` | `required` | allowed: VIDEO, IMAGE, AD_TEXT, LANDING_PAGE_URL |
| `material_list[].material_id` | `json_body` | `string` | `required` | rule: To search for video IDs within your ad account, use /file/video/ad/search/ and check the returned video_id; rule: To search for image IDs within your ad account, use /file/image/ad/search/ and check the returned image_id |
| `location_codes` | `json_body` | `string[]` | `required` | size: 1; allowed: AD, AE, AG, AI, AL, AO, AR, AT, AU, AW, AZ, BA, BB, BD, BE, BG, BH, BL, BM, BO, BQ, BR, BS, BY, BZ, CA, CD, CH, CL, CO, CR, CU, CV, CW, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, ER, ES, FI, FO, FR, GB, GD, GE, GF, GG, GI, GL, GN, GP, GQ, GR, GT, GW, HK, HN, HR, HT, HU, ID, IE, IL, IM, IN, IQ, IS, IT, JE, JM, JO, JP, KE, KH, KM, KN, KR, KW, KY, KZ, LB, LC, LI, LK, LT, LU, LV, LY, MA, MC, MD, ME, MF, MK, MM, MO, MQ, MR, MS, MT, MX, MY, MZ, NG, NI, NL, NO, NP, NZ, OM, PA, PE, PF, PH, PK, PL, PM, PR, PS, PT, PY, QA, RO, RS, RU, SA, SD, SE, SG, SI, SJ, SK, SM, SO, SS, ST, SV, SX, SY, TC, TD, TF, TH, TN, TR, TT, TW, UA, US, UY, UZ, VC, VE, VG, VI, VN, YE, ZA |
| `is_ecommerce` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.pre_review_task_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
