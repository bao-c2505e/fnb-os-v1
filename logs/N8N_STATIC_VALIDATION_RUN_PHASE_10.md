# n8n Static Validation Run — Phase 10

**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Phase:** 10 — n8n Import Dry Run and Validation
**Validator Script:** `scripts/validate_n8n_workflows.mjs`

---

## Session Details

| Field | Value |
|-------|-------|
| Date | 2026-05-28 |
| Agent | Claude Code (AGT-02) |
| Phase | 10 |
| Working Directory | `D:\FNB_OS_V1` |
| Node.js Detected | **NO** |
| Validator Run Status | **BLOCKED_BY_ENVIRONMENT** |
| Manual Inspection Status | **PASS** |
| Phase 8 JSON Modified | **NO — untouched** |
| Secrets Found | **NONE** |

---

## Node.js Environment Status

```
Command: node --version
Result:  'node' is not recognized / command not found
Exit:    127 (not found)
Status:  BLOCKED_BY_ENVIRONMENT
```

Node.js is not installed or not on the system PATH on this machine.
The automated script `scripts/validate_n8n_workflows.mjs` could not be executed.

**This is not a project failure.** Per approved Phase 10 conditions (condition 11):
> If Node.js is not confirmed/available, record validator run as BLOCKED_BY_ENVIRONMENT, not project failure.

To resolve: Install Node.js >= 16 (`https://nodejs.org`) and re-run `node scripts/validate_n8n_workflows.mjs`.

---

## Automated Validator Run Result

| Status | BLOCKED_BY_ENVIRONMENT |
|--------|----------------------|
| Script path | `scripts/validate_n8n_workflows.mjs` |
| Reason | Node.js not found on system PATH |
| Action required | Owner installs Node.js >= 16 and re-runs script |
| Exit code | N/A — not executed |

---

## Manual Static Inspection — Summary

All 6 Phase 8 workflow JSON files were read and inspected manually against the 11-check criteria from `scripts/validate_n8n_workflows.mjs`. This inspection covers the same checks the automated script would perform.

### Inspection Criteria

| # | Check | Applies To |
|---|-------|-----------|
| C-01 | File exists at expected path | All 6 |
| C-02 | Valid JSON (parseable) | All 6 |
| C-03 | `"active": false` | All 6 |
| C-04 | `"name"` field present and non-empty | All 6 |
| C-05 | `"name"` contains `[SKELETON]` | All 6 |
| C-06 | `"nodes"` array present and non-empty | All 6 |
| C-07 | `Error Trigger` node present | All 6 |
| C-08 | `Sticky Note: WARNING` node present | All 6 |
| C-09 | Secret scan: 7 patterns (see below) | All 6 |
| C-10 | `"versionId"` is placeholder | All 6 |
| C-11 | `"meta.instanceId"` is placeholder | All 6 |

### Secret Scan Patterns Checked

| Pattern | What It Detects |
|---------|----------------|
| `sk-ant-` | Anthropic API key (live) |
| `sk-` | OpenAI / other provider key prefix |
| `BEGIN PRIVATE KEY` | PEM private key |
| `ghp_` or `github_pat_` | GitHub personal access token |
| `eyJhbGciOi` | JWT token (base64 header) |
| Telegram bot token regex | Format: `[0-9]+:AA[A-Za-z0-9_-]{33}` |
| `"type": "service_account"` | Google service account JSON |

---

## Per-File Inspection Results

### WF-01: `n8n/workflows/content_auto_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed, no syntax errors |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — Content Auto [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 15 nodes |
| C-07 Error Trigger present | PASS | Node id `a1000001-0012`, type `n8n-nodes-base.errorTrigger` |
| C-08 Sticky Note present | PASS | Node id `a1000001-0015`, type `n8n-nodes-base.stickyNote` |
| C-09 Secret scan | PASS — CLEAN | All credentials are `REPLACE_WITH_*` placeholders only |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**Additional checks:**
- Approval gate: `Set: approval_status = Draft` ✓
- Log step: `Code: Write Log Entry` ✓
- NoOp publish stub: `NoOp: STUB — Send to Approval Queue` ✓
- Codex constraint enforced: No `hashtags` or `human_review_required` in content output ✓

