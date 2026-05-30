# Phase 24A Handoff — Sandbox Runbook Index & Owner Runtime Readiness

Created By: Claude Code (Builder, AGT-02) — 2026-05-30
Phase: 24A — Sandbox Runbook Index & Owner Runtime Readiness
Type: Documentation / Governance — Runbooks
Branch: main

---

## Phase Name and Objective

**Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness**

Create documentation-only runtime readiness materials — a `docs/runbooks/` directory containing an index, an Owner-facing checklist, a sandbox import runbook, and a runtime approval decision tree — so the Owner knows when and how sandbox/runtime import/test may be allowed in the future.

Documentation/governance only. No runtime automation. No n8n workflow changes. No CI/CD.

---

## Files Created

| File | Description |
|------|-------------|
| `docs/runbooks/README.md` | Runbooks directory index. Explains purpose, four readiness levels, runbook index table, reading order, key principles, and relationship to governance docs. |
| `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` | Master index of all workflow runbooks. Shows which workflows are at which readiness stage, which roles may use each runbook, allowed vs. forbidden actions table, evidence log locations, and links to future runbooks. |
| `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` | Owner-facing pre-action checklist (12 sections, A–L): repo state checks, phase handoff exists, Codex PASS exists, no secrets, workflow JSON safety, approval gate documentation, test data confirmation, output safety, rollback note, evidence capture plan, explicit approval phrase templates, final pre-action sign-off with Owner sign-off block. |
| `docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md` | Step-by-step guide for future safe sandbox import. Covers: 13 preconditions, allowed actions, forbidden actions, 10-step import flow, evidence capture, failure handling (import fail, credential errors, active=true, node version mismatch), stop conditions, and strong warning that import ≠ execution approval. |
| `docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md` | Decision tree in markdown for determining approval level. Q1–Q9 cover: documentation only, sandbox import, sandbox execution, production runtime, production credentials, real customers, public posting, ads/campaign/budget, session-specific approval. Four outcomes defined plus BLOCKED default. |
| `handoff/PHASE_24A_HANDOFF.md` | This file. |

---

## Files Updated

| File | Change |
|------|--------|
| `docs/governance/README.md` | Added "Runbooks" section linking to `docs/runbooks/` with a one-line description. |
| `docs/governance/OWNER_APPROVAL_GATE.md` | Added "Related Runbooks" note at the bottom of the Related section. |
| `handoff/CURRENT_PHASE.md` | Updated to Phase 24A BUILD_READY |
| `handoff/SESSION_SUMMARY.md` | New Phase 24A entry prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | New Phase 24A row prepended |
| `09_LOGS/PHASE_LOG.md` | New Phase 24A entry prepended |

---

## Files NOT Modified

| File | Status |
|------|--------|
| All `n8n/workflows/*.json` (6 files) | UNTOUCHED |
| `.github/workflows/repo-safety-check.yml` | UNTOUCHED |
| `scripts/validate_json.py` | UNTOUCHED |
| `scripts/check_no_secrets.py` | UNTOUCHED |
| `scripts/check_n8n_workflows.py` | UNTOUCHED |
| `docs/governance/AGENT_OS_OPERATING_MANUAL.md` | UNTOUCHED |
| `docs/governance/AGENT_STARTUP_CHECKLIST.md` | UNTOUCHED |
| `docs/governance/AGENT_OPERATION_RULES.md` | UNTOUCHED |
| `docs/governance/REPO_VALIDATION_CHECKLIST.md` | UNTOUCHED |
| `docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md` | UNTOUCHED |
| `docs/governance/SESSION_HANDOFF_RULES.md` | UNTOUCHED |
| All schema JSON files | UNTOUCHED |
| All sample output files | UNTOUCHED |
| All prior phase docs (20A–23) | UNTOUCHED |
| `.env` | UNTOUCHED / gitignored |

---

## What Phase 24A Adds

