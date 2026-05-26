# SOP — Automated Content Generation

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
- Scheduled: daily at [FILL: time] for next-day content
- Manual: campaign intake triggers content generation
- On-demand: user requests content for specific dish/date

## Pre-conditions
- Campaign data available in Google Sheet
- BRAIN files complete and up-to-date
- Content Agent prompt loaded

## Steps

1. **Read campaign data**
   - Source: Google Sheet `Campaigns` tab
   - Fields: campaign_id, dish_name, content_pillar, platform, target_segment, offer

2. **Load BRAIN context**
   - Load: brand_brain.md, menu_brain.md, content_brain.md, offer_brain.md

3. **Generate caption (Content Agent)**
   - Input: campaign brief + BRAIN context
   - Output: caption_vi, hashtags, cta, post_time_suggestion

4. **Generate image brief (Content Agent)**
   - Input: dish_name, platform, mood
   - Output: image_brief string

5. **Compile content pack**
   - Output: content_pack JSON per schema `05_SCHEMAS/content_pack_schema.json`
   - Write to: Google Drive `/Content Packs/[YYYY-MM]/`
   - Write row to: Google Sheet `Content Packs` tab

6. **QC Agent reviews content pack**
   - Score: brand voice, grammar, safety, schema
   - If score ≥ 0.80 → proceed to approval
   - If score < 0.80 → regenerate (max 3 retries)

7. **Approval Gate (Telegram)**
   - Send: caption preview + image brief summary
   - Wait for user response

8. **Post approved → Schedule**
   - Write scheduled datetime to Google Sheet
   - Status: `scheduled`

## Output
- `content_pack_schema.json` in Google Drive
- Row in Google Sheet `Content Packs`
- Approval log entry

## Notes
- Do NOT post content without approval
- If 3 QC retries fail, escalate to user with error details
- All generated content is DRAFT until approved
