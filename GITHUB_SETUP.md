# Pushing to GitHub

## One-Time Setup

### 1. Create GitHub Repository

Go to https://github.com/new and create a new repository:
- Repository name: `nyqp-2025-maps` (or your choice)
- Description: "Interactive mobile tracking maps for NYQP 2025"
- **Do NOT** initialize with README, .gitignore, or license (we already have these)
- Public or Private (your choice)

### 2. Configure Git (if not already done)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Rename Branch to Main (GitHub default)

```bash
cd /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis
git branch -M main
```

### 4. Add GitHub Remote

Replace `YOUR_USERNAME` and `REPO_NAME` with your values:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

Example:
```bash
git remote add origin https://github.com/mgilmer/nyqp-2025-maps.git
```

### 5. Push to GitHub

```bash
git push -u origin main
```

You'll be prompted for your GitHub credentials:
- Username: your GitHub username
- Password: use a **Personal Access Token** (not your password)

#### Creating a Personal Access Token:
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "NYQP Maps CLI"
4. Select scopes: check `repo` (full control of private repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again)
7. Use this token as your password when pushing

## Future Pushes

After making changes:

```bash
cd /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis

# Stage changes
git add <files>

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

## Verify

After pushing, visit:
```
https://github.com/YOUR_USERNAME/REPO_NAME
```

You should see all your files and commit history.

## Using SSH Instead (Optional)

If you prefer SSH over HTTPS:

1. Generate SSH key (if you don't have one):
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

2. Add to GitHub: https://github.com/settings/keys

3. Change remote URL:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/REPO_NAME.git
```

4. Push:
```bash
git push -u origin main
```

## Troubleshooting

**"remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

**"failed to push some refs"**
```bash
git pull origin main --rebase
git push -u origin main
```

**Authentication failed**
- Make sure you're using a Personal Access Token, not your password
- Token must have `repo` scope enabled
