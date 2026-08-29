# TikTok Ads gated-document recovery audit

Date: `2026-08-30`
Pinned Mercury SHA: `9f35c86a6ec3d56fe442046282803b79206f97a5`
Selected provider app: `REDACTED_SELECTED_APP_ID`
Method: live official TikTok docs API and current API Reference, read-only.

## Verdict

The region-access fix recovered implementation-grade contracts for **63 of the 116 missing selected paths**. Yang can implement **40 GET actions and 23 POST actions** from current official evidence. HTTP method does not determine side effects; each POST still needs an ability and cleanup review before live certification.

Three selected Reporting Subscription paths have current replacement pages, but those operations require developer secrets and a `REPORT_DATA_CHANGE` allowlist. Keep them in auth/platform design. Do not implement the stale `/report/subscription/*` paths or expose secrets as tool inputs.

| Decision | Count |
|---|---:|
| `ABSENT_UNRESOLVED` | 39 |
| `AUTH_SECRET_FLOW` | 1 |
| `CURRENT_ROUTE_REPLACEMENT` | 3 |
| `DEPRECATED_OR_NOT_V1_3` | 3 |
| `HUMAN_CONNECTION_FLOW` | 1 |
| `IMPLEMENTABLE_FROM_OFFICIAL_DOCS` | 63 |
| `PERMISSION_ONLY_NO_CONTRACT` | 1 |
| `PROVIDER_CONTRACT_CONTRADICTION` | 2 |
| `PROVIDER_DOC_DEFECT` | 1 |
| `SEPARATE_EVENTS_AUTH` | 1 |
| `UNSAFE_NO_ROLLBACK` | 1 |

The earlier public-only audit is superseded for contract availability. TikTok's permission document proves first-level inheritance. Of the 63 implementation-grade paths, 17 have a direct permission-table path mapping; the other 46 rely on the provider-supplied selected-endpoint category export plus the official inheritance rule. Feature allowlists remain separate gates.

## Implementation batch: 63 actions

