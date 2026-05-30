# Owner Approval Gate — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 22 — ECC Lite Repo Governance)
Type: Governance — Approval Gate Definitions
Scope: All phases and sessions in this repository

---

## Purpose

This document defines every approval gate in the FnB OS V1 project.
Each gate requires an explicit Owner decision before the gated action may proceed.
No AI agent (Builder, Reviewer, or Architect) may self-authorize any gate.

---

## Gate Definitions

### Gate 1 — Planning Approval

**What it covers:** Approving the phase plan and scope before any build work begins.

| Item | Required |
|------|---------|
| Owner has read the phase plan document | YES |
| Owner confirms scope (adopt / delay / reject tables where applicable) | YES |
| Owner confirms the assigned Builder and Reviewer | YES |
| Owner says `OWNER_APPROVED` (or equivalent clear approval) | YES |

**Triggered by:** Chief Architect (ChatGPT) creating a phase plan and Builder completing intake.
**Blocks:** Build work from starting.
**Recorded in:** `commands/COMMAND_INBOX.md` or relevant handoff file.

---

### Gate 2 — Build Approval (Pre-Commit)

**What it covers:** Confirming that Builder's output is correct before a local commit.

| Item | Required |
|------|---------|
| Builder has completed the phase deliverables | YES |
| Reviewer (Codex) has reviewed and output PASS (or Owner has done direct review) | YES |
| Secret scan = CLEAN | YES |
| No workflow JSON modified outside scope | YES |
| No `"active": true` introduced | YES |
| No runtime execution performed | YES |
| Logs and handoff files updated | YES |
| Owner says `OWNER_APPROVED` for commit | YES |

**Triggered by:** Builder completing build and requesting Codex review + Owner approval.
**Blocks:** `git commit` from being made.
**Recorded in:** `commands/COMMAND_INBOX.md` — status updated to `OWNER_APPROVED`.

---

### Gate 3 — Commit Approval

**What it covers:** Local `git commit` only — not push.

| Item | Required |
|------|---------|
| Gate 2 conditions met | YES |
| Pre-commit checklist complete (`docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md`) | YES |
| Owner explicitly approves commit | YES |

**Note:** Local commit does NOT authorize push. Push is a separate gate.
**Recorded in:** Commit message, `handoff/CURRENT_PHASE.md`, `handoff/SESSION_SUMMARY.md`.

---

### Gate 4 — Push Approval

**What it covers:** Pushing the local commit to `origin main` on GitHub.

| Item | Required |
|------|---------|
| Gate 3 complete (commit made and clean) | YES |
| Pre-push checklist complete | YES |
| Owner explicitly says `OWNER_APPROVED` for push (separate from commit approval) | YES |
| No force push | NEVER — force push is prohibited |

**Note:** This is a separate gate from commit. Owner must explicitly authorize push even if commit was already approved.
**Recorded in:** `handoff/CURRENT_PHASE.md` — status updated to `PUSHED`.

---

### Gate 5 — Runtime Import Approval

**What it covers:** Importing a workflow JSON file into an n8n instance.

| Item | Required |
|------|---------|
| Workflow JSON committed and reviewed | YES |
| Owner confirms sandbox instance (not production) | YES |
| Owner confirms workflow will be imported as INACTIVE | YES |
| Owner explicitly approves this specific import | YES |

**Triggered by:** Owner preparing for manual sandbox execution.
**Blocks:** n8n import from proceeding.
**Recorded in:** Phase-specific runbook and evidence log.

---

### Gate 6 — Runtime Execution Approval

**What it covers:** Actually triggering / running a workflow in n8n.

| Item | Required |
|------|---------|
| Gate 5 complete (workflow imported and inactive) | YES |
| Phase runbook read and pre-run checklist complete | YES |
| Sandbox instance confirmed | YES |
| No real credentials configured | YES |
| Owner explicitly approves this specific execution | YES |

