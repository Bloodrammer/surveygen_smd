---
name: creator-earnings-estimate
description: Estimate a content creator's income from public data, with conservative / realistic / optimistic scenarios broken down by revenue source (YouTube ads long-form vs Shorts, sponsorships, Instagram/TikTok deals, fan funding, creator codes, merch) and deductions (MCN cut, withholding tax). Use when asked how much a YouTuber/influencer earns or is worth. Includes 2025–26 RPM and rate-card benchmarks incl. MENA/Arabic markets.
---

# Creator earnings estimate

Inputs come from **creator-social-audit** (views by format, geography, kid share) and
**creator-collab-mapping** (deal frequency, codes, agency). Show every assumption; give ranges,
never a single number. Third-party "estimated earnings" (Social Blade, vidIQ) ignore format mix,
geography and sponsorships — cite them only as a cross-check.

## Formula

```
Monthly gross = Σ_format (monthly views_format × RPM_format / 1000)
              + sponsorships + fan funding + codes/affiliate/merch + other platforms
Net           = gross − MCN/agency cut − withholding tax
```
RPM already includes YouTube's cut (creator keeps 55% long-form, 45% of Shorts pool) and
unmonetized views (~53% of views monetized on median) — **don't apply those twice**.

## YouTube ad RPM benchmarks (creator RPM, USD per 1,000 views)

| Audience | Long-form | Shorts |
|---|---|---|
| Gaming, global/US-mixed | 1.0–3.5 (median ~2) | 0.02–0.10 |
| UAE / Kuwait / Qatar heavy | 3–8 (Qatar to 12) | 0.05–0.15 |
| Saudi heavy | 0.7–3 (measured creator data lower than blog CPM lists) | 0.02–0.08 |
| Egypt / Iraq / Maghreb heavy | 0.2–2 | ≤0.03 |
| **Arabic gaming scenario** | Cons 0.40 · Real 0.8–1.5 · Opt 2.5–3.5 | Cons 0.01 · Real 0.03 · Opt 0.08 |

- Shorts RPM ≈ 3–14% of the same channel's long-form RPM.
- **Made for Kids**: no personalized ads → multiply RPM by 0.2–0.4 for MFK share of views.
- Shorts with music: 1 track halves that Short's revenue pool share.

## Sponsorship benchmarks

- YouTube integration: price = median views (last 10) × CPM/1000. General CPM $20–50;
  **gaming $5–15**; MENA gaming usually low end. Dedicated video ≈ 2–3× integration.
- Instagram post: mid-tier (50–500K) $1–5K; macro (500K–1M) $5–15K. Reel ≈1.5–2× post; story ≈0.3–0.5×.
- KSA per post: micro SAR 3–15K; macro SAR 15–75K; mega SAR 75–300K+. Snapchat often > IG in KSA.
  Ramadan +20–40%.
- UAE: mega IG AED 15K+, TikTok 20–40% below IG.
- Deal frequency: derive from collab mapping (observed disclosed deals ÷ months). With no evidence,
  Cons 0–1/quarter, Real ~1/month, Opt 2–4/month.

## Other sources
- Memberships / Super Chat / Super Thanks: creator gets 70% of net. Model 5–15% of ad revenue if
  streams often, 0–3% if not.
- Creator codes: Epic Support-A-Creator ~5%; Supercell ~5% (unpublished); Roblox — no public YouTuber code rate.
- TikTok Creator Rewards: $0.4–1.0/1K qualified views globally; assume $0.2–0.6 for MENA; only >1-min videos.
- Merch, events, TV/media, game-dev revenue (Roblox DevEx $0.0038/Robux) only if evidenced.

## Deductions
- MCN/agency: 10–30% typical (range 1–50%), often only on some streams.
- US withholding for non-US creators: 30% on **US-viewer** earnings w/o treaty (UAE, KSA, Kuwait,
  Iraq have none); 24% of worldwide if no tax form. For Arabic channels effective ≈1–3% of AdSense.
- Personal income tax: none in GCC (mention local tax only when known).

## Procedure
1. Monthly views by format (from audit; if only total known, estimate Shorts share from upload mix
   and say so). Use last-30-days *and* trailing-12-month average.
2. Pick RPMs per scenario from the audience geography; apply MFK factor.
3. Add sponsorship/IG/TikTok/fan/code revenue per scenario with stated deal counts.
4. Subtract deductions.
5. Output a table: source × {conservative, realistic, optimistic} monthly and annual, plus a
   short "what would move the number" list and a confidence note.
