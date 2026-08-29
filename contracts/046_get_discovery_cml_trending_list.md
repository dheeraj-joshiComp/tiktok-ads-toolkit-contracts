# TIKTOK_ADS_DISCOVERY_CML_TRENDING_LIST

- Operation: Get popular tracks from the Commercial Music Library
- Wire: `GET /discovery/cml/trending_list/`
- Request encoding: `query string`
- Ability hint: `reads`
- Parent scope: `6`
- Permission evidence: `selected_export_category_plus_first_level_inheritance`
- Selected category: `Creative Management`
- Source: [doc 1825119063013505](https://business-api.tiktok.com/portal/docs?id=1825119063013505)
- Source content SHA-256: `fd021b078d09ea4c05a81fd64f59b01208f0759c602faf5deda715359fdec8dc`
- Product/fixture gate: Provider-eligible advertiser and endpoint-specific IDs from prior read actions
- Live boundary: Read-only call permitted after fixture discovery

## Request contract

| Field path | Placement | Type | Requiredness | Constraints |
|---|---|---|---|---|
| `business_id` | `query` | `string` | `required` | - |
| `genre` | `query` | `string` | `optional` | default: ALL; allowed: ALL, ROCK, POP, LATIN, METAL, ELECTRONIC, HIP_HOP/RAP, ALTERNATIVE/INDIE, FOLK, R&B/SOUL, COUNTRY, CLASSICAL, JAZZ, REGGAE, CHILDHOOD, BLUES, EASY_LISTENING, NEW_AGE, WORLD_MUSIC, EXPERIMENTAL, DEVOTIONAL, CHINESE_TRADITION, 8_BIT, A_CAPPELLA, AFRO-POP, ALTERNATIVE_HIP_HOP, ALTERNATIVE_ROCK, AMBIENT, ARABIC_POP, BASS_HOUSE, BGM, BOOMBAP, BOSSA_NOVA, BRAZILIAN_FUNK_STYLE, BUDDHIST_MUSIC, CANTOPOP, CELTIC_POP, CHAMBER_MUSIC, CHILL_BEATS, CHILLOUT, CHINESE_FOLK, CHINESE_OPERA, CHINESE_POP, CHINESE_STYLE, CHINOISERIE_ELECTRONIC, CHINOISERIE_RAP, CHRISTIAN_MUSIC, CONTEMPORARY_R&B, COUNTRY_POP, DANCE_POP, DISCO, DJ, DRUM&BASS, DUBSTEP, EDM, EDM_TRAP, ELECTRO_POP, EPIC, FOLK_POP, FUNK, FUTURE_BASS, GOSPEL, GUFENG_MUSIC, HARD_ROCK, HIP_HOUSE, HOLIDAY_MUSIC, HOUSE, INDIAN_POP, INDIE_FOLK, INDIE_POP, INDIE_ROCK, INSTRUMENTAL_HIP_HOP, INSTRUMENTAL_ROCK, IRISH_FOLK, J_ROCK, JAPANESE_TRADITIONAL_MUSIC, JAZZ_FUSION, JAZZ_HIP_HOP, JAZZ_POP, J-POP, K-POP, LATIN_POP, LO-FI, MC, NOISE, OLD_SCHOOL, OTHERS, POP_RAP, POP_ROCK, POP_SOUL, PSYCHEDELIC_ROCK, PUNK, R&B_RAP, REGGAETON, RUSSIAN_POP, SERTANEJO, SON_CUBANO, SOUL, SOUNDTRACK, SYMPHONY, SYNTH_POP, TANGO, TECHNO, TEEN_POP, TRADITIONAL_CHINESE_FOLK, TRANCE, TRAP_RAP, TRIP_HOP, TROPICAL_HOUSE, TURKISH_POP |
| `country_code` | `query` | `string` | `optional` | default: US |
| `date_range` | `query` | `string` | `optional` | allowed: 1DAY, 7DAY, 30DAY, 90DAY; default: 7DAY |

## Response contract

Provider response nullability is unspecified. Model documented fields permissively unless live evidence proves otherwise.

| Field path | Type | Constraints and presence rules |
|---|---|---|
| `code` | `number` | - |
| `message` | `string` | - |
| `request_id` | `string` | - |
| `data` | `object` | - |
| `data.list` | `object[]` | - |
| `data.list[].commercial_music_id` | `string` | - |
| `data.list[].commercial_music_name` | `string` | - |
| `data.list[].duration` | `integer` | - |
| `data.list[].thumbnail_url` | `string` | - |
| `data.list[].artist` | `string` | - |
| `data.list[].preview_url` | `string` | - |
| `data.list[].genres` | `string[]` | - |
| `data.list[].rank_position` | `string` | - |
| `data.list[].trending_history` | `object[]` | - |
| `data.list[].trending_history[].date` | `string` | rule: Date, in the format of YYYY-MM-DD |
| `data.list[].trending_history[].rank_position_daily` | `string` | - |
| `data.list[].full_duration_song_clip` | `object` | - |
| `data.list[].full_duration_song_clip.preview_url` | `string` | - |
| `data.list[].full_duration_song_clip.duration` | `integer` | - |
| `data.list[].full_duration_song_clip.song_clip_id` | `string` | - |
| `data.list[].trending_song_clip` | `object` | - |
| `data.list[].trending_song_clip.preview_url` | `string` | - |
| `data.list[].trending_song_clip.duration` | `integer` | - |
| `data.list[].trending_song_clip.song_clip_id` | `string` | - |

## Implementation and test boundary

- Use the existing TikTok declarative action utilities and provider envelope handling.
- Do not add undocumented fields or tighten response nullability.
- Test exact placement/serialization, required and conditional inputs, enums/defaults/limits, nested response shaping, empty data, and provider errors.
- Do not claim live verification without an eligible fixture and cleanup proof.
