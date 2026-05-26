# Telegram Setup Checklist

## Step 1 — Create Bot

- [ ] Open Telegram, search for `@BotFather`
- [ ] Send `/newbot`
- [ ] Enter bot name: `Vị Cuốn OS Bot` (or your preference)
- [ ] Enter username: `vicuon_os_bot` (must end in `bot`)
- [ ] Copy the bot token → store in `.env` as `TELEGRAM_BOT_TOKEN`

## Step 2 — Create Approval Channel/Group

- [ ] Create a private group: `FnB OS Approvals`
- [ ] Add bot to the group
- [ ] Make bot an admin (needed to read messages)
- [ ] Get chat ID:
  - Option A: Forward a message to `@userinfobot`
  - Option B: Call `https://api.telegram.org/bot[TOKEN]/getUpdates` after sending a message
- [ ] Store chat ID in `.env` as `TELEGRAM_APPROVAL_CHAT_ID`

## Step 3 — Create Escalation Channel (optional, can reuse approval)

- [ ] Create group: `FnB OS Escalations` (or use same group)
- [ ] Store ID as `TELEGRAM_ESCALATION_CHAT_ID`

## Step 4 — Configure Bot Commands

- [ ] Send `/setcommands` to BotFather
- [ ] Set commands:
  ```
  approve - Approve pending item
  reject - Reject pending item
  status - Check pending approvals
  help - Show available commands
  ```

## Step 5 — Test

- [ ] n8n sends test message to approval chat
- [ ] Message received successfully
- [ ] Reply `/approve_TEST` confirms bot reads responses

## Bot Permissions Needed
- Send messages
- Read messages (for command responses)
- No admin privileges needed beyond reading chat

## Security Notes
- Bot token is a secret — never share or commit
- Use private groups only, not public channels
- Revoke and regenerate token if compromised (via BotFather `/revoke`)
