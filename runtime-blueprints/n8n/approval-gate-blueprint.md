# Approval Gate — n8n Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT — Not implemented. No workflow JSON. No execution.

---

## Purpose

Define the approval gate that all content, ads, CRM messages, and inbox replies must pass before any publishing, sending, or spending action. This gate enforces Owner control over every output that reaches customers or incurs cost.

This blueprint does NOT create any executable workflow. No n8n JSON is included. All channels are placeholders.

**Phase 7 Rule: No auto-publish. No auto-send. No auto-spend. All actions require Owner approval.**

---

## Allowed Approval States

All output items must use these approval states. Defined in `schemas/approval-status.schema.json`.

| State | Meaning | Who Sets |
|-------|---------|---------|
| `Draft` | Initial output — not reviewed | Builder agent |
| `Ready for Review` | Agent has completed output; ready for Owner review | Builder agent |
| `Needs Revision` | Owner or Reviewer has flagged issues | Owner / Codex |
| `Approved` | Owner has reviewed and approved | Owner only |
| `Rejected` | Owner has rejected — will not proceed | Owner only |
| `Scheduled` | Approved and scheduled for future delivery | Owner only (requires Approved first) |
| `Published` | Delivered to platform or customer | Owner only (requires Approved first) |

---

## Approval Rules

| Rule | Detail |
|------|--------|
| Published requires Approved | An item may not be set to `Published` unless it was first set to `Approved` by Owner |
| Scheduled requires Approved | An item may not be scheduled unless it was first `Approved` by Owner |
| Ads spend requires Approved | No ads budget may be committed unless the ads pack has `approval_status: Approved` |
| Real customer reply requires Approved | No CRM message or inbox reply may be sent to a real customer without Owner approval |
| Approval set by Owner only | Only the Owner (Bo Bao) may set `approval_status: Approved` |
| Draft → Ready for Review is agent action | Agents may move items from `Draft` to `Ready for Review` |
| Rejection is final | `Rejected` items require a new request to restart the workflow |

---

## Future Approval Channels

These channels will be implemented in a future phase. All are placeholders in Phase 7.

| Channel | Method | Notes |
|---------|--------|-------|
| Telegram approval | Owner receives approval message via Telegram Bot; replies with `/approve` or `/reject` | Requires Telegram Bot API credential (placeholder) |
| Google Sheet approval table | Owner reviews draft row in Google Sheet and sets `approval_status` column | Requires Google Sheets credential (placeholder) |
| Supabase approval table | Owner or admin updates `approval_status` field in Supabase table | Requires Supabase credential (placeholder) |
| Manual Owner review | Owner reads draft in handoff file or direct output; sets status manually | Current Phase 7 method |

---

## Future n8n Node Plan

The following node sequence describes the intended approval gate workflow. Node names and types are illustrative — exact implementation defined in Phase 8.

| Step | Node Type | Node Name | Action |
|------|-----------|-----------|--------|
| 1 | Webhook / Trigger | Receive Draft Item | Receive draft item from content, ads, or CRM workflow |
| 2 | Telegram / HTTP Request | Send Approval Message | Send draft summary to Owner via Telegram or Google Sheet row |
| 3 | Wait | Wait for Owner Decision | Pause workflow until Owner responds (timeout configurable) |
| 4 | Switch / If | Route by Decision | Check Owner response: Approved / Rejected / Needs Revision |
| 5 | Set | Update approval_status | Set `approval_status` to Owner's decision |
| 6 | Function / Code | Write Approval Log | Write structured log entry with decision, timestamp, owner_action |
| 7 | Switch | Route Next Step | Route to: publish workflow (if Approved), revision queue (if Needs Revision), archive (if Rejected) |

---

## Phase 7 Constraint

**Phase 7 does not implement any approval channel or workflow.**

In Phase 7:
- Approval is manual — Owner reviews files in repo handoff or output.
- `approval_status` is set manually in output files.
- No n8n approval workflow is active.
- No Telegram Bot is connected.
- No Google Sheet approval table is live.

This blueprint defines the future design only.

---

## Failure Handling

| Failure | Required Behavior |
|---------|------------------|
| Owner does not respond within timeout | Stop workflow; write timeout log; notify Owner via secondary channel |
| Approval message delivery fails | Stop workflow; write error log; do not proceed to publish |
| Invalid approval state returned | Stop workflow; write error log; request Owner to resubmit decision |
| Publishing attempted without Approved status | Block action immediately; write error log; set `owner_action_required: true` |

See `runtime-blueprints/n8n/error-handling-blueprint.md` for full error handling design.

---

## Done Criteria

This blueprint is complete when:

- [ ] All 7 approval states are defined with who sets each
- [ ] All approval rules are documented
- [ ] All future approval channels are listed with method and credential note
- [ ] n8n node plan covers receive, send, wait, route, log steps
- [ ] Phase 7 no-auto-publish constraint is explicitly stated
- [ ] All failure cases have required behavior defined
- [ ] No real n8n JSON created
- [ ] No credentials stored
- [ ] No publishing action described as executable in Phase 7

---

_This is a design document only. Implementation in Phase 8._
