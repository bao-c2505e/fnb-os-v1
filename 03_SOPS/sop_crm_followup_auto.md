# SOP — Automated CRM Follow-up

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
- Scheduled: daily at [FILL: time], check for customers due for follow-up
- Event-based: new order completed → post-order sequence starts

## Pre-conditions
- Google Sheet `CRM` tab populated with customer data
- CRM Brain loaded
- Customer consent confirmed (Zalo OA follow or explicit opt-in)

## Steps

1. **Read CRM data**
   - Source: Google Sheet `CRM` tab
   - Filter: customers due for follow-up based on lifecycle stage and last contact date

2. **Segment customers**
   - Apply rules from `01_BRAIN/crm_brain.md`
   - Group by: new, active, at_risk, lapsed, vip

3. **CRM Agent generates messages**
   - For each customer: generate personalized message
   - Schema: `05_SCHEMAS/crm_followup_schema.json`
   - Include any relevant offer from offer_brain.md

4. **QC review**
   - Check: personalization present, no promises not in brief, consent confirmed
   - Any complaint history → `requires_human_review: true`

5. **Batch approval (Telegram)**
   - Send summary: "N follow-up messages ready. [Preview 3 samples]. Approve all / Review individually?"
   - User approves batch or reviews one-by-one

6. **Send approved messages**
   - Channel: Zalo OA API (Phase 6+)
   - Log: Google Sheet `CRM Messages Sent` tab
   - Update last_contact_date in CRM

## Failure Handling
| Failure | Action |
|---------|--------|
| Zalo API error | Log, retry once, then alert user |
| Customer opt-out detected | Remove from queue, update do_not_contact flag |
| Missing customer data | Skip, log in ERROR_LOG.md |

## Output
- CRM messages sent (Phase 6+)
- Draft messages in Google Sheet (Phase 0–5)
- Send log in Google Sheet
