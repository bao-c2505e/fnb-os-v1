# Sandbox Execution Log Template — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-06-01 (Phase 24B — Sandbox Evidence Pack Template & Execution Log Standardization)
Type: Template — per-run execution detail log for Phase 26+ sandbox manual execution
Path: `docs/runbooks/SANDBOX_EXECUTION_LOG_TEMPLATE.md`

---

> **PHASE RESTRICTION — NOT USABLE IN PHASE 24B.**
>
> This template is prepared in Phase 24B for future use only.
> It becomes usable only in **Phase 26+**, when Owner has issued explicit approval:
> `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow/module name] — [date]`
>
> Phase 24B does not authorize sandbox import.
> Phase 24B does not authorize sandbox execution.
> Possessing this template does not grant permission to execute any workflow.

---

## How to Use This Template

1. Copy this entire file.
2. Rename it: `logs/execution_log_[WORKFLOW_NAME]_[PHASE]_run[N]_[DATE].md`
   - Example: `logs/execution_log_content_auto_phase26_run1_2026-07-01.md`
3. Fill every field before triggering the workflow.
4. Complete remaining fields immediately after execution.
5. Attach to or link from the corresponding Evidence Pack (use `SANDBOX_EVIDENCE_PACK_TEMPLATE.md`).
6. Do not leave fields blank — write `N/A` or `NONE` if not applicable.

---

## Execution Log Header

| Field | Value |
|-------|-------|
| **Run ID** | RUN-[PHASE]-[WORKFLOW_SHORT]-[DATE]-[N] *(e.g., RUN-26-CONTENT-2026-07-01-1)* |
| **Workflow / Module** | *(exact filename from `n8n/workflows/`)* |
| **Phase** | Phase [XX] — [Phase Name] |
| **Approval Phrase** | *(paste exact Owner approval phrase)* |
| **Evidence Pack Link** | *(file path or ID of the corresponding Evidence Pack)* |
| **Credentials Mode** | MOCK / SANDBOX ONLY — no real credentials *(confirm one)* |
| **Trigger Method** | Manual trigger by Owner in sandbox n8n UI |
| **Test Data Set** | *(ID or description of test data used — see SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md)* |
| **Operator** | Owner *(only Owner may manually trigger — Builder cannot)* |
| **Execution Date** | YYYY-MM-DD |
| **Execution Start** | HH:MM (timezone) |
| **Execution End** | HH:MM (timezone) |
| **Total Duration** | HH:MM:SS |

---

## A — Pre-Execution Checklist

*Complete before triggering the workflow.*

| Check | Status | Notes |
|-------|--------|-------|
| Approval phrase received and recorded above | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — STOP | |
| Evidence Pack created and header filled | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — STOP | EP ID: |
| Sandbox n8n confirmed (not production) | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — STOP | |
| Workflow is INACTIVE (`"active": false`) | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No real credentials connected | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| Test data is synthetic / mock (no real customer PII) | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | Data set: |
| OWNER_RUNTIME_READINESS_CHECKLIST completed | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — STOP | |
| Rollback / cleanup plan noted | `[ ]` YES &nbsp;&nbsp; `[ ]` NO | Plan: |

**Pre-execution result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — STOP

---

## B — Input Summary

*Describe the test input sent to the workflow.*

**Input type:** *(e.g., webhook payload, form data, manual test event)*

**Input content (no real customer PII):**

```json
{
  // paste sanitized test input here
  // replace any real data with MOCK_DATA placeholders
}
```

**Input source:** *(e.g., manually typed, copied from `07_TEST_FIXTURES/`)*

---

## C — Nodes / Steps Observed

*List each node in the workflow and its observed behavior.*

| Step | Node Name | Node Type | Status | Notes |
|------|-----------|-----------|--------|-------|
| 1 | | | `[ ]` Pass / `[ ]` Skip / `[ ]` Error | |
| 2 | | | `[ ]` Pass / `[ ]` Skip / `[ ]` Error | |
| 3 | | | `[ ]` Pass / `[ ]` Skip / `[ ]` Error | |
| 4 | | | `[ ]` Pass / `[ ]` Skip / `[ ]` Error | |
| 5 | | | `[ ]` Pass / `[ ]` Skip / `[ ]` Error | |

*(Add rows as needed)*

**Execution path:** *(describe which branch was followed if workflow has conditionals)*

---

## D — Output Summary

*Describe the output produced by the workflow.*

**Output type:** *(e.g., JSON response, file created, message generated, n8n node output)*

**Output content (no real customer PII — redact or use placeholder):**

```
(paste sanitized output here)
```

**Output matches expected?** `[ ]` YES &nbsp;&nbsp; `[ ]` NO — explain:

**Unexpected outputs observed:** *(write `NONE` if none)*

---

## E — Error Summary

*List every error, warning, or unexpected behavior.*

| Error ID | Node | Severity | Description | Resolution |
|----------|------|----------|-------------|------------|
| ERR-001 | | | | |

*(Write `NONE` if no errors encountered.)*

---

## F — Post-Execution Safety Checks

| Safety Item | Status | Notes |
|-------------|--------|-------|
| Workflow remains INACTIVE after execution | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No real customer message sent | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No post published to social media | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No ad spend triggered | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No real API charged or rate-limited | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed | |
| No real credentials used or logged | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |
| No real customer PII in output | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` NOT confirmed — STOP | |

---

## G — Rollback and Cleanup

| Item | Status | Notes |
|------|--------|-------|
| Rollback / cleanup needed? | `[ ]` YES &nbsp;&nbsp; `[ ]` NO | |
| Cleanup steps taken | | |
| Workflow deactivated (if it was activated temporarily) | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` N/A | |
| Test data removed or flagged as used | `[ ]` Confirmed &nbsp;&nbsp; `[ ]` N/A | |

---

## H — Decision

| Field | Value |
|-------|-------|
| **Run result** | `[ ]` PASS &nbsp;&nbsp; `[ ]` PASS WITH NOTES &nbsp;&nbsp; `[ ]` FAIL &nbsp;&nbsp; `[ ]` BLOCKED |
| **Issue report filed?** | `[ ]` YES — ID: &nbsp;&nbsp; `[ ]` NO |
| **Evidence Pack updated with this log?** | `[ ]` YES &nbsp;&nbsp; `[ ]` NO |
| **Recommended next action** | *(e.g., "submit evidence to Owner", "fix issue ERR-001 and re-run", "escalate to production phase")* |

---

## Related Documents

- [SANDBOX_EVIDENCE_PACK_TEMPLATE.md](SANDBOX_EVIDENCE_PACK_TEMPLATE.md) — parent evidence record for this run
- [SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md](SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md) — test data source registration
- [SANDBOX_ISSUE_REPORT_TEMPLATE.md](SANDBOX_ISSUE_REPORT_TEMPLATE.md) — file if errors need Owner decision
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — must be completed before first execution
- [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) — pre-action readiness gate

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This template is documentation-only. Not usable until Phase 26+ with explicit Owner approval.*
*Possessing this template does not authorize sandbox import or sandbox execution.*
