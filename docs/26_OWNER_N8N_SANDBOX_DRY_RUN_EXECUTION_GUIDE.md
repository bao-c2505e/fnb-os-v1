# Phase 14 — Owner/Operator Guide: n8n Sandbox Import Dry-Run Execution

**Purpose:** Simple, plain-language guide for Owner/operator to perform the actual n8n sandbox import dry-run safely and record the result.

Phase: 14
Version: 1.0
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Audience: Owner (Bo Bao) or designated operator

---

## What This Guide Is For

This guide tells you exactly how to:

1. Confirm you are ready to run the dry-run.
2. Import the 6 Phase 8 workflow JSON files into n8n safely.
3. Check the import result.
4. Fill in the execution log (`logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md`).
5. Report the result.

This guide does NOT replace the Phase 10 procedure or Phase 13 handoff. Read those first if you want the full technical detail. This guide is the quick-start checklist version.

---

## What This Is NOT

| This is NOT | Reason |
|-------------|--------|
| A guide to activating workflows | Workflows must stay inactive at all times |
| A guide to connecting real credentials | Placeholder credentials only — never real |
| A guide to testing actual automation | The dry-run only imports the JSON structure |
| A guide to fixing workflow logic | Builder phases handle that |
| A guide to going live | Production activation is a future phase |

---

## Before You Start — 4 Mandatory Checks

You must complete these 4 checks before opening n8n.

### Check 1 — Use a sandbox or test n8n instance

You must use a **local, sandbox, or test** n8n instance.

- Acceptable: `http://localhost:5678` (local Docker or installed n8n)
- Acceptable: A test instance you own, with no live connections
- **NOT acceptable:** Your production n8n instance, any instance with live workflows, any instance connected to real customer data

If you are not sure which instance is which: stop. Ask for help before proceeding.

### Check 2 — Read the Phase 12 Readiness Gate

Open `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` and confirm the result is **GO**, not NO-GO.

If the gate says NO-GO or you have not confirmed the environment-side criteria (E-01–E-09): stop. Resolve the blocking criteria first.

### Check 3 — Have the execution log open

Open `logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md` in a text editor.
You will fill it in as you go. Do not rely on memory.

### Check 4 — Allocate at least 30 minutes

Do not start the session if you will be interrupted. The dry-run requires focused attention, especially for the 4 high-risk workflows (WF-03 through WF-06).

---

## What to Check Before Importing

Work through the pre-import checklist in Section 4 of the execution log (PRE-01 through PRE-13). The most important items:

| Item | What to do |
|------|-----------|
| n8n is sandbox | Verify URL is not your production instance |
| No real credentials | Go to Settings → Credentials in n8n — confirm no real tokens or API keys exist |
| All 6 JSON files present | Check `n8n/workflows/` in the repo — all 6 skeleton files should be there |
| git status clean | Run `git status --short` — no Phase 8 JSON files should show as modified |
| Validator passed (if Node.js available) | Run `node scripts/validate_n8n_workflows.mjs` — should exit with 0 failures |

If all PRE checks pass, you are ready to import.

---

## Exact Safe Sequence — Step by Step

Follow this sequence exactly. Do not skip steps.

**Step 1 — Fill Section 1 of the execution log**

Before opening n8n, fill in:
- Your name (Operator name)
- Today's date
- Start time
- n8n instance URL
- n8n version (check Settings → About in n8n)

**Step 2 — Fill Section 2 of the execution log**

Run `git log --oneline -3` and `git status --short` in your terminal.
Copy the output into Section 2. This records the repo state before you touched anything.

**Step 3 — Confirm Section 3 workflow files are present**

Check each of the 6 files in `n8n/workflows/` exists. Mark YES or NO in Section 3.
If any file is missing, STOP. Do not proceed until you find and restore it.

**Step 4 — Complete Section 4 pre-import checklist**

Go through PRE-01 to PRE-13 in order. Mark PASS, FAIL, or BLOCKED for each.
If PRE-01, PRE-02, PRE-05, PRE-06, or PRE-07 is FAIL: stop and resolve before continuing.

**Step 5 — Import WF-01 (Content Auto — Standard risk)**

In n8n:
1. Go to Workflows.
2. Click **Add Workflow** or the import button.
3. Choose **Import from file**.
4. Select `n8n/workflows/content_auto_skeleton.json`.
5. Confirm the workflow appears without an error message.
6. Open the workflow canvas.
7. Verify: the name contains `[SKELETON]`.
8. Verify: the Active toggle shows **Inactive**. Do NOT activate it.
9. Scroll through nodes — you should see an Error Trigger node and a Sticky Note.
10. Note any credential warnings — these are expected and not a failure.

