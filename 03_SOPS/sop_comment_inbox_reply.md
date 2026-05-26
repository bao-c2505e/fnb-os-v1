# SOP — Comment & Inbox Auto-Reply

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
New comment on Facebook/TikTok/Instagram post, or new inbox message.

## Pre-conditions
- Platform webhook/API connected to n8n
- Comment Reply Brain loaded
- Reply Agent prompt loaded

## Steps

1. **Receive comment/message**
   - Source: Platform webhook → n8n
   - Data: comment_id, platform, text, commenter_name, post_context

2. **Reply Agent classifies comment**
   - Category: location, price, compliment, complaint, delivery, tag_friend, other
   - Sentiment: positive, neutral, negative
   - Escalation check: food safety, refunds, aggressive language

3. **If escalation_flag = true**
   - Action: Alert human via Telegram immediately
   - Do NOT generate auto-reply
   - Log in `06_HANDOFF/ERROR_LOG.md`

4. **If escalation_flag = false**
   - Generate reply_vi
   - QC Agent quick-check (auto_post_safe flag)

5. **If auto_post_safe = true AND confidence ≥ 0.85**
   - Post reply via platform API
   - Log in Google Sheet `Comment Replies` tab

6. **If auto_post_safe = false OR confidence < 0.85**
   - Send to Telegram for human review
   - Human approves or edits, then posts

7. **Log all replies**
   - Google Sheet `Comment Replies`: comment_id, reply, status, posted_at

## Failure Handling
| Failure | Action |
|---------|--------|
| Platform API error | Log, retry once, alert user |
| Sentiment detection fails | Default to `requires_human_review: true` |
| Reply queue > 50 unprocessed | Alert user, pause auto-reply |

## Output
- Reply posted to platform (auto or human-approved)
- Log row in Google Sheet
- Escalations flagged in Telegram
