# 19 — Approval Gate Runtime Design

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT

---

## Purpose

This document defines the approval gate in depth: the state machine, allowed and blocked transitions, who controls each transition, and the locks that prevent unsafe actions. It is the authoritative reference for how approval works in FnB OS V1.

---

## State Machine

All content outputs, CRM messages, ads packs, and inbox replies have an `approval_status` field. The state machine below governs all allowed transitions.

```
            [New Output Created]
                    │
                    ▼
                 Draft
                    │
         Agent marks ready
                    │
                    ▼
          Ready for Review
                    │
          ┌─────────┴──────────┐
          │                    │
    Owner approves      Owner flags issue
          │                    │
          ▼                    ▼
       Approved          Needs Revision
          │                    │
    ┌─────┴──────┐       Agent revises
    │            │             │
 Schedule     Publish    Ready for Review
  (future)   (future)    (back to Owner)
                    │
             Owner rejects
                    │
                    ▼
                Rejected
                (terminal)
```

---

## Approval States — Full Definition

| State | Code | Meaning | Who Sets |
|-------|------|---------|---------|
| Draft | `Draft` | Initial output created by agent — not reviewed | Builder agent / n8n workflow |
| Ready for Review | `Ready for Review` | Agent has completed output; ready for Owner | Builder agent / n8n workflow |
| Needs Revision | `Needs Revision` | Owner or Reviewer flagged issues — must be revised | Owner / Codex |
| Approved | `Approved` | Owner has reviewed and approved — safe to proceed | **Owner only** |
| Rejected | `Rejected` | Owner rejected — will not proceed; terminal state | **Owner only** |
| Scheduled | `Scheduled` | Approved and queued for future delivery (future phase) | **Owner only** (requires Approved first) |
| Published | `Published` | Delivered to platform or customer (future phase) | **Owner only** (requires Approved first) |

---

## Allowed Transitions

| From | To | Allowed By | Condition |
|------|-----|-----------|-----------|
| (new) | `Draft` | Builder agent | Output created |
| `Draft` | `Ready for Review` | Builder agent | All required fields complete |
| `Ready for Review` | `Approved` | Owner only | Owner has reviewed |
| `Ready for Review` | `Needs Revision` | Owner / Codex | Issues found |
| `Ready for Review` | `Rejected` | Owner only | Owner rejects |
| `Needs Revision` | `Ready for Review` | Builder agent | After revision complete |
| `Approved` | `Scheduled` | Owner only | Approved first; time set |
| `Approved` | `Published` | Owner only | Approved first; platform ready |
| `Approved` | `Needs Revision` | Owner only | Owner changes mind before publish |
| `Scheduled` | `Published` | Owner only | Delivery time reached; Owner confirms |

---

## Blocked Transitions

| From | To | Blocked Reason |
|------|-----|---------------|
| `Draft` | `Published` | Must be Approved first |
| `Draft` | `Scheduled` | Must be Approved first |
| `Ready for Review` | `Published` | Must be Approved first |
| `Ready for Review` | `Scheduled` | Must be Approved first |
| `Rejected` | any state | Terminal — rejected items cannot be reactivated; new request required |
| any state | `Approved` | Only Owner may set Approved — agents cannot set this |
| `Needs Revision` | `Published` | Must be Approved first |

---

## Owner Approval Requirement

**Only the Owner (Bo Bao) may set `approval_status: Approved`.**

No agent, automation, n8n workflow, or scheduled job may set `approval_status: Approved` on behalf of the Owner. Approval is always a human action.

This rule applies to:
- Content posts (Facebook, Instagram, TikTok, Zalo)
- Creative briefs sent to designers or photographers
- Ads packs before any budget is committed
- CRM messages before any message is sent to a customer
- Inbox replies before any reply is sent to a customer

---

## Manual Review Requirement for CRM and Inbox

**All CRM messages and inbox replies have `human_review_required: true` as a constant (defined in schemas).**

This means:
- CRM messages and inbox replies may never be sent automatically, even if `approval_status: Approved`.
- Owner must read the message, confirm tone and accuracy, then manually trigger sending.
- There is no "auto-send on approval" for CRM or inbox reply types.

This is enforced at the schema level (`schemas/crm-followup.schema.json` and `schemas/comment-inbox-reply.schema.json` use `const: true` for `human_review_required`).

---

## Ads Spend Lock

**No ads budget may be committed until `approval_status: Approved` is set by Owner on the ads pack.**

Additional rules:
- Owner must review the target audience, daily budget, bid strategy, and compliance notes before approving.
- The approval record must log the Owner's confirmation timestamp.
- Any change to an approved ads pack (budget, targeting, creative) resets `approval_status` to `Draft` and requires re-approval.

---

## Publishing Lock

**No content may be published to any platform until `approval_status: Approved` is set by Owner.**

Additional rules:
- The n8n publish node must check `approval_status` before executing any platform API call.
- If `approval_status != Approved`: block immediately, write error log, do not proceed.
- Publishing a rejected item is permanently blocked — a new request is required.

---

## Audit Log Requirement

Every approval state change must produce an audit log entry:

| Event | Required Log Fields |
|-------|-------------------|
| Draft created | log_id, timestamp, agent, output_ref, approval_status: Draft |
| Ready for Review set | log_id, timestamp, agent, output_ref, approval_status: Ready for Review |
| Owner approves | log_id, timestamp, owner, output_ref, approval_status: Approved, decision_note |
| Owner rejects | log_id, timestamp, owner, output_ref, approval_status: Rejected, rejection_reason |
| Needs Revision set | log_id, timestamp, reviewer, output_ref, approval_status: Needs Revision, revision_notes |
| Published | log_id, timestamp, owner, output_ref, approval_status: Published, platform, publish_ref |

Logs are written to `logs/AGENT_ACTIVITY_LOG.md` (build phase) and Google Sheets / Supabase (runtime phase).

---

## Future Approval Channel Ideas

These channels have not been configured. They are design ideas for future phases.

| Channel | How It Works | Prerequisite |
|---------|-------------|-------------|
| Telegram approval | Owner receives draft summary in Telegram; taps `/approve` or `/reject` button; n8n webhook receives decision | Telegram Bot API token; n8n Telegram node configured |
| Google Sheet approval table | n8n writes draft to Google Sheet row; Owner updates `approval_status` column; n8n detects change and routes | Google Sheets credential; approval sheet set up by Owner |
| Supabase approval table | n8n writes draft to Supabase; Owner updates `approval_status` via admin UI or form; n8n webhook on row update | Supabase credential; `approvals` table created; webhook configured |
| Direct Owner command | Owner types approval command in Claude Code or equivalent tool; Builder agent writes log | No infrastructure required; current method |

Phase 7 uses "Direct Owner command" only — the Owner manually reviews files and sets status.

---

_This is a design document only. Implementation begins in Phase 8._
