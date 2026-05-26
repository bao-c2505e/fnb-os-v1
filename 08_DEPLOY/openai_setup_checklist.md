# OpenAI Setup Checklist

## Step 1 — Account & Project

- [ ] OpenAI account created at platform.openai.com
- [ ] Create a new Project: `FnB OS V1` (keeps usage separate)
- [ ] Billing method added
- [ ] Usage limits set (recommended: monthly hard limit to prevent runaway costs)

## Step 2 — API Key

- [ ] Go to API Keys → Create new secret key
- [ ] Name: `fnb-os-v1`
- [ ] Scope: project-scoped (not personal)
- [ ] Copy key immediately (shown only once)
- [ ] Store in `.env` as `OPENAI_API_KEY`
- [ ] Store in n8n credential store as `OpenAI FnB OS`

## Step 3 — Model Access

- [ ] Confirm `gpt-4o` access (may require verified billing)
- [ ] Note model IDs:
  - Content generation: `gpt-4o`
  - Fallback: `gpt-4o-mini` (lower cost)
  - Codex tasks: `gpt-4o` (Codex is integrated into GPT-4o as of 2024)

## Step 4 — Rate Limits

- [ ] Check rate limits in your tier
- [ ] Tier 1: 500 RPM, 200,000 TPM (upgrade if needed)
- [ ] Set retry logic in n8n: max 3 retries, 5s delay

## Step 5 — Test

- [ ] Test API call in n8n with simple prompt
- [ ] Confirm response received
- [ ] Check usage logged in OpenAI dashboard

## Security Notes
- Project-scoped keys are safer than personal keys
- Rotate key every 90 days or if compromised
- Never log the API key in execution logs