Phase 23 completed the Agent OS Layer (AGENT_OS_OPERATING_MANUAL, AGENT_STARTUP_CHECKLIST, governance README). Phase 24A creates the Owner-facing runtime readiness layer — the missing bridge between "repo documentation complete" and "Owner ready to safely use the sandbox."

| Before Phase 24A | After Phase 24A |
|-----------------|----------------|
| No consolidated index of which workflows have runbooks | `SANDBOX_RUNBOOK_INDEX.md` — 6 workflows tracked across 4 stages |
| No single Owner pre-action checklist | `OWNER_RUNTIME_READINESS_CHECKLIST.md` — 12-section checklist with sign-off |
| No explicit approval phrase templates | Three approval phrase templates: import / execution / production |
| No decision tree for "is this allowed?" | `RUNTIME_APPROVAL_DECISION_TREE.md` — Q1–Q9 with four outcomes |
| No consolidated sandbox import guide | `SANDBOX_IMPORT_TEST_RUNBOOK.md` — 13 preconditions + 10-step flow |
| No `docs/runbooks/` directory | `docs/runbooks/` created with README and 4 runbooks |

---

## Runtime Safety Confirmation

| Check | Result |
|-------|--------|
| n8n workflow executed | NO |
| External API called | NO |
| Live workflow triggered | NO |
| Production system modified | NO |
| Real credentials added | NO |
| Real customer data used | NO |
| Auto-post performed | NO |
| Auto-reply performed | NO |
| Ads spend committed | NO |
| Workflow JSON modified | NO |
| `"active": true` introduced | NO |
| Secret scan (new files) | CLEAN — all new files contain only documentation text |
| `docs/runbooks/` files contain secrets | NO |

---

## Acceptance Criteria

| Criterion | Status |
|-----------|--------|
| `docs/runbooks/README.md` created | PASS |
| README explains four readiness levels | PASS |
| README links all runbook files | PASS |
| README states no runtime without Owner approval | PASS |
| `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` created | PASS |
| Index table covers all 6 workflows across 4 stages | PASS |
| Index defines role permissions (Owner / Builder / Codex / LangGraph) | PASS |
| Index lists allowed vs. forbidden actions | PASS |
| `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` created | PASS |
| Checklist covers all required items (repo state, secrets, active=false, approval gate, test data, output safety, rollback, evidence, sign-off) | PASS |
| Explicit approval phrase templates provided (import / execution / production) | PASS |
| `docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md` created | PASS |
| Runbook covers preconditions, allowed/forbidden actions, 10-step flow | PASS |
| Runbook covers what to do on import fail, credential errors, active=true, node version mismatch | PASS |
| Runbook states import ≠ execution approval | PASS |
| `docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md` created | PASS |
| Decision tree covers Q1–Q9 (documentation, import, execution, production, customers, publishing, ads, session approval) | PASS |
| Four outcomes defined (Documentation, Import, Execution, Production) | PASS |
| BLOCKED default stated | PASS |
| Auto-post / auto-reply / ads spend blocked by default | PASS |
| `docs/governance/README.md` updated to link runbooks | PASS |
| `docs/governance/OWNER_APPROVAL_GATE.md` updated with runbook reference | PASS |
| `handoff/PHASE_24A_HANDOFF.md` created | PASS |
| `handoff/CURRENT_PHASE.md` updated | PASS |
| `handoff/SESSION_SUMMARY.md` updated | PASS |
| `09_LOGS/PHASE_LOG.md` updated | PASS |
| `logs/AGENT_ACTIVITY_LOG.md` updated | PASS |
| No workflow JSON modified | PASS |
| No runtime action performed | PASS |
| No secrets added | PASS |
| Markdown links are valid relative links | PASS |
| Governance docs link to runbooks | PASS |

---

## No-Execution Confirmation

| Item | Confirmed |
|------|-----------|
| n8n workflow executed | NO |
| External API called | NO |
| Live workflow triggered | NO |
| Production system modified | NO |
| Real credentials added | NO |
| Real customer data used | NO |
| Auto-post performed | NO |
| Auto-reply performed | NO |
| Ads spend committed | NO |
| Workflow JSON modified | NO |
| `"active": true` introduced | NO |

