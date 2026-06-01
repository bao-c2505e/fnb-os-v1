# Phase 25 — Sandbox Import Readiness Gate

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 25 — Sandbox Import Readiness Gate
**By:** Claude Code (Builder, AGT-02)
**Date:** 2026-06-01
**Status:** BUILD_READY — READY FOR CODEX REVIEW

---

## Section A — Purpose

Phase 25 prepares the repo for controlled sandbox imports in later phases.

This phase is **documentation and readiness only**. It does not import any workflow into n8n. It does not activate any workflow. It does not execute any workflow. It does not call any real API. It does not use or store production credentials.

Phase 25 answers the following gate questions before sandbox import can be authorized in any future phase:

| # | Gate Question |
|---|--------------|
| 1 | Which workflow/module is being considered for sandbox import? |
| 2 | Has the correct sandbox import approval phrase been provided by the Owner? |
| 3 | Is the import target confirmed as sandbox-only (not production)? |
| 4 | Are production credentials confirmed absent? |
| 5 | Is workflow activation forbidden in this phase? |
| 6 | Is manual execution forbidden in this phase? |
| 7 | Are API calls forbidden in this phase? |
| 8 | Are secrets absent from the repo? |
| 9 | Are expected evidence/log files ready for use after import? |
| 10 | Is the rollback/non-import path documented? |

**All 10 gates must be confirmed before Owner issues sandbox import approval.**

---

## Section B — Import Approval Gate

### Required Approval Phrase

Before any sandbox import can occur in a future phase, the Owner must issue this **exact** approval phrase:

```
APPROVED FOR SANDBOX IMPORT ONLY — [workflow/module name] — [date]
```

**Examples of valid approval phrases:**
- `APPROVED FOR SANDBOX IMPORT ONLY — content_auto_skeleton — 2026-07-01`
- `APPROVED FOR SANDBOX IMPORT ONLY — creative_asset_auto_skeleton — 2026-07-15`

### Vague Approvals Are NOT Sufficient

The following phrases do **NOT** constitute import approval and must be rejected by Builder and Reviewer:

| Vague phrase | Why it is rejected |
|-------------|-------------------|
| "ok" | Does not name the workflow or date |
| "triển khai" | Does not name the workflow or date |
| "import đi" | Does not name the workflow or date |
| "approved" | Does not name the workflow or date |
| "go ahead" | Does not name the workflow or date |
| "yes" | Does not name the workflow or date |
| Any approval without the workflow name | Cannot be attributed to a specific import |
| Any approval without a date | Cannot be time-bounded |

**Rule:** If the exact phrase format is not met, treat the request as NOT APPROVED and request Owner to re-issue the phrase in the exact format above.

### Approval Phrase Documentation

When the Owner issues an import approval phrase, it must be recorded in:
1. The relevant evidence pack (`docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md`)
2. The session handoff (`handoff/PHASE_XX_HANDOFF.md`)
3. The activity log (`logs/AGENT_ACTIVITY_LOG.md`)

---

## Section C — Pre-Import Checklist

The following checklist must be completed and all items confirmed before any import occurs. This checklist is to be filled in the future import phase, not in Phase 25.

See also: [`docs/runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md`](runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md) for the standalone copy-fillable version.

### C1 — Repo State

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C1.1 | Git branch | `main` | `[ ]` |
| C1.2 | HEAD equals origin/main | Yes — no unpushed commits | `[ ]` |
| C1.3 | Working tree | Clean — no uncommitted changes | `[ ]` |
| C1.4 | Latest phase handoff exists | `handoff/PHASE_XX_HANDOFF.md` present | `[ ]` |
| C1.5 | CI checks pass on latest commit | GitHub Actions green | `[ ]` |

### C2 — Workflow / Module Identity

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C2.1 | Candidate workflow clearly named | Exact file name from `n8n/workflows/` | `[ ]` |
| C2.2 | Workflow JSON path identified | `n8n/workflows/[name].json` exists in repo | `[ ]` |
| C2.3 | Workflow JSON is valid JSON | CI `validate_json.py` passed | `[ ]` |
| C2.4 | Workflow JSON has `"active": false` | Confirmed by `check_n8n_workflows.py` | `[ ]` |
| C2.5 | Phase handoff for this workflow exists | Prior phase runbook/evidence doc committed | `[ ]` |

### C3 — Import Target

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C3.1 | Import target is sandbox n8n | Not the production n8n instance | `[ ]` |
| C3.2 | Sandbox n8n URL confirmed | Sandbox URL separate from production | `[ ]` |
| C3.3 | Sandbox n8n is isolated | No shared credentials with production | `[ ]` |

