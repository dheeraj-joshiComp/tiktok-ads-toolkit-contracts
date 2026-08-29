# TIKTOK_ADS_GET_ADVERTISER_QUALIFICATION

- Operation: Get qualifications within a Business Center
- Wire: `GET /bc/advertiser/qualification/get/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `1`
- Permission evidence: `direct_permission_table_mapping`
- Selected category: `Ad Account Management`
- Source: [doc 1770118680584194](https://business-api.tiktok.com/portal/docs?id=1770118680584194)
- Source content SHA-256: `c696bff72c963c956e3fa3f1b16b3a22044fee8fa930ec4275312e61a177c8e2`
- Product/fixture gate: Authorized Business Center and advertiser/asset fixture with the required role
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `query` | `string` | `required` | - |
| `filtering` | `query` | `object` | `optional` | - |
| `filtering.verified` | `query` | `boolean` | `optional` | - |
| `page` | `query` | `int` | `optional` | default: 1; range: ≥ 1; rule: Value range : ≥ 1 |
| `page_size` | `query` | `int` | `optional` | default: 10; range: 1-100; rule: Value range: 1-100 |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `data` | `object` | - |
| `data.qualifications` | `object[]` | - |
| `data.qualifications[].qualification_id` | `string` | - |
| `data.qualifications[].company_name` | `string` | - |
| `data.qualifications[].status` | `string` | allowed: VERIFIED, UNVERIFIED |
| `data.qualifications[].owner_advertiser_id` | `string` | - |
| `data.qualifications[].linked_advertiser_count` | `int` | - |
| `data.qualifications[].region_code` | `string` | - |
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