Fill in Section 5 / WF-01 in the execution log.

**Step 6 — Import WF-02 (Creative Asset Auto — Standard risk)**

Repeat Step 5 with `creative_asset_auto_skeleton.json`.
Fill in Section 5 / WF-02.

**Step 7 — Import WF-03 (Ads Pack Auto — HIGH RISK)**

Extra checks required:
- After import, confirm the Sticky Note says **NO ADS SPEND** (or similar warning).
- Confirm there is NO Ads API node or budget field anywhere in the canvas.
- Confirm the Active toggle shows Inactive.
- Do NOT click anything that looks like it connects to Meta Ads, Google Ads, or any ad platform.

Fill in Section 5 / WF-03, including all high-risk checks.

**Step 8 — Import WF-04 (CRM Followup Auto — HIGH RISK)**

Extra checks required:
- Confirm the Sticky Note says **NO AUTO-SEND** (or similar warning).
- Confirm `human_review_required` is visible in the mock output node (look in Code or Set nodes).
- Confirm there is NO messaging API node (Zalo, Messenger, WhatsApp, SMS).
- Confirm the Active toggle shows Inactive.
- Do NOT connect to any customer communication platform.

Fill in Section 5 / WF-04, including all high-risk checks.

**Step 9 — Import WF-05 (Comment Inbox Reply Assistant — HIGH RISK)**

Extra checks required:
- Confirm the escalation If-node is visible (it routes complaint/angry comments separately).
- Confirm BOTH branches of the If-node end with human review — not an auto-reply.
- Confirm there is NO reply API node that could send a message to any platform.
- Confirm the Active toggle shows Inactive.

Fill in Section 5 / WF-05, including all high-risk checks.

**Step 10 — Import WF-06 (Approval Publishing — HIGH RISK)**

Extra checks required:
- Confirm all 5 publish branch nodes are NoOp stubs (labeled STUB DISABLED or similar).
- Confirm the not-approved path ends with a Stop and Error node.
- Confirm there is NO live platform publish node (no Facebook/TikTok/Zalo publisher node).
- Confirm the Active toggle shows Inactive.

Fill in Section 5 / WF-06, including all high-risk checks.

**Step 11 — Complete post-import verification (Section 7)**

After all 6 workflows are imported, go through POST-01 to POST-11 in Section 7.
Confirm all workflows are inactive, no executions occurred, and no real credentials were added.

Check the n8n **Executions** tab — the execution count should be zero or unchanged from before you started.

**Step 12 — Fill Section 8, Section 9, Section 10**

- Section 8: Record whether credential warnings appeared for each workflow.
- Section 9: Confirm each workflow's active toggle state.
- Section 10: Confirm the approval gate structure of WF-06.

**Step 13 — Complete Section 12 safety confirmation gate**

Initial each item SC-01 through SC-08. This is your sign-off that the session was safe.

**Step 14 — Set final result in Section 13**

Change `NOT_RUN` to:
- **PASS** — all 6 workflows imported, all Inactive, no real credentials, no activations, no executions, zero issues
- **BLOCKED** — any STOP condition triggered, or any POST check failed; record issues in Section 6 first
- **PARTIAL** — some imports succeeded but the session could not be completed; record count and reason

Record your session end time in Section 1.

---

## What to Check After Importing

| Check | Where to verify |
|-------|----------------|
| All 6 workflows appear in n8n Workflows list | n8n Workflows page |
| All 6 show Inactive status | Toggle on each workflow card |
| Executions tab shows zero new runs | n8n Executions tab |
| No credentials were added | Settings → Credentials in n8n |
| Sections 7, 8, 9, 10, 12, 13 all filled | Execution log file |
| Section 6 either says NONE or has all issues recorded | Execution log file |

---

## What NOT to Do

These are absolute prohibitions. Violating any of these stops the dry-run and requires you to record a BLOCKED result.

```
DO NOT activate any workflow.
  → If you see a workflow become Active unexpectedly, deactivate it immediately.
  → Record as an issue in Section 6. Mark final result BLOCKED.

DO NOT enter real API keys, tokens, passwords, or private keys.
  → "Credential not found" warnings are expected. Leave them unresolved.
  → Do NOT create new credentials in Settings → Credentials to resolve these warnings.

DO NOT execute any workflow or trigger any node.
  → Do not click "Execute workflow" or "Test step" on any node.
  → The dry-run is import and visual inspection only.

DO NOT post content to any social media platform.
  → Do not connect n8n to any Facebook, TikTok, Instagram, Zalo, or other platform.

DO NOT reply to real customers.
  → Do not connect the inbox or CRM workflow to any real messaging channel.

DO NOT commit any ad budget or spend.
  → Do not connect the Ads Pack workflow to any ad platform API.

DO NOT use your production n8n instance.
  → If you realize mid-session that you opened the wrong instance, stop immediately.
  → Record the issue and mark the result BLOCKED.

DO NOT skip filling the execution log.
  → The log is the only record of what happened.
  → Screenshots supplement the log but do not replace it.
```

