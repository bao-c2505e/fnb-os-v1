# Phase 31 — Creative Asset Auto Sandbox Re-import & Manual Execution Planning

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Phase: 31 — Creative Asset Auto Sandbox Re-import & Manual Execution Planning
Type: PLAN_READY — AWAITING CODEX REVIEW
Branch: main

---

## 1. Purpose

Chuẩn bị hướng dẫn re-import workflow Creative Asset Auto Skeleton vào n8n sandbox để kiểm tra safe sample input sau Phase 30.

Phase 31 là **planning/docs/runbook only**. Không có thao tác runtime nào được thực hiện trong phase này.

Phase 30 đã patch `Set Input Variables` node (7 → 19 fields). Workflow JSON hiện tại trong repo đã valid và importable. Mục tiêu Phase 31 là chuẩn bị đầy đủ hướng dẫn để Owner có thể re-import và re-execute trong phase sau một cách an toàn.

---

## 2. Current State

| Item | Detail |
|------|--------|
| Phase 30 result | DONE + PUSHED (commit `18c681d`) |
| Phase 30 Codex result | PASS |
| Workflow file patched | `n8n/workflows/creative_asset_auto_skeleton.json` |
| Node patched in Phase 30 | `Set Input Variables` only |
| Fields after patch | 19 (was 7) |
| `active` field | `false` — unchanged |
| n8n re-import in Phase 30 | NOT PERFORMED |
| n8n execution in Phase 30 | NOT PERFORMED |
| Workflow JSON changed in Phase 31 | NO |
| n8n import in Phase 31 | NOT PERFORMED |
| n8n execution in Phase 31 | NOT PERFORMED |

**Phase 31 is planning only.** All runtime actions are deferred to Phase 32/33.

---

## 3. Workflow File To Import

The patched workflow JSON to be imported in a future phase:

| Item | Value |
|------|-------|
| File path in repo | `n8n/workflows/creative_asset_auto_skeleton.json` |
| Workflow name (n8n) | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| Workflow ID in n8n sandbox | `VW5PDkOOtrjLQBps` (from Phase 26 evidence) |
| `active` field | `false` |
| Total nodes | 15 (14 execution + 1 Sticky Note) |
| Node to verify | `Set Input Variables` — 19 fields expected |

---

## 4. Manual Re-import Plan For Owner

**This plan is for a future phase. No import is performed in Phase 31.**

The following steps describe how Owner should re-import the patched workflow to n8n sandbox. These steps should be executed only after Phase 32 is approved.

### Pre-import Checks (Before Starting)

| Check | How To Verify |
|-------|---------------|
| Repo is clean and HEAD = latest push | `git status` → clean; `git log --oneline -1` → `18c681d` or later |
| Workflow file is the patched version | Open `n8n/workflows/creative_asset_auto_skeleton.json` — Set Input Variables should show 19 assignments |
| Working in n8n sandbox (NOT production) | Confirm n8n URL: `https://n8n.baon8n.blog` — confirm this is the sandbox instance |
| No real credentials to attach | All credential fields in workflow remain `REPLACE_WITH_*` |

### Re-import Steps

1. Open n8n sandbox: `https://n8n.baon8n.blog`
2. Navigate to the existing `FnB OS V1 — Creative Asset Auto [SKELETON]` workflow (ID: `VW5PDkOOtrjLQBps`) — or go to Workflows list.
3. **Confirm workflow is currently INACTIVE** before proceeding. Do NOT activate.
4. Export / download the patched workflow JSON from repo: `n8n/workflows/creative_asset_auto_skeleton.json`.
5. In n8n: use **Import from file** (top menu → Import) to import the patched JSON.
6. If n8n prompts **"Overwrite existing workflow?"** or similar — choose the safe option per n8n sandbox convention (confirm replace is acceptable in sandbox context, not production).
7. After import: **immediately verify `active` status = INACTIVE**. If n8n auto-activated during import, de-activate immediately and stop — do not execute.
8. **Do NOT attach any real credentials** to any node.
9. **Do NOT execute the workflow** unless Phase 32/33 has been Owner-approved for execution.
10. Record: workflow imported, inactive, no credentials attached.

### Safety Notes

