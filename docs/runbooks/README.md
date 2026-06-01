# Runbooks Directory — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness)
Type: Index
Path: `docs/runbooks/`

---

## Purpose

This directory contains **Owner-facing runbooks** for FnB OS V1.
Runbooks guide the Owner through decisions and actions related to runtime readiness, sandbox testing, and production approval.

They do not contain runtime automation logic, workflow JSON, or credentials.
**No file in this directory authorizes runtime execution. Runtime execution always requires explicit Owner approval.**

---

## Four Levels of Readiness — Know Where You Are

| Level | What It Means | Who Acts | Runtime Action? |
|-------|--------------|---------|-----------------|
| 1 — Documentation / Repo | Files exist in repo. Governance and workflow JSON committed. No import has occurred. | Builder, Reviewer | **None** |
| 2 — Sandbox Import | Workflow JSON imported into a sandbox n8n instance. Workflow is INACTIVE. No execution. | Owner only | **Import only** — requires explicit Owner approval |
| 3 — Sandbox Manual Execution | Owner manually triggers a workflow in sandbox using dummy data. Workflow is still INACTIVE. | Owner only | **Manual test only** — requires explicit Owner approval, separate from import approval |
| 4 — Production Runtime | Workflow connected to real credentials, real customers, real budget. | Owner only | **Production** — requires explicit Owner approval, separate from all sandbox approvals |

> **Critical rule:** Moving from one level to the next always requires a new, explicit Owner approval for that specific action.
> Sandbox import approval does NOT authorize sandbox execution.
> Sandbox execution approval does NOT authorize production runtime.

---

## Runbook Index

| File | Purpose | When to Use |
|------|---------|------------|
| [README.md](README.md) | This file — directory overview and reading guide. | First read in this directory. |
| [SANDBOX_RUNBOOK_INDEX.md](SANDBOX_RUNBOOK_INDEX.md) | Master index of all runbooks: which workflows have been runbooked, which roles use each runbook, allowed vs. forbidden actions, and the four readiness levels. | When deciding which runbook to use or checking overall sandbox status. |
| [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) | Owner-facing checklist to verify repo and environment are ready before any runtime action. Includes explicit approval phrase templates. | Before any sandbox import, sandbox execution, or production runtime decision. |
| [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) | Step-by-step guide for future safe sandbox import and test. Covers preconditions, allowed actions, forbidden actions, evidence capture, and failure handling. | When Owner is preparing for or executing sandbox import. |
| [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) | Decision tree for determining whether a runtime action is allowed. Answers: Is this documentation? Sandbox import? Sandbox execution? Production? Touches real customers? | Before any runtime action to confirm what approval level applies. |

**Phase 25 Import Readiness Gate** — *documentation and readiness only; does not authorize import:*

| File | Purpose | When to Use |
|------|---------|------------|
| [SANDBOX_IMPORT_READINESS_CHECKLIST.md](SANDBOX_IMPORT_READINESS_CHECKLIST.md) | Copy-fillable pre-import readiness checklist. 7 sections covering repo state, workflow identity, sandbox target, credential safety, forbidden actions, evidence readiness, and Owner approval phrase. | Copy and fill before requesting Owner sandbox import approval. |

See also: [`docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md`](../PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md) for the full gate reference.

**Phase 24B Evidence and Log Templates** — *templates only; do not authorize runtime action:*

| File | Purpose | When to Use |
|------|---------|------------|
| [SANDBOX_EVIDENCE_PACK_TEMPLATE.md](SANDBOX_EVIDENCE_PACK_TEMPLATE.md) | Standard evidence recording template for any sandbox import or sandbox execution event. Covers pre-checks, action description, screenshots, safety checks, and Owner review. | Copy and fill for each sandbox import (Phase 25+) or sandbox execution (Phase 26+) event. |
| [SANDBOX_EXECUTION_LOG_TEMPLATE.md](SANDBOX_EXECUTION_LOG_TEMPLATE.md) | Per-run detail log for Phase 26+ sandbox manual execution. Not usable in Phase 24B. Records input, nodes observed, output, errors, and post-execution safety checks. | Copy and fill for each manual execution run in Phase 26+ only. |
| [SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md](SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md) | Template for registering test data sets before sandbox execution. Prohibits real customer PII by default. Requires Owner approval before use. | Copy and fill when preparing test data for sandbox execution. |
| [SANDBOX_ISSUE_REPORT_TEMPLATE.md](SANDBOX_ISSUE_REPORT_TEMPLATE.md) | Template for documenting issues found during sandbox import or execution. Covers severity, reproduction, safety boundary check, fix notes, and resolution. | Copy and fill when any issue is found during sandbox activity. |

---

## Reading Order

```
1. RUNTIME_APPROVAL_DECISION_TREE.md    ← determine what category of action this is
2. OWNER_RUNTIME_READINESS_CHECKLIST.md ← verify repo + environment are ready
3. SANDBOX_RUNBOOK_INDEX.md             ← confirm which workflow and which runbook applies
4. SANDBOX_IMPORT_TEST_RUNBOOK.md       ← follow if performing sandbox import
```

Per-workflow runbooks (Phase 20B, Phase 22A) are in `docs/` and listed in `SANDBOX_RUNBOOK_INDEX.md`.

---

## Key Principles

1. **No runtime execution without explicit Owner approval** — documentation and repo work never imply runtime permission.
2. **Each level requires its own approval** — import ≠ execution approval; sandbox ≠ production approval.
3. **No automation without Owner approval** — auto-post, auto-reply, and ads spend are always blocked by default.
4. **Sandbox is not production** — a PASS in sandbox does not mean the workflow is production-ready.
5. **Owner is the only authority** — no agent (Builder, Reviewer, Architect) may self-authorize any runtime action.

---

## Relationship to Governance Docs

| These runbooks... | ...complement governance docs in `docs/governance/` |
|-------------------|-----------------------------------------------------|
| Guide Owner decisions about runtime | Governance docs guide agent behavior in sessions |
| Focus on sandbox and production readiness | Governance docs focus on repo, commits, and approval gates |
| Are Owner-facing | Governance docs are agent-facing |

See [docs/governance/OWNER_APPROVAL_GATE.md](../governance/OWNER_APPROVAL_GATE.md) for formal gate definitions.
See [docs/governance/README.md](../governance/README.md) for the full governance index.

---

## Phase History

| Phase | Contribution |
|-------|-------------|
| Phase 24A | Created this `docs/runbooks/` directory. Created: README.md, SANDBOX_RUNBOOK_INDEX.md, OWNER_RUNTIME_READINESS_CHECKLIST.md, SANDBOX_IMPORT_TEST_RUNBOOK.md, RUNTIME_APPROVAL_DECISION_TREE.md. |
| Phase 24B | Added evidence and log templates (documentation-only). Created: SANDBOX_EVIDENCE_PACK_TEMPLATE.md, SANDBOX_EXECUTION_LOG_TEMPLATE.md, SANDBOX_TEST_DATA_REGISTER_TEMPLATE.md, SANDBOX_ISSUE_REPORT_TEMPLATE.md. |
| Phase 25 | Added sandbox import readiness gate (documentation-only). Created: SANDBOX_IMPORT_READINESS_CHECKLIST.md. Full gate doc at `docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md`. |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*All runbooks are documentation-only. No runtime automation is performed or authorized by any file in this directory.*