---

## Owner Next Action

1. Review 5 new files in `docs/runbooks/`: `README.md`, `SANDBOX_RUNBOOK_INDEX.md`, `OWNER_RUNTIME_READINESS_CHECKLIST.md`, `SANDBOX_IMPORT_TEST_RUNBOOK.md`, `RUNTIME_APPROVAL_DECISION_TREE.md`.
2. Review `handoff/PHASE_24A_HANDOFF.md`.
3. If approved: say `OWNER_APPROVED` and authorize local commit.
4. Verify commit completes cleanly.
5. Decide whether to push to GitHub (separate authorization required from commit authorization).

---

## Codex Review Instructions (when available)

1. Review `docs/runbooks/README.md` — confirm: four readiness levels clear, runbook links correct, no runtime claimed.
2. Review `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` — confirm: workflow status table accurate (Phase 14 PASS for import, Phase 20C PASS for content_auto execution, Phase 22A evidence pack for creative_asset), role permissions complete, forbidden actions table accurate.
3. Review `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` — confirm: all required checklist items present, approval phrase templates are explicit, no secrets or credentials in the file.
4. Review `docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md` — confirm: preconditions complete, forbidden actions clear, failure handling covers all critical scenarios, import ≠ execution warning explicit.
5. Review `docs/runbooks/RUNTIME_APPROVAL_DECISION_TREE.md` — confirm: Q1–Q9 logic is sound, outcomes correctly match gate definitions in `docs/governance/OWNER_APPROVAL_GATE.md`, auto-post/auto-reply/ads blocked by default.
6. Confirm: governance docs (`docs/governance/README.md`, `docs/governance/OWNER_APPROVAL_GATE.md`) updated to link runbooks.
7. Output: PASS / PASS WITH NOTES / BLOCK.

---

## Recommended Next Phase Options

**Option 1: Phase 24B — Sandbox Evidence Pack Template & Execution Log Standardization**
Create standardized evidence pack templates and execution log formats for all remaining HIGH RISK workflows (ads_pack, crm_followup, comment_inbox_reply, approval_publishing). These templates will guide Owner through Phases that expand beyond the current content_auto and creative_asset sandbox tracks.

**Option 2: Phase 24C — Governance QA Cleanup for Stale Text and Startup Order Alignment**
Review all governance docs for stale references, mismatched file paths, and startup order inconsistencies. Requires Codex availability for systematic review. Lower priority than Phase 24B.

**Option 3: Phase 22B — Creative Asset Sandbox Execution Runbook**
Create the Phase 22B Owner execution runbook for `creative_asset_auto_skeleton` (the evidence pack was created in Phase 22A but the execution runbook has not been built). Direct continuation of the sandbox execution track.

**Option 4: Phase 25 — Runtime Observability Evidence Templates**
Create structured templates for capturing n8n execution panel screenshots, node output JSON, and log entry evidence in a standardized format usable across all future sandbox and production phases.

**Owner decides which track to prioritize.**

---

## Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 20 CI | Repository CI & Runtime Safety Gate | DONE — commit `26ba8dc` |
| Phase 21 ECC Lite | Brief Intake & Adoption Planning | DONE — commit `7f8c7d2` |
| Phase 22 Governance | ECC Lite Repo Governance (5 governance docs) | DONE — commit `d34306e` |
| Phase 23 Agent OS | Agent OS Layer / Protocol Index | DONE — commit `41186df` |
| **Phase 24A Runbooks** | **Sandbox Runbook Index & Owner Runtime Readiness (this phase)** | **BUILD_READY** |
| Phase 24B | Sandbox Evidence Pack Template & Execution Log Standardization | FUTURE |
| Phase 24C | Governance QA Cleanup | FUTURE (requires Codex) |
| Phase 22B | Creative Asset Sandbox Execution Runbook | FUTURE |
| Phase 25 | Runtime Observability Evidence Templates | FUTURE |
