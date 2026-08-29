# TIKTOK_ADS_CATALOG_VIDEO_FILE

- Operation: Upload catalog videos via a file URL
- Wire: `POST /catalog/video/file/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `9`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `DPA Catalog Management`
- Source: [doc 1803655037415489](https://business-api.tiktok.com/portal/docs?id=1803655037415489)
- Source content SHA-256: `56f110b548398f7257469a4e67eb172d068c9d5c6107f53278bc13af79740227`
- Product/fixture gate: Authorized Business Center catalog with the required products, videos, feed, or diagnostics
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `bc_id` | `json_body` | `string` | `required` | - |
| `catalog_id` | `json_body` | `string` | `required` | - |
| `file_url` | `json_body` | `string` | `required` | - |
| `advertiser_ids` | `json_body` | `string[]` | `optional` | size: 100; rule: The ad account and the catalog (catalog_id) must be within the same Business Center (bc_id) and you need to have Admin or Operator permission for the ad account |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.feed_log_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
