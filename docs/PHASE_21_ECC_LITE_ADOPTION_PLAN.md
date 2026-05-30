# Phase 21 — ECC Lite Brief Intake & Adoption Plan

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 21 — ECC Lite Brief Intake & Adoption Planning
**By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-30
**Status:** PLAN_READY — READY FOR OWNER REVIEW
**Brief source:** `docs/proposals/OS_V1_WORKFLOW_INFRA_ECC_LITE_ADOPTION_BRIEF.md`

---

## Section A — Executive Summary

The Owner uploaded an ECC Lite adoption brief outlining a strategic path to
evolve FnB OS V1 from a repo + n8n workflow + manual approval system into a
structured AI Agent Operating System. This document converts that brief into
a concrete, phased adoption plan with clear boundaries on what to build now,
what to defer, and what to reject entirely at this stage.

**Key decisions from the brief:**

1. Do NOT copy ECC wholesale (61 agents, 246 skills is too large).
2. Apply **ECC-lite** — a selective subset appropriate for a solo-owner F&B
   marketing OS.
3. Phase 20 CI Safety Gate is already DONE — it was the correct first step.
4. Phase 21 next: build the **Agent Operating Layer** (`/00_AGENT_OS`).
5. Production infrastructure (Docker, Supabase, Coolify) only after OS V1 is
   stable at the workflow + approval + log level.

**OS V1 current production readiness score (from brief):**

| After | Score |
|-------|-------|
| Before Phase 20 | ~4/10 |
| After Phase 20 CI | ~6/10 |
| Target after ECC Lite | ~8/10 |

---

## Section B — What ECC Lite Means for FnB OS V1

ECC (Everything Claude Code) defines a full agent operating layer with memory,
skills, hooks, schemas, and structured agent roles. ECC-lite is the
right-sized subset for OS V1:

| ECC Concept | ECC Full | ECC-lite for OS V1 |
|-------------|----------|--------------------|
| Agents | 61 agents | 8 agents (Chief Architect, Builder, Reviewer, Security, Validator, Doc Maintainer, Sandbox Reporter, Brand Strategist) |
| Skills | 246 skills | 15 skills (core marketing + governance) |
| Hooks | Automated git hooks | Checklist-based pre-commit/pre-push gates |
| Memory | Distributed memory files | 5 files (decisions, constraints, known-issues, patterns, learning-log) |
| Schemas | Full output typing | 8 schemas (task, review, skill, handoff, validation, security, sandbox, approval) |
| CI | Full CI/CD pipeline | GitHub Actions safety gate (DONE — Phase 20) |
| Runtime | Docker + Coolify + Sentry | n8n + Google Sheet + approval gate |

**Core insight from brief:**

> "Thứ cần build tiếp không phải thêm thật nhiều workflow, mà là lớp vận
> hành giúp AI agent làm việc có luật, có kiểm tra, có trí nhớ, có bảo mật
> và có khả năng scale."

---

## Section C — Recommended Adoption Scope for V1

### Adopt Now (Phase 21 → 23)

| Item | Phase | Reason |
|------|-------|--------|
| Agent Operating Layer `/00_AGENT_OS` | Phase 21 (next) | Core structure needed before any skill or memory work |
| 8 agent profiles | Phase 21 | Formalizes existing roles; prevents scope drift |
| Memory layer (5 files) | Phase 21 | Preserves decisions across sessions |
| Hooks checklist (doc-level) | Phase 21 | Pre-commit/pre-push gates as markdown until Husky is warranted |
| 8 schemas in `/00_AGENT_OS/schemas` | Phase 21 | Structured output foundation |
| 15 core skills | Phase 22 | Reusable skill packs for marketing modules |
| Runtime observability schemas | Phase 23 | Log format + error classification |
| Prettier for .md/.json/.yml | Phase 21 (optional) | Format consistency — low risk, high benefit |

### Delay (Phase 24+)

| Item | Delay Until | Reason |
|------|-------------|--------|
| Docker / Docker Compose | Phase 24 | Not needed until production VPS deployment |
| Supabase | OS V1.5 | Google Sheet adequate for current scale |
| Coolify | Phase 24 | No app/API/dashboard service yet |
| Sentry | Phase 24 | No web app or production API to monitor |
| PostHog | OS V2 | No user dashboard or funnel to track |

### Reject Now

| Item | Reason |
|------|--------|
| Full ECC (61 agents, 246 skills) | Scope too large for solo-owner F&B OS; over-engineering |
| ESLint | No JS/TS source files to lint; repo is markdown + JSON + n8n |
| Husky | Team of one + AI agents; no large local dev team committing |
| MCP (Model Context Protocol) | Premature — repo + n8n CI not fully stable yet |
| Next.js dashboard | OS V2 scope — not V1 |
| LangGraph orchestrator | OS V2 scope |
| Multi-brand infrastructure | OS V2 scope |

