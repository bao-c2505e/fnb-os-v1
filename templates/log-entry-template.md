# Log Entry Template

**Schema:** `schemas/log-entry.schema.json`
**Used by:** All agents in FnB OS V1

---

## log_id
[AUTO_GENERATED — Format: LOG-[YYYYMMDD]-[NNN] — e.g., LOG-20260528-001]

## timestamp
[AUTO_GENERATED — ISO 8601 datetime — e.g., 2026-05-28T09:00:00+07:00]

## phase
[TO_FILL — Phase this log entry belongs to — e.g., "Phase 4" or "Phase 1.7"]

## agent_name
[TO_FILL — Name and ID of the agent — e.g., "Claude Code (AGT-02)" or "Content Agent (AGT-Content)"]

## action_type
[TO_FILL — Select one:
File Created | File Updated | Schema Validated | Content Draft | Creative Brief Draft |
Ads Pack Draft | CRM Sequence Draft | Reply Draft | Approval Decision |
Phase Start | Phase Complete | Review Pass | Review Fail | Owner Approved | Error]

## input_ref
[TO_FILL or null — Reference to input that triggered this action — e.g., "CMD-4.0-001" or "CC-VQ-20260528-001". Set to null if no specific input ref.]

## output_ref
[TO_FILL or null — Reference to output produced — e.g., file path or item ID — e.g., "templates/content-output-template.md". Set to null if no specific output.]

## status
[TO_FILL — Select one: Success | In Progress | Blocked | Failed | Needs Review]

## summary
[TO_FILL — Human-readable summary of the action. 1–3 sentences. What was done, what was produced, what is next.]

## errors
[TO_FILL or null — List of errors encountered. Set to null if none. Example:
- "Missing required field: brand_id"
- "Schema validation failed: invalid enum value"]

## next_action
[TO_FILL or null — Recommended next action — e.g., "Owner to review and approve." or "Awaiting Codex review." Set to null if no follow-up needed.]

## owner_action_required
[TO_FILL — true or false. True if Owner must act before next step can proceed.]
