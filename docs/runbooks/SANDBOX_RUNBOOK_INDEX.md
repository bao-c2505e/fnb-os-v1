# Sandbox Runbook Index — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness)
Type: Runbook Index
Scope: All sandbox and runtime readiness activities for FnB OS V1

---

## Purpose

This index tracks all sandbox runbooks created for FnB OS V1 workflows, shows which phase documents each workflow, and defines which roles may use each runbook and what actions are allowed.

**Important:** Owning or reading a runbook does not authorize any runtime action. Each runtime action requires explicit Owner approval for that specific action at that specific time.

---

## Four Readiness Stages

| Stage | Description | Required Before |
|-------|-------------|----------------|
| **1 — Repo Documentation** | Workflow JSON committed. Governance docs complete. No import. | Nothing — baseline |
| **2 — Sandbox Import Readiness** | Runbook and evidence pack created. Owner has read and confirmed checklist. | Explicit Owner approval: "APPROVED FOR SANDBOX IMPORT ONLY" |
| **3 — Sandbox Manual Execution Readiness** | Workflow imported and inactive. Dummy payload ready. Evidence log template ready. | Explicit Owner approval: "APPROVED FOR SANDBOX MANUAL EXECUTION ONLY" — separate from import approval |
| **4 — Production Readiness** | Sandbox PASS recorded. Real credentials available. Real customer data policy confirmed. | Explicit Owner approval: "APPROVED FOR PRODUCTION RUNTIME ONLY" — never implied by sandbox PASS |

---

## Workflow Runbook Status

| Workflow | Risk | Stage 1 (Repo) | Stage 2 (Import Runbook) | Stage 3 (Execution Runbook) | Stage 4 (Production) |
|----------|------|----------------|--------------------------|------------------------------|----------------------|
| `content_auto_skeleton` | Standard | DONE — Phase 8 | DONE — Phase 20A/20B | DONE — Phase 20C (PASS recorded) | NOT STARTED |
| `creative_asset_auto_skeleton` | Standard | DONE — Phase 8 | DONE — Phase 22A (evidence pack) | NOT STARTED (Phase 22B pending) | NOT STARTED |
| `ads_pack_auto_skeleton` | HIGH RISK | DONE — Phase 8 | NOT STARTED | NOT STARTED | NOT STARTED |
| `crm_followup_auto_skeleton` | HIGH RISK | DONE — Phase 8 | NOT STARTED | NOT STARTED | NOT STARTED |
| `comment_inbox_reply_assistant_skeleton` | HIGH RISK | DONE — Phase 8 | NOT STARTED | NOT STARTED | NOT STARTED |
| `approval_publishing_skeleton` | HIGH RISK | DONE — Phase 8 | NOT STARTED | NOT STARTED | NOT STARTED |

---

## Runbook Document Index

### Existing Runbooks (Prior Phases)

| Runbook / Pack | Workflow | Stage | Phase | Doc Path | Status |
|----------------|----------|-------|-------|----------|--------|
| Manual Sandbox Evidence Capture Pack | `content_auto_skeleton` | 2 (Import Readiness) | Phase 20A | `docs/32_PHASE_20A_MANUAL_SANDBOX_EVIDENCE_CAPTURE_PACK.md` | COMMITTED (commit `50df2af`) |
| Owner Manual Sandbox Runbook | `content_auto_skeleton` | 3 (Execution) | Phase 20B | `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` | COMMITTED (commit `50df2af`) |
| Owner Evidence Submission | `content_auto_skeleton` | 3 (Execution PASS) | Phase 20C | `docs/34_PHASE_20C_OWNER_EVIDENCE_SUBMISSION_CONTENT_AUTO.md` | COMMITTED (commit `50df2af`) |
| Sandbox Manual Execution Expansion Plan | All 5 remaining workflows | 1 (Plan) | Phase 21 | `docs/35_PHASE_21_SANDBOX_MANUAL_EXECUTION_EXPANSION_PLAN.md` | COMMITTED (commit `7f8c7d2`) |
| Creative Asset Evidence Capture Pack | `creative_asset_auto_skeleton` | 2 (Import Readiness) | Phase 22A | `docs/36_PHASE_22A_CREATIVE_ASSET_SANDBOX_EVIDENCE_CAPTURE_PACK.md` | COMMITTED (commit `41186df`) |