| Category | Method | Endpoint | Proposed tool | Scope | Docs | QA boundary |
|---|---|---|---|---:|---|---|
| Ad Account Management | GET | `/asset/bind/quota/` | `TIKTOK_ADS_GET_ASSET_BINDING_QUOTA` | `1` | [doc 1739659584022529](https://business-api.tiktok.com/portal/docs?id=1739659584022529) | Read-only; live fixture may still be required |
| Ad Account Management | GET | `/bc/account/cost/get/` | `TIKTOK_ADS_LIST_BUSINESS_CENTER_ACCOUNT_COSTS` | `1` | [doc 1829079287639041](https://business-api.tiktok.com/portal/docs?id=1829079287639041) | Read-only; live fixture may still be required |
| Ad Account Management | GET | `/bc/advertiser/attribute/` | `TIKTOK_ADS_GET_BUSINESS_CENTER_ADVERTISER_ATTRIBUTES` | `1` | [doc 1775752357139457](https://business-api.tiktok.com/portal/docs?id=1775752357139457) | Read-only; live fixture may still be required |
| Ad Account Management | POST | `/bc/advertiser/disable/` | `TIKTOK_ADS_DISABLE_BUSINESS_CENTER_ADVERTISER` | `1` | [doc 1752349244331009](https://business-api.tiktok.com/portal/docs?id=1752349244331009) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ad Account Management | GET | `/bc/advertiser/qualification/get/` | `TIKTOK_ADS_GET_ADVERTISER_QUALIFICATION` | `1` | [doc 1770118680584194](https://business-api.tiktok.com/portal/docs?id=1770118680584194) | Read-only; live fixture may still be required |
| Ad Account Management | GET | `/bc/advertiser/unionpay_info/check/` | `TIKTOK_ADS_CHECK_UNIONPAY_VERIFICATION_REQUIREMENT` | `1` | [doc 1813772238056449](https://business-api.tiktok.com/portal/docs?id=1813772238056449) | Read-only; live fixture may still be required |
| Ad Account Management | POST | `/bc/asset/advertiser/assign/` | `TIKTOK_ADS_ASSIGN_TIKTOK_ACCOUNT_TO_ADVERTISER` | `1` | [doc 1846868953025538](https://business-api.tiktok.com/portal/docs?id=1846868953025538) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ad Account Management | GET | `/bc/asset/advertiser/assigned/` | `TIKTOK_ADS_LIST_ADVERTISER_ASSIGNED_TIKTOK_ACCOUNTS` | `1` | [doc 1855027294743554](https://business-api.tiktok.com/portal/docs?id=1855027294743554) | Read-only; live fixture may still be required |
| Ad Account Management | POST | `/bc/asset/advertiser/unassign/` | `TIKTOK_ADS_UNASSIGN_TIKTOK_ACCOUNT_FROM_ADVERTISER` | `1` | [doc 1855027260369921](https://business-api.tiktok.com/portal/docs?id=1855027260369921) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ad Account Management | POST | `/bc/oa/create/` | `TIKTOK_ADS_CREATE_BUSINESS_CENTER_ORGANIZATION_ACCOUNT` | `1` | [doc 1855027199571138](https://business-api.tiktok.com/portal/docs?id=1855027199571138) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ad Account Management | GET | `/report/bid_protection/detail/get/` | `TIKTOK_ADS_GET_BID_PROTECTION_DETAILS` | `1` | [doc 1874392516418561](https://business-api.tiktok.com/portal/docs?id=1874392516418561) | Read-only; live fixture may still be required |
| Ad Account Management | GET | `/report/bid_protection/status/get/` | `TIKTOK_ADS_GET_BID_PROTECTION_STATUSES` | `1` | [doc 1874392512912449](https://business-api.tiktok.com/portal/docs?id=1874392512912449) | Read-only; live fixture may still be required |
| Ads Management | POST | `/business/spark_ad/create/` | `TIKTOK_ADS_BUSINESS_SPARK_AD_CREATE` | `2` | [doc 1829744071179330](https://business-api.tiktok.com/portal/docs?id=1829744071179330) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | POST | `/campaign/gmv_max/creative/update/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_CREATIVE_UPDATE` | `2` | [doc 1861260625563202](https://business-api.tiktok.com/portal/docs?id=1861260625563202) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | POST | `/campaign/gmv_max/session/create/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_CREATE` | `2` | [doc 1835246967275522](https://business-api.tiktok.com/portal/docs?id=1835246967275522) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | POST | `/campaign/gmv_max/session/delete/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_DELETE` | `2` | [doc 1835246983475217](https://business-api.tiktok.com/portal/docs?id=1835246983475217) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | GET | `/campaign/gmv_max/session/get/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_GET` | `2` | [doc 1835247031331842](https://business-api.tiktok.com/portal/docs?id=1835247031331842) | Read-only; live fixture may still be required |
| Ads Management | GET | `/campaign/gmv_max/session/list/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_LIST` | `2` | [doc 1835246996436162](https://business-api.tiktok.com/portal/docs?id=1835246996436162) | Read-only; live fixture may still be required |
| Ads Management | POST | `/campaign/gmv_max/session/update/` | `TIKTOK_ADS_CAMPAIGN_GMV_MAX_SESSION_UPDATE` | `2` | [doc 1835247009119233](https://business-api.tiktok.com/portal/docs?id=1835247009119233) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | GET | `/campaign/quota/info/` | `TIKTOK_ADS_CAMPAIGN_QUOTA_INFO` | `2` | [doc 1752256376677378](https://business-api.tiktok.com/portal/docs?id=1752256376677378) | Read-only; live fixture may still be required |
| Ads Management | GET | `/campaign_label/get/` | `TIKTOK_ADS_CAMPAIGN_LABEL_GET` | `2` | [doc 1851286489283585](https://business-api.tiktok.com/portal/docs?id=1851286489283585) | Read-only; live fixture may still be required |
| Ads Management | GET | `/changelog/get/` | `TIKTOK_ADS_CHANGELOG_GET` | `2` | [doc 1820767460168705](https://business-api.tiktok.com/portal/docs?id=1820767460168705) | Read-only; live fixture may still be required |
| Ads Management | GET | `/changelog/task/download/` | `TIKTOK_ADS_CHANGELOG_TASK_DOWNLOAD` | `2` | [doc 1739924165710849](https://business-api.tiktok.com/portal/docs?id=1739924165710849) | Read-only; live fixture may still be required |
| Ads Management | POST | `/gmv_max/creation/custom_anchor_video_list/delete/` | `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_DELETE` | `2` | [doc 1866513159202306](https://business-api.tiktok.com/portal/docs?id=1866513159202306) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | POST | `/gmv_max/creation/custom_anchor_video_list/get/` | `TIKTOK_ADS_GMV_MAX_CREATION_CUSTOM_ANCHOR_VIDEO_LIST_GET` | `2` | [doc 1866513156712449](https://business-api.tiktok.com/portal/docs?id=1866513156712449) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | GET | `/gmv_max/exclusive_authorization/get/` | `TIKTOK_ADS_GMV_MAX_EXCLUSIVE_AUTHORIZATION_GET` | `2` | [doc 1822001184635905](https://business-api.tiktok.com/portal/docs?id=1822001184635905) | Read-only; live fixture may still be required |
| Ads Management | GET | `/gmv_max/identity/get/` | `TIKTOK_ADS_GMV_MAX_IDENTITY_GET` | `2` | [doc 1822001101474882](https://business-api.tiktok.com/portal/docs?id=1822001101474882) | Read-only; live fixture may still be required |
| Ads Management | GET | `/gmv_max/occupied_custom_shop_ads/list/` | `TIKTOK_ADS_GMV_MAX_OCCUPIED_CUSTOM_SHOP_ADS_LIST` | `2` | [doc 1822001136924674](https://business-api.tiktok.com/portal/docs?id=1822001136924674) | Read-only; live fixture may still be required |
| Ads Management | GET | `/gmv_max/store/list/` | `TIKTOK_ADS_GMV_MAX_STORE_LIST` | `2` | [doc 1822001044479041](https://business-api.tiktok.com/portal/docs?id=1822001044479041) | Read-only; live fixture may still be required |
| Ads Management | GET | `/gmv_max/store/shop_ad_usage_check/` | `TIKTOK_ADS_GMV_MAX_STORE_SHOP_AD_USAGE_CHECK` | `2` | [doc 1822001084174338](https://business-api.tiktok.com/portal/docs?id=1822001084174338) | Read-only; live fixture may still be required |
| Ads Management | GET | `/gmv_max/video/get/` | `TIKTOK_ADS_GMV_MAX_VIDEO_GET` | `2` | [doc 1822001168512129](https://business-api.tiktok.com/portal/docs?id=1822001168512129) | Read-only; live fixture may still be required |
| Ads Management | POST | `/search_ad/negative_keyword/add/` | `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_ADD` | `2` | [doc 1775104895291393](https://business-api.tiktok.com/portal/docs?id=1775104895291393) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | POST | `/search_ad/negative_keyword/delete/` | `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_DELETE` | `2` | [doc 1775104910010369](https://business-api.tiktok.com/portal/docs?id=1775104910010369) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | GET | `/search_ad/negative_keyword/get/` | `TIKTOK_ADS_SEARCH_AD_NEGATIVE_KEYWORD_GET` | `2` | [doc 1775104887052289](https://business-api.tiktok.com/portal/docs?id=1775104887052289) | Read-only; live fixture may still be required |
| Ads Management | GET | `/showcase/identity/get/` | `TIKTOK_ADS_SHOWCASE_IDENTITY_GET` | `2` | [doc 1759233549899778](https://business-api.tiktok.com/portal/docs?id=1759233549899778) | Read-only; live fixture may still be required |
| Ads Management | GET | `/showcase/product/get/` | `TIKTOK_ADS_SHOWCASE_PRODUCT_GET` | `2` | [doc 1759233576199169](https://business-api.tiktok.com/portal/docs?id=1759233576199169) | Read-only; live fixture may still be required |
| Ads Management | GET | `/showcase/region/get/` | `TIKTOK_ADS_SHOWCASE_REGION_GET` | `2` | [doc 1759233561597954](https://business-api.tiktok.com/portal/docs?id=1759233561597954) | Read-only; live fixture may still be required |
| Ads Management | POST | `/smart_plus/adgroup/budget/update/` | `TIKTOK_ADS_SMART_PLUS_ADGROUP_BUDGET_UPDATE` | `2` | [doc 1843314914438466](https://business-api.tiktok.com/portal/docs?id=1843314914438466) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Ads Management | GET | `/smart_plus/campaign/copy/task/check/` | `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CHECK` | `2` | [doc 1866529943741441](https://business-api.tiktok.com/portal/docs?id=1866529943741441) | Read-only; live fixture may still be required |
| Ads Management | POST | `/smart_plus/campaign/copy/task/create/` | `TIKTOK_ADS_SMART_PLUS_CAMPAIGN_COPY_TASK_CREATE` | `2` | [doc 1866528879472641](https://business-api.tiktok.com/portal/docs?id=1866528879472641) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | POST | `/creative/asset/delete/` | `TIKTOK_ADS_CREATIVE_ASSET_DELETE` | `6` | [doc 1797202997456897](https://business-api.tiktok.com/portal/docs?id=1797202997456897) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | POST | `/creative/auto_message/create/` | `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_CREATE` | `6` | [doc 1822106113771521](https://business-api.tiktok.com/portal/docs?id=1822106113771521) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | GET | `/creative/auto_message/get/` | `TIKTOK_ADS_CREATIVE_AUTO_MESSAGE_GET` | `6` | [doc 1822106498804738](https://business-api.tiktok.com/portal/docs?id=1822106498804738) | Read-only; live fixture may still be required |
| Creative Management | POST | `/creative/pre_review/task/create/` | `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_CREATE` | `6` | [doc 1874110632584577](https://business-api.tiktok.com/portal/docs?id=1874110632584577) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | GET | `/creative/pre_review/task/get/` | `TIKTOK_ADS_CREATIVE_PRE_REVIEW_TASK_GET` | `6` | [doc 1874110636550082](https://business-api.tiktok.com/portal/docs?id=1874110636550082) | Read-only; live fixture may still be required |
| Creative Management | GET | `/discovery/cml/trending_list/` | `TIKTOK_ADS_DISCOVERY_CML_TRENDING_LIST` | `6` | [doc 1825119063013505](https://business-api.tiktok.com/portal/docs?id=1825119063013505) | Read-only; live fixture may still be required |
| Creative Management | GET | `/discovery/cml/video_list/` | `TIKTOK_ADS_DISCOVERY_CML_VIDEO_LIST` | `6` | [doc 1825119068941314](https://business-api.tiktok.com/portal/docs?id=1825119068941314) | Read-only; live fixture may still be required |
| Creative Management | GET | `/discovery/trending/search/` | `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH` | `6` | [doc 1832798345014338](https://business-api.tiktok.com/portal/docs?id=1832798345014338) | Read-only; live fixture may still be required |
| Creative Management | GET | `/discovery/trending/search/keyword/` | `TIKTOK_ADS_DISCOVERY_TRENDING_SEARCH_KEYWORD` | `6` | [doc 1832798361818114](https://business-api.tiktok.com/portal/docs?id=1832798361818114) | Read-only; live fixture may still be required |
| Creative Management | GET | `/file/name/check/` | `TIKTOK_ADS_FILE_NAME_CHECK` | `6` | [doc 1759130033155073](https://business-api.tiktok.com/portal/docs?id=1759130033155073) | Read-only; live fixture may still be required |
| Creative Management | POST | `/smart_plus/ad/preview/` | `TIKTOK_ADS_SMART_PLUS_AD_PREVIEW` | `6` | [doc 1843317445798914](https://business-api.tiktok.com/portal/docs?id=1843317445798914) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | POST | `/video/fix/task/create/` | `TIKTOK_ADS_VIDEO_FIX_TASK_CREATE` | `6` | [doc 1741468875279361](https://business-api.tiktok.com/portal/docs?id=1741468875279361) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| Creative Management | GET | `/video/fix/task/get/` | `TIKTOK_ADS_VIDEO_FIX_TASK_GET` | `6` | [doc 1741469487859714](https://business-api.tiktok.com/portal/docs?id=1741469487859714) | Read-only; live fixture may still be required |
| DPA Catalog Management | GET | `/catalog/insight/product/get/` | `TIKTOK_ADS_CATALOG_INSIGHT_PRODUCT_GET` | `9` | [doc 1805640886872066](https://business-api.tiktok.com/portal/docs?id=1805640886872066) | Read-only; live fixture may still be required |
| DPA Catalog Management | POST | `/catalog/set/upload/` | `TIKTOK_ADS_CATALOG_SET_UPLOAD` | `9` | [doc 1846770644217858](https://business-api.tiktok.com/portal/docs?id=1846770644217858) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| DPA Catalog Management | POST | `/catalog/video/file/` | `TIKTOK_ADS_CATALOG_VIDEO_FILE` | `9` | [doc 1803655037415489](https://business-api.tiktok.com/portal/docs?id=1803655037415489) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| DPA Catalog Management | GET | `/catalog/video/get/` | `TIKTOK_ADS_CATALOG_VIDEO_GET` | `9` | [doc 1803655082498050](https://business-api.tiktok.com/portal/docs?id=1803655082498050) | Read-only; live fixture may still be required |
| DPA Catalog Management | GET | `/diagnostic/catalog/` | `TIKTOK_ADS_DIAGNOSTIC_CATALOG` | `9` | [doc 1771117232728066](https://business-api.tiktok.com/portal/docs?id=1771117232728066) | Read-only; live fixture may still be required |
| DPA Catalog Management | POST | `/diagnostic/catalog/product/task/create/` | `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_CREATE` | `9` | [doc 1771117279175682](https://business-api.tiktok.com/portal/docs?id=1771117279175682) | POST contract; classify side effects and require the appropriate fixture/cleanup before live certification |
| DPA Catalog Management | GET | `/diagnostic/catalog/product/task/get/` | `TIKTOK_ADS_DIAGNOSTIC_CATALOG_PRODUCT_TASK_GET` | `9` | [doc 1771117294731266](https://business-api.tiktok.com/portal/docs?id=1771117294731266) | Read-only; live fixture may still be required |
| Reporting | GET | `/creative_fatigue/get/` | `TIKTOK_ADS_CREATIVE_FATIGUE_GET` | `4` | [doc 1767568466842626](https://business-api.tiktok.com/portal/docs?id=1767568466842626) | Read-only; live fixture may still be required |
| Reporting | GET | `/report/ad_benchmark/get/` | `TIKTOK_ADS_REPORT_AD_BENCHMARK_GET` | `4` | [doc 1738824501176321](https://business-api.tiktok.com/portal/docs?id=1738824501176321) | Read-only; live fixture may still be required |
| Reporting | GET | `/report/video_performance/get/` | `TIKTOK_ADS_REPORT_VIDEO_PERFORMANCE_GET` | `4` | [doc 1738825259075586](https://business-api.tiktok.com/portal/docs?id=1738825259075586) | Read-only; live fixture may still be required |

## Still blocked: 53 paths

| Category | Selected path | Decision | Current path | Evidence |
|---|---|---|---|---|
| Ad Account Management | `/bc/asset/account/authorization/` | `HUMAN_CONNECTION_FLOW` | `/bc/asset/account/authorization/` | [doc 1846868897541122](https://business-api.tiktok.com/portal/docs?id=1846868897541122) |
| Ad Account Management | `/bc/asset_group/update/` | `PROVIDER_DOC_DEFECT` | `/bc/asset_group/update/` | [doc 1749001662156801](https://business-api.tiktok.com/portal/docs?id=1749001662156801) |
| Ad Account Management | `/bc/child/invite/` | `ABSENT_UNRESOLVED` | `/bc/child/invite/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/child/unbind/` | `ABSENT_UNRESOLVED` | `/bc/child/unbind/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/inspiration_tool/ad_performance/` | `ABSENT_UNRESOLVED` | `/bc/inspiration_tool/ad_performance/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/inspiration_tool/audience_insight/` | `ABSENT_UNRESOLVED` | `/bc/inspiration_tool/audience_insight/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/invoice/billing_report/get/` | `ABSENT_UNRESOLVED` | `/bc/invoice/billing_report/get/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/member/assign/` | `ABSENT_UNRESOLVED` | `/bc/member/assign/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/bc/pixel/get/` | `ABSENT_UNRESOLVED` | `/bc/pixel/get/` | No exact current contract in the 1,200-document tree |
| Ad Account Management | `/oauth2/advertiser/get/` | `AUTH_SECRET_FLOW` | `/oauth2/advertiser/get/` | [doc 1738455508553729](https://business-api.tiktok.com/portal/docs?id=1738455508553729) |
| Ads Management | `/account/optimization/account/` | `ABSENT_UNRESOLVED` | `/account/optimization/account/` | No exact current contract in the 1,200-document tree |
| Ads Management | `/account/optimization/entity/` | `ABSENT_UNRESOLVED` | `/account/optimization/entity/` | No exact current contract in the 1,200-document tree |
| Ads Management | `/campaign/spc/quota/get/` | `DEPRECATED_OR_NOT_V1_3` | `/campaign/spc/quota/get/` | [doc 1831564498409473](https://business-api.tiktok.com/portal/docs?id=1831564498409473) |
| Ads Management | `/gmv_max/creation/custom_anchor_video_list/create/` | `PROVIDER_CONTRACT_CONTRADICTION` | `/gmv_max/creation/custom_anchor_video_list/create/` | [doc 1866513154013585](https://business-api.tiktok.com/portal/docs?id=1866513154013585) |
| Ads Management | `/gmv_max/creation/shop_video/video_anchors/` | `PROVIDER_CONTRACT_CONTRADICTION` | `/gmv_max/creation/shop_video/video_anchors/` | [doc 1866513161692161](https://business-api.tiktok.com/portal/docs?id=1866513161692161) |
| Ads Management | `/gmv_max/custom_anchor_video_list/get/` | `DEPRECATED_OR_NOT_V1_3` | `/gmv_max/custom_anchor_video_list/get/` | [doc 1830215925061633](https://business-api.tiktok.com/portal/docs?id=1830215925061633) |
| Ads Management | `/gmv_max/exclusive_authorization/create/` | `UNSAFE_NO_ROLLBACK` | `/gmv_max/exclusive_authorization/create/` | [doc 1822001200356354](https://business-api.tiktok.com/portal/docs?id=1822001200356354) |
| Ads Management | `/smart_plus/campaign/review/` | `ABSENT_UNRESOLVED` | `/smart_plus/campaign/review/` | No exact current contract in the 1,200-document tree |
| Ads Management | `/smart_plus/mmt/ad/get/` | `ABSENT_UNRESOLVED` | `/smart_plus/mmt/ad/get/` | No exact current contract in the 1,200-document tree |
| Ads Management | `/ttms/account/list/` | `ABSENT_UNRESOLVED` | `/ttms/account/list/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/app_center/advanced_function/check/` | `ABSENT_UNRESOLVED` | `/creative/app_center/advanced_function/check/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/app_center/user/record/` | `ABSENT_UNRESOLVED` | `/creative/app_center/user/record/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/gmv_max/pre_review/task/create/` | `ABSENT_UNRESOLVED` | `/creative/gmv_max/pre_review/task/create/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/gmv_max/pre_review/task/get/` | `ABSENT_UNRESOLVED` | `/creative/gmv_max/pre_review/task/get/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shareable_link/create/` | `ABSENT_UNRESOLVED` | `/creative/shareable_link/create/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shared_folder/advertiser/authorize/` | `ABSENT_UNRESOLVED` | `/creative/shared_folder/advertiser/authorize/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shared_folder/associated_advertiser/` | `ABSENT_UNRESOLVED` | `/creative/shared_folder/associated_advertiser/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shared_folder/create/` | `ABSENT_UNRESOLVED` | `/creative/shared_folder/create/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shared_folder/detail/` | `ABSENT_UNRESOLVED` | `/creative/shared_folder/detail/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/creative/shared_folder/partner/` | `ABSENT_UNRESOLVED` | `/creative/shared_folder/partner/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/cml/list/` | `ABSENT_UNRESOLVED` | `/discovery/cml/list/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/cml/post/list/` | `ABSENT_UNRESOLVED` | `/discovery/cml/post/list/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/hashtag/post/list/` | `ABSENT_UNRESOLVED` | `/discovery/hashtag/post/list/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/search/` | `ABSENT_UNRESOLVED` | `/discovery/search/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/search/recommend/` | `ABSENT_UNRESOLVED` | `/discovery/search/recommend/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/trending/hashtag/detail/get/` | `ABSENT_UNRESOLVED` | `/discovery/trending/hashtag/detail/get/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/discovery/trending/hashtag/list/` | `ABSENT_UNRESOLVED` | `/discovery/trending/hashtag/list/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/file/delete/` | `ABSENT_UNRESOLVED` | `/file/delete/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/file/video/ad/bind/` | `ABSENT_UNRESOLVED` | `/file/video/ad/bind/` | No exact current contract in the 1,200-document tree |
| Creative Management | `/file/video/ad/task/get/` | `ABSENT_UNRESOLVED` | `/file/video/ad/task/get/` | No exact current contract in the 1,200-document tree |
| DPA Catalog Management | `/catalog/template_preview/create/` | `DEPRECATED_OR_NOT_V1_3` | `/catalog/template_preview/create/` | [doc 1740665368159233](https://business-api.tiktok.com/portal/docs?id=1740665368159233) |
| DPA Catalog Management | `/catalog/video_package/audit/` | `ABSENT_UNRESOLVED` | `/catalog/video_package/audit/` | No exact current contract in the 1,200-document tree |
| Measurement | `/app/s2s_deeplink/` | `ABSENT_UNRESOLVED` | `/app/s2s_deeplink/` | No exact current contract in the 1,200-document tree |
| Measurement | `/event/track/` | `SEPARATE_EVENTS_AUTH` | `/event/track/` | [doc 1771101303285761](https://business-api.tiktok.com/portal/docs?id=1771101303285761) |
| Measurement | `/pps/advertiser/event/update/` | `ABSENT_UNRESOLVED` | `/pps/advertiser/event/update/` | No exact current contract in the 1,200-document tree |
| Measurement | `/pps/advertiser/verify/` | `ABSENT_UNRESOLVED` | `/pps/advertiser/verify/` | No exact current contract in the 1,200-document tree |
| Measurement | `/pps/survey/metric/` | `ABSENT_UNRESOLVED` | `/pps/survey/metric/` | No exact current contract in the 1,200-document tree |
| Measurement | `/pps/survey/upload/` | `ABSENT_UNRESOLVED` | `/pps/survey/upload/` | No exact current contract in the 1,200-document tree |
| Reporting | `/gmv_max/video_list/report/get/` | `ABSENT_UNRESOLVED` | `/gmv_max/video_list/report/get/` | No exact current contract in the 1,200-document tree |
| Reporting | `/report/subscription/get/` | `CURRENT_ROUTE_REPLACEMENT` | `/subscription/get/` | [doc 1739093832125442](https://business-api.tiktok.com/portal/docs?id=1739093832125442) |
| Reporting | `/report/subscription/subscribe/` | `CURRENT_ROUTE_REPLACEMENT` | `/subscription/subscribe/` | [doc 1739092028876801](https://business-api.tiktok.com/portal/docs?id=1739092028876801) |
| Reporting | `/report/subscription/unsubscribe/` | `CURRENT_ROUTE_REPLACEMENT` | `/subscription/unsubscribe/` | [doc 1739094758789122](https://business-api.tiktok.com/portal/docs?id=1739094758789122) |
| Reporting | `/report/subscription/update/` | `PERMISSION_ONLY_NO_CONTRACT` | `/subscription/update/` | No exact current contract in the 1,200-document tree |

## Important corrections

- Three selected Reporting Subscription routes are stale. Current docs use `/subscription/subscribe/`, `/subscription/get/`, and `/subscription/unsubscribe/`.
- `/subscription/update/` appears only in the permission table. TikTok publishes no current request/response page.
- `/bc/asset_group/update/` is not in the implementation batch. Its response table exposes only generic `data: object`, and its example is copied from `/bc/invoice/get/`; the endpoint-specific success shape is unknown.
- `/gmv_max/creation/shop_video/video_anchors/` is blocked: the request table says `item_ids`, the curl uses `item_id_list`, and response table object types conflict with array examples.
- `/gmv_max/creation/custom_anchor_video_list/create/` is blocked: the documented `failure_list` and nested child types conflict with the success example.
- `/report/ad_benchmark/get/` remains codeable with a contradiction note: the response table types `list` as an object while the success example is an array, and `metrics.metric_name` represents dynamic metric keys. Model this defensively and test both documented structures.
- The allowlist rejection screenshot is for app `REDACTED_OTHER_APP_ID`, not selected app `REDACTED_SELECTED_APP_ID`. Do not attribute that rejection to the selected app without matching OAuth app evidence.

## Official sources

- [Current API Reference](https://business-api.tiktok.com/portal/docs?id=1735713875563521)
- [Permission scope](https://business-api.tiktok.com/portal/docs?id=1753986142651394)
- Live docs endpoint: `GET /gateway/api/doc/client/node/get/v2/`
- Live tree endpoint: `GET /gateway/api/doc/client/platform/tree/get/`