- Re-importing overwrites the previous (un-patched) version in n8n — this is the intended outcome.
- n8n import does not automatically activate a workflow if the JSON has `"active": false`.
- If the sandbox instance URL has changed since Phase 26/27, Owner must confirm the correct URL before importing.

---

## 5. Manual Execution Plan For Later Phase

**This checklist is for Phase 33 or the execution sub-phase. No execution in Phase 31 or Phase 32.**

### Pre-execution Checklist

| ID | Check | Expected |
|----|-------|----------|
| PE-01 | Workflow just re-imported | YES |
| PE-02 | Workflow `active` status | INACTIVE |
| PE-03 | No real credentials attached to any node | CONFIRMED |
| PE-04 | sandbox_mode visible in Set Input Variables configuration | YES |
| PE-05 | approval_required visible in Set Input Variables configuration | YES |
| PE-06 | Owner has Phase 33 approval phrase ready | YES |
| PE-07 | n8n instance is sandbox (not production) | CONFIRMED |
| PE-08 | No auto-post, auto-reply, or ad spend can occur | CONFIRMED — stubs only |

### Execution Steps

1. Open the re-imported `FnB OS V1 — Creative Asset Auto [SKELETON]` workflow in n8n sandbox.
2. **Confirm workflow is INACTIVE** (toggle off — grey, not green).
3. Click **Manual Trigger** node.
4. Click **Execute workflow** (or "Test step" / "Execute node" per n8n version UI).
5. Observe workflow execution — all nodes should turn green on the happy path.
6. Click **Set Input Variables** node to view its output panel.
7. **Verify output JSON shows all expected fields** (see Section 6).
8. Confirm no error state on any node.
9. Record: execution count incremented from 0 to 1 (or from prior count + 1).
10. Capture evidence as described in Section 7.

---

## 6. Expected Output After Manual Execution

After successful execution, the `Set Input Variables` node output panel should show:

| Field | Expected Value | Type |
|-------|----------------|------|
| `brand_id` | `"VQ"` | string |
| `brand_name` | `"Vi Cuon"` | string |
| `brief_request` | `"REPLACE_WITH_OWNER_BRIEF_REQUEST"` | string |
| `asset_type` | `"social_static_post"` | string |
| `platform` | `"Facebook"` | string |
| `format` | `"1:1 square 1080x1080"` | string |
| `objective` | `"Engagement"` | string |
| `request_id` | `"creative_asset_sandbox_001"` | string |
| `campaign_name` | `"Sandbox Creative Asset Test"` | string |
| `channel` | `"facebook"` | string |
| `product_name` | `"Heo quay nuong lu"` | string |
| `offer` | `"Sandbox sample only - no real promotion"` | string |
| `target_audience` | `"office workers and local food lovers in Vinh"` | string |
| `key_message` | `"Fresh rolled food with warm street-premium visual direction"` | string |
| `tone_of_voice` | `"friendly, appetizing, local, premium-but-accessible"` | string |
| `visual_direction` | `"warm brown, orange accent, clean food photography style"` | string |
| `required_output` | `"design_brief"` | string |
| `approval_required` | `true` | boolean |
| `sandbox_mode` | `true` | boolean |

**Key verification targets:**

- `brand_name` = `"Vi Cuon"` (ASCII, no Unicode duplicate, no extra `brand_name` field)
- `approval_required` = `true` (boolean, not string `"true"`)
- `sandbox_mode` = `true` (boolean, not string `"true"`)
- Total field count = 19
- Message **"No fields - item(s) exist, but they're empty."** should NOT appear in the output panel (it may still appear in the input panel for the incoming `{}` from Manual Trigger — that is expected)

---

## 7. Evidence To Capture By Phase

Evidence requirements differ between Phase 32 (re-import only) and Phase 33 (manual execution). Do NOT mix them.

### Phase 32 Evidence — Re-import Only

Owner should record the following immediately after re-import in Phase 32. No execution evidence is required or expected in Phase 32.

| Evidence Item | Required | Expected Value |
|---------------|----------|----------------|
| Workflow name in n8n after import | YES | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| Workflow `active` status after import | YES | INACTIVE |
| Node count visible on canvas | YES | 10 on canvas (15 in JSON — expected) |
| Credentials attached to any node | NO | NONE / placeholder only |
| Execution performed during import | NO | NOT PERFORMED |
| n8n execution count after import | YES | 0 (unchanged from pre-import) |

