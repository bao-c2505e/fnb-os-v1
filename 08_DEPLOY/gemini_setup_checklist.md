# Google Gemini Setup Checklist

## Step 1 — Google AI Studio

- [ ] Go to aistudio.google.com
- [ ] Sign in with Google account
- [ ] Create API key (Get API Key → Create API Key in new project)
- [ ] Name project: `fnb-os-v1`
- [ ] Copy API key
- [ ] Store in `.env` as `GEMINI_API_KEY`

## Step 2 — Model Selection

- [ ] Primary model: `gemini-1.5-pro` (best quality)
- [ ] Fast model: `gemini-1.5-flash` (lower cost, faster)
- [ ] Multimodal tasks: `gemini-1.5-pro` (handles images)

## Step 3 — Rate Limits (Free Tier)

- [ ] Free tier: 15 RPM, 1M TPM, 1500 requests/day
- [ ] If needed, upgrade to paid tier via Google Cloud
- [ ] Note: free tier has lower limits — may need paid for production

## Step 4 — Google Cloud Setup (for production)

- [ ] Create Google Cloud project (same as Sheets/Drive project if possible)
- [ ] Enable Vertex AI API (for Gemini via Cloud)
- [ ] OR use AI Studio key directly (simpler for Phase 0–3)

## Step 5 — Test

- [ ] Test API call with curl or n8n HTTP request node
- [ ] Confirm `gemini-1.5-pro` responds
- [ ] Check usage in AI Studio dashboard

## Security Notes
- AI Studio API keys are tied to your Google account
- Rotate if compromised
- Do not use personal Google account for production — use service account via Vertex AI
