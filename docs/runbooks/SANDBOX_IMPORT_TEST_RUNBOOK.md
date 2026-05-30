# Sandbox Import Test Runbook — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness)
Type: Owner-Facing Runbook — Future Safe Import and Test Guide
Audience: Owner (Bo Bao)

---

## Purpose

This runbook guides the Owner through a safe, controlled n8n sandbox import and test in the future.

**This runbook does NOT authorize any import or execution.** Reading this runbook is a preparation step only.
Actual import requires a separate, explicit Owner approval: `"APPROVED FOR SANDBOX IMPORT ONLY — [workflow name] — [date]"`.
Actual execution requires a further, separate, explicit Owner approval: `"APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow name] — [date]"`.

> **Strong warning:** Importing a workflow into n8n does NOT mean the workflow is approved for execution. Import and execution are two separate approval gates.

---

## Preconditions

All of the following must be true before beginning:

| # | Precondition | How to Verify |
|---|-------------|--------------|
| PRE-01 | `git status --short` is clean | Run `git status --short` — must return no output |
| PRE-02 | HEAD equals origin/main | Run `git log -1 --oneline` and compare to GitHub latest commit |
| PRE-03 | Latest phase handoff exists and is reviewed | Open `handoff/CURRENT_PHASE.md` |
| PRE-04 | Codex PASS or Owner direct review confirmed for relevant phase | Open relevant `handoff/PHASE_XX_HANDOFF.md` |
| PRE-05 | All workflow JSON `"active": false` | Run `scripts/check_n8n_workflows.py` — must show 0 violations |
| PRE-06 | No secrets in repo | Run `scripts/check_no_secrets.py` — must show CLEAN |
| PRE-07 | Per-workflow evidence pack exists | Open `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` and confirm |
| PRE-08 | n8n sandbox instance accessible | Open n8n UI — confirm instance URL is sandbox/test, not production |
| PRE-09 | Sandbox instance has NO real credentials configured | Open n8n Settings → Credentials — must be empty or show only test/placeholder names |
| PRE-10 | Dummy payload file accessible | Open relevant `samples/sandbox/phase_17_test_payloads/` file |
| PRE-11 | Evidence log template open | Open relevant `logs/phase_[XX]_[workflow]_sandbox_evidence_log.md` |
| PRE-12 | 60-minute time window available | Confirm before starting |
| PRE-13 | Owner has written explicit import approval phrase | Written in session or evidence log |

**If any precondition fails:** Stop. Do not proceed. Resolve the failure first.

---

## Allowed Actions During Sandbox Import

| Action | Allowed? |
|--------|---------|
| Import workflow JSON file into sandbox n8n | **YES — import only** |
| View workflow canvas and node structure | **YES** |
| Confirm sticky notes and DO NOT ACTIVATE warnings are visible | **YES** |
| Check node names and connections | **YES** |
| Confirm workflow is INACTIVE after import | **YES** |
| Note credential warning messages (not errors — expected) | **YES** |
| Capture screenshots of the canvas | **YES** |
| Fill evidence log with import results | **YES** |

---

## Forbidden Actions During Sandbox Import

| Forbidden Action | Why |
|-----------------|-----|
| Toggle the workflow to ACTIVE | Would enable automatic triggering — STOP if this happens |
| Enter or connect real credentials (OpenAI, Meta, Zalo, etc.) | Risk of real charges or real customer contact |
| Click "Execute Workflow" or "Test Workflow" | That is execution — not import |
| Modify any node content inside n8n | Workflow must remain as-is from JSON |
| Add, remove, or rename nodes | Workflow must remain as-is |
| Share the n8n instance URL publicly | Security risk |
| Import into a production n8n instance | Production impact — sandbox only |

---

## Step-by-Step Import Readiness Flow

### Step 1 — Confirm Repo State

```
git status --short         ← must be clean (no output)
git branch --show-current  ← must show: main
git log -1 --oneline       ← note the commit hash
```

Record the commit hash in the evidence log before opening n8n.

### Step 2 — Verify Workflow JSON Before Import

Locate the workflow file in `n8n/workflows/[workflow_name].json`.
Confirm:
- `"active": false` is present
- `"name"` contains `[SKELETON]`
- No real credentials or API keys in the file

### Step 3 — Open n8n Sandbox Instance

Open your n8n sandbox URL (the test instance, not production).
Confirm the instance URL matches your expected sandbox domain.
If in doubt: do NOT proceed. Confirm the URL before importing.

### Step 4 — Import the Workflow JSON

In n8n UI:
1. Go to Workflows → click `+` (New Workflow) or `Import`.
2. Select "Import from File".
3. Browse to `n8n/workflows/[workflow_name].json`.
4. Click Import.
5. Confirm: no import error displayed.
6. Confirm: workflow opens in canvas view.

### Step 5 — Confirm Workflow is INACTIVE

After import:
- Check the toggle in the top-right of the workflow canvas.
- It must show **INACTIVE** (greyed out).
- If it shows ACTIVE: **STOP immediately.** Do not proceed. Toggle it back to INACTIVE.

### Step 6 — Inspect Canvas

Check:
- [ ] Sticky Note is visible with warning (DO NOT ACTIVATE)
- [ ] Node names are in English and match the runbook
- [ ] Error Trigger node is present
- [ ] Credential warning messages appear (this is expected — not an error)
- [ ] No credential is actually connected (just warning — not configured)

### Step 7 — Document Import Result

