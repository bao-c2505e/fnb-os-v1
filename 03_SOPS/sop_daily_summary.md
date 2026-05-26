# SOP — Daily Summary Report

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
Scheduled: daily at [FILL: time, e.g., 21:00]

## Pre-conditions
- Google Sheets accessible
- Previous day's data logged

## Steps

1. **Collect execution data**
   - Source: Google Sheet `Execution Log` tab
   - Fields: actions taken, errors, approvals, posts made

2. **Collect content performance** (Phase 6+)
   - Source: Platform APIs or manual entry
   - Fields: reach, engagement, clicks, comments

3. **Collect CRM activity**
   - Source: Google Sheet `CRM Messages Sent`
   - Fields: messages sent, open rate (if available)

4. **Generate daily summary**
   - Agent: Summary Agent (can be Claude or GPT-4o)
   - Output: structured summary JSON + human-readable text

5. **Send to Telegram**
   - Format: daily digest message
   - Include: highlights, errors, pending approvals, next day preview

## Summary Message Format

```
📊 Vị Cuốn Daily Summary — [DATE]

✅ Completed today:
- [N] content packs generated
- [N] posts approved
- [N] CRM messages sent
- [N] comments replied

⚠️ Issues:
- [list any errors or pending items]

📅 Tomorrow:
- [N] posts scheduled
- [list upcoming campaigns]

Full log: [Google Sheet link]
```

## Output
- Summary message sent to Telegram
- Summary row written to Google Sheet `Daily Summaries` tab