### C4 — Credential and Secret Safety

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C4.1 | No production credentials used | Confirmed — mock/sandbox/none only | `[ ]` |
| C4.2 | No secrets in repo | CI `check_no_secrets.py` passed | `[ ]` |
| C4.3 | No API keys in workflow JSON | `REPLACE_WITH_*` placeholders in place | `[ ]` |
| C4.4 | No webhook URLs pointing to production | Sandbox or stub URLs only | `[ ]` |

### C5 — Phase Boundary Checks

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C5.1 | Workflow activation forbidden | Will NOT be activated after import | `[ ]` |
| C5.2 | Workflow execution forbidden | Will NOT be manually triggered after import | `[ ]` |
| C5.3 | Real API calls forbidden | No external paid or production API calls | `[ ]` |
| C5.4 | Auto-post forbidden | No social media or messaging auto-post | `[ ]` |
| C5.5 | Auto-reply to customers forbidden | No customer-facing automated reply | `[ ]` |
| C5.6 | Ad spend forbidden | No Meta Ads, TikTok Ads, or Zalo Ads triggered | `[ ]` |

### C6 — Evidence and Rollback Readiness

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C6.1 | Evidence log path prepared | `logs/[phase]_[workflow]_sandbox_evidence_log.md` ready | `[ ]` |
| C6.2 | Evidence pack template available | `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md` exists | `[ ]` |
| C6.3 | Rollback path documented | Non-import path: if import fails, do not retry without Owner re-approval | `[ ]` |
| C6.4 | Stop conditions known | Owner and Builder both aware of stop conditions (see Section F) | `[ ]` |

### C7 — Approval

| # | Check | Required State | Confirmed? |
|---|-------|---------------|------------|
| C7.1 | Owner approval phrase captured | Exact phrase: `APPROVED FOR SANDBOX IMPORT ONLY — [workflow] — [date]` | `[ ]` |
| C7.2 | Approval phrase recorded in evidence pack | Evidence pack header field filled | `[ ]` |
| C7.3 | Approval is session-specific | The phrase was issued this session for this workflow | `[ ]` |

---

## Section D — Import Boundary

### What Future Sandbox Import May Allow

When Owner issues the exact approval phrase for a future phase, these actions are permitted:

| Allowed Action | Conditions |
|---------------|------------|
| Import workflow JSON into sandbox n8n | Sandbox only — not production |
| View workflow canvas after import | Read-only inspection |
| Confirm node structure | Read-only — do not modify nodes |
| Confirm `"active": false` status | Visual confirmation only |
| Take screenshots of the import state | Evidence capture |
| Fill evidence pack (SANDBOX_EVIDENCE_PACK_TEMPLATE.md) | Document results |

### What Future Sandbox Import Still Forbids

Even after import approval is granted, the following remain forbidden:

| Forbidden Action | Why |
|----------------|-----|
| Activate the workflow (`"active": true`) | Enables automatic triggering — permanently forbidden without separate approval |
| Execute the workflow manually | Separate approval required: `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY` |
| Connect production credentials | Financial and customer data risk |
| Trigger webhooks | May call external production services |
| Call real paid APIs (OpenAI, Meta, Zalo) | Cost and data risk |
| Send messages to real customers | Customer-facing — requires highest-level approval |
| Publish content to social media | Customer-facing — requires highest-level approval |
| Spend ads budget | Financial risk — requires explicit ads approval |
| Claim production readiness after import | Import ≠ production readiness |

---

## Section E — Evidence Pack Expectation

After any future sandbox import (authorized in a future phase), the following evidence must be captured. Phase 25 defines the expectation — it does not perform the capture.

Use template: [`docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md`](runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md)

| Evidence Item | Expected Value | Notes |
|--------------|---------------|-------|
| Import date/time | YYYY-MM-DD HH:MM | Record immediately after import |
| Workflow / module name | Exact filename from `n8n/workflows/` | Must match approval phrase |
| n8n sandbox target | Sandbox URL (not production) | Confirm sandbox, not production |
| Import status | Success / Failed | If failed, stop — do not retry without re-approval |
| Workflow active status | **INACTIVE** (`"active": false`) | If active=true appears: STOP immediately |
| Execution count | **Zero** | Must be zero — if non-zero: STOP |
| Credential status | Sandbox / mock / none | No production credentials |
| Screenshot / manual note | Workflow canvas screenshot | Owner does not need to debug via screenshots — just confirm state |
| Issues / blockers | Any error messages or unexpected nodes | Document exactly as observed |
| Next recommended gate | `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY` or stop | Owner decides |

---

## Section F — Stop Conditions

If any of the following are observed during future sandbox import, stop immediately and notify Owner. Do not proceed.

