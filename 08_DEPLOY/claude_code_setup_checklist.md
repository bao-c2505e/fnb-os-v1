# Anthropic Claude Setup Checklist

## Step 1 — Anthropic Account

- [ ] Create account at console.anthropic.com
- [ ] Add billing method
- [ ] Set usage limits (recommended: monthly limit for cost control)

## Step 2 — API Key

- [ ] Go to API Keys → Create Key
- [ ] Name: `fnb-os-v1`
- [ ] Copy key immediately
- [ ] Store in `.env` as `ANTHROPIC_API_KEY`
- [ ] Store in n8n credential store

## Step 3 — Model Selection

| Use Case | Model | Notes |
|----------|-------|-------|
| Primary content generation | `claude-sonnet-4-5` | Balance of quality and cost |
| Complex reasoning | `claude-opus-4-7` | Highest quality, higher cost |
| Fast tasks | `claude-haiku-4-5-20251001` | Cheapest, fastest |

## Step 4 — Claude Code CLI (for Builder Agent sessions)

- [ ] Install: `npm install -g @anthropic-ai/claude-code`
- [ ] Authenticate: `claude` (follow prompts)
- [ ] Verify: `claude --version`
- [ ] Working directory: project root `D:\FNB_OS_V1`

## Step 5 — Test

- [ ] Test API call in n8n
- [ ] Test Claude Code CLI in project directory
- [ ] Confirm model responds correctly

## Security Notes
- Anthropic API keys have no project scoping (as of 2025) — treat as org-level secret
- Do not expose in logs
- Rotate if compromised via console.anthropic.com