---

## Section D — Items to Adopt Now (Detail)

### D1. `/00_AGENT_OS` Directory Structure

Create the root Agent Operating Layer directory with four sub-directories:

```
/00_AGENT_OS
  /agents        -- 8 agent profile markdown files
  /hooks         -- pre-commit and pre-push gate checklists
  /memory        -- 5 persistent memory files
  /schemas       -- 8 JSON schemas for structured agent output
```

This is the Phase 21 Agent Operating Layer deliverable (from brief Section 5–9).

### D2. Agent Profiles (8 agents)

Each agent file defines: role, allowed actions, forbidden actions, output
format, handoff behavior. Agents:

1. `chief-architect.md` — Phases, design, task writing, scope decisions
2. `claude-builder.md` — File creation, workflow build, doc/log updates
3. `codex-reviewer.md` — Review only; 6 defined blocker conditions
4. `security-reviewer.md` — Secret scan, credential check, webhook exposure
5. `n8n-workflow-validator.md` — JSON validity, active=false, importability
6. `documentation-maintainer.md` — README, CURRENT_PHASE, logs, handoff sync
7. `sandbox-test-reporter.md` — Evidence packs, execution results, no live data
8. `brand-marketing-strategist.md` — Brand Brain guard, tone review, output QA

### D3. Memory Layer (5 files)

Persistent cross-session knowledge base:

1. `decisions.md` — Confirmed architectural and operational decisions
2. `constraints.md` — Rules that must never be violated
3. `known-issues.md` — Bugs and workarounds discovered in operation
4. `reusable-patterns.md` — Proven patterns (phase-based delivery, evidence packs, etc.)
5. `agent-learning-log.md` — Lessons for agents across sessions

### D4. Hooks Checklist (doc-level)

Two checklist files (markdown, not code hooks yet):

1. `pre-commit-checklist.md` — 8 checks before any commit
2. `pre-push-checklist.md` — 5 checks before any push

Husky-based automation deferred to Phase 24+ per brief Section 3.3.

### D5. Schemas (8 files)

Structured JSON schemas for AI agent output in `/00_AGENT_OS/schemas`:

1. `agent_task.schema.json`
2. `review_report.schema.json`
3. `skill_output.schema.json`
4. `phase_handoff.schema.json`
5. `workflow_validation_report.schema.json`
6. `security_scan_report.schema.json`
7. `sandbox_execution_report.schema.json`
8. `approval_gate.schema.json`

---

## Section E — Required Repo Structure Updates

From brief Section 5 and current repo state:

| Change | Status |
|--------|--------|
| Create `/00_AGENT_OS/agents/` | Phase 21 next |
| Create `/00_AGENT_OS/hooks/` | Phase 21 next |
| Create `/00_AGENT_OS/memory/` | Phase 21 next |
| Create `/00_AGENT_OS/schemas/` | Phase 21 next |
| Move brief to `docs/proposals/` | DONE (this phase) |
| GitHub Actions CI | DONE (Phase 20) |
| `scripts/` Python validators | DONE (Phase 20) |
| Prettier config | Optional (Phase 21) |

No changes to existing `n8n/workflows/`, `schemas/`, `docs/` numbered docs,
`handoff/`, `logs/`, or `samples/` are required by Phase 21.

---

## Section F — Required Workflow/Runtime Governance Updates

Based on brief Section 7 (Hooks/Gates):

### Pre-Commit Gate (documentation checklist)

Before any commit, verify:

| Check | Gate |
|-------|------|
| Files within phase scope | Builder responsibility |
| No unexpected new files | Builder + Codex |
| No secrets in staged files | `scripts/check_no_secrets.py` |
| `.env` not staged | `.gitignore` enforced |
| Workflow JSON valid | `scripts/validate_json.py` |
| n8n workflows `active=false` | `scripts/check_n8n_workflows.py` |
| PHASE_LOG updated | Builder responsibility |
| SESSION_SUMMARY / CURRENT_PHASE updated | Builder responsibility |

### Pre-Push Gate (documentation checklist)

Before any push, verify:

| Check | Gate |
|-------|------|
| `git status` clean after commit | Required |
| Commit message matches phase | Required |
| No credential in any committed file | `scripts/check_no_secrets.py` |
| Owner has given push approval | Owner verbal confirmation |
| Codex PASS (if phase requires review) | Codex gate |

### CI Required Checks (already implemented — Phase 20)

