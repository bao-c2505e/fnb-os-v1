# Phase 0.4 — n8n Smoke Test Workflows

**Phase:** 0.4
**Created:** 2026-05-26
**Created By:** Claude Code (Builder Agent)
**Status:** READY FOR HUMAN ACTION IN n8n

---

## Objective

Verify that all n8n credentials are working before any real automation workflow is built.

Each smoke test is a minimal, safe, read-only or test-send workflow that:
- Runs **manually only** (never on a schedule)
- Has **`active: false`** (cannot be triggered automatically)
- Does **not post** to customers, social media, or ads platforms
- Does **not write** to production data
- Proves the credential is connected and the API responds

A PASS on all 5 smoke tests = green light to proceed to Phase 1 workflow scaffolding.

---

## Safety Rules

| Rule | Detail |
|------|--------|
| `active: false` | All 5 workflows must remain inactive — never enable on schedule |
| No auto-publish | `AUTO_PUBLISH_ENABLED=false` in `.env` at all times during Phase 0 |
| No auto-reply | No workflow replies to real customers in Phase 0 |
| No ads spend | No workflow touches Facebook Ads, TikTok Ads, or Google Ads |
| Manual trigger only | Every test is started by clicking **Execute Workflow** in n8n UI |
| No hardcoded secrets | All secrets live in n8n's encrypted credential store, never in JSON files |
| `.env` stays local | Never commit `.env` to GitHub |
| Revoke exposed keys | If any key appeared in a screenshot or chat, revoke it immediately (see bottom of this doc) |

---

## Workflow List

| ID | File | Purpose | Credential Used |
|----|------|---------|-----------------|
| SMOKE-01 | `smoke-01-telegram-credential-test.json` | Send test message to Telegram | `Telegram - FNB OS V1` |
| SMOKE-02 | `smoke-02-google-sheets-read-test.json` | Read rows from `Config` tab | `Google Sheets - FNB OS V1` |
| SMOKE-03 | `smoke-03-google-drive-folder-search-test.json` | Search for Drive folder by name | `Google Drive - FNB OS V1` |
| SMOKE-04 | `smoke-04-openai-short-reply-test.json` | One-sentence OpenAI completion | `OpenAI - FNB OS V1` |
| SMOKE-05 | `smoke-05-gemini-short-reply-test.json` | One-sentence Gemini completion | `Gemini - FNB OS V1` |

All files are located in: `n8n/smoke-tests/`

---

## Import Instructions

### Step 1 — Open n8n

Navigate to: **https://n8n.baon8n.blog**

### Step 2 — Import each workflow

For each of the 5 JSON files:

1. Go to **Workflows → Add Workflow → Import from file**
2. Select the JSON file from `n8n/smoke-tests/`
3. n8n will show the imported workflow
4. **Do NOT activate** — leave the toggle OFF
5. Proceed to credential mapping (Step 3) before running

### Step 3 — Map credentials after import

When n8n imports a workflow, it attempts to match credentials by name.
If the credential names in your n8n instance exactly match the names below, mapping is automatic.
If there is a mismatch, open each node and re-select the credential manually.

| Workflow | Node | Credential Name Required |
|----------|------|--------------------------|
| SMOKE-01 | Telegram Send Message | `Telegram - FNB OS V1` |
| SMOKE-02 | Read Config Sheet | `Google Sheets - FNB OS V1` |
| SMOKE-03 | Search Drive Folder | `Google Drive - FNB OS V1` |
| SMOKE-04 | OpenAI Short Reply | `OpenAI - FNB OS V1` |
| SMOKE-05 | Gemini Short Reply | `Gemini - FNB OS V1` |

### Step 4 — Manual field replacements required

Some fields use safe placeholders that must be filled in the n8n UI (not in the repo JSON):