In the evidence log:
- `active_status_before_run`: `inactive` (before any action)
- `import_result`: `PASS` or `BLOCKED`
- `active_status_after_import`: `inactive` (must be INACTIVE)
- `credentials_used`: `placeholder_or_none`
- `import_timestamp`: (fill in)
- `operator`: `Bo Bao`

### Step 8 — Capture Required Screenshots

Capture at minimum:
1. n8n workflow canvas showing workflow name and INACTIVE toggle.
2. Full canvas view showing node structure.

Name screenshots following the convention in the per-workflow evidence pack.

### Step 9 — Record in Evidence Log

Fill all import-related fields in the evidence log.
Do NOT fill execution fields (node execution results, key output fields) — those are for Phase 3 (execution) only.

### Step 10 — Decide Next Action

After import:
- If import PASS: update evidence log with PASS. Report result. Wait for Owner decision on whether to proceed to sandbox execution (requires separate approval).
- If import BLOCKED/FAIL: record the error in the evidence log. Do NOT attempt to fix inside n8n. Report to Builder.

---

## What Evidence the Owner Should Capture

| Evidence Item | When to Capture | Where to Store |
|--------------|----------------|---------------|
| Canvas screenshot — full view with INACTIVE toggle | After import | `evidence/phase_[XX]/[workflow_name]/` folder |
| Canvas screenshot — sticky note visible | After import | Same folder |
| n8n workflow name displayed | After import | Same folder |
| Import confirmation (no error message) | During import | Screenshot or note |
| Evidence log — all import fields filled | After import | `logs/phase_[XX]_[workflow]_sandbox_evidence_log.md` |

---

## What to Do if Import Fails

| Scenario | Action |
|---------|--------|
| Import error message from n8n (e.g., "Invalid JSON") | Stop. Record exact error. Do NOT retry. Report to Builder. |
| Workflow imports but shows as ACTIVE | Stop. Toggle to INACTIVE. Record this happened. Report to Builder. |
| Credential error (not "not found" warning — actual connection error) | Stop. Remove any credential if accidentally connected. Report to Builder. |
| Node names mismatch from what the runbook says | Stop. Record the discrepancy. Report to Builder — do not assume it is OK. |
| n8n version warning or node version mismatch | Stop. Record the version numbers. Report to Builder. |

---

## What to Do if Credential Errors Appear

n8n will show **"Credential not found"** warnings for all API credentials (OpenAI, Meta, Zalo, Google, etc.) when a workflow is imported without credentials configured. This is **expected and normal**. These warnings mean:
- The workflow correctly references credential slots.
- No real credentials are connected.
- The workflow cannot execute against real APIs (correct for sandbox import).

**Do NOT:**
- Add real credentials to silence these warnings.
- Interpret warnings as failures — import can still succeed.

**DO:**
- Note the warning messages in the evidence log.
- Confirm that no real credentials were added.

---

## What to Do if Workflow Shows `active: true`

If the workflow toggles to ACTIVE at any point:
1. **Stop immediately.**
2. Toggle the workflow back to INACTIVE.
3. Do NOT click any trigger or execute.
4. Record that this happened in the evidence log.
5. Report to Builder — do NOT proceed with any test until the cause is investigated.

This is a stop condition. Active workflows can trigger automatically.

---

## What to Do if Node Versions Mismatch

If n8n reports a node version warning (e.g., "This node version is deprecated"):
1. Record the warning in the evidence log.
2. Do NOT update or change the node inside n8n.
3. Do NOT attempt to fix the mismatch inside n8n.
4. Report to Builder — any node version changes must be made in the JSON file and re-committed.

---

## What to Do Before Any Manual Execution

After a successful sandbox import, manual execution is NOT automatically authorized. Before any execution:

1. Return to `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` and complete it again.
2. Confirm the per-workflow execution runbook exists (e.g., `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md`).
3. Confirm dummy payload file is accessible and matches the runbook.
4. Write the explicit execution approval phrase: `"APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow name] — [date]"`.
5. Follow the per-workflow execution runbook step by step.

> **Reminder:** Import approval does NOT authorize execution. A separate, explicit approval is required for each execution session.

---

## Stop Conditions

Stop immediately and do NOT proceed if any of the following occur:

| Stop Condition | Action |
|---------------|--------|
| SC-01 — Workflow becomes ACTIVE | Toggle to INACTIVE immediately. Record. Report. |
| SC-02 — Real credential accidentally connected | Disconnect immediately. Record. Report. |
| SC-03 — External API call detected (not expected for import) | Stop. Record. Report. |
| SC-04 — Real customer data appears anywhere in output | Stop. Record. Report. |
| SC-05 — Post, publish, or reply action detected | Stop. Record. Report. |
| SC-06 — n8n shows unexpected execution in the executions tab | Stop. Record. Do not delete execution log. Report. |
| SC-07 — n8n instance URL turns out to be production | Stop immediately. Do NOT import into production. Report. |
| SC-08 — Unclear node behavior or unexpected node output | Stop. Record. Report. Do not interpret. |

---

## Related Documents

- [SANDBOX_RUNBOOK_INDEX.md](SANDBOX_RUNBOOK_INDEX.md) — workflow status and runbook index
- [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) — pre-action readiness checklist
- [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) — decision tree for approvals
- `docs/26_OWNER_N8N_SANDBOX_DRY_RUN_EXECUTION_GUIDE.md` — detailed Owner execution guide (Phase 14)
- `docs/governance/OWNER_APPROVAL_GATE.md` — formal gate definitions (Gates 5 and 6)

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This runbook is documentation-only. It guides future safe import. No import or execution is authorized by this document.*
