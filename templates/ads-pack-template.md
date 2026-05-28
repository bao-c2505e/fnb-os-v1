# Ads Pack Template

**Schema:** `schemas/ads-pack.schema.json`
**Agent:** Ads Pack Agent (AGT-Ads)
**SOP:** `module-sops/ads-pack-auto-sop.md`

---

## ads_pack_id
[AUTO_GENERATED — Format: AP-[BRAND]-[YYYYMMDD]-[NNN] — e.g., AP-VQ-20260528-001]

## brand_id
[TO_FILL — Default: VQ for Vị Cuốn. Replace for other brands.]

## brand_name
[TO_FILL — Default: Vị Cuốn. Replace for other brands.]

## campaign_objective
[TO_FILL — Select one: Awareness | Traffic | Engagement | Lead Generation | Conversion | Retargeting]

## platform
[TO_FILL — Select one: Facebook Ads | TikTok Ads | Instagram Ads | Multi-Platform]

## funnel_stage
[TO_FILL — Select one: Top of Funnel (TOF) | Middle of Funnel (MOF) | Bottom of Funnel (BOF)]

## target_audience
[TO_FILL — Audience description. Must NOT contain PII. — e.g., "Office workers in Vinh, 22–40, interested in Vietnamese food and lunch delivery"]

## angle
[TO_FILL — Creative angle and positioning hook — e.g., "Fresh rolls, ready in 5 minutes — lunchtime solved."]

## primary_text
[TO_FILL — Main ad body copy. Brand voice. No fake scarcity, no unverified health claims.]

## headline
[TO_FILL — Short headline shown in the ad unit — e.g., "Bữa trưa tươi ngon — Giao nhanh tận nơi"]

## description
[TO_FILL or null — Optional short description line below headline. Set to null if not needed.]

## cta
[TO_FILL — Select one: Learn More | Order Now | Shop Now | Contact Us | See Menu | Get Offer | Sign Up]

## creative_brief_ref
[TO_FILL or null — Reference to creative brief ID for the visual asset — e.g., CB-VQ-20260528-001. Set to null if no brief yet.]

## offer
[OWNER_TO_PROVIDE_OFFER — Do not hardcode prices or discounts. Leave as [OWNER_TO_PROVIDE_OFFER] until Owner confirms.]

## compliance_notes
[TO_FILL — Note any compliance risks or confirm "No compliance risks detected." Required field. Examples:
- No health claims included
- No fake scarcity language
- Pricing not hardcoded — pending Owner confirmation
- Ad complies with Facebook/TikTok advertising policies]

## approval_status
Draft

## created_by_agent
Ads Pack Agent (AGT-Ads)

## created_at
[AUTO_GENERATED — ISO 8601 datetime — e.g., 2026-05-28T09:00:00+07:00]

## notes
[TO_FILL or null — Optional notes for Owner or Reviewer. Include any pending inputs or escalation flags.]

---

> **WARNING:** This ads pack is a DRAFT. No ad campaign may be launched and no budget may be spent until `approval_status` is set to `Approved` by Owner.
