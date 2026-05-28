# 11 — Module SOP System

**Phase:** 4 — Module SOP + Output Templates
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28

---

## What Are Module SOPs?

Module SOPs (Standard Operating Procedures) are the practical operating instructions for each marketing module in FnB OS V1. Each SOP tells an agent exactly:

- What inputs it needs before starting
- What steps to follow in order
- What output template to use
- When to stop and escalate to the Owner
- What the approval gate rules are
- When the job is done

Module SOPs are not the same as agent role files (`agents/*.md`). Agent files define *who* an agent is and its core behavior. Module SOPs define *how* a specific task type is executed end-to-end.

---

## SOP Registry

| SOP File | Module | Agent | Schema | Template |
|----------|--------|-------|--------|----------|
| `module-sops/content-auto-sop.md` | Content Auto | Content Agent (AGT-Content) | `schemas/content-output.schema.json` | `templates/content-output-template.md` |
| `module-sops/creative-asset-auto-sop.md` | Creative Asset Auto | Creative Asset Agent (AGT-Creative) | `schemas/creative-brief.schema.json` | `templates/creative-brief-template.md` |
| `module-sops/ads-pack-auto-sop.md` | Ads Pack Auto | Ads Pack Agent (AGT-Ads) | `schemas/ads-pack.schema.json` | `templates/ads-pack-template.md` |
| `module-sops/crm-followup-auto-sop.md` | CRM Follow-Up Auto | CRM Follow-Up Agent (AGT-CRM) | `schemas/crm-followup.schema.json` | `templates/crm-followup-template.md` |
| `module-sops/comment-inbox-assistant-sop.md` | Comment Inbox Assistant | Comment Inbox Agent (AGT-Inbox) | `schemas/comment-inbox-reply.schema.json` | `templates/comment-inbox-reply-template.md` |
| `module-sops/approval-publishing-sop.md` | Approval & Publishing | Approval Publishing Agent (AGT-Approval) | `schemas/approval-status.schema.json` | `templates/approval-status-template.md` |

---

## How Owner Approval Works

Every item produced by an agent starts at `approval_status: Draft`. The path to publishing is:

```
Draft → Ready for Review → [Reviewer checks] → Approved (Owner only) → Scheduled / Published
```

Only the Owner may set `Approved`. No agent may self-approve its own output.

No item may be `Published` or `Scheduled` without a prior `Approved` state and a recorded `approved_at` timestamp.

If an item is `Rejected` or stuck in `Needs Revision` for more than 2 cycles, the Owner makes the final call.

---

## Why the Owner Does Not Debug Agent Outputs Manually

The Owner's role is to review, approve, and decide — not to fix agent output line by line.

If an agent output has errors, missing fields, or scope violations, the correct path is:
1. Reviewer (Codex or Owner) marks `Needs Revision` with specific `review_notes`.
2. Agent receives the revision instruction and produces a corrected output.
3. Owner reviews the corrected output.

The Owner should not be editing template fields, fixing JSON, or patching agent mistakes by hand. That is the agent's job on re-run.

---

## Why Screenshots Are Not Substitutes for Logs

Screenshots capture a visual moment but:
- Cannot be parsed by future agents or automation.
- Cannot be searched or referenced by ID.
- Do not record which agent took which action at which time.
- Cannot trigger n8n/LangGraph workflows downstream.

Every agent action must produce a structured log entry in `logs/AGENT_ACTIVITY_LOG.md` using `templates/log-entry-template.md`. Screenshots may supplement but never replace log entries.

---

## No Runtime Automation in Phase 4

Phase 4 defines the operating procedures and output templates. It does not:
- Create n8n workflows.
- Write automation scripts.
- Connect to any API (Zalo, Facebook, TikTok, Google, etc.).
- Trigger any real customer-facing action.

Automation wiring (n8n, LangGraph) happens in Phase 5 and beyond, using the schemas, SOPs, and templates defined in Phases 3 and 4 as the contract.

---

## Related Files

- Agent role definitions: `agents/*.md`
- Brand reference: `brand-brain/vi-cuon.md`
- Schema contracts: `schemas/*.schema.json`
- Output templates: `templates/*.md`
- Template system doc: `docs/12_OUTPUT_TEMPLATE_SYSTEM.md`
