# 24 — n8n Import Dry-Run Readiness Gate

**Phase:** 12 — n8n Import Dry-Run Execution Readiness
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Purpose:** Define the readiness gate that must be satisfied before the Owner/operator performs the actual n8n import dry-run.

---

## What This Document Is

This is the **readiness gate** for the n8n import dry-run. It specifies the criteria that must be met — on both the repo side and the environment side — before the actual import session begins.

### Phase Distinction

| Phase | Role | Output |
|-------|------|--------|
| Phase 10 | Procedure | Step-by-step import dry-run instructions (`docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`) |
| Phase 11 | Evidence / Checklist Pack | Pre-structured evidence log + quick-reference checklist (`logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md`, `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md`) |
| Phase 12 | Readiness Gate | This document — criteria check before actual execution begins |

**Phase 12 does NOT execute the dry-run.** It verifies that the repo and environment are ready for the Owner to execute it safely.

---

## Hard Constraints

The following are non-negotiable before any import session begins:

1. **n8n instance must be test/sandbox only** — not the production instance.
2. **Import only** — no workflow activation (`active` must remain `false` after import).
3. **Placeholder credentials only** — no real API keys, tokens, passwords, or secrets.
4. **No production posting** — no content published to social media.
5. **No auto-reply** — no messages sent to real customers.
6. **No ads spend** — no Meta/TikTok/Zalo Ads budget committed.
7. **Evidence log must be prepared** before starting — copy and open `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md`.
8. **Owner is the operator** — Builder does not execute, approve, or validate the live environment.

---

## GO / NO-GO Criteria

### Repo-Side Criteria (Builder-verifiable)

| ID | Criterion | Required State | Status |
|----|-----------|---------------|--------|
| R-01 | Phase 8 workflow JSON files present | All 6 files exist in `n8n/workflows/` | VERIFIED — see Phase 8 (commit `ad867b3`) |
| R-02 | Phase 8 workflow JSON files untouched | No modifications since commit `ad867b3` | VERIFIED — Phase 12 build confirms no changes |
| R-03 | `active: false` in all workflow JSONs | Each JSON has `"active": false` | VERIFIED — Phase 10 manual inspection PASS |
| R-04 | No real credentials in workflow JSONs | All placeholders use `REPLACE_WITH_*` format | VERIFIED — Phase 10 secret scan CLEAN (42 checks) |
| R-05 | Phase 10 procedure document present | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` exists | VERIFIED |
| R-06 | Phase 11 evidence log present | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` exists | VERIFIED |
| R-07 | Phase 11 checklist present | `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` exists | VERIFIED |
| R-08 | Phase 11 evidence template present | `logs/templates/N8N_IMPORT_DRY_RUN_EVIDENCE_TEMPLATE.md` exists | VERIFIED |
| R-09 | Validation script present | `scripts/validate_n8n_workflows.mjs` exists | VERIFIED |
| R-10 | Static validation result documented | Phase 10 manual inspection: 66 checks PASS | VERIFIED |

**Repo-side gate:** All R-01 through R-10 are VERIFIED. **Repo is READY.**

---

### Environment-Side Criteria (Owner-verifiable — NOT auto-checked)

These criteria require Owner action. Builder cannot verify these without access to the Owner's machine and n8n instance.

