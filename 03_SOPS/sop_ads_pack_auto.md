# SOP — Automated Ads Pack Generation

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
Campaign with `type: ads` created in Google Sheet, or manual request.

## Pre-conditions
- Campaign brief with offer, target segment, platform, objective
- Ads Brain loaded

## Steps

1. **Read campaign brief**
   - Source: Google Sheet `Campaigns` tab

2. **Load ads context**
   - Load: ads_brain.md, offer_brain.md, customer_brain.md

3. **Ads Agent generates pack**
   - Output: headline, body copy, CTA, audience brief, creative direction
   - Schema: `05_SCHEMAS/ads_pack_schema.json`

4. **Write output**
   - Google Drive: `/Ads Packs/[YYYY-MM]/[id].json`
   - Google Sheet: `Ads Packs` tab

5. **QC review**
   - Check: character limits, no invented claims, budget is placeholder
   - Pass: 0.80 overall, safety rules 1.00

6. **Approval Gate (Telegram)**
   - Send ads pack summary
   - User approves → status: `approved`, ready for human upload to Ads Manager

## Critical Notes
- NEVER automatically activate ads campaigns
- Budget values in all outputs are PLACEHOLDERS only
- Human must manually upload to Facebook/TikTok Ads Manager until Phase 5+

## Output
- Ads pack JSON in Google Drive
- Row in Google Sheet `Ads Packs`
- Status: `approved` (ready for manual upload)
