# SOP — Campaign Intake

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
User or Chief Architect creates a new campaign in Google Sheet `Campaigns` tab.

## Pre-conditions
- Google Sheet is live with correct schema
- BRAIN files are complete
- Phase 1 is complete

## Steps

1. **Campaign row created in Google Sheet**
   - Who: User or Chief Architect
   - Fields: campaign_id, name, start_date, end_date, type, target_segment, offer, status=`new`

2. **n8n detects new campaign** (Phase 3+)
   - Trigger: Google Sheets webhook or scheduled poll
   - Action: Read campaign row

3. **LangGraph routes to Content Agent**
   - Input: campaign data + relevant BRAIN sections
   - Action: Generate content pack

4. **Content Agent generates content pack**
   - Output: `content_pack` JSON, written to Google Drive + Sheets

5. **Design Agent generates design brief**
   - Input: content pack
   - Output: `design_brief` JSON, written to Google Drive

6. **QC Agent reviews both outputs**
   - Input: content pack + design brief
   - Output: QC report, pass/fail

7. **If QC passes → Approval Gate**
   - Action: Telegram message sent to user with preview
   - User replies: ✅ Approve / ❌ Reject / ✏️ Edit

8. **If Approved → Schedule**
   - Action: Post scheduled in content calendar (Google Sheet)
   - Status updated: `approved`

9. **If Rejected → Regenerate**
   - Action: User feedback sent back to Content Agent
   - Loop back to Step 4 (max 3 retries)

## Output
- Content pack JSON in Google Drive
- Design brief JSON in Google Drive
- Campaign status updated in Google Sheet
- Approval logged in `09_LOGS/approval_log_template.md`

## Failure Handling
| Failure | Action |
|---------|--------|
| QC fails | Regenerate with updated instructions (max 3 times) |
| Telegram not responding | Log and email fallback (if configured) |
| Google Sheets write error | Retry 3x, then log error and alert |

## Approval Gate
Telegram message with content preview.
User must approve before any scheduling or posting.
