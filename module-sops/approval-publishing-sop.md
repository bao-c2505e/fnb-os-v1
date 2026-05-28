# Approval & Publishing SOP

**Module:** Approval & Publishing
**Agent:** Approval Publishing Agent (AGT-Approval)
**Schema:** `schemas/approval-status.schema.json`
**Template:** `templates/approval-status-template.md`

---

## Purpose

Define the approval state machine for all content items, creative briefs, ads packs, CRM sequences, and inbox reply drafts in FnB OS V1. Ensure no item is published, scheduled, sent, or launched without Owner-approved status. No publishing automation runs in Phase 4.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Item ID | Output from any agent | Yes |
| Item type | Output from any agent | Yes |
| Current `approval_status` | Output from any agent | Yes |
| Owner decision | Owner (human only) | Required to advance to Approved |

---

## Process Steps

1. Receive item with `approval_status: Draft` from an agent.
2. Agent self-checks output against its SOP done criteria and schema requirements.
3. If self-check passes: agent advances `approval_status` to `Ready for Review`.
4. Reviewer (Codex or Owner) inspects item:
   - If revision needed: set `Needs Revision`, write `review_notes`.
   - If rejected: set `Rejected`, write `review_notes`.
   - If acceptable: flag to Owner for final decision.
5. Owner reviews item:
   - Owner sets `Approved` (only Owner may do this) and records `approved_at`.
   - Owner sets `Rejected` or `Needs Revision` if not satisfied.
6. After `Approved`:
   - Item may be `Scheduled` — requires non-null `approved_at`.
   - Item may be `Published` — requires non-null `approved_at`.
7. Record every state change in `change_log` array.
8. Output using `templates/approval-status-template.md`.

---

## Output Template

`templates/approval-status-template.md`

---

## Approval Gate — State Machine

| State | Who Can Set | Prerequisite |
|-------|-------------|--------------|
| Draft | Any agent | None |
| Ready for Review | Agent (self-check pass) | Draft |
| Needs Revision | Reviewer or Owner | Ready for Review or Draft |
| Approved | **Owner only** | Ready for Review |
| Rejected | Owner or Reviewer | Any state |
| Scheduled | Agent or system (Phase 5+) | Approved + `approved_at` set |
| Published | Agent or system (Phase 5+) | Approved + `approved_at` set |

**Phase 4 constraint:** `Scheduled` and `Published` states are defined in the schema but no automation executes them in Phase 4. Any scheduling or publishing is manual, performed by Owner.

---

## Logging Requirements

- Every status change must be appended to the `change_log` array in the approval record.
- Add one row to `logs/AGENT_ACTIVITY_LOG.md` per approval decision.
- Use `templates/log-entry-template.md` format.

---

## Human Escalation Rules

- Only Owner may grant `Approved` — no agent may self-approve.
- Any item stuck in `Needs Revision` for more than 2 revision cycles must be escalated to Owner for a final decision.
- `Rejected` items must not be resubmitted without explicit Owner instruction.
- `Scheduled` and `Published` status for ads require Owner to confirm budget allocation separately in Ads Manager.

---

## Done Criteria

- All required approval schema fields filled.
- `change_log` updated for every state transition.
- `Published` and `Scheduled` only set after `Approved` and `approved_at` are confirmed.
- No publishing automation triggered in Phase 4.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
