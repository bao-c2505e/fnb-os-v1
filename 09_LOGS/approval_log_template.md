# Approval Log Template

## Format (for Google Sheet `Approvals` tab)

| Field | Value |
|-------|-------|
| approval_id | VQ-APR-[YYYYMMDD]-[SEQ] |
| object_type | content_pack / design_brief / ads_pack / crm_message / comment_reply / escalation |
| object_id | ID of the approved/rejected object |
| preview_text | Short preview sent to Telegram |
| telegram_message_id | Telegram message ID |
| status | pending / approved / rejected / edited / timeout / escalated |
| reviewer | Human username or "System" |
| reviewer_notes | Notes from reviewer |
| created_at | ISO8601 timestamp |
| responded_at | ISO8601 timestamp |

---

## Example Approval Entry

```
approval_id: VQ-APR-20260601-001
object_type: content_pack
object_id: VQ-CP-20260601-001
preview_text: "Caption: Combo Trưa ngon lành... [Facebook post]"
telegram_message_id: 12345
status: approved
reviewer: User
reviewer_notes: 
created_at: 2026-06-01T10:00:00+07:00
responded_at: 2026-06-01T10:15:00+07:00
```

---

## Approval Metrics (Daily Summary)

- Total approval requests sent
- Approved count + percentage
- Rejected count + percentage
- Average response time
- Timeout count
- Escalation count
