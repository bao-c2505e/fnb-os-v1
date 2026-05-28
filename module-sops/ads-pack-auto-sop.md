# Ads Pack Auto SOP

**Module:** Ads Pack Auto
**Agent:** Ads Pack Agent (AGT-Ads)
**Schema:** `schemas/ads-pack.schema.json`
**Template:** `templates/ads-pack-template.md`
**Brand Reference:** `brand-brain/vi-cuon.md`

---

## Purpose

Guide the Ads Pack Agent to draft ad angles, ad copy, headlines, CTAs, and campaign notes for Facebook Ads, TikTok Ads, or Instagram Ads. No ad is launched and no budget is spent without Owner approval. Phase 4 produces drafts only.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Brand Brain | `brand-brain/vi-cuon.md` | Yes |
| Campaign objective | Owner brief or command | Yes |
| Platform | Owner brief | Yes |
| Funnel stage | Owner brief | Yes |
| Target audience description | Owner brief | Yes |
| Offer | Owner-provided or `[OWNER_TO_PROVIDE_OFFER]` | If promotion ad |
| Creative brief ref | Creative Asset Agent output | If visual asset exists |

---

## Process Steps

1. Read `brand-brain/vi-cuon.md` — confirm brand voice, compliance rules, and offer policy.
2. Confirm campaign objective, platform, and funnel stage from the input.
3. Draft ad angle (creative positioning and hook concept).
4. Write primary text (main ad body copy, brand voice).
5. Write headline (short, attention-grabbing).
6. Select CTA from allowed enum: Learn More, Order Now, Shop Now, Contact Us, See Menu, Get Offer, Sign Up.
7. Add compliance notes: flag any health claims, scarcity language, or pricing risks.
8. Insert `[OWNER_TO_PROVIDE_OFFER]` if offer is needed but not yet confirmed.
9. Fill all required fields from `schemas/ads-pack.schema.json`.
10. Set `approval_status: Draft`.
11. Set `created_by_agent: Ads Pack Agent (AGT-Ads)`.
12. Output using `templates/ads-pack-template.md`.

---

## Output Template

`templates/ads-pack-template.md`

---

## Approval Gate

- No ad campaign is launched without `Approved` status.
- No budget is spent at any time — especially not in Phase 4.
- No ad account credentials, campaign IDs, or ad set IDs are stored in output.
- Owner must explicitly set `Approved` and then manually launch in Ads Manager.
- `Published` and `Scheduled` states are defined but require Owner action and Phase 5+ automation.

---

## Logging Requirements

- Add one row to `logs/AGENT_ACTIVITY_LOG.md` per ads pack produced.
- Use `templates/log-entry-template.md` format.

---

## Human Escalation Rules

Stop and escalate to Owner if:
- Offer price, discount, or promotion is required but not confirmed.
- Ad copy includes health claims, awards, or statistics not in Brand Brain.
- Targeting description includes PII or sensitive demographic categories.
- A compliance risk is detected in the requested angle (e.g., "guaranteed results", fake scarcity).
- Creative asset is needed but no approved brief exists.

---

## Done Criteria

- All required schema fields filled.
- `approval_status` is `Draft` or `Ready for Review`.
- `compliance_notes` field is populated (even if just confirming "No compliance risks detected").
- No campaign launched, no budget committed, no ad account accessed.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