| Check | Script |
|-------|--------|
| JSON validity | `scripts/validate_json.py` |
| Secret patterns | `scripts/check_no_secrets.py` |
| n8n `active=false` | `scripts/check_n8n_workflows.py` |

---

## Section G — Safety Rules

Carried forward from brief Section 1, Section 4, and OS V1 CLAUDE.md:

| Rule | Enforcement |
|------|-------------|
| No hardcoded API keys, tokens, passwords | CI + secret scan |
| No `.env` committed | `.gitignore` |
| No `active=true` in n8n workflow JSON | CI + check_n8n_workflows.py |
| No auto-post to real platforms | No platform publish API in skeleton nodes |
| No auto-reply to real customers | No messaging API in activated state |
| No ads spend without Owner approval | No Meta/TikTok/Zalo Ads credential |
| No push without Owner approval | Protocol (not automated) |
| No scope creep beyond active phase | Builder + Codex gate |
| One Builder per phase | AGT-02 (Claude Code) |
| Codex does not commit or push | Role constraint |
| Owner approval before any production action | Approval gate |

---

## Section H — Suggested Future Phases

Aligned with brief Section 10 and brief Sections 3.1–3.2:

| Phase | Name | Scope |
|-------|------|-------|
| **Phase 21 (this)** | ECC Lite Brief Intake & Adoption Plan | Brief moved, plan created |
| **Phase 21 Agent** | Agent Operating Layer | `/00_AGENT_OS` structure, 8 agents, memory, hooks, schemas |
| **Phase 22 Skills** | FnB Marketing Skill Pack | 15 skills with input/output schema + checklist |
| **Phase 23** | Runtime Observability Foundation | Log schema, error report, approval history |
| **Phase 24+** | Production Infrastructure | Docker, Supabase, Coolify, Sentry, PostHog |

**Note on naming:** The existing repo also uses "Phase 21" and "Phase 22" for
sandbox execution sub-phases (20A/20B/20C series). These are separate
numbering tracks from the ECC Lite roadmap phases. Future phase numbering
will be aligned with the brief's roadmap.

---

## Section I — Owner Approval Gates

| Gate | Condition | Action |
|------|-----------|--------|
| Phase 21 Agent start | Owner reviews this plan + Codex PASS | Builder begins `/00_AGENT_OS` build |
| Phase 22 Skills start | Phase 21 Agent DONE + committed | Builder begins skill pack |
| Phase 23 start | Phase 22 DONE + committed | Builder begins observability schemas |
| Any production workflow activation | Owner OWNER_APPROVED + Codex PASS | n8n activation in production |
| Any real data execution | Owner OWNER_APPROVED + evidence log ready | Execution with real brand data |
| Any push to GitHub | Owner verbal/written approval | `git push` executed |

---

## Section J — What This Phase Does NOT Do

| Non-Goal | Reason |
|----------|--------|
| Does not create `/00_AGENT_OS` yet | That is Phase 21 Agent (next phase) |
| Does not create skill files | Phase 22 scope |
| Does not modify n8n workflows | Not in scope |
| Does not activate any workflow | Never without Owner approval |
| Does not implement Prettier | Optional — deferred to Phase 21 Agent |
| Does not implement Docker/Supabase/Coolify | Phase 24+ scope |
| Does not claim production readiness | Documentation-first phase |
| Does not run any paid ads | Forbidden |
| Does not auto-post or auto-reply | Forbidden |

---

## Section K — Safety Confirmations

| Check | Status |
|-------|--------|
| Workflow JSON modified | NO |
| `active: true` introduced | NO |
| Real credentials added | NO |
| Real customer data | NO |
| Workflow execution performed | NO |
| Auto-post | NO |
| Auto-reply | NO |
| Ads spend | NO |
| Brief file deleted | NO — moved to `docs/proposals/` |
| Secret scan (new files) | CLEAN |
| Branch | main |
| Latest commit before this phase | 26ba8dc |

---

## Section L — Codex Review Checklist

| Item | Verify |
|------|--------|
| CR-01 | Brief moved to `docs/proposals/`, not deleted |
| CR-02 | Adoption plan covers all 9 required sections (A–I) |
| CR-03 | Adoption scope table is complete (now / delay / reject) |
| CR-04 | Safety rules in Section G match CLAUDE.md constraints |
| CR-05 | Suggested future phases align with brief Section 10 |
| CR-06 | Owner approval gates are explicit (Section I) |
| CR-07 | No credentials in any new file |
| CR-08 | No n8n workflow JSON modified |
| CR-09 | No `active: true` introduced |
| CR-10 | Non-goals list complete (Section J) |