### Phase 24A Runbooks

| Runbook | Stage | Doc Path | Status |
|---------|-------|----------|--------|
| Sandbox Runbook Index (this file) | All | `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` | Phase 24A — DONE |
| Owner Runtime Readiness Checklist | All | `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` | Phase 24A — DONE |
| Sandbox Import Test Runbook | 2 | `docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md` | Phase 24A — DONE |
| Runtime Approval Decision Tree | All | `docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md` | Phase 24A — DONE |

### Phase 24B Evidence and Log Templates

> **Phase 24B is documentation-only.** These templates do not authorize sandbox import or sandbox execution.
> Templates become usable in Phase 25+ (import) or Phase 26+ (execution) with explicit Owner approval.

| Template | Purpose | Stage | Doc Path | Status |
|----------|---------|-------|----------|--------|
| Sandbox Evidence Pack Template | Standard evidence record for any sandbox import or execution event | 2 and 3 | `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md` | Phase 24B — DONE |
| Sandbox Execution Log Template | Per-run detail log for Phase 26+ sandbox manual execution only | 3 | `docs/runbooks/SANDBOX_EXECUTION_LOG_TEMPLATE.md` | Phase 24B — DONE |
| Sandbox Test Data Register Template | Register and approve test data before sandbox execution | 3 | `docs/runbooks/SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md` | Phase 24B — DONE |
| Sandbox Issue Report Template | Document issues found during sandbox import or execution | 2 and 3 | `docs/runbooks/SANDBOX_ISSUE_REPORT_TEMPLATE.md` | Phase 24B — DONE |

### Phase 25 Import Readiness Gate

> **Phase 25 is documentation and readiness only.** This section does not authorize sandbox import.
> Import requires explicit Owner approval: `APPROVED FOR SANDBOX IMPORT ONLY — [workflow] — [date]`

| Document | Stage | Doc Path | Status |
|----------|-------|----------|--------|
| Sandbox Import Readiness Gate | 2 (Pre-import) | `docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md` | Phase 25 — DONE |
| Sandbox Import Readiness Checklist | 2 (Pre-import) | `docs/runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md` | Phase 25 — DONE |

### Future Runbooks (Not Yet Created)

| Runbook | Workflow | Stage | Future Phase |
|---------|----------|-------|-------------|
| Phase 22B Owner Sandbox Runbook | `creative_asset_auto_skeleton` | 3 (Execution) | Phase 22B |
| Phase 22C Evidence Submission | `creative_asset_auto_skeleton` | 3 (Execution record) | Phase 22C |
| Ads Pack Evidence Pack | `ads_pack_auto_skeleton` | 2 (Import Readiness) | Future |
| Ads Pack Execution Runbook | `ads_pack_auto_skeleton` | 3 (Execution) | Future |
| CRM Followup Evidence Pack | `crm_followup_auto_skeleton` | 2 | Future |
| CRM Followup Execution Runbook | `crm_followup_auto_skeleton` | 3 | Future |
| Comment Inbox Evidence Pack | `comment_inbox_reply_assistant_skeleton` | 2 | Future |
| Comment Inbox Execution Runbook | `comment_inbox_reply_assistant_skeleton` | 3 | Future |
| Approval Publishing Evidence Pack | `approval_publishing_skeleton` | 2 | Future |
| Approval Publishing Execution Runbook | `approval_publishing_skeleton` | 3 | Future |

---

## Role Permissions per Stage

