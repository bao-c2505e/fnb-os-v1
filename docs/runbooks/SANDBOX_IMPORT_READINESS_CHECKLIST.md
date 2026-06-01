# Sandbox Import Readiness Checklist — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-06-01 (Phase 25 — Sandbox Import Readiness Gate)
Type: Checklist Template — copy and fill for each sandbox import event
Path: `docs/runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md`

---

> **IMPORTANT — THIS IS A CHECKLIST TEMPLATE ONLY.**
> Completing this checklist does not authorize sandbox import.
> Sandbox import requires an explicit Owner approval phrase in this exact format:
>
> **`APPROVED FOR SANDBOX IMPORT ONLY — [workflow/module name] — [date]`**
>
> Any vague approval ("ok", "approved", "triển khai", "import đi", "go ahead") is NOT sufficient.
> Phase 25 does not import, activate, or execute any workflow.
> This checklist becomes usable in a future import phase only with explicit Owner approval.

---

## How to Use This Template

1. Copy this entire file.
2. Rename it: `logs/import_readiness_[WORKFLOW_NAME]_[PHASE]_[DATE].md`
3. Fill every item below before requesting import approval.
4. All items must be confirmed before asking Owner to issue the approval phrase.
5. Do not skip any item — write `N/A` only if genuinely not applicable, with a reason.

---

## Checklist Header

| Field | Value |
|-------|-------|
| **Checklist ID** | IRC-[PHASE]-[WORKFLOW_SHORT]-[DATE] |
| **Workflow / Module** | *(exact filename from `n8n/workflows/` — no abbreviations)* |
| **Proposed Import Phase** | Phase [XX] |
| **Prepared By** | *(name and role)* |
| **Date** | YYYY-MM-DD |
| **Owner Approval Status** | `[ ]` Not yet requested &nbsp;&nbsp; `[ ]` Approval phrase received |
| **Owner Approval Phrase** | *(paste exact phrase here after Owner issues it)* |

---

## Section 1 — Repo State

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 1.1 | Branch is `main` | `git branch` | `[ ]` PASS / `[ ]` FAIL |
| 1.2 | HEAD equals `origin/main` | `git status` shows "up to date" | `[ ]` PASS / `[ ]` FAIL |
| 1.3 | Working tree is clean | `git status` shows "nothing to commit" | `[ ]` PASS / `[ ]` FAIL |
| 1.4 | Latest phase handoff exists | `handoff/PHASE_XX_HANDOFF.md` confirmed present | `[ ]` PASS / `[ ]` FAIL |
| 1.5 | CI checks pass on latest commit | GitHub Actions tab shows green on latest commit | `[ ]` PASS / `[ ]` FAIL |

**Section 1 result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — stop and fix

---

## Section 2 — Workflow / Module Identity

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 2.1 | Workflow name clearly stated | File exists at `n8n/workflows/[name].json` | `[ ]` PASS / `[ ]` FAIL |
| 2.2 | Workflow JSON path identified | Full path noted above | `[ ]` PASS / `[ ]` FAIL |
| 2.3 | Workflow JSON is valid JSON | CI `validate_json.py` passed | `[ ]` PASS / `[ ]` FAIL |
| 2.4 | Workflow JSON has `"active": false` | CI `check_n8n_workflows.py` passed | `[ ]` PASS / `[ ]` FAIL |
| 2.5 | Prior phase runbook/evidence doc exists | Doc path: | `[ ]` PASS / `[ ]` FAIL |

**Workflow JSON path confirmed:** `n8n/workflows/_____________________.json`

**Section 2 result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — stop and fix

---

## Section 3 — Import Target (Sandbox Confirmation)

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 3.1 | Import target is sandbox n8n | URL confirmed to be sandbox instance | `[ ]` PASS / `[ ]` FAIL |
| 3.2 | Sandbox URL is separate from production | Two different URLs confirmed | `[ ]` PASS / `[ ]` FAIL |
| 3.3 | Sandbox n8n is isolated from production data | No shared credentials or database | `[ ]` PASS / `[ ]` FAIL |

**Sandbox n8n URL (confirm it is NOT production):** *(do not record production URL here)*

**Section 3 result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — stop and fix

---

## Section 4 — Credential and Secret Safety

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 4.1 | No production credentials will be used | Only mock/sandbox/none credentials | `[ ]` PASS / `[ ]` FAIL |
| 4.2 | No secrets in repo | CI `check_no_secrets.py` passed | `[ ]` PASS / `[ ]` FAIL |
| 4.3 | Workflow JSON uses `REPLACE_WITH_*` placeholders for credentials | Grep confirmed | `[ ]` PASS / `[ ]` FAIL |
| 4.4 | No production webhook URLs in workflow JSON | Stub or sandbox URLs only | `[ ]` PASS / `[ ]` FAIL |

