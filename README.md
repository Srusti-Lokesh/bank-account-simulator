# Bank Account Simulator

A Python menu-driven bank account simulator built for practicing **functions, loops, validation, state management, and transaction history**. The project also includes a lightweight Flask web interface so it can be deployed publicly on Render.

## Features

- Balance inquiry
- Deposit with validation
- Withdrawal with insufficient-balance protection
- Transaction history stored in a list
- Reusable `BankAccount` class
- Terminal menu-driven interface
- Flask web interface
- `/health` endpoint for deployment health checks
- Automated tests with pytest
- Render deployment configuration

## Technologies

- Python 3.13
- Flask
- Gunicorn
- pytest
- Git/GitHub
- Render

## Project Structure

```text
Bank_Account_Simulator/
├── app.py
├── bank_simulator.py
├── requirements.txt
├── render.yaml
├── .python-version
├── .gitignore
├── README.md
├── DEPLOYMENT_GUIDE.md
├── SUBMISSION_CHECKLIST.md
├── templates/
│   └── index.html
└── tests/
    └── test_bank_simulator.py
```

## Run the terminal simulator

```powershell
python bank_simulator.py
```

## Run the web version locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Run tests

```powershell
python -m pytest -q
```

## Render deployment

Render settings:

- **Service type:** Web Service
- **Runtime:** Python
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`
- **Health check path:** `/health`
- **Plan:** Free

The included `render.yaml` can be used as a deployment blueprint.

> Note: this educational version stores account state in memory. Restarting or redeploying the service resets the balance and transaction history. It does not store real banking data and must not be used for real financial transactions.

## Interview questions

**How is application state maintained?**  
The current account state is held by a `BankAccount` object. Its balance and transaction list are updated by deposit and withdrawal operations.

**Why should invalid withdrawals be rejected?**  
A withdrawal greater than the available balance would produce an invalid negative account balance. The simulator validates the amount before changing state.

**What data structure is used for transaction history?**  
A Python list is used because transactions are recorded in chronological order and can be iterated easily.

## License

Educational project created for internship/project submission.
