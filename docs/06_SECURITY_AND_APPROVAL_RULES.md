# Security and Approval Rules — FnB OS V1

Version: 1.0
Date: 2026-05-28
Authority: ChatGPT (Chief Architect) + Owner (Bo Bao)
Enforced by: All agents

These rules protect the Owner's business, customer data, ad budget, and brand reputation.
They apply to every agent, every session, and every workflow — no exceptions.

---

## 1. Secret and Credential Rules

### 1.1 Never hardcode credentials

No agent may write a real value for any of the following into any file in this repository:

- API keys (OpenAI, Google, Airtable, any service)
- Bot tokens (Telegram, Slack, Discord)
- OAuth client secrets or access tokens
- Database passwords or connection strings
- Private keys or certificates
- Session secrets or JWT signing keys
- Ad account IDs combined with access tokens

Use only placeholder values:
```
REPLACE_WITH_TELEGRAM_BOT_TOKEN
REPLACE_WITH_OPENAI_API_KEY
REPLACE_WITH_[SERVICE]_[TYPE]
[FILL — set in n8n credential manager]
```

### 1.2 .env files

- `.env` must never be committed. It is in `.gitignore`.
- `.env.example` may be committed with placeholder values only.
- If `.env` appears in `git status`, stop all work and remove it from staging before proceeding.

### 1.3 Secret found mid-session

If any agent discovers a real credential in any file during a session:
1. Stop all work immediately.
2. Do not commit or push anything.
3. Report the file path and line to the Owner.
4. Request the Owner rotates the credential.
5. Set command status `BLOCKED` with reason "SECRET_FOUND".
6. Do not continue until the credential is rotated and the file is cleaned.

---

## 2. Approval Gate — What Requires Owner Approval

The following actions are **forbidden** without an explicit Owner approval recorded in the command or task file:

| Action | Why Approval Required |
|--------|-----------------------|
| Post to TikTok, Facebook, Instagram, or any social platform | Customer-facing; brand risk |
| Send Telegram, SMS, or email to real customers | Customer-facing; legal risk |
| Reply to customer comments or DMs | Customer-facing; brand risk |
| Activate or enable any n8n workflow | Automation risk |
| Create, modify, or pause any paid ad campaign | Financial risk |
| Spend any budget (ads, credits, subscriptions) | Financial risk |
| Access or modify production data | Data integrity risk |
| Merge a PR or deploy to production | Code quality risk |
| Grant API access or create credentials | Security risk |
| Integrate a new external service | Scope and security risk |

### 2.1 How approval is recorded

Approval must be documented as one of:
- `OWNER_APPROVED` status on the active command in `commands/COMMAND_INBOX.md`.
- An explicit written approval from the Owner in the session thread (for real-time sessions).
- An approved n8n workflow execution log after the approval gate node passes.

Verbal agreement or assumed approval is not sufficient.

---

## 3. Content and Customer Safety Rules

- No AI-generated content may be posted without Owner review.
- No automated responses to customer complaints, refund requests, or sensitive topics.
- No AI-generated offers or discounts may be communicated without Owner approval.
- Gemini and other content agents may draft content — they must not publish it.
- All content must pass the approval gate in `03_APPROVAL_PIPELINE/` before publishing.

---

## 4. Data Handling Rules

- No real customer PII (names, phone numbers, addresses, order history) in test fixtures.
- Test fixtures in `07_TEST_FIXTURES/` use anonymized or synthetic data only.
- No customer data in agent prompts sent to external LLM APIs without Owner consent.
- Google Sheets data accessed by n8n is treated as sensitive — log all access.

---

## 5. Commit and Push Rules

| Gate | Required State |
|------|---------------|
| `git add` | Only files in `scope_files` |
| `git commit` | Command status = `OWNER_APPROVED` |
| `git push` | Owner has run the command manually in their terminal |

Agents (Claude Code, Codex, Gemini, n8n) must never push to GitHub autonomously.
The Owner is the only entity who runs `git push` — always manually.

---

## 6. Incident Response

If a security incident occurs (secret exposed, unauthorized publish, unexpected workflow activation):

1. **Stop** — halt all active agent sessions.
2. **Contain** — if secret was committed, immediately `git revert` or remove from history.
3. **Rotate** — Owner rotates any exposed credentials.
4. **Log** — record the incident in `09_LOGS/PHASE_LOG.md` with timestamp, nature, and actions taken.
5. **Review** — ChatGPT reviews what rule was violated and proposes a prevention measure.
6. **Update** — update this document or the relevant protocol if a rule gap is identified.

---

## 7. Rule Hierarchy

When rules conflict, apply in this order:

1. Owner's explicit real-time instruction (highest authority).
2. This document (`docs/06_SECURITY_AND_APPROVAL_RULES.md`).
3. `AGENTS.md` constraints table.
4. `docs/03_AGENT_OPERATING_RULES.md`.
5. Agent-specific protocol (`agents/BUILDER_PROTOCOL.md`, `agents/REVIEWER_PROTOCOL.md`).
6. Active command fields (`forbidden_actions`, `acceptance_criteria`).
