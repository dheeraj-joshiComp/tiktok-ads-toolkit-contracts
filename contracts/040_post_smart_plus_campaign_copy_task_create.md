# TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CREATE

- Operation: Create an asynchronous copy task for an Upgraded Smart+ Campaign
- Wire: `POST /smart_plus/campaign/copy/task/create/`
- Request encoding: `application/json`
- Ability hint: `creates-or-starts-job`
- Parent scope: `2`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Ads Management`
- Source: [doc 1866528879472641](https://business-api.tiktok.com/portal/docs?id=1866528879472641)
- Source content SHA-256: `92e9dd7c171d932434ac0ebff41040a392df3bf2be9de61d8b7d96ab99073a6c`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Implementation and mocked contract tests only in this batch; no live POST
- Additional enum source: [doc 1737174886619138](https://business-api.tiktok.com/portal/docs?id=1737174886619138), SHA-256 `ef72527cf986285a6b4f22173fe0bd9c4b9295504f3affe22e99844acaf208c2`

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `advertiser_id` | `json_body` | `string` | `required` | - |
| `request_id` | `json_body` | `string` | `required` | rule: If you retry requests with the same request ID multiple times within the 10-second cache time, then only one request will succeed; rule: If a duplicate request with the expired request ID is received after the cache time, the server will treat it as a new request and process it accordingly |
| `campaign_id` | `json_body` | `string` | `required` | rule: To retrieve Upgraded Smart+ Campaigns within your ad account, use /smart_plus/campaign/get/; rule: Note : The source campaign must use one of these advertising objectives: APP_PROMOTION, LEAD_GENERATION, WEB_CONVERSIONS; rule: The source campaign must not be deleted; rule: The source campaign must contain at least 1 undeleted ad group, which must contain at least 1 undeleted ad; rule: The source campaign must satisfy all per-level limits, and the total copied assets must also not exceed the global new campaign limits: On the source campaign: you may have a maximum of 10 undeleted a |
| `operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: DISABLE; rule: If you want to update the status of the campaign after creation, use /smart_plus/campaign/status/update/ |
| `campaign_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `budget` | `json_body` | `number` | `optional` | rule: The budget for the new campaign or the budget limit for all ad groups under the new campaign; rule: To retrieve the current campaign budget, use /smart_plus/campaign/get/ after the copy task is completed and check the returned current_budget; rule: When budget_optimize_on of the source campaign is false, this field represents the budget limit for all ad groups under the new campaign; rule: When budget_mode is BUDGET_MODE_DAY, this field represents the daily limit for all ad groups under the new campaign; rule: When budget_mode is BUDGET_MODE_TOTAL, this field represents the total limit for all ad groups under the new campaign |
| `schedule_type` | `json_body` | `string` | `optional` | allowed: SCHEDULE_START_END, SCHEDULE_FROM_NOW; rule: You need to pass both schedule_start_time and schedule_end_time at the same time |
| `schedule_start_time` | `json_body` | `string` | `conditional` | condition: schedule_type is passed; rule: Required when schedule_type is passed; rule: Schedule start time (UTC+0) for all new ad groups, in the format of YYYY-MM-DD HH:MM:SS; rule: The start time can be up to 12 hours earlier than the current time, but cannot be later than 2028-01-01 00:00:00 |
| `schedule_end_time` | `json_body` | `string` | `conditional` | condition: schedule_type is SCHEDULE_START_END; rule: Required when schedule_type is SCHEDULE_START_END; rule: Not supported when schedule_type is SCHEDULE_FROM_NOW; rule: Schedule end time (UTC+0) for all new ad groups, in the format of YYYY-MM-DD HH:MM:SS; rule: The end time cannot be later than 2038-01-01 00:00:00 |
| `dayparting` | `json_body` | `string` | `optional` | rule: Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters |
| `deep_copy_mode` | `json_body` | `string` | `optional` | allowed: DEFAULT, CUSTOM; default: DEFAULT; rule: You can copy a maximum of 20 ads per ad group, across a maximum of 30 ad groups |
| `adgroup_list` | `json_body` | `object[]` | `optional` | size: 10; rule: When deep_copy_mode is set to CUSTOM, this field is required |
| `adgroup_list[].adgroup_id` | `json_body` | `string` | `conditional` | condition: adgroup_list is passed; rule: Required when adgroup_list is passed |
| `adgroup_list[].operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: ENABLE; rule: If you want to update the status of the ad group after creation, use /smart_plus/adgroup/status/update/ |
| `adgroup_list[].adgroup_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `adgroup_list[].budget` | `json_body` | `number` | `optional` | rule: To retrieve the current ad group budget, use /smart_plus/adgroup/get/ after the copy task is completed and check the returned current_budget |
| `adgroup_list[].min_budget` | `json_body` | `number` | `optional` | all-of: At the campaign level:budget_optimize_on is truebudget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET || At the ad group level:bid_type is BID_TYPE_NO_BID; rule: Valid only when the following conditions are all met: At the campaign level: budget_optimize_on is true; rule: The system will aim to spend at least this amount, but it is not guaranteed |
| `adgroup_list[].targeting_spec` | `json_body` | `object` | `optional` | - |
| `adgroup_list[].targeting_spec.location_ids` | `json_body` | `string[]` | `optional` | rule: Note : If you add the US as your target location, then you can not remove the US after ad group creation |
| `adgroup_list[].targeting_spec.zipcode_ids` | `json_body` | `string[]` | `optional` | size: 3,000; rule: If you provide both location_ids and zipcode_ids, the combined total of location IDs, zip code IDs, and postal code IDs cannot exceed 3,000 per ad group; rule: Note : Zip code targeting is currently only supported for the US and postal code targeting is currently only supported for Canada, Brazil, Indonesia, Thailand, and Vietnam; rule: You cannot use zip code targeting or postal code targeting in campaigns that have enabled special ad categories (special_industries); rule: Overlapping targeted locations are not supported; rule: For instance, you cannot target the US and the state of California at the same time |
| `adgroup_list[].targeting_spec.excluded_audience_ids` | `json_body` | `string[]` | `optional` | rule: Note : When at the campaign level rta_id is specified, this field is not supported |
| `adgroup_list[].targeting_spec.audience_ids` | `json_body` | `string[]` | `optional` | rule: Note : When at the campaign level rta_id is specified, this field is not supported |
| `adgroup_list[].targeting_spec.saved_audience_id` | `json_body` | `string` | `optional` | all-of: The targeting_optimization_mode of the source ad group is MANUAL. || The category of Housing, Employment, or Credit (specical_industries) is NOT specified in your campaign. || TikTok placement is selected in your; rule: Before using this field, call /dmp/saved_audience/create/ to create a Saved Audience and get the Saved Audience ID in response; rule: If you use saved_audience_id to create an ad group, we will return both the Saved Audience ID and the targeting options that are included within your Saved Audience in response; rule: However, be aware that if you are creating an ad group based on a Saved Audience, it’s essential to avoid setting both the saved_audience_id and targeting options (such as gender) defined within your ; rule: Make sure that the age targeting setting is allowed before you use the Saved Audience (saved_audience_id ) in the ad group |
| `adgroup_list[].ad_list` | `json_body` | `object[]` | `conditional` | size: 30; rule: When deep_copy_mode is set to CUSTOM, this field is required; rule: Note : The maximum number of ads that you can specify in the new campaign is 200 |
| `adgroup_list[].ad_list[].smart_plus_ad_id` | `json_body` | `string` | `conditional` | condition: ad_list is passed; rule: Required when ad_list is passed |
| `adgroup_list[].ad_list[].operation_status` | `json_body` | `string` | `optional` | allowed: ENABLE, DISABLE; default: ENABLE; rule: If you want to update the status of the ad after creation, use /smart_plus/ad/status/update/ |
| `adgroup_list[].ad_list[].ad_name` | `json_body` | `string` | `optional` | length: 512 characters; rule: Length limit: 512 characters; rule: Emojis are not supported |
| `adgroup_list[].ad_list[].creative_list` | `json_body` | `object[]` | `optional` | size: 1-50; rule: Size range: 1-50; rule: The maximum number of creatives that you can specify in the new campaign is 1,000 |
| `adgroup_list[].ad_list[].creative_list[].creative_info` | `json_body` | `object` | `conditional` | condition: creative_list is specified; rule: Required when creative_list is specified |
| `adgroup_list[].ad_list[].creative_list[].creative_info.ad_format` | `json_body` | `string` | `conditional` | condition: creative_info is specified; any-of: SINGLE_VIDEO: Single Video.To use this format, specify any of the following:a video through video_id and a video cover through web_uria TikTok video post through tiktok_item_id. || CAROUSEL_ADS: Standard Carousel; rule: Required when creative_info is specified; rule: The ad format; rule: To use this format, specify any of the following: a video through video_id and a video cover through web_uri; rule: To use this format, specify any of the following: carousel images through web_uri and a piece of music through music_id |
| `adgroup_list[].ad_list[].creative_list[].creative_info.video_info` | `json_body` | `object` | `conditional` | rule: Required for Spark Ads Single Video ads through Spark Ads Push |
| `video_id` | `json_body` | `string` | `conditional` | condition: video_info is specified; rule: Required when video_info is specified; rule: To search for videos within your ad account, use /file/video/ad/search/ |
| `file_name` | `json_body` | `string` | `optional` | - |
| `adgroup_list[].ad_list[].creative_list[].creative_info.image_info` | `json_body` | `object[]` | `conditional` | any-of: Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. || Spark Ads Standard Carousel ads through Spark Ads Push. You need to specify one to 35 carousel images. || Catalog Carousel ; rule: Required for the following types of ads: Spark Ads Single Video ads through Spark Ads Push; rule: Not supported for Catalog Carousel ads in Upgraded Smart+ Web Ads |
| `web_uri` | `json_body` | `string` | `conditional` | condition: image_info is specified; rule: Required when image_info is specified; rule: To search for images within your ad account, use /file/image/ad/search/ |
| `adgroup_list[].ad_list[].creative_list[].creative_info.music_info` | `json_body` | `object` | `conditional` | any-of: When you create Standard Carousel Ads, including:Spark Ads Standard Carousel ads through Spark Ads PushSpark Ads Standard Carousel ads through Spark Ads Pull || When objective_type is WEB_CONVERSIONS or LEAD_GENE; rule: Required for the following scenarios: When you create Standard Carousel Ads, including: Spark Ads Standard Carousel ads through Spark Ads Push |
| `music_id` | `json_body` | `string` | `conditional` | condition: music_info is specified; rule: Required when music_info is specified |
| `adgroup_list[].ad_list[].creative_list[].creative_info.aigc_disclosure_type` | `json_body` | `string` | `optional` | allowed: SELF_DISCLOSURE, NOT_DECLARED; default: NOT_DECLARED; rule: After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full |
| `adgroup_list[].ad_list[].creative_list[].creative_info.tiktok_item_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; any-of: Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. || Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post.; rule: Required when you create Spark Ads through Spark Ads Pull, including: Spark Ads Single Video ads through Spark Ads Pull; rule: Not supported when catalog_creative_toggle is true |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_type` | `json_body` | `string` | `conditional` | allowed: AUTH_CODE, TT_USER, BC_AUTH_TT; condition: you create Spark Ads; rule: Required when you create Spark Ads |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_id` | `json_body` | `string` | `conditional` | condition: you create Spark Ads; rule: Required when you create Spark Ads |
| `adgroup_list[].ad_list[].creative_list[].creative_info.identity_authorized_bc_id` | `json_body` | `string` | `conditional` | condition: identity_type is BC_AUTH_TT; rule: Required when identity_type is BC_AUTH_TT |
| `adgroup_list[].ad_list[].ad_text_list` | `json_body` | `object[]` | `conditional` | size: 5; condition: tiktok_item_id is not specified; rule: Required when tiktok_item_id is not specified |
| `adgroup_list[].ad_list[].ad_text_list[].ad_text` | `json_body` | `string` | `conditional` | condition: ad_text_list is specified; rule: Required when ad_text_list is specified |
| `adgroup_list[].ad_list[].call_to_action_list` | `json_body` | `object[]` | `conditional` | size: 3; rule: Note : This field is not supported in any of the following scenarios and you need to use call_to_action_id instead; rule: At the ad level, identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE |
| `adgroup_list[].ad_list[].call_to_action_list[].call_to_action` | `json_body` | `string` | `conditional` | condition: call_to_action_list is specified; rule: Required when call_to_action_list is specified; allowed: APPLY_NOW, BOOK_NOW, CALL_NOW, CHECK_AVAILABLILITY, CONTACT_US, DOWNLOAD_NOW, EXPERIENCE_NOW, GET_QUOTE, GET_SHOWTIMES, GET_TICKETS_NOW, INSTALL_NOW, INTERESTED, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, PREORDER_NOW, READ_MORE, SEND_MESSAGE, SHOP_NOW, SIGN_UP, SUBSCRIBE, VIEW_NOW, VIEW_PROFILE, VISIT_STORE, WATCH_LIVE, WATCH_NOW, JOIN_THIS_HASHTAG, SHOOT_WITH_THIS_EFFECT, VIEW_VIDEO_WITH_THIS_EFFECT |
| `adgroup_list[].ad_list[].landing_page_url_list` | `json_body` | `object[]` | `optional` | size: 0-1; rule: Size range: 0-1 |
| `adgroup_list[].ad_list[].landing_page_url_list[].landing_page_url` | `json_body` | `string` | `conditional` | condition: landing_page_url_list is specified; rule: Required when landing_page_url_list is specified |
| `adgroup_list[].ad_list[].ad_configuration` | `json_body` | `object` | `optional` | - |
| `adgroup_list[].ad_list[].ad_configuration.utm_params` | `json_body` | `object[]` | `optional` | size: 14; cross-field: when landing_page_url to a URL that already includes URL parameters, you can optionally pass utm_params at the same time to store the URL parameters used in the URL. In such cases,; rule: If you set landing_page_url to a URL that already includes URL parameters, you can optionally pass utm_params at the same time to store the URL parameters used in the URL |
| `adgroup_list[].ad_list[].ad_configuration.utm_params[].key` | `json_body` | `string` | `optional` | rule: Length limit when you specify a custom parameter: 100 characters |
| `adgroup_list[].ad_list[].ad_configuration.utm_params[].value` | `json_body` | `string` | `optional` | rule: Length limit when you specify a custom value: 600 characters |
| `adgroup_list[].ad_list[].ad_configuration.call_to_action_id` | `json_body` | `string` | `optional` | rule: At the ad level, identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.task_id` | `string` | - |
| `data.adgroup_error_list` | `object[]` | - |
| `data.adgroup_error_list[].adgroup_id` | `string` | - |
| `data.adgroup_error_list[].error_message` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
