# n8n Import Issue Template

**Template Version:** 1.0 — 2026-05-28
**Usage:** Copy this file to `logs/N8N_IMPORT_ISSUE_[WORKFLOW]-[DATE].md` and fill in all fields.

---

## Issue Details

| Field | Value |
|-------|-------|
| Issue ID | `II-[WORKFLOW_SHORT]-[DATE]-[SEQ]` (e.g. `II-CONTENT-20260529-001`) |
| Date | [FILL: YYYY-MM-DD] |
| Reported By | [FILL: Owner / Claude Code / Codex] |
| Phase | 10 |
| Workflow File | [FILL: e.g. `n8n/workflows/content_auto_skeleton.json`] |
| Workflow Name | [FILL: e.g. `FnB OS V1 — Content Auto [SKELETON]`] |
| n8n Version | [FILL: e.g. `1.45.0`] |
| Issue Type | [SELECT: Import Error / Active Status / Credential Found / Execution Triggered / Node Type Mismatch / STOP Condition / Other] |
| Severity | [SELECT: BLOCKER / WARNING / INFO] |
| Status | [SELECT: OPEN / INVESTIGATING / RESOLVED / WONT_FIX] |

---

## Issue Description

### What Happened

[FILL: Describe exactly what happened during the import or post-import check.]

### Expected Behavior

[FILL: What should have happened according to the Phase 8 spec and Phase 9 checklist.]

### Actual Behavior

[FILL: What was observed.]

---

## Reproduction Steps

1. [FILL: Step 1]
2. [FILL: Step 2]
3. [FILL: Step 3]

---

## Affected Checks

| Check | Expected | Actual |
|-------|----------|--------|
| [FILL e.g. C-03 active=false] | false | [FILL] |

---

## STOP Condition Triggered

| STOP Condition | Triggered? |
|---------------|-----------|
| S-01: Workflow failed to import | [YES / NO] |
| S-02: Workflow shows active=true after import | [YES / NO] |
| S-03: Real credential found (non-placeholder) | [YES / NO] |
| S-04: Execution triggered during import | [YES / NO] |
| S-05: Platform API node not a NoOp stub | [YES / NO] |
| S-06: Secret scan failed before import | [YES / NO] |

---

## Evidence

| Evidence Type | Description |
|--------------|-------------|
| n8n execution log | [FILL or N/A] |
| Node error message | [FILL or N/A] |
| Screenshot reference | [FILL filename or N/A — screenshots do not replace this log] |
| JSON line reference | [FILL: file + line number if relevant] |

---

## Resolution

### Root Cause

[FILL: Why did this happen?]

### Fix Applied

[FILL: What was changed to resolve the issue? If no fix, explain why.]

### Files Modified

[FILL: List any files modified to resolve. If Phase 8 workflow JSON was touched, note the specific change and confirm active=false was not altered.]

### Verified By

[FILL: Who confirmed the fix resolved the issue, and how.]

---

## Resolution Status

| Field | Value |
|-------|-------|
| Resolved Date | [FILL: YYYY-MM-DD or OPEN] |
| Resolved By | [FILL or OPEN] |
| Re-check Required | [YES / NO] |
| Phase 11 Blocker | [YES / NO — is this issue a blocker for Phase 11?] |

---

## Sign-Off

| Role | Name | Date | Verdict |
|------|------|------|---------|
| Builder | Claude Code (AGT-02) | [FILL] | [FILL] |
| Owner | Bo Bao | [FILL] | [SELECT: APPROVED TO PROCEED / HOLD / ESCALATE] |

---

*Template: n8n Import Issue — Phase 10*
*Do not fill original template — copy to a new file first.*
