---
name: creator-collab-mapping
description: Map a content creator's brand deals, creator-to-creator collaborations, agency/MCN ties and game-publisher programs from public signals (paid-promotion labels, #ad, promo codes, description links, co-appearances, contact emails, SponsorBlock). Use when asked who a YouTuber/influencer works with, what sponsorships or collabs they have, or who manages them.
---

# Creator collaboration mapping

Only public, professional signals. Rate each finding **confirmed** (explicit disclosure),
**likely** (strong indirect signal) or **speculative** (pattern-based guess) — and never present
speculation as fact.

## Signals checklist

| Signal | Where |
|---|---|
| "Includes paid promotion" overlay | YouTube videos (first seconds); creator self-declares |
| Disclosures | #ad, #sponsored, #إعلان, "إعلان مدفوع", "sponsored by", "شكراً لـ" in title/description/pinned comment |
| "Paid partnership with @brand" | Instagram / TikTok post header |
| Promo codes, UTM links, affiliate domains | Descriptions, link-in-bio (amzn.to, bit.ly, impact, partnerize, top-up stores) |
| Sponsor segments | SponsorBlock API `/api/skipSegments?videoID=…&category=sponsor` |
| Publisher programs | "Use code X" (Supercell, Epic, EA), Roblox/Garena/Tencent creator events, early access, partner badges |
| Creator collabs | Guests in titles/thumbnails, @mentions, shared videos, cross-posts → co-appearance graph (count, recency) |
| Agency / MCN | Business email domain, "for business inquiries" links, management credit in bio |
| Recurrence | Same brand ≥3× = ongoing partnership; seasonal spikes (Ramadan, game launches) |

Search in English **and** the creator's language. Useful queries:
`"<name>" اعلان`, `"<name>" كود خصم`, `"<name>" sponsored`, `"<name>" ft`, `"<name>" مع`,
`site:instagram.com "<handle>"`, plus brand-tracker sites (Sponsorship.so, SponsorRadar, Modash).

## Category priors for gaming creators (MENA)
When evidence is thin, name the *plausible* categories as hypotheses, labelled speculative:
mobile games (UA installs), game top-up/gift-card stores (Midasbuy, Razer Gold, Jawaker, SEAGM),
telcos (STC, Zain, Mobily, du, Etisalat/e&), gaming peripherals, snacks/energy drinks,
delivery & fintech apps, Roblox/Minecraft experiences, toy/kids brands if the audience is young.

## Output
1. Brand table: brand · category · platform · date(s) · disclosure type · evidence URL · recurrence · confidence · est. value (from creator-earnings-estimate rates).
2. Creator-collab table: creator · their size · # joint appearances · last seen · relationship (friend group / one-off / network).
3. Agency / MCN / program affiliations with confidence.
4. "Most likely deal profile" paragraph: what kinds of brands realistically pay this creator and why
   (audience age, geography, platform), clearly separating evidence from inference.
