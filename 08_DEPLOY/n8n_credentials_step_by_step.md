# n8n Credential Creation — Step-by-Step Guide

**Phase:** 0.3
**Created:** 2026-05-26
**Created By:** Claude Code (Builder Agent)
**Status:** READY FOR HUMAN ACTION

---

## Before You Start

| Rule | Detail |
|------|--------|
| Never paste secrets into chat | Fill credentials only inside n8n UI or your local `.env` file |
| `.env` stays local | Never commit `.env` to GitHub |
| No auto-publish in Phase 0 | `AUTO_PUBLISH_ENABLED=false` must remain set |
| No auto-reply in Phase 0 | All reply workflows are disabled until Phase 6 |
| Source of truth | This file documents the credential *names and structure* only — real values live in n8n's encrypted credential store |

Open your n8n instance at: **https://n8n.baon8n.blog**

Navigate to: **Settings → Credentials → Add Credential**

---

## Credential 1 — OpenAI

**Credential name in n8n:** `OpenAI - FNB OS V1`

### Steps

1. In n8n: **New Credential → OpenAI**
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `OpenAI - FNB OS V1` |
| API Key | Paste from your `.env`: `OPENAI_API_KEY` |

3. Click **Save** and then **Test** to confirm the connection.
4. n8n will show a green checkmark if the key is valid.

### Notes
- The Organization ID and Project ID are optional in n8n's built-in OpenAI node.
- If you use an HTTP Request node to call OpenAI directly, add a **Header Auth** credential instead with header `Authorization: Bearer <your key>`.
- Model used: `gpt-5.5` (set at the node level, not in the credential).

---

## Credential 2 — Gemini (Google AI)

**Credential name in n8n:** `Gemini - FNB OS V1`

### Steps

1. In n8n: **New Credential → HTTP Header Auth** (Gemini does not have a native n8n node yet — use HTTP Request)
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `Gemini - FNB OS V1` |
| Header Name | `x-goog-api-key` |
| Header Value | Paste from your `.env`: `GEMINI_API_KEY` |

3. Click **Save**.

### Alternative: Query Parameter Auth
Some Gemini endpoints accept the key as a query parameter:

| Field | Value |
|-------|-------|
| Name | `Gemini - FNB OS V1` |
| Auth Type | Query Parameter |
| Parameter Name | `key` |
| Parameter Value | Paste `GEMINI_API_KEY` |

4. In the HTTP Request node, set base URL to:
   ```
   https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent
   ```

### Notes
- Model: `gemini-2.5-flash` (set in the request body, not the credential).
- Keep the credential name exactly `Gemini - FNB OS V1` so workflow JSON references are consistent.

---

## Credential 3 — Telegram

**Credential name in n8n:** `Telegram - FNB OS V1`

### Steps

1. In n8n: **New Credential → Telegram**
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `Telegram - FNB OS V1` |
| Access Token | Paste from your `.env`: `TELEGRAM_BOT_TOKEN` |

3. Click **Save** and **Test**.
4. n8n will call `getMe` on the bot API to verify the token.

### Notes
- The Chat ID (`TELEGRAM_CHAT_ID`) is **not** stored in the credential — it goes in the **node parameter** inside each workflow (Telegram Send Message → Chat ID field).
- Use `TELEGRAM_CHAT_ID` from your `.env` as a workflow variable or hardcode the chat ID in the node directly.
- For the escalation channel, use `TELEGRAM_ESCALATION_CHAT_ID` (if separate from the approval chat).

---

## Credential 4 — Google Drive

**Credential name in n8n:** `Google Drive - FNB OS V1`

### Google Cloud Setup (do this first)

#### Step A — Enable the Google Drive API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Select your project (or create one: `fnb-os-v1`)
3. Navigate to: **APIs & Services → Library**
4. Search: **Google Drive API** → Click **Enable**

#### Step B — Create OAuth 2.0 Credentials

1. Navigate to: **APIs & Services → Credentials → Create Credentials → OAuth client ID**
2. Application type: **Web application**
3. Name: `n8n FNB OS V1`
4. **Authorized redirect URIs** — add the URI from n8n:
   - In n8n, when creating a Google credential, n8n shows you its OAuth redirect URL
   - It looks like: `https://n8n.baon8n.blog/rest/oauth2-credential/callback`
   - Copy that URL exactly and paste it into the Google Cloud redirect URI field
5. Click **Create** → Download or copy the **Client ID** and **Client Secret**

#### Step C — Create the n8n Credential

1. In n8n: **New Credential → Google Drive OAuth2**
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `Google Drive - FNB OS V1` |
| Client ID | Paste from Google Cloud |
| Client Secret | Paste from Google Cloud |

3. Click **Sign in with Google** — authorize the account that owns the Drive folder.
4. n8n stores the OAuth tokens automatically.

### Notes
- The Root Folder ID (`GOOGLE_DRIVE_ROOT_FOLDER_ID`) goes in the **node parameter** inside workflows, not in the credential.
- The service account path in your `.env` (`GOOGLE_SERVICE_ACCOUNT_KEY_PATH`) is for non-n8n scripts only. n8n itself uses OAuth.

---

## Credential 5 — Google Sheets

**Credential name in n8n:** `Google Sheets - FNB OS V1`

### Google Cloud Setup (do this first)

#### Step A — Enable the Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Same project as above (`fnb-os-v1`)
3. Navigate to: **APIs & Services → Library**
4. Search: **Google Sheets API** → Click **Enable**