**Section 4 result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — STOP — credential/secret risk

---

## Section 5 — Phase Boundary (Forbidden Actions)

These actions are forbidden during sandbox import. Confirm all are understood:

| # | Forbidden Action | Understood? |
|---|-----------------|-------------|
| 5.1 | Activating the workflow (`"active": true`) | `[ ]` Understood |
| 5.2 | Manually executing / triggering the workflow | `[ ]` Understood |
| 5.3 | Calling any real external API | `[ ]` Understood |
| 5.4 | Connecting production credentials | `[ ]` Understood |
| 5.5 | Sending any real customer message | `[ ]` Understood |
| 5.6 | Publishing any social media content | `[ ]` Understood |
| 5.7 | Committing any ad spend | `[ ]` Understood |
| 5.8 | Claiming production readiness after import | `[ ]` Understood |

**Section 5 result:** `[ ]` ALL UNDERSTOOD — proceed &nbsp;&nbsp; `[ ]` NOT UNDERSTOOD — stop

---

## Section 6 — Evidence and Rollback Readiness

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 6.1 | Evidence log path prepared | `logs/phase_[XX]_[workflow]_sandbox_evidence_log.md` path noted | `[ ]` PASS / `[ ]` FAIL |
| 6.2 | Evidence pack template is available | `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md` exists | `[ ]` PASS / `[ ]` FAIL |
| 6.3 | Rollback path known | If import fails: stop, do not retry without Owner re-approval | `[ ]` PASS / `[ ]` FAIL |
| 6.4 | Stop conditions reviewed | Section F of `docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md` read | `[ ]` PASS / `[ ]` FAIL |

**Evidence log path:** `logs/phase_[XX]_[workflow_name]_sandbox_evidence_log.md`

**Section 6 result:** `[ ]` ALL PASS — proceed &nbsp;&nbsp; `[ ]` FAIL — stop and fix

---

## Section 7 — Owner Approval Phrase

| # | Check | Status |
|---|-------|--------|
| 7.1 | Owner has been shown this checklist and all items PASS | `[ ]` PASS / `[ ]` NOT YET |
| 7.2 | Owner has issued exact approval phrase | `[ ]` PASS / `[ ]` NOT YET |
| 7.3 | Approval phrase includes workflow name | `[ ]` PASS / `[ ]` FAIL |
| 7.4 | Approval phrase includes date | `[ ]` PASS / `[ ]` FAIL |
| 7.5 | Approval phrase is session-specific (not carried from prior session) | `[ ]` PASS / `[ ]` FAIL |

**Approval phrase received:** *(paste exact Owner phrase here)*

```
APPROVED FOR SANDBOX IMPORT ONLY — [workflow/module name] — [date]
```

**Section 7 result:** `[ ]` ALL PASS — import may proceed &nbsp;&nbsp; `[ ]` NOT YET — do not import

---

## Final Decision

| All sections PASS? | Decision |
|-------------------|---------|
| `[ ]` YES — all 7 sections pass, approval phrase received | **READY FOR SANDBOX IMPORT** — Owner may proceed |
| `[ ]` NO — one or more sections fail (non-safety) | **NOT READY — FIX DOCUMENTATION** — fix and re-run |
| `[ ]` NO — credential, secret, or safety risk found | **BLOCKED — SAFETY RISK** — stop all activity, notify Owner |

---

## Quick Stop-Condition Reference

Stop immediately and notify Owner if any of these occur during import:

- Workflow shows `"active": true` after import
- Production credential prompt appears in n8n
- Execution count is non-zero after import
- Any real customer message is sent
- Any social media content is published
- Any ad budget is committed
- Any paid API is charged
- Import fails with an unexpected error
- The target URL turns out to be production

---

## Related Documents

- [`docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md`](../PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md) — full gate reference
- [`docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md`](SANDBOX_IMPORT_TEST_RUNBOOK.md) — step-by-step import process
- [`docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md`](SANDBOX_EVIDENCE_PACK_TEMPLATE.md) — evidence recording
- [`docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md`](RUNTIME_APPROVAL_DECISION_TREE.md) — confirm approval level
- [`docs/governance/OWNER_APPROVAL_GATE.md`](../governance/OWNER_APPROVAL_GATE.md) — formal gate definitions

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This checklist is documentation-only. Completing it does not authorize sandbox import.*
*Import requires explicit Owner approval in the exact format specified above.*
