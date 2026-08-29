# TikTok Ads US runtime eligibility

Date: `2026-08-30`
Mercury PR: `#26271` at `9f35c86a6ec3d56fe442046282803b79206f97a5`
Reference set: 63 implementation candidates from the gated-doc contract pack.
Method: official TikTok endpoint pages and official product availability/help pages. No US live provider calls ran.

## Verdict

The Singapore connection unlocked the developer documentation. It did not make the APIs Singapore-only.

| US status | Actions | Meaning |
|---|---:|---|
| Explicit US support, no special product gate | 9 | Official docs include US for the endpoint/product flow |
| Product or allowlist gated | 22 | 21 have positive US product evidence; Creative Fatigue is allowlist-only and region-silent |
| Unconfirmed general | 31 | Full endpoint contract and no US exclusion, but no endpoint-level US availability statement |
| Special-region workflow | 1 | UnionPay business-license check is a Chinese-Mainland workflow |
| Explicit US exclusion | 0 | No audited action explicitly excludes US |

Strong official US product evidence exists for 30 actions. Thirty-two remain region-silent, including Creative Fatigue, and need a US advertiser probe. UnionPay is not a useful normal US workflow.

## Explicit US support: 9

- `/bc/oa/create/`
- `/business/spark_ad/create/`
- `/creative/pre_review/task/create/`
- `/creative/pre_review/task/get/`
- `/discovery/cml/trending_list/`
- `/discovery/cml/video_list/`
- `/search_ad/negative_keyword/add/`
- `/search_ad/negative_keyword/delete/`
- `/search_ad/negative_keyword/get/`

## US-supported product, but gated: 21

### GMV Max: 14

- `/campaign/gmv_max/creative/update/`
- `/campaign/gmv_max/session/create/`
- `/campaign/gmv_max/session/delete/`
- `/campaign/gmv_max/session/get/`
- `/campaign/gmv_max/session/list/`
- `/campaign/gmv_max/session/update/`
- `/gmv_max/creation/custom_anchor_video_list/delete/`
- `/gmv_max/creation/custom_anchor_video_list/get/`
- `/gmv_max/exclusive_authorization/get/`
- `/gmv_max/identity/get/`
- `/gmv_max/occupied_custom_shop_ads/list/`
- `/gmv_max/store/list/`
- `/gmv_max/store/shop_ad_usage_check/`
- `/gmv_max/video/get/`

Requires a US TikTok Shop, authorized Business Center, advertiser, TikTok identity, Shop permissions, and GMV Max authorization.

### Showcase: 3

- `/showcase/identity/get/`
- `/showcase/product/get/`
- `/showcase/region/get/`

Requires a US-supported Shop/Showcase identity and eligible products.

### Upgraded Smart+: 4

- `/smart_plus/adgroup/budget/update/`
- `/smart_plus/campaign/copy/task/check/`
- `/smart_plus/campaign/copy/task/create/`
- `/smart_plus/ad/preview/`

US is supported at product level. Campaign objective, account eligibility, and feature allowlists still apply.

## Allowlist-only and region-silent: 1

- `/creative_fatigue/get/`

The endpoint page requires Creative Fatigue allowlisting and delivered-ad history. It does not publish a US availability statement.

## Unconfirmed general: 31

- `/asset/bind/quota/`
- `/bc/account/cost/get/`
- `/bc/advertiser/attribute/`
- `/bc/advertiser/disable/`
- `/bc/advertiser/qualification/get/`
- `/bc/asset/advertiser/assign/`
- `/bc/asset/advertiser/assigned/`
- `/bc/asset/advertiser/unassign/`
- `/report/bid_protection/detail/get/`
- `/report/bid_protection/status/get/`
- `/campaign/quota/info/`
- `/campaign_label/get/`
- `/changelog/get/`
- `/changelog/task/download/`
- `/creative/asset/delete/`
- `/creative/auto_message/create/`
- `/creative/auto_message/get/`
- `/discovery/trending/search/`
- `/discovery/trending/search/keyword/`
- `/file/name/check/`
- `/video/fix/task/create/`
- `/video/fix/task/get/`
- `/catalog/insight/product/get/`
- `/catalog/set/upload/`
- `/catalog/video/file/`
- `/catalog/video/get/`
- `/diagnostic/catalog/`
- `/diagnostic/catalog/product/task/create/`
- `/diagnostic/catalog/product/task/get/`
- `/report/ad_benchmark/get/`
- `/report/video_performance/get/`

These are not US failures. Official pages are silent on endpoint-level market availability. A US OAuth connection and provider fixtures are required for certification.

## Special-region workflow: 1

- `/bc/advertiser/unionpay_info/check/`

TikTok documents this for specified business-license types registered in the Chinese Mainland. Do not position it as a normal US customer action without a live US response proving useful behavior.

## Runtime boundary

- Docs portal geography affects developer access to documentation.
- OAuth authorization depends on the customer's TikTok account and developer app.
- Tool execution originates from Composio infrastructure, not from the customer's browser IP.
- Provider results depend on advertiser registration market, TikTok Shop/Business Center relationships, product eligibility, app permissions, feature allowlists, and fixtures.

## Official sources

- [GMV Max US availability and prerequisites](https://ads.tiktok.com/resources/help/article/troubleshoot-account-settings-for-gmv-max-in-tiktok-ads-manager)
- [GMV Max authorization requirements](https://ads.tiktok.com/help/article/how-to-request-gmv-max-authorization-for-tiktok-accounts?lang=en)
- [TikTok Shop and Showcase markets](https://ads.tiktok.com/help/article/tiktok-shopping-and-showcase?lang=en)
- [TikTok Shop Ads markets](https://ads.tiktok.com/help/article/how-to-create-product-shopping-ads?lang=en)
- [Business verification includes US](https://ads.tiktok.com/help/article/about-business-registration?lang=en)
- [Business Account entitlements](https://ads.tiktok.com/help/article/about-tiktok-account-entitlements?lang=en)
- [Current API Reference](https://business-api.tiktok.com/portal/docs?id=1735713875563521)

## One test that settles the remaining uncertainty

Use an approved US advertiser connection. Run all safe GET actions with real US Business Center, Shop, Showcase, campaign, creative, catalog, and reporting fixtures. Record provider success, allowlist denial, eligibility denial, and empty-but-valid responses separately. Do not run destructive POST actions without exact cleanup.
