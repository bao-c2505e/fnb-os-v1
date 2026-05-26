# n8n Credentials Checklist

## n8n Instance Setup

- [ ] n8n running (self-hosted Docker or n8n.cloud)
- [ ] n8n URL accessible at `N8N_BASE_URL`
- [ ] n8n API key generated (Settings → n8n API)
- [ ] Webhook URL format confirmed: `[N8N_BASE_URL]/webhook/[id]`

---

## Credentials to Add in n8n Credential Store

All credentials are stored IN n8n (encrypted), NOT in the repo.

### 1. Google Sheets / Drive
- Credential Type: Google Service Account
- Fields: Service Account Email, Private Key (from JSON file)
- Name in n8n: `Vị Cuốn Google SA`
- Test: Create test node, read a cell

### 2. OpenAI
- Credential Type: OpenAI API
- Fields: API Key
- Name in n8n: `OpenAI FnB OS`
- Test: Simple completion call

### 3. Anthropic Claude
- Credential Type: HTTP Header Auth (or Anthropic plugin if available)
- Header: `x-api-key: [ANTHROPIC_API_KEY]`
- Name in n8n: `Anthropic FnB OS`

### 4. Telegram Bot
- Credential Type: Telegram API
- Fields: Bot Token
- Name in n8n: `Vị Cuốn Telegram Bot`
- Test: Send test message to approval chat

### 5. HTTP Request (Generic)
- Used for: LangGraph API, custom webhooks
- Credential Type: HTTP Header Auth
- Configure per endpoint

---

## Environment Variables in n8n

Set these in n8n Settings → Environment Variables:
```
BRAND_NAME=Vị Cuốn
TIMEZONE=Asia/Ho_Chi_Minh
GOOGLE_SHEET_ID=[your sheet id]
GOOGLE_DRIVE_FOLDER_ID=[your folder id]
TELEGRAM_APPROVAL_CHAT_ID=[your chat id]
```

---

## Pre-Activation Checklist

Before any workflow goes live:
- [ ] All credentials tested individually
- [ ] Test workflow (read Sheet + write Sheet) passes
- [ ] Test Telegram message sent and received
- [ ] Error notification workflow working
- [ ] User has approved workflow activation via Telegram
