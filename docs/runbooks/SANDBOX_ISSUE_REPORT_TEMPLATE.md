# Sandbox Issue Report Template — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-06-01 (Phase 24B — Sandbox Evidence Pack Template & Execution Log Standardization)
Type: Template — document issues found during future sandbox import or sandbox execution
Path: `docs/runbooks/SANDBOX_ISSUE_REPORT_TEMPLATE.md`

---

> **IMPORTANT — THIS IS A TEMPLATE ONLY.**
> Filing an issue report does not authorize any runtime action or fix.
> All fix actions require new Owner approval.
> Phase 24B does not authorize sandbox import or sandbox execution.

---

## How to Use This Template

1. Copy this entire file when an issue is found during sandbox import or execution.
2. Rename it: `logs/issue_report_[WORKFLOW_NAME]_[PHASE]_ISS[N]_[DATE].md`
   - Example: `logs/issue_report_content_auto_phase26_ISS001_2026-07-01.md`
3. Fill all fields as completely as possible.
4. Link to the relevant Evidence Pack and Execution Log.
5. Submit to Owner for decision. Do not self-authorize a fix.

---

## Issue Report Header

| Field | Value |
|-------|-------|
| **Issue ID** | ISS-[PHASE]-[WORKFLOW_SHORT]-[N] *(e.g., ISS-26-CONTENT-001)* |
| **Related Phase** | Phase [XX] — [Phase Name] |
| **Related Workflow / Module** | *(exact filename from `n8n/workflows/`)* |
| **Related Evidence Pack** | *(EP ID or file path)* |
| **Related Execution Log** | *(RUN ID or file path, if applicable)* |
| **Reported By** | *(name and role)* |
| **Report Date** | YYYY-MM-DD |
| **Report Time** | HH:MM (timezone) |
| **Action Type When Found** | `[ ]` Sandbox Import &nbsp;&nbsp; `[ ]` Sandbox Manual Execution &nbsp;&nbsp; `[ ]` Documentation Review |

---

## A — Severity

| Severity | Definition | This Issue |
|----------|------------|------------|
| **Blocker** | Prevents proceeding. Workflow cannot be used. Safety boundary violated or may be violated. Stop immediately. | `[ ]` |
| **High** | Significant problem requiring Owner decision before any further action. | `[ ]` |
| **Medium** | Issue that should be fixed before next phase but does not block evidence submission. | `[ ]` |
| **Low** | Minor issue — cosmetic, labeling, non-functional. Can note and continue. | `[ ]` |

**Selected severity:** *(Blocker / High / Medium / Low)*

**If Blocker:** Stop all sandbox activity now. Do not proceed. Notify Owner immediately.

---

## B — Reproduction Notes

*Describe how to reproduce this issue reliably.*

**Environment:** SANDBOX *(confirm — not production)*

**Steps to reproduce:**

```
1.
2.
3.
(continue as needed)
```

**Reproducible?** `[ ]` YES — every time &nbsp;&nbsp; `[ ]` YES — intermittent &nbsp;&nbsp; `[ ]` NOT yet confirmed

**Test data used:** *(Test Data ID from SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md)*

---

## C — Expected vs. Actual

| | Description |
|-|-------------|
| **Expected** | *(what should have happened)* |
| **Actual** | *(what actually happened)* |
| **Difference** | *(describe the gap clearly)* |

---

## D — Evidence References

*List every screenshot, log file, or recording that documents this issue.*

| Reference ID | Type | Description | File / Location |
|-------------|------|-------------|-----------------|
| SCR-001 | Screenshot | | |
| LOG-001 | Execution log | | |

*(Write `NONE` if no evidence captured — note that severity may need to be upgraded if evidence is missing.)*

---

## E — Suspected Cause

*Builder's assessment of what caused the issue. This is an assessment only — Owner decides the fix.*

| Option | Selected? | Notes |
|--------|-----------|-------|
| Workflow JSON configuration error | `[ ]` | |
| n8n node version incompatibility | `[ ]` | |
| Test data not matching expected input format | `[ ]` | |
| Missing or incorrect credentials (mock/sandbox) | `[ ]` | |
| n8n sandbox environment configuration | `[ ]` | |
| Workflow logic error | `[ ]` | |
| Evidence capture gap (not a workflow error) | `[ ]` | |
| Unknown — needs further investigation | `[ ]` | |

**Notes on suspected cause:**

```
(explain reasoning — reference specific nodes or fields if known)
```

---

## F — Safety Boundary Check

*Assess whether any safety boundary was crossed or is at risk.*

| Safety Boundary | Status |
|----------------|--------|
| Workflow was activated (`"active": true`) during issue | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |
| Real credentials were exposed or used | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |
| Real customer data was accessed or sent | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |
| Auto-post or auto-reply occurred | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |
| Ad spend was triggered | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |
| External paid API was called unexpectedly | `[ ]` YES — HIGH &nbsp;&nbsp; `[ ]` NO |
| Production system was modified | `[ ]` YES — BLOCKER &nbsp;&nbsp; `[ ]` NO |

**If any BLOCKER item is YES:** halt all further action immediately and escalate to Owner.

---

## G — Recommended Owner Decision

*Builder's recommendation only — Owner decides.*

`[ ]` Fix workflow JSON and re-import (requires new Owner approval for re-import)
`[ ]` Fix test data and re-run (requires new Owner approval for re-execution)
`[ ]` Accept issue and proceed (document as known limitation)
`[ ]` Defer to future phase (document and skip)
`[ ]` Halt sandbox activity for this workflow pending further investigation
`[ ]` Escalate to ChatGPT (Chief Architect) for design review
`[ ]` Other: *(describe)*

**Builder rationale:**

```
(explain why this recommendation was made)
```

---

## H — Builder Fix Notes

*If Owner approves a fix, Builder records fix details here after implementation.*

| Field | Value |
|-------|-------|
| **Fix authorized by Owner?** | `[ ]` YES &nbsp;&nbsp; `[ ]` NO — STOP |
| **Owner authorization phrase / date** | |
| **Fix description** | |
| **Files changed** | |
| **Commit (if applicable)** | |
| **Fix verified by** | |
| **Re-test required?** | `[ ]` YES &nbsp;&nbsp; `[ ]` NO |

---

## I — Reviewer Status

*Codex or Owner review after fix is applied.*

| Field | Value |
|-------|-------|
| **Reviewer** | *(Codex / Owner direct)* |
| **Review date** | |
| **Review result** | `[ ]` PASS &nbsp;&nbsp; `[ ]` PASS WITH NOTES &nbsp;&nbsp; `[ ]` BLOCK |
| **Review notes** | |

---

## J — Final Resolution

| Field | Value |
|-------|-------|
| **Resolution date** | |
| **Resolution** | `[ ]` FIXED — re-verified &nbsp;&nbsp; `[ ]` ACCEPTED AS-IS — documented &nbsp;&nbsp; `[ ]` DEFERRED &nbsp;&nbsp; `[ ]` WONT FIX |
| **Resolution notes** | |
| **Issue closed by** | *(name and role)* |

---

## Related Documents

- [SANDBOX_EVIDENCE_PACK_TEMPLATE.md](SANDBOX_EVIDENCE_PACK_TEMPLATE.md) — parent evidence record
- [SANDBOX_EXECUTION_LOG_TEMPLATE.md](SANDBOX_EXECUTION_LOG_TEMPLATE.md) — execution log where issue was found
- [SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md](SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md) — test data used
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — import process reference
- [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) — re-confirm approval before any fix action

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This template is documentation-only. Filing an issue report does not authorize runtime action or self-authorized fixes.*
