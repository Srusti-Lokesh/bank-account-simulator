# Deployment Guide — PowerShell, GitHub and Render

## 1. Prerequisites

Install these on Windows:

1. Python 3.13.x
2. Git
3. A GitHub account
4. A Render account

Verify installations in PowerShell:

```powershell
python --version
git --version
```

If `python` is not recognized, install Python and enable **Add Python to PATH** during installation.

## 2. Extract the ZIP

Extract the project to a simple folder, for example:

```text
C:\Users\YOUR_NAME\Documents\Bank_Account_Simulator
```

Open PowerShell in that folder.

## 3. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 5. Test the project locally

Run automated tests:

```powershell
python -m pytest -q
```

Expected result is five passing test groups with no failures.

Run the terminal application:

```powershell
python bank_simulator.py
```

Run the web application:

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Health check:

```text
http://127.0.0.1:5000/health
```

Stop the server with `Ctrl+C`.

## 6. Create the GitHub repository

Recommended repository name:

```text
bank-account-simulator
```

Recommended GitHub description:

```text
A Python menu-driven bank account simulator with balance inquiry, deposits, withdrawals, transaction history, validation, automated tests, and a Flask web interface deployable on Render.
```

Create a **Public** repository if your internship submission requires a public GitHub link.

Important: when using the local-push method below, create the GitHub repository empty. Do not add another README, .gitignore, or license from the GitHub creation screen because this project already contains those files.

## 7. Push from PowerShell

From the project root:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "Initial bank account simulator project"
git remote add origin https://github.com/YOUR-USERNAME/bank-account-simulator.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

If Git asks for authentication, complete GitHub's sign-in flow. Do not put a GitHub password or token inside the source code.

Verify the repository in your browser.

## 8. Deploy on Render

### Dashboard method

1. Sign in to Render.
2. Select **New +** → **Web Service**.
3. Connect GitHub if requested.
4. Select `bank-account-simulator`.
5. Select branch `main`.
6. Use these settings:

```text
Name: bank-account-simulator
Language/Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Health Check Path: /health
Plan: Free
```

7. Click **Create Web Service**.
8. Wait for the build and deploy logs to finish successfully.
9. Open the generated `onrender.com` URL.
10. Test:
    - Home page loads.
    - Deposit works.
    - Withdrawal works.
    - Withdrawal above balance is rejected.
    - Transaction history updates.
    - `/health` returns `{"status":"ok"}`.

Render can automatically redeploy when new commits are pushed to the connected branch.

## 9. If Render fails

Check the deploy logs.

Common checks:

```text
requirements.txt exists in repository root
app.py exists in repository root
render.yaml is valid
Start command is exactly: gunicorn app:app
Build command is exactly: pip install -r requirements.txt
```

Do not use:

```text
python app.py
```

as the production Render start command when following this configuration. Use Gunicorn.

## 10. Update after deployment

After changing code:

```powershell
git add .
git commit -m "Improve bank simulator"
git push
```

If Render is connected to `main`, it will normally start a new deployment automatically.

## 11. Final submission package

Submit/provide:

- Public GitHub repository link
- Live Render URL
- Project ZIP
- Project report PDF
- README containing setup, features, testing and deployment information
- Deployment evidence/screenshots if the internship portal requests them

Do not upload `.venv`, secrets, passwords, API keys, or personal access tokens.

## 12. Important simulator limitation

This is an educational simulator. Account data is stored in memory only. A service restart/redeploy resets the account to the initial balance. It is not a real banking application and must not process real financial information.