| Role | Stage 1 (Repo Doc) | Stage 2 (Import) | Stage 3 (Execution) | Stage 4 (Production) |
|------|-------------------|-----------------|---------------------|----------------------|
| **Owner** | Read, review, approve | Read, approve, perform import | Read, approve, perform execution | Read, approve, perform production actions |
| **Claude Code (Builder)** | Create, edit runbooks and docs | Create evidence packs and runbooks; CANNOT perform import | CANNOT trigger or execute workflows | CANNOT interact with production |
| **Codex (Reviewer)** | Review runbooks and docs | Review evidence packs; CANNOT perform import | CANNOT trigger or execute workflows | CANNOT interact with production |
| **Future LangGraph Orchestrator** | Read governance docs | CANNOT perform import without Owner approval | CANNOT execute without Owner approval per-session | CANNOT access production without Owner approval |

---

## Allowed vs. Forbidden Actions

### Allowed at Each Stage

| Stage | Allowed Actions |
|-------|----------------|
| Stage 1 | Read repo files; create/edit documentation; run CI scripts locally; commit and push documentation changes; review runbooks and governance docs |
| Stage 2 (Import) | Import workflow JSON into a sandbox n8n instance (INACTIVE only); view workflow canvas; confirm node structure; do NOT activate; do NOT connect real credentials |
| Stage 3 (Execution) | Manually trigger workflow in sandbox using dummy data; observe node output; capture evidence screenshots; fill evidence log; do NOT activate; do NOT use real credentials |
| Stage 4 (Production) | Connect real credentials (only those explicitly approved); activate workflow; monitor execution; all require explicit Owner approval for each workflow |

### Forbidden at All Stages Unless Explicitly Approved

| Forbidden Action | Why |
|-----------------|-----|
| Set `"active": true` on any workflow | Enables automatic triggering — explicitly blocked |
| Connect real API credentials (OpenAI, Meta, Zalo, etc.) | Risk of real customer data or charges |
| Post to social media | Customer-facing — always requires Owner explicit approval |
| Reply to real customer messages | Customer-facing — always requires Owner explicit approval |
| Commit real ad spend (Meta Ads, TikTok Ads, Zalo Ads) | Financial risk — always requires Owner explicit approval |
| Call external paid APIs | Cost risk (OpenAI, image generation, etc.) |
| Use real customer PII (names, phones, emails) in test | Privacy risk |
| Claim production readiness based on sandbox PASS | Sandbox ≠ production |
| Use a higher-level approval to authorize a lower-level action at next stage | Each stage requires its own approval |

---

## Evidence Log Locations

| Workflow | Evidence Log Path | Phase |
|----------|------------------|-------|
| `content_auto_skeleton` | `logs/phase_20a_content_auto_sandbox_evidence_log.md` | Phase 20A/20B/20C |
| `creative_asset_auto_skeleton` | `logs/phase_22a_creative_asset_sandbox_evidence_log.md` | Phase 22A/22B/22C |
| `ads_pack_auto_skeleton` | `logs/phase_[XX]_ads_pack_sandbox_evidence_log.md` | Future |
| `crm_followup_auto_skeleton` | `logs/phase_[XX]_crm_followup_sandbox_evidence_log.md` | Future |
| `comment_inbox_reply_assistant_skeleton` | `logs/phase_[XX]_comment_inbox_sandbox_evidence_log.md` | Future |
| `approval_publishing_skeleton` | `logs/phase_[XX]_approval_publishing_sandbox_evidence_log.md` | Future |

---

## Related Documents

- [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) — pre-action readiness check
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — import step-by-step
- [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) — decision tree for approvals
- [docs/governance/OWNER_APPROVAL_GATE.md](../governance/OWNER_APPROVAL_GATE.md) — formal gate definitions (10 gates)
- [docs/governance/AGENT_OS_OPERATING_MANUAL.md](../governance/AGENT_OS_OPERATING_MANUAL.md) — agent session rules

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This index is documentation-only. No runtime action is performed or authorized by this document.*