| ID | Criterion | Required State | Owner Action |
|----|-----------|---------------|-------------|
| E-01 | Node.js version | `node --version` returns >= 16.x | Run `node --version`. If not found: install from nodejs.org |
| E-02 | Validation script passes | `node scripts/validate_n8n_workflows.mjs` exits 0 | Run script from repo root. Resolve any failures before proceeding |
| E-03 | n8n test instance accessible | Can open n8n UI at sandbox/test URL | Open n8n. Confirm it is the test instance, not production |
| E-04 | n8n instance is local/sandbox | Instance is NOT connected to live social media accounts | Verify: Settings → Credentials — no real tokens should be active |
| E-05 | n8n version noted | Version visible in n8n UI footer or Settings | Note version before import (needed for evidence log Section 4) |
| E-06 | All 6 workflow files accessible | Can navigate to `n8n/workflows/` from file manager | Confirm repo is accessible from the machine where n8n runs |
| E-07 | Evidence log is open and ready | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` open in editor | Open and prepare to fill Section 2 (repo state) before first import |
| E-08 | No production credentials loaded | n8n has no real API tokens for Meta, TikTok, Zalo, Telegram, Supabase | Check credentials list in n8n Settings before starting |
| E-09 | Dry-run time window allocated | Owner has uninterrupted time to complete all 6 imports + logging | Allocate 30–60 minutes minimum |

**Environment-side gate:** Owner must satisfy E-01 through E-09. Builder cannot pre-verify these.

---

## Required Files — Pre-Import Reading

Owner/operator must read the following before starting the import session:

| Order | File | Purpose |
|-------|------|---------|
| 1 | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | Full 10-step procedure, STOP conditions, PASS criteria |
| 2 | `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | Quick-reference companion checklist, per-workflow checks |
| 3 | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | Pre-structured evidence log to fill during and after session |
| 4 | `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` | This document — confirm GO / NO-GO before starting |

---

## Environment Prerequisites — Detail

### n8n Test/Sandbox Instance

- Must be a local or isolated n8n instance.
- Must NOT be connected to live Facebook Pages, Instagram accounts, TikTok accounts, Zalo OA, Meta Ads Manager, or any production service.
- Import will add 6 workflow nodes to the instance. These workflows will be **inactive** after import.
- If n8n has existing production workflows, the sandbox instance must be separate.

**Placeholder credentials:**
All workflows reference credentials by name only (e.g., `REPLACE_WITH_N8N_SUPABASE_CREDENTIAL_NAME`). During the dry-run, these credential names may not resolve. This is expected — the import test is checking that the workflow JSON imports without structural errors, not that credentials are live.

### Workflow Import Only — No Activation

After importing each workflow:
- Open the workflow in n8n.
- Confirm the toggle/switch shows **Inactive**.
- Do NOT click Activate.
- Do NOT click Execute.
- Do NOT manually trigger any node.

### Placeholder Credentials Only

No real credentials should be entered into n8n at any point during the dry-run. If n8n prompts to configure credentials for a node, either:
- Enter a placeholder value (e.g., `TEST_PLACEHOLDER`), or
- Skip/cancel the credential dialog.

Do not enter real API keys, tokens, usernames, or passwords.

### No Production Posting / Replying / Ads

These are hard stops. If any workflow node in n8n shows a live connection to a production account, abort the session and record a STOP condition in the evidence log.

### Evidence Log

Before the first import:
1. Open `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md`.
2. Fill in Section 2 (repo state: run `git log --oneline -3` and paste output).
3. Fill in Section 4 (environment: n8n instance URL, n8n version, Node.js version).
4. Note the session start time.

After each workflow import, immediately fill the corresponding observation table in Section 6.

---

## Explicit Stop Conditions

Stop the import session immediately if any of the following occur:

| Stop ID | Condition | Action |
|---------|-----------|--------|
| S-01 | n8n import returns a hard error for any workflow | Record in evidence log Section 9. Do not proceed to next workflow. Investigate cause. |
| S-02 | Any imported workflow shows `active: true` after import | Immediately set to Inactive. Record in evidence log. Treat as FAIL. |
| S-03 | Any node in any workflow is connected to a live production account | Abort session. Record in evidence log. Investigate how credential was connected. |
| S-04 | n8n instance is identified as the production instance (not sandbox) | Abort session immediately. Do not import any workflow. |
| S-05 | Real API key, token, or password is accidentally entered | Revoke the credential immediately. Record in evidence log. |
| S-06 | Any automated execution is triggered (node runs, message sent, post published) | Abort session. Record in evidence log. Determine cause. |
| S-07 | Validation script (`scripts/validate_n8n_workflows.mjs`) fails | Do not proceed with import. Fix reported issues first. |
| S-08 | Any of the 6 workflow JSON files are missing or corrupted | Do not proceed. Restore from git: `git checkout HEAD -- n8n/workflows/` |