---

### WF-02: `n8n/workflows/creative_asset_auto_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — Creative Asset Auto [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 15 nodes |
| C-07 Error Trigger present | PASS | Node id `a2000002-0012` |
| C-08 Sticky Note present | PASS | Node id `a2000002-0015` |
| C-09 Secret scan | PASS — CLEAN | All credentials are `REPLACE_WITH_*` placeholders |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**Additional checks:**
- Brief-only output confirmed (no asset generation in skeleton) ✓
- Approval gate: `Set: approval_status = Draft` ✓
- Log step: `Code: Write Log Entry` ✓
- NoOp publish stub present ✓

---

### WF-03: `n8n/workflows/ads_pack_auto_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — Ads Pack Auto [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 15 nodes |
| C-07 Error Trigger present | PASS | Node id `a3000003-0012` |
| C-08 Sticky Note present | PASS | Node id `a3000003-0015`, color=4 (orange — high-risk) |
| C-09 Secret scan | PASS — CLEAN | No Meta Ads / TikTok Ads API credentials present |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**High-risk checks (ads):**
- No Meta/TikTok/Zalo Ads API call nodes ✓
- `compliance_notes` field populated in mock output ✓
- `ads_spend_committed: false` in error log node ✓
- NoOp stub: "CRITICAL: NO Meta / TikTok / Zalo Ads API call here" ✓
- Approval gate enforces no-ads-spend until Owner approval ✓

---

### WF-04: `n8n/workflows/crm_followup_auto_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — CRM Follow-Up Auto [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 15 nodes |
| C-07 Error Trigger present | PASS | Node id `a4000004-0012` |
| C-08 Sticky Note present | PASS | Node id `a4000004-0015`, color=4 (orange — high-risk) |
| C-09 Secret scan | PASS — CLEAN | No Zalo/Messenger/SMS credentials present |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**High-risk checks (CRM/messaging):**
- No Zalo / Facebook Messenger / SMS API call nodes ✓
- `human_review_required: true` hardcoded in `Set: Draft Status + Human Review Flag` node ✓
- Schema const enforced in validation node (check: `seq.human_review_required !== true` fails) ✓
- `messages_sent_to_customers: false` in error log node ✓
- NoOp stub: "CRITICAL: NO Zalo / Facebook Messenger / SMS API call here" ✓

---

### WF-05: `n8n/workflows/comment_inbox_reply_assistant_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 13 nodes (escalation gate reduces count vs other workflows) |
| C-07 Error Trigger present | PASS | Node id `a5000005-0010` |
| C-08 Sticky Note present | PASS | Node id `a5000005-0015`, color=4 (orange — high-risk) |
| C-09 Secret scan | PASS — CLEAN | No FB/TikTok/Instagram/Zalo credentials present |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**High-risk checks (inbox/auto-reply):**
- Escalation gate present: `If: Escalation Required` node ✓
- TRUE branch (escalated): `Set: Escalation Flag — No Draft` → `draft_reply = ""`, no AI generation ✓
- FALSE branch (safe): `Code: AI Generate Reply Draft` → stub only ✓
- `human_review_required: true` set on both escalation and draft paths ✓
- `auto_reply_sent: false` in error log node ✓
- NoOp stub: "CRITICAL: NO Facebook / TikTok / Instagram / Zalo API call here" ✓

---

### WF-06: `n8n/workflows/approval_publishing_skeleton.json`

