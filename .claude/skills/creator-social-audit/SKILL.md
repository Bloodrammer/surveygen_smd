---
name: creator-social-audit
description: Audit a content creator's public YouTube / Instagram / TikTok presence — size, growth, performance, engagement, content pillars, audience quality and bot red flags — and produce a benchmarked scorecard. Use when asked to analyze, audit, vet or benchmark an influencer/YouTuber/streamer's socials. Pairs with creator-earnings-estimate and creator-collab-mapping.
---

# Creator social audit

Business audit of a **public creator's professional output**. Stay on content, metrics and
commercial activity — never dig into private life, family, addresses or non-public accounts.

## 0. Data collection (do this first, in parallel)

Sources in order of preference (fall back if the network blocks a host — don't spoof user
agents or bypass bot checks; use WebSearch snippets instead and say so):

| Need | Source |
|---|---|
| Subs / views / video count, daily history | Social Blade, vidIQ stats page, Playboard, NoxInfluencer |
| Video list, titles, dates, views, "Includes paid promotion" | YouTube channel /videos, /shorts, /streams tabs |
| IG / TikTok followers, ER, audience geo, fake % | HypeAuditor, Modash free checker, Favikon, the profile itself |
| Cross-platform handles | Channel "About" links, IG bio / link-in-bio |

Field notes (learned the hard way):
- The YouTube **About** dialog ("…and N more links") gives the registered **country**, exact views,
  video count, join date and all cross-platform links — read it before guessing nationality from dialect.
- To get the Shorts vs long-form split, scroll the /shorts tab in a headless browser and sum the per-Short
  view counts; compare with lifetime views. Check /videos and /streams tabs too.
- YouTube rate-limits after ~100 page loads (redirect to google.com/sorry). Stop when that happens —
  don't rotate user agents or otherwise evade it. Batch what you need into few requests.
- Links on the channel can be dead (renamed second channels) — verify each one.

Search in **the creator's language too** (e.g. Arabic name spellings: جود قيمر / جيمر).
Similarly-named channels are common — verify every number belongs to the exact handle/channel ID.
Label every fact **verified / inferred / uncertain** with its source URL.

## 1. Profile & identity
Handles on every platform, verification, channel creation date, country/language/dialect,
business-contact email domain (gmail vs. agency domain → feeds collab mapping).

## 2. Size & growth
- Current subs/followers, total views, videos.
- 30-day, 90-day, 12-month gains; lifetime views ÷ channel age = average monthly views.
- Flag anomalies: staircase jumps with no viral video, sudden drops (purges).

## 3. Performance (always medians, never means)
- Median views of last 10–20 uploads **per format** (long-form, Shorts, live, Reels, TikTok).
- Shorts vs long-form share of monthly views (critical for revenue — Shorts RPM is 3–14% of long-form).
- **Reach ratio** = median long-form views ÷ subs. <2% red flag; 5–30% normal long-form.
- Upload cadence and consistency.

## 4. Engagement
- ER by views = (likes + comments [+shares]) ÷ views ×100 — use for YouTube/TikTok/Reels.
- ER by followers = (likes + comments) ÷ followers ×100 — Instagram when views hidden.

Consensus healthy ranges (2025–26; sources disagree 2–3×):
| Platform | Healthy | Notes |
|---|---|---|
| Instagram (by followers) | 1–3% | falls with size; >6% at macro tier is suspicious |
| TikTok (by views) | 4–10% | |
| YouTube (by views) | 2–5% | long-form median ~3.5%, Shorts ~2.7% |

## 5. Content pillars
Tag recent uploads by theme (game title, format: challenge/reaction/let's-play/short),
compute share of output and median views per pillar → what drives the channel.

## 6. Audience quality & brand safety
- Geography vs. content language (Arabic content with large South/Southeast-Asia share = suspicious).
- Age skew: kid-heavy audience / "Made for Kids" flags → slashes RPM, limits brand categories.
- Bot red flags: generic/emoji-only comments, flat engagement across posts, odd like:comment
  ratio, very low ER, high following count on IG, follower-shop accounts.
- Controversies, content-safety issues.

## 7. Output
1. One-paragraph summary.
2. Metrics table with benchmark verdict per metric (below / at / above tier norm).
3. Content-pillar table.
4. Audience-quality & risk notes.
5. Data gaps + confidence level; full source list.
Hand the numbers to **creator-earnings-estimate** and the commercial signals to **creator-collab-mapping**.
