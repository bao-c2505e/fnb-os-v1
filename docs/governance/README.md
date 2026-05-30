# Governance Directory — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 23 — Agent OS Layer)
Type: Index
Path: `docs/governance/`

---

## Purpose

This directory contains all agent-facing governance documents for FnB OS V1.
These documents define how agents start sessions, validate work, and interact with the Owner approval system.

They do not contain runtime automation logic, workflow JSON, or credentials.

---

## Document Index

### Start Here

| File | Description | When to use |
|------|-------------|-------------|
| [AGENT_OS_OPERATING_MANUAL.md](AGENT_OS_OPERATING_MANUAL.md) | **Main operating manual.** Agent roles, phase lifecycle, startup procedure, constraints, builder/reviewer rules, approval gates summary, session handoff rule, all doc links. | **First file every agent reads each session.** |
| [AGENT_STARTUP_CHECKLIST.md](AGENT_STARTUP_CHECKLIST.md) | **Quick-start checklist.** Identity check, repo check, source-of-truth check, safety check, output checklist. Checkbox format. | **Run before starting any work.** |

---

### Detailed Reference Documents

| File | Description | When to use |
|------|-------------|-------------|
| [AGENT_OPERATION_RULES.md](AGENT_OPERATION_RULES.md) | Full agent operation rules: 7-role roster, scope compliance, reviewer restrictions, no-secrets policy (13 patterns), no-runtime policy, no-customer-facing automation, session limit, end-of-session report format, commit/push gate table, guardrails summary. | When in doubt about a specific agent rule or constraint. |
| [REPO_VALIDATION_CHECKLIST.md](REPO_VALIDATION_CHECKLIST.md) | Full pre-commit validation: before-work state checks, changed file inspection, 13-pattern secret scan with REPLACE_WITH_* exception, workflow JSON check, runtime execution confirmation, handoff/log update check, commit message check, final gate table, push gate. | Before every `git commit`. |
| [PRE_COMMIT_PRE_PUSH_CHECKLIST.md](PRE_COMMIT_PRE_PUSH_CHECKLIST.md) | Quick-reference checkbox checklist for pre-commit and pre-push. Summarizes 4 gate types (pre-commit, pre-push, runtime, customer output). | Quick self-check before committing or pushing. |
| [OWNER_APPROVAL_GATE.md](OWNER_APPROVAL_GATE.md) | Formal definitions of all 10 approval gates: Planning, Build, Commit, Push, Runtime Import, Runtime Execution, Customer Output, Ads Spend, Publishing, Emergency Rollback. Each gate has trigger condition, blocking condition, and recording location. | Before any gated action. Key rule: commit ≠ push authorization. |
| [SESSION_HANDOFF_RULES.md](SESSION_HANDOFF_RULES.md) | Session continuity protocol: 10-exchange limit, required SESSION_SUMMARY fields (14 fields), new session start procedure, source-of-truth hierarchy (repo files > chat history > agent memory), long-context degradation mitigation, builder switching, Codex handoff, emergency stop. | Before ending any session or switching agents. |

---

## Reading Order for a New Session

```
1. handoff/CURRENT_PHASE.md          ← what phase are we on?
2. handoff/SESSION_SUMMARY.md        ← what happened last session?
3. handoff/PHASE_XX_HANDOFF.md       ← phase-specific context
4. docs/governance/AGENT_OS_OPERATING_MANUAL.md   ← rules + startup procedure
5. docs/governance/AGENT_STARTUP_CHECKLIST.md     ← run through checklist
```

Then refer to detailed docs as needed for commits, approvals, and handoff.

---

## Key Principles

These principles are enforced by every document in this directory:

1. **GitHub is source of truth** — repo files beat chat history, screenshots, and agent memory.
2. **Owner is final authority** — no agent self-authorizes any approval gate.
3. **No secrets** — no API keys, tokens, passwords, or credentials in any file.
4. **No runtime without Owner approval** — `"active": true` is never introduced by Builder.
5. **Commit ≠ push** — these are separate approval gates.
6. **Max 10 exchanges per session** — then update handoff and request a new session.
7. **Scope compliance** — Builder only touches `scope_files`; BLOCKED if a needed file is out of scope.

---

## Owner Runtime Runbooks

Owner-facing runtime readiness materials are in a separate directory:

| Directory | Purpose |
|-----------|---------|
| [docs/runbooks/](../runbooks/README.md) | Runbooks for sandbox import, sandbox execution, production runtime decisions. Owner-facing. Includes runtime readiness checklist, sandbox runbook index, import runbook, and approval decision tree. |

See [docs/runbooks/README.md](../runbooks/README.md) for the full runbook index.

---

## Phase History

| Phase | Contribution |
|-------|-------------|
| Phase 22 | Created this `docs/governance/` directory. Created: AGENT_OPERATION_RULES.md, REPO_VALIDATION_CHECKLIST.md, PRE_COMMIT_PRE_PUSH_CHECKLIST.md, OWNER_APPROVAL_GATE.md, SESSION_HANDOFF_RULES.md. |
| Phase 23 | Added Agent OS Layer. Created: AGENT_OS_OPERATING_MANUAL.md, AGENT_STARTUP_CHECKLIST.md, README.md (this file). |
| Phase 24A | Added Owner Runtime Runbooks directory (`docs/runbooks/`). Created: README.md, SANDBOX_RUNBOOK_INDEX.md, OWNER_RUNTIME_READINESS_CHECKLIST.md, SANDBOX_IMPORT_TEST_RUNBOOK.md, RUNTIME_APPROVAL_DECISION_TREE.md. |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*All governance documents are documentation-only. No runtime automation.*
