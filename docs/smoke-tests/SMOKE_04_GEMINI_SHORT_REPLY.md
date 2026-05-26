# SMOKE-04 — Gemini Short Reply Test (Fixed)

**File:** `n8n/smoke-tests/smoke-04-gemini-short-reply.json`
**Phase:** 0.4
**Status:** READY — import and run manually in n8n

---

## Why the Previous Version Failed

The original `smoke-05-gemini-short-reply-test.json` used:

```
Authentication: Generic Credential Type → HTTP Header Auth
Header: x-goog-api-key: <your key>
```

The Google Generative Language REST API **does not accept the API key via HTTP header**.
It requires the key as a **URL query parameter**:

```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_KEY
```

Sending the key in a header returns:
```
403 Forbidden
"Method doesn't allow unregistered callers (callers without established identity).
Please use API Key or other form of API consumer identity to call this API."
```

**The fix:** `authentication: none` + query parameter `key = {{ $env.GEMINI_API_KEY }}`

---

## Step 1 — Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click **Get API key** → **Create API key**
3. Select project `fnb-os-v1` (or create new)
4. Copy the key — it looks like: `AIzaSy...`
5. Store it in your local `D:\FNB_OS_V1\.env` as:
   ```
   GEMINI_API_KEY=AIzaSy_YOUR_KEY_HERE
   ```
6. **Never paste the key into any file that gets committed to GitHub.**

---

## Step 2 — Set GEMINI_API_KEY in n8n's Environment

The workflow uses `={{ $env.GEMINI_API_KEY }}` — an n8n expression that reads the key
from n8n's own environment variables at runtime. You must add it to n8n's environment
**before** running the workflow.

### Option A — Self-hosted n8n with Docker (recommended)

Open your n8n `docker-compose.yml` and add the variable under `environment:`:

```yaml
services:
  n8n:
    image: n8nio/n8n
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      # ... your existing vars ...
      - GEMINI_API_KEY=AIzaSy_YOUR_KEY_HERE   # <-- add this
```

Then restart:
```bash
docker compose down && docker compose up -d
```

### Option B — Self-hosted n8n with .env file

If n8n reads from an `.env` file in its working directory, add:
```
GEMINI_API_KEY=AIzaSy_YOUR_KEY_HERE
```
Restart n8n after editing.

### Option C — n8n Cloud

n8n Cloud does not support `$env` access to custom environment variables.
Use the fallback credential approach described at the end of this document.

### Verify the variable is available

In n8n, create a temporary **Code node** with:
```javascript
return [{ env_set: !!$env.GEMINI_API_KEY, key_length: ($env.GEMINI_API_KEY || '').length }];
```
Execute it — if `env_set: true` and `key_length > 0`, the variable is accessible.
**Delete the Code node after verifying** — do not leave it in any saved workflow.

---

## Step 3 — Import the Workflow into n8n

1. Open n8n at **https://n8n.baon8n.blog**
2. Go to **Workflows → ⊕ Add Workflow → Import from file**
3. Select: `n8n/smoke-tests/smoke-04-gemini-short-reply.json`
4. n8n will load the workflow with 2 nodes: `Manual Trigger` → `Gemini Short Reply`
5. **Do NOT toggle the Active switch** — leave it OFF

No credential mapping is required after import. The API key comes from `$env`, not from an n8n credential store.

---

## Step 4 — Run the Workflow

1. Open the imported workflow
2. Click **Execute Workflow** (top-right button)
3. n8n sends this request:
   ```
   POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=<your key>
   Body: { "contents": [{ "parts": [{ "text": "Reply with exactly this text: FnB OS V1 Gemini smoke test passed." }] }] }
   ```
4. Observe the output in the execution panel

---

## Expected Output

A successful run returns a JSON response from Gemini. The key part to look for:

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "FnB OS V1 Gemini smoke test passed."
          }
        ]
      }
    }
  ]
}
```

The `text` field inside `candidates[0].content.parts[0]` should contain:
```
FnB OS V1 Gemini smoke test passed.
```

If you see this → **SMOKE-04 PASS**. Record it in `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`.

---

## Troubleshooting

### Still getting 403 Forbidden
- Confirm `GEMINI_API_KEY` is set in n8n's environment (Step 2)
- Restart n8n after setting the variable
- Verify the key is valid at [AI Studio](https://aistudio.google.com)

### `$env.GEMINI_API_KEY` returns empty / undefined
- The variable is not in n8n's environment — follow Step 2 again
- Check `N8N_BLOCK_ENV_ACCESS_IN_NODE` — if set to `true`, env access is disabled
  - To fix: remove this setting or set it to `false` and restart n8n

### 400 Bad Request — model not found
- `gemini-1.5-flash` may not be available in your region or API version
- Try changing the URL to use `gemini-1.0-pro` instead:
  ```
  https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro:generateContent
  ```

### 429 Resource Exhausted
- Free tier rate limit reached — wait 1 minute and retry
- Or upgrade to a paid tier at console.cloud.google.com

---

## Fallback — If `$env` Is Not Available (n8n Cloud or Restricted)

If your n8n instance does not support `$env`, use this approach instead:

1. In n8n: **Settings → Credentials → Add Credential → HTTP Query Auth**
2. Fill in:
   - Name: `Gemini Query - FNB OS V1`
   - Parameter name: `key`
   - Parameter value: your Gemini API key
3. In the `Gemini Short Reply` node:
   - Change **Authentication** to `Generic Credential Type`
   - Change **Generic Auth Type** to `Query Auth`
   - Select credential: `Gemini Query - FNB OS V1`
   - Remove the manual `key` query parameter (the credential handles it)
4. Save and re-run

This keeps the key encrypted in n8n's credential store — never in the workflow JSON or repo.

---

## Security Notes

| Rule | Status |
|------|--------|
| API key hardcoded in workflow JSON | NO — uses `$env.GEMINI_API_KEY` expression |
| API key committed to GitHub | NO — stays in n8n environment only |
| Workflow active flag | `false` — manual trigger only |
| Auto-publish enabled | NO — `AUTO_PUBLISH_ENABLED=false` |
| Human approval required | YES — `HUMAN_APPROVAL_REQUIRED=true` |

If your Gemini API key was ever shown in a screenshot or chat:
→ Revoke it at [aistudio.google.com](https://aistudio.google.com) → API Keys → Delete
→ Create a new key → update n8n environment → restart n8n
