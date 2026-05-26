# GitHub Setup Checklist

## Step 1 — Repository

- [ ] Create new repository: `fnb-os-v1`
- [ ] Visibility: Private (recommended)
- [ ] Initialize with README: No (we have our own)
- [ ] Add `.gitignore`: choose `Node` or create custom

## Step 2 — .gitignore

Create `.gitignore` in repo root with at minimum:
```
.env
*.key
*.pem
*.p12
service-account-*.json
node_modules/
__pycache__/
*.pyc
.DS_Store
Thumbs.db
*.log
/tmp/
```

- [ ] `.gitignore` created and committed
- [ ] Verify `.env` is listed in `.gitignore`
- [ ] Run `git status` to confirm `.env` is not tracked

## Step 3 — Branch Protection

- [ ] Go to Settings → Branches → Add rule
- [ ] Branch name pattern: `main`
- [ ] Enable: Require pull request reviews before merging
- [ ] Enable: Require status checks to pass (when CI is added)
- [ ] Enable: Do not allow force pushes

## Step 4 — Access

- [ ] Repo owner: [your GitHub account]
- [ ] Add collaborators if needed (Settings → Collaborators)
- [ ] For agents using GitHub API: create Personal Access Token
  - Scopes: `repo` (read/write to private repos)
  - Store as `GITHUB_TOKEN` in `.env`

## Step 5 — Branch Naming Convention

```
main              — production / source of truth
phase-0/setup     — Phase 0 work
phase-1/data-layer — Phase 1 work
fix/[issue-name]  — bug fixes
```

## Step 6 — First Commit

- [ ] Initial files committed to `main`
- [ ] `.env` confirmed NOT in commit
- [ ] Commit message format: `feat(phase-0): initial repo structure`

## Security Notes
- Private repo for all proprietary brand data
- Never commit `.env`, credentials, or service account JSON
- Rotate `GITHUB_TOKEN` every 90 days
- Enable 2FA on GitHub account
