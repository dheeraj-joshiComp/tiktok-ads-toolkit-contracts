# TIKTOK_ADS_SMART_PLUS_AD_PREVIEW

- Operation: Preview Upgraded Smart+ Ads
- Wire: `POST /smart_plus/ad/preview/`
- Request encoding: `application/json`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1843317445798914](https://business-api.tiktok.com/portal/docs?id=1843317445798914)
- Source content SHA-256: `a2e1f35b5c18fb30fef25b223d714209f509f2cbfb6ed9a48835615e28d7882f`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST
- Additional enum source: [doc 1737174886619138](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`

## Request contract

### Variant: Preview ads that you plan to create

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `preview_type` | `json_body` | `string` | `required` | allowed: ADS_CREATION |
| `catalog_enabled` | `json_body` | `boolean` | `optional` | allowed: true, false |
| `catalog_id` | `json_body` | `string` | `conditional` | condition: catalog_enabled is true; rule: Required when catalog_enabled is true; rule: To retrieve the catalogs within your Business Center, use /catalog/get/ |
| `catalog_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: catalog_enabled is true; rule: Required when catalog_enabled is true |
| `creative_list` | `json_body` | `object[]` | `required` | size: 1- 31; rule: Size range: 1- 31 |
| `creative_list[].creative_info` | `json_body` | `object` | `required` | - |
| `creative_list[].creative_info.video_info` | `json_body` | `object` | `conditional` | any-of: Non-Spark Ads Single Video ads. || Spark Ads Single Video ads through Spark Ads Push.; rule: Required for the following types of ads: Non-Spark Ads Single Video ads |
| `creative_list[].creative_info.video_info.video_id` | `json_body` | `string` | `conditional` | condition: video_info is specified; rule: Required when video_info is specified; rule: To search for videos within your ad account, use /file/video/ad/search/ |
| `creative_list[].creative_info.image_info` | `json_body` | `object[]` | `conditional` | any-of: Non-Spark Ads Single Video ads. You need to specify a video cover. || Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. || Non-Spark Ads Standard Carousel ads. You need to spec; rule: Required for the following types of ads: Non-Spark Ads Single Video ads; rule: Not supported for Catalog Carousel ads |
| `creative_list[].creative_info.image_info[].web_uri` | `json_body` | `string` | `conditional` | condition: image_info is specified; rule: Required when image_info is specified; rule: To search for images within your ad account, use /file/image/ad/search/ |
| `creative_list[].creative_info.music_info` | `json_body` | `object` | `conditional` | any-of: When you create Standard Carousel Ads, including:Non-Spark Ads Standard Carousel adsSpark Ads Standard Carousel ads through Spark Ads PushSpark Ads Standard Carousel ads through Sp || When objective_type is WEB_C; rule: Required for the following scenarios: When you create Standard Carousel Ads, including: Non-Spark Ads Standard Carousel ads |
| `creative_list[].creative_info.music_info.music_id` | `json_body` | `string` | `conditional` | condition: music_info is specified; rule: Required when music_info is specified |
| `creative_list[].creative_info.tiktok_item_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; any-of: Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. || Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post.; rule: Required when you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; rule: Not supported when catalog_creative_toggle is true |
| `creative_list[].creative_info.identity_type` | `json_body` | `string` | `conditional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT; condition: you create Spark Ads without using catalog creatives; all-of: At the campaign level, objective_type is APP_PROMOTION or WEB_CONVERSIONS. || At the ad group level, placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK, or placement_type is PLACEMEN; rule: Required when you create Spark Ads without using catalog creatives; rule: Note : If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the identity_type and identity_id within ad_configuration |
| `creative_list[].creative_info.identity_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads without using catalog creatives; rule: Required when you create Spark Ads without using catalog creatives; rule: Note : If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the identity_type and identity_id within ad_configuration |
| `creative_list[].creative_info.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type within creative_info is BC_AUTH_TT; rule: Required when identity_type within creative_info is BC_AUTH_TT |
| `ad_text_list` | `json_body` | `object[]` | `conditional` | size: 5; condition: tiktok_item_id is not specified; rule: Required when tiktok_item_id is not specified |
| `ad_text_list[].ad_text` | `json_body` | `string` | `conditional` | condition: ad_text_list is specified; rule: Required when ad_text_list is specified |
| `call_to_action_list` | `json_body` | `object[]` | `optional` | size: 3; rule: Note : This field is not supported for Upgraded Smart+ Lead Generation Campaigns; rule: call_to_action_list and call_to_action_id cannot be set at the same time |
| `call_to_action_list[].call_to_action` | `json_body` | `string` | `conditional` | condition: call_to_action_list is specified; rule: Required when call_to_action_list is specified; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `ad_configuration` | `json_body` | `object` | `optional` | - |
| `ad_configuration.identity_type` | `json_body` | `string` | `conditional` | allowed: CUSTOMIZED_USER, TT_USER, BC_AUTH_TT; any-of: You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. || You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more; rule: Required in any of the following scenarios: You are creating non-Spark Ads on non-TikTok placements |
| `ad_configuration.identity_id` | `json_body` | `string` | `conditional` | any-of: You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. || You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more; rule: Required in any of the following scenarios: You are creating non-Spark Ads on non-TikTok placements |
| `ad_configuration.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type within ad_configuration is BC_AUTH_TT; rule: Required when identity_type within ad_configuration is BC_AUTH_TT |
| `ad_configuration.product_specific_type` | `json_body` | `string` | `conditional` | allowed: ALL, PRODUCT_SET, CUSTOMIZED_PRODUCTS; condition: catalog_enabled is true at the campaign level; any-of: ALL: Allow TikTok to dynamically choose from all products. || PRODUCT_SET: Specify a product set. TikTok will dynamically choose products from this set. || CUSTOMIZED_PRODUCTS: Specify a customized number of prod; rule: Required when catalog_enabled is true at the campaign level; rule: If this field is set to CUSTOMIZED_PRODUCTS, product_ids is required |
| `ad_configuration.product_set_id` | `json_body` | `string` | `conditional` | condition: product_specific_type is PRODUCT_SET; any-of: To retrieve the product sets within your ad account, use /catalog/set/get/. || To create a product set, use /catalog/set/create/.; rule: Required when product_specific_type is PRODUCT_SET |
| `ad_configuration.product_ids` | `json_body` | `string[]` | `conditional` | size: 20; condition: product_specific_type is CUSTOMIZED_PRODUCTS; rule: Required when product_specific_type is CUSTOMIZED_PRODUCTS |
| `ad_configuration.catalog_creative_toggle` | `json_body` | `boolean` | `optional` | allowed: true, false; default: false; cross-field: Valid only when catalog_enabled is true.; ; Whether to enable auto-selection of creatives from your catalog.; ; Supported values: true, false.; Default value: false.; ; If you set  |
| `ad_configuration.catalog_creative_info` | `json_body` | `object` | `optional` | any-of: The ad is an Upgraded Smart+ E-commerce Catalog Ad or Upgraded Smart+ Streaming Ad. || catalog_creative_toggle is true.; rule: Valid only when the following conditions are met: The ad is an Upgraded Smart+ E-commerce Catalog Ad or Upgraded Smart+ Streaming Ad |
| `ad_configuration.catalog_creative_info.catalog_media_settings` | `json_body` | `string[]` | `optional` | rule: If you include this value in catalog_media_settings, you can optionally specify catalog_template_video_id at the same time; rule: If you include this value in catalog_media_settings, you cannot specify catalog_template_video_id at the same time; rule: Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library |
| `ad_configuration.catalog_creative_info.catalog_template_video_id` | `json_body` | `string` | `optional` | any-of: The ad is an Upgraded Smart+ Streaming Ad. || TEMPLATE_VIDEO is included in catalog_media_settings.; rule: Valid only when the following conditions are met: The ad is an Upgraded Smart+ Streaming Ad |
| `ad_configuration.call_to_action_id` | `json_body` | `string` | `optional` | rule: Note : call_to_action_list and call_to_action_id cannot be set at the same time |

### Variant: Preview existing ads

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `preview_type` | `json_body` | `string` | `required` | allowed: AD |
| `smart_plus_ad_id` | `json_body` | `string` | `required` | - |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.preview_link` | `string` | - |
| `data.iframe` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