| Stop Condition | Action |
|---------------|--------|
| Workflow shows `"active": true` after import | Stop — deactivate if possible, notify Owner, do not proceed |
| Real production credential prompt appears | Stop — do not enter credentials, notify Owner |
| Execution count is non-zero after import | Stop — something triggered unexpectedly, notify Owner |
| Any real customer message sent | Stop — document and escalate immediately |
| Any social media post published | Stop — document and escalate immediately |
| Any ad budget committed | Stop — document and escalate immediately |
| Any paid API charged or rate-limited | Stop — document and escalate immediately |
| Import fails with unexpected error | Stop — do not retry without Owner re-approval |
| Sandbox URL is actually the production URL | Stop — abort import entirely |

---

## Section G — Decision Outcomes

After completing the pre-import checklist and all readiness checks, one of three decisions applies:

| Decision | Meaning | Next Action |
|----------|---------|-------------|
| **READY FOR OWNER SANDBOX IMPORT APPROVAL** | All checks pass. Evidence pack ready. Owner may now issue the approval phrase for a specific workflow. | Owner issues: `APPROVED FOR SANDBOX IMPORT ONLY — [workflow] — [date]` |
| **NOT READY — FIX DOCUMENTATION** | One or more checklist items fail due to missing or stale documentation. No safety risk. | Builder fixes documentation gap. Re-run checklist. |
| **BLOCKED — SAFETY / RUNTIME RISK** | A safety boundary is at risk (credential leak, active=true, execution detected). | Stop all activity. Notify Owner. Do not proceed until Owner clears the block. |

---

## Section H — Phase 25 Status

Phase 25 is documentation and readiness only.

| Confirmation | Status |
|-------------|--------|
| Workflow imported into n8n | NO |
| Workflow activated | NO |
| Workflow executed | NO |
| Real API called | NO |
| Production credentials added | NO |
| Real customer data used | NO |
| Auto-post performed | NO |
| Auto-reply performed | NO |
| Ad spend committed | NO |
| Workflow JSON modified | NO |
| `"active": true` introduced | NO |
| Secrets added to repo | NO |

---

## Section I — Workflow Readiness Status

Current readiness status per workflow as of Phase 25:

| Workflow | Risk | Stage 1 (Repo) | Stage 2 (Import Runbook) | Phase 25 Readiness |
|----------|------|----------------|--------------------------|--------------------|
| `content_auto_skeleton` | Standard | DONE | DONE (Phase 20A/20B) | IMPORT COMPLETE — Phase 20C PASS |
| `creative_asset_auto_skeleton` | Standard | DONE | DONE (Phase 22A) | READY for import approval |
| `ads_pack_auto_skeleton` | HIGH RISK | DONE | NOT STARTED | NOT READY — import runbook needed first |
| `crm_followup_auto_skeleton` | HIGH RISK | DONE | NOT STARTED | NOT READY — import runbook needed first |
| `comment_inbox_reply_assistant_skeleton` | HIGH RISK | DONE | NOT STARTED | NOT READY — import runbook needed first |
| `approval_publishing_skeleton` | HIGH RISK | DONE | NOT STARTED | NOT READY — import runbook needed first |

**Next recommended import candidates:** `creative_asset_auto_skeleton` (Standard risk, evidence pack exists from Phase 22A).

HIGH RISK workflows require dedicated import runbooks before they may be considered for Owner approval.

---

## Section J — Rollback / Non-Import Path

If at any point the Owner decides not to proceed with sandbox import, or if the pre-import checklist fails, the following applies:

1. No import has occurred. There is nothing to roll back in n8n.
2. Return to documentation state. The repo remains unchanged.
3. Fix the blocking issue (documentation gap or safety concern).
4. Re-run the pre-import checklist from the beginning.
5. Do not carry forward partial approval — the Owner must re-issue the approval phrase.

**Partial completion of this checklist does not authorize any import.**
**A prior session's approval phrase does not carry forward to a new session.**

---

## Section K — Related Documents

| Document | Path | Purpose |
|----------|------|---------|
| Sandbox Import Readiness Checklist | [`docs/runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md`](runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md) | Copy-fillable checklist for each import event |
| Sandbox Import Test Runbook | [`docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md`](runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md) | Step-by-step import process (Phase 24A) |
| Owner Runtime Readiness Checklist | [`docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md`](runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md) | Full pre-action Owner readiness gate |
| Runtime Approval Decision Tree | [`docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md`](runbooks/RUNTIME_APPROVAL_DECISION_TREE.md) | Decision tree for approval level |
| Sandbox Evidence Pack Template | [`docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md`](runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md) | Evidence recording after import |
| Owner Approval Gate | [`docs/governance/OWNER_APPROVAL_GATE.md`](governance/OWNER_APPROVAL_GATE.md) | Formal gate definitions |
| Phase 24B Evidence Templates | [`docs/runbooks/SANDBOX_RUNBOOK_INDEX.md`](runbooks/SANDBOX_RUNBOOK_INDEX.md) | Index of all sandbox runbooks |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*Phase 25 is documentation-only. No runtime action is authorized by this document.*
*Sandbox import requires explicit Owner approval in the exact format specified in Section B.*