### Phase 33 Evidence — Manual Execution Check

Owner should record the following after manual execution in Phase 33. These items are NOT collected in Phase 32.

| Evidence Item | Required | Expected Value |
|---------------|----------|----------------|
| Workflow `active` status before execution | YES | INACTIVE |
| Workflow `active` status after execution | YES | still INACTIVE |
| Node checked | Set Input Variables | — |
| Output fields visible | YES | 19 fields |
| `"No fields - item(s) exist, but they're empty."` gone from output panel | YES | gone |
| `brand_name` value | YES | `"Vi Cuon"` |
| `approval_required` value | YES | `true` (boolean) |
| `sandbox_mode` value | YES | `true` (boolean) |
| Credentials attached | NO | NONE / placeholder only |
| Real API call observed | NO | NONE |
| Auto-post / auto-reply / ads | NO | NONE |
| n8n execution ID | Record if available | — |
| Execution timestamp | YES | — |
| Screenshot (optional) | Recommended | Not blocking if execution log text is complete |

---

## 8. Safety Checklist

| Item | Phase 31 Status |
|------|----------------|
| Workflow JSON changed in Phase 31 | NO |
| `active = true` introduced | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n import executed in Phase 31 | NO |
| n8n execution performed in Phase 31 | NO |
| Auto-post / auto-reply / ads | NO |
| Real customer data used | NO |
| Production system modified | NO |
| Production side effect risk | NO |

---

## 9. Next Phase Plan — Phase 32 & Phase 33

The following is the **default and required plan**. This is not optional.

| Phase | Name | Scope | Constraint |
|-------|------|-------|------------|
| **Phase 32** | Creative Asset Auto Sandbox Re-import Only | Re-import patched workflow JSON to n8n sandbox. Verify INACTIVE. Verify no credentials. Stop. No execution. | No execution. No activation. No credentials. No API calls. |
| **Phase 33** | Creative Asset Auto Sandbox Manual Execution Check | Manual execution of re-imported workflow. Verify Set Input Variables 19-field output. Verify no "empty" message. | No activation. No publish. No credentials. No real API calls. Sandbox only. |

**Rationale:** Re-import and execution are separate actions with separate risk profiles and separate Owner approval gates. If re-import reveals unexpected behavior (node upgrade prompt, overwrite conflict, wrong n8n version), Owner can stop at Phase 32 before any execution decision is required.

### Combined Import + Execution — Owner Override Only

Combining Phase 32 and Phase 33 into a single phase (re-import + execute in one session) is **not the default path** and should not be treated as a normal option.

Owner may override to a combined phase **only if**:
1. Owner explicitly states the override in the session approval.
2. ChatGPT Architect approves the combined scope in the command.
3. Phase 32 import steps complete without any unexpected behavior before execution begins.

If any unexpected behavior occurs during import in a combined session, Owner must stop and treat it as Phase 32 only — no execution until a new phase is opened.

---

## 10. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build — `creative_asset_auto_skeleton` created | DONE + PUSHED |
| Phase 26 | First Sandbox Import — PASS | DONE + PUSHED |
| Phase 27 | Sandbox Manual Execution — PASS WITH NOTES (Set Input Variables empty display) | DONE + PUSHED |
| Phase 28 | Sandbox I/O Standardization | DONE + PUSHED |
| Phase 29 | Safe Sample Input Patch Planning | DONE + PUSHED |
| Phase 30 | Safe Sample Input Patch Implementation | DONE + PUSHED (commit `18c681d`) |
| **Phase 31** | **Sandbox Re-import & Manual Execution Planning (this phase)** | **PLAN_READY** |
| Phase 32 (TBD) | Re-import patched workflow to n8n sandbox | NOT STARTED |
| Phase 33 (TBD) | Manual execution check — verify 19-field output | NOT STARTED |

---

## 11. Safety Confirmation

| Item | Confirmed |
|------|-----------|
| Workflow JSON modified | NO |
| `active = true` introduced | NO |
| Real credentials in any new file | NO |
| Real API calls | NO |
| Auto-post / auto-reply / ads | NO |
| Real customer data | NO |
| n8n import performed | NO |
| n8n execution performed | NO |
| Production system modified | NO |
| Production side effect risk | NO |
| Scope creep beyond planning/docs | NO |
