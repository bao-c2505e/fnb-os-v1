# SOP — Automated Design Brief Generation

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
Content pack approved OR design brief requested for campaign.

## Steps

1. **Read content pack**
   - Source: Google Drive `/Content Packs/[YYYY-MM]/[id].json`
   - Fields: campaign_id, dish_name, caption_line, mood, platform

2. **Load design context**
   - Load: design_brain.md (colors, fonts, formats)

3. **Design Agent generates brief**
   - Input: content pack + design context
   - Output: design_brief JSON per `05_SCHEMAS/design_brief_schema.json`

4. **Write output**
   - Google Drive: `/Design Briefs/[YYYY-MM]/[id].json`
   - Google Sheet: `Design Briefs` tab, row added

5. **QC Agent reviews brief**
   - Check: dimensions correct, brand colors referenced, AI prompt self-contained
   - Pass threshold: 0.80

6. **Approval Gate (Telegram)**
   - Send brief summary to user
   - User approves → status: `approved`, brief sent to designer/AI tool

## Output
- `design_brief_schema.json` in Google Drive
- Row in Google Sheet `Design Briefs`
