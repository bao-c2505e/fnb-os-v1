# SOP — Telegram Approval Gate

**Version:** v0.1.0
**Status:** DRAFT

---

## Purpose
Every significant automated output requires human approval before action.
The Telegram bot is the approval interface.

## Trigger
Any agent output that requires approval (content, design, ads, CRM batch, escalation).

## Approval Message Format

```
🤖 FnB OS — Approval Required

Type: [Content Pack | Design Brief | Ads Pack | CRM Batch | Escalation]
Campaign: [campaign_id or description]
Generated: [datetime]

Preview:
[2–3 line summary of the output]

Actions:
✅ /approve_[id]
❌ /reject_[id]
✏️ /edit_[id] [your notes]
```

## Response Handling

| Response | Action |
|----------|--------|
| `/approve_[id]` | Mark status: `approved`, proceed to next step |
| `/reject_[id]` | Mark status: `rejected`, regenerate or discard |
| `/edit_[id] [notes]` | Send notes back to generating agent, regenerate |
| No response in 24h | Escalate with reminder, mark as `pending_timeout` |

## Escalation Approval Format

```
🚨 ESCALATION — Human Action Required

Source: [platform] — [commenter_name]
Comment: "[comment_text]"
Reason: [escalation_reason]
Time: [timestamp]

This requires a HUMAN response. Do NOT auto-reply.

Reply here with your response text or /skip_[id] to ignore.
```

## SLA
- Standard approvals: 24-hour response window
- Escalations: 30-minute response window during operating hours
- Off-hours escalations: Flagged for next available human

## Rules
- Only one approval message per output (no duplicates)
- Approval IDs are unique and traceable to agent output
- All approval decisions logged in `09_LOGS/approval_log_template.md`