| Workflow | Field | Placeholder in JSON | Action Required |
|----------|-------|--------------------|-----------------| 
| SMOKE-01 | Chat ID | `REPLACE_WITH_TELEGRAM_CHAT_ID` | Open node → paste your `TELEGRAM_CHAT_ID` from `.env` |
| SMOKE-02 | Document | `REPLACE_WITH_GOOGLE_SHEET_ID` | Open node → click Document selector → search for `FNB_OS_V1_CONTROL_CENTER` → select it |
| SMOKE-03 | (none) | — | No manual field required — query is pre-set |
| SMOKE-04 | (none) | — | No manual field required |
| SMOKE-05 | (none) | — | No manual field required |

> **Important:** Do not paste Sheet IDs or Chat IDs back into the JSON files and commit them.
> All IDs that identify your accounts stay in n8n's runtime config, not in the repo.

### Step 5 — Run each workflow

1. Open the workflow in n8n
2. Click **Execute Workflow** (top right)
3. Observe the output in the execution panel
4. Record PASS or FAIL in `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`

---

## Credential Mapping Instructions

### How n8n resolves credentials on import

When you import a workflow JSON, n8n looks for credentials in its database that match the `name` field in the JSON's `credentials` block. Example:

```json
"credentials": {
  "telegramApi": {
    "id": "REPLACE_AFTER_IMPORT",
    "name": "Telegram - FNB OS V1"
  }
}
```

n8n ignores the `id` value from the file and searches its database for a credential named exactly **`Telegram - FNB OS V1`**. If found, it maps automatically. The `id` is re-assigned to the n8n-internal ID.

### If credential mapping fails after import

1. Open the workflow node that shows a credential error
2. Click the credential dropdown
3. Select the correct credential from your n8n store
4. Save the workflow

---

## SMOKE-05 Gemini — Credential Type Note

SMOKE-05 uses an HTTP Request node (n8n has no native Gemini node).

The credential type used is **`httpHeaderAuth`** with:
- Header name: `x-goog-api-key`
- Header value: your Gemini API key (stored encrypted in n8n)

If your `Gemini - FNB OS V1` credential was created as **Query Parameter Auth** instead:
1. Open the SMOKE-05 node in n8n
2. Change **Generic Auth Type** from `Header Auth` to `Query Auth`
3. Re-map the credential
4. The API key will be sent as `?key=YOUR_KEY` instead of a header

---

## Test Checklist

Complete in order. Mark each item before proceeding to the next.

### Pre-flight
- [ ] All 5 credentials exist in n8n and show green "Connection tested"
- [ ] Google Drive API enabled in Google Cloud Console
- [ ] Google Sheets API enabled in Google Cloud Console
- [ ] Telegram bot added to approval chat group
- [ ] `.env` confirmed NOT committed (`git status` shows no `.env`)
- [ ] All 5 workflow files imported into n8n

### Per-workflow
- [ ] SMOKE-01: Chat ID replaced, workflow saved, execution triggered
- [ ] SMOKE-02: Document selected as `FNB_OS_V1_CONTROL_CENTER / Config`, execution triggered
- [ ] SMOKE-03: Execution triggered, folder result returned
- [ ] SMOKE-04: Execution triggered, Vietnamese sentence returned
- [ ] SMOKE-05: Execution triggered, Vietnamese sentence returned

### Post-run
- [ ] All 5 results logged in `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`
- [ ] All 5 workflows still have `active = OFF` (verify in n8n workflow list)
- [ ] No workflow is running on a schedule
- [ ] Results committed to GitHub

---

## PASS / FAIL Result Table

Fill this in after running each workflow. Also update `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`.

| ID | Workflow | Status | Notes |
|----|----------|--------|-------|
| SMOKE-01 | Telegram Credential Test | ☐ PASS / ☐ FAIL | |
| SMOKE-02 | Google Sheets Read Test | ☐ PASS / ☐ FAIL | |
| SMOKE-03 | Google Drive Folder Search | ☐ PASS / ☐ FAIL | |
| SMOKE-04 | OpenAI Short Reply | ☐ PASS / ☐ FAIL | |
| SMOKE-05 | Gemini Short Reply | ☐ PASS / ☐ FAIL | |