---

## How to Handle Unexpected Issues

If anything unexpected happens during the dry-run:

1. **Stop.** Do not continue to the next step.
2. **Do not attempt to fix it yourself** unless the fix is clearly safe (e.g., deactivating a workflow that accidentally activated).
3. **Record the issue** in Section 6 of the execution log using the template block provided.
4. **Check the stop conditions table** in Phase 13 (`docs/25_CONTROLLED_N8N_IMPORT_DRY_RUN_HANDOFF.md`, Section — Stop Conditions) to see which condition applies.
5. **Take a screenshot** if possible. Note the file path or location in Section 6.
6. **Mark the final result BLOCKED** in Section 13.
7. **End the session** and report the blocked result.

You do not need to debug the issue. The Builder (Claude Code) or Reviewer (Codex) will review the recorded issue and determine next steps.

---

## How to Fill the Execution Log

The execution log is `logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md`.

| Section | When to fill |
|---------|-------------|
| Section 1 — Session Identity | Before opening n8n |
| Section 2 — Repo State | Before opening n8n (run git commands) |
| Section 3 — Workflow Files | Before opening n8n (check file system) |
| Section 4 — Pre-Import Checklist | Before importing first workflow |
| Section 5 — Import Action Log | During import — fill each WF table as you go |
| Section 6 — Issue Log | As issues occur |
| Section 7 — Post-Import Checklist | After all imports complete |
| Section 8 — Credential Status | After all imports complete |
| Section 9 — Active = false Status | After all imports complete |
| Section 10 — Approval Gate Status | After WF-06 import |
| Section 11 — Evidence Links | After all imports complete |
| Section 12 — Safety Confirmation Gate | At end of session (sign-off) |
| Section 13 — Final Result | At end of session (last step) |

**Important:** Fill each section as you reach that point in the session. Do not try to fill the entire log from memory at the end.

---

## After a Successful PASS

If the final result is PASS:

1. Save the filled execution log file.
2. Note that no workflows are active and no real credentials are configured.
3. Report the PASS result for Codex review.
4. Do NOT activate any workflow yet. Production activation is a future phase.
5. Do NOT add real credentials yet. Credential configuration is a future phase.
6. Do NOT share the log file publicly — it contains your operator name and n8n instance URL.

---

## After a BLOCKED Result

If the final result is BLOCKED:

1. Save the filled execution log file with the issue recorded in Section 6.
2. Report the BLOCKED result to the Builder (Claude Code) or Owner for review.
3. The Builder will review the issue and create a remediation plan.
4. Do NOT attempt to re-run the import without a new remediation plan.

---

## Phase Connections

| Phase | What it provides |
|-------|-----------------|
| Phase 8 | `n8n/workflows/*.json` — the 6 workflow files you import |
| Phase 9 | `scripts/validate_n8n_workflows.mjs` — static validator |
| Phase 10 | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` — detailed 10-step procedure |
| Phase 11 | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` — detailed per-node evidence log |
| Phase 12 | `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` — GO/NO-GO gate (must be GO first) |
| Phase 13 | `docs/25_CONTROLLED_N8N_IMPORT_DRY_RUN_HANDOFF.md` — comprehensive operator session guide |
| Phase 14 | `logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md` — execution log you fill in |
| Phase 14 | This file — simple guide for using the execution log |

---

## Known Limitations

1. This guide cannot verify whether your n8n instance is truly isolated from production systems. Owner/operator is responsible for confirming the instance type before starting.
2. "Credential not found" warnings will appear for all 6 workflows — this is expected and not a failure. Do not add real credentials to resolve them.
3. The static validator requires Node.js >= 16. If not available, proceed with manual visual inspection and note PRE-09 as BLOCKED in the log.
4. Screenshots are encouraged as supplementary evidence but are not stored in this repo. Note the screenshot location in Section 11 of the execution log.
5. This guide covers the import dry-run only. It does not cover production credential setup, workflow activation, or production go-live — those are future phases.

---

*This guide was created by Claude Code (Builder, AGT-02) as a documentation-only artifact.*
*No import was performed. No n8n was accessed. No workflow was executed.*
*Phase 8 workflow JSON files remain untouched at commit `ad867b3`.*
