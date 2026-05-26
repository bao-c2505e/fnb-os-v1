# Phase 0.4 — Smoke Test Results

Append-only log. Fill in after running each workflow in n8n.
Do not delete entries. Add new entries below existing ones if re-testing.

---

## How to fill this log

After running a smoke test in n8n:
1. Open this file
2. Find the correct section
3. Fill in Status, Executed at, Result, and Error (if any)
4. Set Next action
5. Commit the updated log to GitHub

---

## SMOKE-01 — Telegram Credential Test

**File:** `n8n/smoke-tests/smoke-01-telegram-credential-test.json`
**Credential:** `Telegram - FNB OS V1`
**Workflow:** Manual trigger → Send message to approval chat

```
Status:       [ ] PASS  [ ] FAIL  [ ] NOT RUN
Executed at:  
Result:       
Error if any: 
Next action:  
```

---

## SMOKE-02 — Google Sheets Read Test

**File:** `n8n/smoke-tests/smoke-02-google-sheets-read-test.json`
**Credential:** `Google Sheets - FNB OS V1`
**Workflow:** Manual trigger → Read rows from `FNB_OS_V1_CONTROL_CENTER / Config`

```
Status:       [ ] PASS  [ ] FAIL  [ ] NOT RUN
Executed at:  
Result:       
Error if any: 
Next action:  
```

---

## SMOKE-03 — Google Drive Folder Search Test

**File:** `n8n/smoke-tests/smoke-03-google-drive-folder-search-test.json`
**Credential:** `Google Drive - FNB OS V1`
**Workflow:** Manual trigger → Search Drive for folder named `FnB OS V1`

```
Status:       [ ] PASS  [ ] FAIL  [ ] NOT RUN
Executed at:  
Result:       
Error if any: 
Next action:  
```

---

## SMOKE-04 — OpenAI Short Reply Test

**File:** `n8n/smoke-tests/smoke-04-openai-short-reply-test.json`
**Credential:** `OpenAI - FNB OS V1`
**Workflow:** Manual trigger → One-sentence Vietnamese completion

Expected output (approximate):
> Credential OpenAI cho FnB OS V1 đang hoạt động.

```
Status:       [ ] PASS  [ ] FAIL  [ ] NOT RUN
Executed at:  
Result:       
Error if any: 
Next action:  
```

---

## SMOKE-05 — Gemini Short Reply Test

**File:** `n8n/smoke-tests/smoke-05-gemini-short-reply-test.json`
**Credential:** `Gemini - FNB OS V1`
**Workflow:** Manual trigger → One-sentence Vietnamese completion via HTTP Request

Expected output (approximate):
> Credential Gemini cho FnB OS V1 đang hoạt động.

```
Status:       [ ] PASS  [ ] FAIL  [ ] NOT RUN
Executed at:  
Result:       
Error if any: 
Next action:  
```

---

## Summary Table

| ID | Workflow | Status | Executed at |
|----|----------|--------|-------------|
| SMOKE-01 | Telegram Credential Test | NOT RUN | — |
| SMOKE-02 | Google Sheets Read Test | NOT RUN | — |
| SMOKE-03 | Google Drive Folder Search | NOT RUN | — |
| SMOKE-04 | OpenAI Short Reply | NOT RUN | — |
| SMOKE-05 | Gemini Short Reply | NOT RUN | — |

---

## Phase 0.4 Gate

Phase 0.4 is COMPLETE when all 5 rows above show **PASS** and this file is committed to GitHub.

**Next phase after all PASS:** Phase 1 — Google Sheet & Drive Setup