---

## Troubleshooting

### SMOKE-01 Telegram — "Chat not found" error
- Cause: Chat ID is wrong or bot is not in the group
- Fix: Confirm `TELEGRAM_CHAT_ID` in `.env` is correct
- Fix: Confirm the bot (`Telegram - FNB OS V1`) has been added to the approval chat group

### SMOKE-01 Telegram — "Unauthorized" error
- Cause: Bot token is incorrect or revoked
- Fix: Regenerate token via BotFather → update in n8n credential → test again
- **If token was exposed in a screenshot:** revoke it via BotFather immediately (see below)

### SMOKE-02 Google Sheets — "Not found" or "403"
- Cause: Sheet ID is wrong, or the Google account used for OAuth does not have access to the sheet
- Fix: Confirm the sheet `FNB_OS_V1_CONTROL_CENTER` is shared with the account used in the credential
- Fix: Re-select the document via the n8n node UI after import

### SMOKE-02 Google Sheets — "Sheets API not enabled"
- Cause: Google Sheets API was not enabled in Google Cloud Console
- Fix: Go to console.cloud.google.com → APIs & Services → Library → enable **Google Sheets API**

### SMOKE-03 Google Drive — "Drive API not enabled"
- Cause: Google Drive API was not enabled
- Fix: Go to console.cloud.google.com → APIs & Services → Library → enable **Google Drive API**

### SMOKE-03 Google Drive — Empty results
- Not an error. The folder just may not be named exactly `FnB OS V1`.
- Fix: Check your Drive folder name and adjust the query in the node if needed

### SMOKE-04 OpenAI — "Incorrect API key"
- Cause: The API key in the `OpenAI - FNB OS V1` credential is wrong or expired
- Fix: Regenerate key at platform.openai.com → update in n8n credential

### SMOKE-04 OpenAI — "Model not found"
- Cause: `gpt-4o` is not available on your plan
- Fix: Open the node in n8n → change model to `gpt-4o-mini` or another available model

### SMOKE-05 Gemini — "400 Bad Request" or "API key not valid"
- Cause: The credential was set up with wrong auth type or wrong key
- Fix: Check whether your credential uses Header Auth (`x-goog-api-key`) or Query Auth (`key`)
- Fix: Regenerate key at aistudio.google.com → update in n8n credential

### SMOKE-05 Gemini — "429 Resource Exhausted"
- Cause: Free tier rate limit hit
- Fix: Wait 1 minute and retry — or upgrade to paid tier

---

## Done Criteria

Phase 0.4 is **COMPLETE** when ALL of the following are true:

1. All 5 smoke tests return PASS in n8n execution panel
2. Results recorded in `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`
3. All 5 workflows remain `active = false` after testing
4. No secret values were committed to GitHub
5. Results committed to the `main` branch

When done, signal to Chief Architect (ChatGPT) to begin **Phase 1 — Google Sheet & Drive Setup**.

---

## Security Reminder — Revoke Exposed Keys

If any of the following were shared in a screenshot, message, or chat window at any point:
- Telegram bot token
- n8n API key
- OpenAI API key
- Gemini API key
- Google OAuth client secret

**Revoke and regenerate them immediately before proceeding to production.**

| Key | Where to Revoke |
|-----|-----------------|
| Telegram bot token | Telegram → BotFather → `/revoke` |
| OpenAI API key | platform.openai.com → API Keys → Delete + Create new |
| Gemini API key | aistudio.google.com → API Keys → Delete + Create new |
| Google OAuth secret | console.cloud.google.com → Credentials → Reset secret |
| n8n API key | n8n → Settings → n8n API → Revoke + Create new |
| GitHub token | github.com → Settings → Developer Settings → Tokens → Revoke |

Revoked keys have no effect on workflow JSON in this repo — credentials are stored in n8n's database, not in the files. Regenerate, update n8n credential, re-test.
