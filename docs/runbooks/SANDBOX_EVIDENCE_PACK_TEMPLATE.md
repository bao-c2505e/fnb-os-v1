# Sandbox Evidence Pack Template — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-06-01 (Phase 24B — Sandbox Evidence Pack Template & Execution Log Standardization)
Type: Template — copy and fill for each sandbox import or sandbox execution event
Path: `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md`

---

> **IMPORTANT — THIS IS A TEMPLATE ONLY.**
> Completing this template does not authorize any sandbox import or sandbox execution.
> Each runtime action requires explicit Owner approval for that specific action at that specific time.
> Phase 24B does not authorize sandbox import. Phase 24B does not authorize sandbox execution.
> Templates become usable in Phase 25 (sandbox import) or Phase 26 (sandbox execution) only with explicit Owner approval.

---

## How to Use This Template

1. Copy this entire file.
2. Rename it: `logs/evidence_pack_[WORKFLOW_NAME]_[PHASE]_[DATE].md`
3. Fill every field before beginning the action.
4. Complete all fields after the action.
5. Do not leave any field blank — write `N/A` or `NONE` if not applicable.
6. Attach or link all screenshots and log files.
7. Submit to Owner for review.

---

## Evidence Pack Header

| Field | Value |
|-------|-------|
| **Evidence Pack ID** | EP-[PHASE]-[WORKFLOW_SHORT]-[DATE] *(e.g., EP-25-CONTENT-2026-06-15)* |
| **Phase** | Phase [XX] — [Phase Name] |
| **Workflow / Module Name** | *(exact filename from `n8n/workflows/`)* |
| **Action Type** | `[ ]` Sandbox Import Only &nbsp;&nbsp; `[ ]` Sandbox Manual Execution &nbsp;&nbsp; `[ ]` Production Runtime *(select one)* |
| **Approval Phrase Used** | *(paste exact phrase from Owner — see templates below)* |
| **Environment** | SANDBOX ONLY — production prohibited |
| **Date** | YYYY-MM-DD |
| **Time (start)** | HH:MM (timezone) |
| **Time (end)** | HH:MM (timezone) |
| **Agent / Operator** | *(name and role — Owner, Builder, etc.)* |
| **n8n Instance** | SANDBOX *(confirm: not production)* |

**Approval phrase templates (must match exactly — fill in brackets):**

- Sandbox import: `APPROVED FOR SANDBOX IMPORT ONLY — [workflow/module name] — [date]`
- Sandbox execution: `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow/module name] — [date]`
- Production: `APPROVED FOR PRODUCTION RUNTIME ONLY — [workflow/module name] — [date]`

---

## A — Pre-Check Summary

*Complete this section before beginning any action.*

| Check | Status | Notes |
|-------|--------|-------|
| git branch is main | `[ ]` Pass / `[ ]` Fail | |
| Working tree is clean | `[ ]` Pass / `[ ]` Fail | |
| Latest commit matches expected | `[ ]` Pass / `[ ]` Fail | Commit: |
| Phase handoff file exists and is current | `[ ]` Pass / `[ ]` Fail | File: |
| Codex PASS (or Owner direct review) on record | `[ ]` Pass / `[ ]` Fail | Review ref: |
| Workflow JSON located in repo | `[ ]` Pass / `[ ]` Fail | Path: |
| Workflow JSON contains `"active": false` | `[ ]` Pass / `[ ]` Fail | |
| No real credentials in workflow JSON | `[ ]` Pass / `[ ]` Fail | |
| No secrets in any new file | `[ ]` Pass / `[ ]` Fail | |
| OWNER_RUNTIME_READINESS_CHECKLIST completed | `[ ]` Pass / `[ ]` Fail | |
| Explicit Owner approval phrase received | `[ ]` Pass / `[ ]` Fail | Phrase: |
| Sandbox n8n environment confirmed (not production) | `[ ]` Pass / `[ ]` Fail | |

**Pre-check result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — STOP, do not proceed

---

## B — Action Performed

*Describe exactly what was done — no more, no less.*

**Action type:** *(sandbox import / sandbox manual execution — specify)*

**Step-by-step description:**

```
1.
2.
3.
(continue as needed)
```

**Workflow / nodes touched:**

*(List all workflow nodes observed or interacted with)*

---

## C — Expected Result

*Describe what should happen if the action succeeds.*

```
(fill before action)
```

---

## D — Actual Result

*Describe what actually happened after the action.*

```
(fill after action)
```

**Result matches expected?** `[ ]` YES &nbsp;&nbsp; `[ ]` NO — explain:

---

## E — Screenshots and Log References

*List every screenshot and log file captured. Do not leave blank.*

| Reference ID | Type | Description | File / Location |
|-------------|------|-------------|-----------------|
| SCR-001 | Screenshot | *(e.g., workflow canvas after import — active=false confirmed)* | |
| SCR-002 | Screenshot | | |
| LOG-001 | n8n execution log | | |
| LOG-002 | | | |

*(Add rows as needed. Every claim about workflow state must have a screenshot or log reference.)*

---

## F — Errors Encountered

*List every error, warning, or unexpected behavior.*

| Error ID | Severity | Description | Resolution / Action Taken |
|----------|----------|-------------|--------------------------|
| ERR-001 | | | |

*(Write `NONE` if no errors were encountered.)*

---

## G — Safety Checks (Post-Action)

*Complete after action is finished.*

| Safety Item | Status | Notes |
|-------------|--------|-------|
| Stop conditions triggered? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Workflow remains INACTIVE (`"active": false`) | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| Secrets exposed during action? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Real customer data touched? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Auto-post triggered? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Auto-reply to real customer triggered? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Ad spend committed? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| External paid API called unexpectedly? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |
| Production system modified? | `[ ]` YES — STOP &nbsp;&nbsp; `[ ]` NO | |

**If any item is YES — STOP:** halt all further action, notify Owner immediately, do not continue.

---

## H — Final Status

| Field | Value |
|-------|-------|
| **Overall result** | `[ ]` PASS &nbsp;&nbsp; `[ ]` PASS WITH NOTES &nbsp;&nbsp; `[ ]` FAIL &nbsp;&nbsp; `[ ]` BLOCKED |
| **Evidence pack complete?** | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — incomplete fields: |
| **Next recommended action** | *(e.g., "proceed to sandbox execution with new approval", "stop — fix noted issues", "submit to Owner for review")* |
| **Issue report filed?** | `[ ]` YES — ID: &nbsp;&nbsp; `[ ]` NO |

---

## I — Owner Review Notes

*To be filled by Owner after reviewing this evidence pack.*

| Field | Value |
|-------|-------|
| **Owner review date** | |
| **Owner decision** | `[ ]` ACCEPTED &nbsp;&nbsp; `[ ]` ACCEPTED WITH NOTES &nbsp;&nbsp; `[ ]` REJECTED |
| **Owner notes** | |
| **Next authorization (if any)** | *(e.g., "APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow] — [date]")* |

---

## Related Documents

- [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) — complete before this template
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — sandbox import process guide
- [SANDBOX_EXECUTION_LOG_TEMPLATE.md](SANDBOX_EXECUTION_LOG_TEMPLATE.md) — per-run execution detail log
- [SANDBOX_ISSUE_REPORT_TEMPLATE.md](SANDBOX_ISSUE_REPORT_TEMPLATE.md) — for any issues found
- [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) — confirm approval level before acting
- [SANDBOX_RUNBOOK_INDEX.md](SANDBOX_RUNBOOK_INDEX.md) — overall sandbox status tracker

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This template is documentation-only. Completing it does not authorize runtime action.*