**Note:** This gate must be re-authorized for each new workflow and each new phase.
**Blocks:** Manual trigger or test webhook from being clicked.
**Recorded in:** Phase evidence log (execution record).

---

### Gate 7 — Customer-Facing Output Approval

**What it covers:** Any output that could reach a real customer: post, reply, DM, comment response.

| Item | Required |
|------|---------|
| Content reviewed and approved by Owner | YES |
| Output is not auto-generated without human review | YES |
| Owner explicitly approves this specific piece of content | YES |

**This gate applies to:** Social media posts, comment replies, Zalo/Messenger messages, SMS, any public-facing content.
**No automation may bypass this gate.**

---

### Gate 8 — Ads Spend Approval

**What it covers:** Any action that would commit real advertising budget.

| Item | Required |
|------|---------|
| Campaign plan reviewed by Owner | YES |
| Budget amount explicitly approved | YES |
| Platform (Meta, TikTok, Zalo) explicitly authorized | YES |
| Owner explicitly approves this specific spend | YES |

**This gate applies to:** Meta Ads, TikTok Ads, Zalo Ads, Google Ads, any paid promotion.
**No automation may bypass this gate.**

---

### Gate 9 — Publishing Approval

**What it covers:** Publishing content to any public platform.

| Item | Required |
|------|---------|
| Content final version reviewed by Owner | YES |
| Platform and timing confirmed | YES |
| Owner explicitly approves this specific publish action | YES |

**This gate applies to:** Instagram, Facebook, TikTok, Zalo, website, email newsletters.

---

### Gate 10 — Emergency Rollback Approval

**What it covers:** Rolling back to a previous commit or reverting changes in an emergency.

| Item | Required |
|------|---------|
| Rollback target commit identified | YES |
| Impact of rollback understood | YES |
| Owner explicitly approves rollback | YES |

**Procedure:**
1. Identify commit to roll back to using `git log`.
2. Report impact to Owner.
3. Await Owner `OWNER_APPROVED`.
4. Execute rollback (e.g., `git revert` preferred over `git reset --hard`).
5. Update `handoff/CURRENT_PHASE.md` with rollback record.

---

## Gate Summary Table

| Gate | Action | Commit Required? | Push Required? | Owner Approval Required? |
|------|--------|-----------------|----------------|--------------------------|
| 1 — Planning | Phase plan accepted | NO | NO | YES |
| 2 — Build | Deliverables reviewed | NO | NO | YES |
| 3 — Commit | Local git commit | YES | NO | YES |
| 4 — Push | Push to GitHub | YES (prior) | YES | YES (separate from commit) |
| 5 — Runtime Import | n8n import | YES (prior) | YES (prior) | YES |
| 6 — Runtime Execution | Workflow run | YES (prior) | YES (prior) | YES |
| 7 — Customer Output | Publish/post/reply | N/A | N/A | YES |
| 8 — Ads Spend | Ad budget commitment | N/A | N/A | YES |
| 9 — Publishing | Content published | N/A | N/A | YES |
| 10 — Rollback | Revert / reset | N/A | N/A | YES |

---

## Important Notes

- **Local commit can happen** after Builder validation passes if the phase plan permits local commit.
- **Push always requires separate explicit Owner approval** — commit approval does not automatically authorize push.
- **Runtime execution always requires explicit Owner approval** — it is never implied by commit or push approval.
- **Customer-facing automation always requires explicit Owner approval** — no automation may self-authorize.
- **No gate may be skipped** — if a gate cannot be completed, work must stop and status must be set to `BLOCKED`.

---

*Related:*
- `docs/governance/AGENT_OPERATION_RULES.md` — Agent roles and restrictions
- `docs/governance/REPO_VALIDATION_CHECKLIST.md` — Pre-commit validation
- `docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md` — Quick-reference checklist
- `docs/governance/SESSION_HANDOFF_RULES.md` — Session handoff protocol