| Check | Result | Notes |
|-------|--------|-------|
| C-01 File exists | PASS | Confirmed |
| C-02 Valid JSON | PASS | Fully parsed |
| C-03 `active: false` | PASS | Line 7: `"active": false` |
| C-04 Name present | PASS | `"FnB OS V1 — Approval and Publishing Gate [SKELETON]"` |
| C-05 Name contains [SKELETON] | PASS | Confirmed |
| C-06 Nodes array non-empty | PASS | 18 nodes (largest workflow — Switch has 5 branches) |
| C-07 Error Trigger present | PASS | Node id `a6000006-0014` |
| C-08 Sticky Note present | PASS | Node id `a6000006-0016`, color=5 (blue — approval gate) |
| C-09 Secret scan | PASS — CLEAN | No platform or Ads API credentials present |
| C-10 versionId placeholder | PASS | `"REPLACE_WITH_VERSION_ID"` |
| C-11 instanceId placeholder | PASS | `"REPLACE_WITH_INSTANCE_ID"` |
| **Overall** | **PASS** | All 11 checks passed |

**High-risk checks (publishing gate):**
- All 5 publish branches are NoOp stubs ✓
  - `NoOp: STUB — Publish Content to Platform` ✓
  - `NoOp: STUB — Archive Creative Brief` ✓
  - `NoOp: STUB — Launch Ads Campaign` ✓
  - `NoOp: STUB — Send CRM Messages` ✓
  - `NoOp: STUB — Post Reply to Channel` ✓
- Not-approved path: `Stop and Error: Not Approved` hard-blocks items without Owner approval ✓
- `publishing_occurred: false` in error log node ✓
- Switch node covers all 5 item_types from `approval-status.schema.json` enum ✓
- Webhook trigger uses placeholder path (`REPLACE_WITH_WEBHOOK_PATH`) ✓

---

## Manual Inspection Overall Result

| Workflow File | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | **Overall** |
|---------------|------|------|------|------|------|------|------|------|------|------|------|------------|
| content_auto_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| creative_asset_auto_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| ads_pack_auto_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| crm_followup_auto_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| comment_inbox_reply_assistant_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| approval_publishing_skeleton.json | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| **Summary** | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | **6/6 PASS** |

---

## Secret Scan Result

| Pattern | WF-01 | WF-02 | WF-03 | WF-04 | WF-05 | WF-06 |
|---------|-------|-------|-------|-------|-------|-------|
| `sk-ant-` (Anthropic key) | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| `sk-` (other provider key) | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| `BEGIN PRIVATE KEY` | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| `ghp_` / `github_pat_` | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| `eyJhbGciOi` (JWT) | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| Telegram bot token | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |
| `"type": "service_account"` | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN |

**All 7 secret patterns × 6 files = 42 checks: ALL CLEAN**

All credential references in workflow files use `REPLACE_WITH_*` placeholder strings only.

---

## Phase 8 Workflow JSON Integrity

All 6 Phase 8 workflow files were **read only** — no edits, no writes, no modifications.

Phase 8 workflow files are committed state (commit `ad867b3`) and were not changed in this session. They remain at committed state with no local modifications.

**Note on overall working tree:** Phase 10 files have not yet been committed. As of this session, `git status --short` shows 4 modified state/log files (tracked) and 4 new Phase 10 files (untracked). This is the expected pre-commit state. The working tree will be clean only after Owner approves commit and commit is executed.

---

## Checks Summary

| Check | Result |
|-------|--------|
| Node.js available | NO — BLOCKED_BY_ENVIRONMENT |
| Automated validator run | BLOCKED_BY_ENVIRONMENT |
| Manual static inspection | PASS — 6/6 files, all 11 checks |
| Secret scan (42 total checks) | ALL CLEAN |
| Phase 8 JSON untouched | CONFIRMED — committed at `ad867b3`, no local modifications |
| Git status | PRE-COMMIT — 4 modified tracked files + 4 untracked Phase 10 files (expected) |
| Commit made | NO |
| Push made | NO |

---

## Next Steps for Owner

1. **Install Node.js >= 16** — download from nodejs.org
2. **Run automated validator**: `node scripts/validate_n8n_workflows.mjs`
3. **Expected result**: all 66 checks PASS (exit code 0)
4. **If any check fails**: use `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` to log the issue
5. **Follow dry run procedure**: see `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`
6. **Fill import log**: copy `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md` and fill after import session
7. **Fill import checklist**: use `docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md`

---

*Phase 10 — n8n Import Dry Run and Validation*
*Builder: Claude Code (AGT-02) — 2026-05-28*