---

## GO / NO-GO Summary

### GO Criteria — All Must Be True

- [ ] All R-01 through R-10 repo-side criteria are satisfied (Builder-verified: PASS)
- [ ] E-01: Node.js >= 16 confirmed on Owner machine
- [ ] E-02: Validation script passes with exit 0
- [ ] E-03: n8n test instance is accessible
- [ ] E-04: n8n instance confirmed as local/sandbox (not production)
- [ ] E-05: n8n version noted
- [ ] E-06: Workflow files accessible from the import machine
- [ ] E-07: Evidence log is open and Sections 2 and 4 are pre-filled
- [ ] E-08: No production credentials loaded in n8n
- [ ] E-09: Time window allocated

**If all boxes are checked: proceed with Phase 10 procedure (`docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`).**

### NO-GO Criteria — Any One Triggers NO-GO

- E-01 is NO: Node.js not installed or version < 16
- E-02 is NO: Validation script fails
- E-03 is NO: n8n not accessible
- E-04 is NO: Instance is production or unclear
- E-07 is NO: Evidence log not prepared
- E-08 is NO: Real credentials present in n8n
- Any Stop Condition (S-01 through S-08) triggered before or during session

**If any NO-GO condition is true: do not proceed. Resolve the condition, re-check, then re-assess.**

---

## Owner Approval Gate

The Owner approves the **readiness assessment output** (this document and `logs/N8N_IMPORT_DRY_RUN_READINESS_PHASE_12.md`). The Owner does not need to debug or resolve Builder-side issues manually. If any repo-side criterion (R-01 through R-10) is unresolved, the Builder resolves it before the Owner sees the readiness gate.

**Owner's decision at this gate:**
1. Review this document and the Phase 12 readiness log.
2. Assess environment-side criteria (E-01 through E-09) against their actual machine and n8n instance.
3. If all GO conditions are met: proceed with dry-run following `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`.
4. If any NO-GO condition applies: resolve it, then re-check.

---

## Phase Connections

| Phase | Document | Role in Readiness Flow |
|-------|----------|------------------------|
| Phase 8 | `docs/20_N8N_WORKFLOW_SKELETONS.md` | Source of 6 workflow JSONs under test |
| Phase 9 | `docs/21_N8N_IMPORT_VALIDATION.md` | Validation check criteria (17 checks) |
| Phase 10 | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | Step-by-step import procedure to follow after GO |
| Phase 11 | `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | Quick-reference checklist companion |
| Phase 11 | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | Evidence log to fill during session |
| Phase 12 | This document | GO / NO-GO readiness gate |
| Phase 12 | `logs/N8N_IMPORT_DRY_RUN_READINESS_PHASE_12.md` | Readiness assessment log |

---

## Known Limitations

1. **Environment-side criteria cannot be auto-verified** — Builder has no access to Owner's machine or n8n instance.
2. **Node.js BLOCKED_BY_ENVIRONMENT** — Phase 10 recorded Node.js as not found on the session machine. Owner must install Node.js >= 16 before E-01 and E-02 can be satisfied.
3. **n8n version compatibility** — Workflow JSONs target n8n's standard import format. Minor `typeVersion` adjustments may be needed for specific n8n versions. Record any such adjustments in the evidence log.
4. **Credential name resolution** — Placeholder credential names (e.g., `REPLACE_WITH_N8N_SUPABASE_CREDENTIAL_NAME`) will not resolve in n8n during the dry-run. This is expected and does not constitute a failure.
5. **This document does not claim the dry-run was executed** — Phase 12 is a readiness gate only.

---

*End of Phase 12 Readiness Gate*