> You need **both** Google Drive API and Google Sheets API enabled.
> Drive API: for listing files, uploading assets.
> Sheets API: for reading and writing spreadsheet data.

#### Step B — Reuse or Create OAuth Credentials

Option A — **Reuse the same OAuth client** created for Google Drive:
- Use the same Client ID and Client Secret.
- Both APIs are accessible with the same OAuth scope if you authorize both when connecting.

Option B — **Create a second OAuth client** (cleaner separation):
- Follow the same Step B process as Google Drive above.
- Name it `n8n FNB OS V1 Sheets`.
- Add the same n8n redirect URI.

#### Step C — Create the n8n Credential

1. In n8n: **New Credential → Google Sheets OAuth2**
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `Google Sheets - FNB OS V1` |
| Client ID | Paste from Google Cloud |
| Client Secret | Paste from Google Cloud |

3. Click **Sign in with Google** → authorize.
4. When Google asks for permissions, allow both **Sheets** and **Drive** scopes.

### Notes
- The Sheet ID (`GOOGLE_SHEET_CONTROL_CENTER_ID`) goes in the **node parameter** inside each workflow.
- Tab names (e.g., `Campaigns`, `Content Packs`) go in the **Sheet Name** field in the node.
- Do not store Sheet IDs inside the credential — they are workflow-level values.

---

## Credential 6 — GitHub

**Credential name in n8n:** `GitHub - FNB OS V1`

### Steps

1. In n8n: **New Credential → GitHub**
2. Fill in:

| Field | Value |
|-------|-------|
| Name | `GitHub - FNB OS V1` |
| Access Token | Paste from your `.env`: `GITHUB_TOKEN` |

3. Click **Save** and **Test**.

### GitHub Token Setup (if not done yet)

1. Go to [github.com → Settings → Developer Settings → Personal Access Tokens → Fine-grained tokens](https://github.com/settings/personal-access-tokens)
2. Click **Generate new token**
3. Token name: `fnb-os-v1-n8n`
4. Expiration: 90 days (rotate on expiry)
5. Repository access: **Only selected repositories** → `bao-c2505e/fnb-os-v1`
6. Repository permissions:
   - **Contents**: Read and Write (for reading/writing files)
   - **Metadata**: Read (required)
7. Click **Generate token** → Copy immediately → paste into `.env` as `GITHUB_TOKEN`

### Notes
- This token is used by n8n to read/write workflow files and phase logs to the repo.
- Fine-grained tokens scoped to a single repo are safer than classic personal access tokens.

---

## Google APIs Summary

Both APIs must be enabled in the same Google Cloud project before n8n credentials will work:

| API | Purpose | Enable At |
|-----|---------|-----------|
| Google Drive API | Upload assets, manage folders | console.cloud.google.com → Library |
| Google Sheets API | Read/write campaign data, CRM, logs | console.cloud.google.com → Library |

OAuth Redirect URI for n8n:
```
https://n8n.baon8n.blog/rest/oauth2-credential/callback
```
This URI must be registered in **Google Cloud → APIs & Services → Credentials → OAuth 2.0 Client → Authorized redirect URIs**.

---

## Safety Checklist After Setup

Run these checks after creating all credentials:

- [ ] All 6 credentials created with exact names above
- [ ] All credentials show green **Connection tested successfully** in n8n
- [ ] `.env` still not committed (`git status` does not show `.env`)
- [ ] `AUTO_PUBLISH_ENABLED=false` in `.env`
- [ ] `HUMAN_APPROVAL_REQUIRED=true` in `.env`
- [ ] No workflow is active yet (all workflows in `04_WORKFLOWS/` are PLANNED state)
- [ ] Telegram bot test message received in approval chat

---

## Credential Name Reference (for workflow JSON authors)

Every workflow JSON in `04_WORKFLOWS/` must reference credentials using these exact names:

```json
"credentials": {
  "openAiApi": {
    "id": "[n8n internal id]",
    "name": "OpenAI - FNB OS V1"
  }
}
```

| Service | Exact Credential Name |
|---------|----------------------|
| OpenAI | `OpenAI - FNB OS V1` |
| Gemini | `Gemini - FNB OS V1` |
| Telegram | `Telegram - FNB OS V1` |
| Google Drive | `Google Drive - FNB OS V1` |
| Google Sheets | `Google Sheets - FNB OS V1` |
| GitHub | `GitHub - FNB OS V1` |

Consistent names mean any exported workflow JSON will reference the same credential names across environments.

---

## What Comes Next

**Phase 0.4 — n8n Smoke Test Workflows**

Once all 6 credentials are created and tested in n8n:

1. Build 3 minimal smoke test workflows (no real logic yet):
   - **Smoke Test 1:** Read one row from `Google Sheets - FNB OS V1` → log to execution log
   - **Smoke Test 2:** Send a test message via `Telegram - FNB OS V1` to approval chat
   - **Smoke Test 3:** List files in root folder via `Google Drive - FNB OS V1`

2. Run each smoke test manually from n8n (not on schedule).

3. Confirm all pass — log results in `09_LOGS/PHASE_LOG.md`.

4. Export workflow JSON files to `04_WORKFLOWS/` (credentials stripped, placeholders only).

5. Update `04_WORKFLOWS/workflow_inventory.md` status from `PLANNED` → `STAGED`.

**Do not activate any workflow on a schedule until Phase 4 dry run is complete and user approves.**
