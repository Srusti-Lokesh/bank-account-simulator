"""
Flask web interface for the Bank Account Simulator.

The application intentionally uses in-memory state because this is an educational
simulator. Restarting/redeploying the service resets the account to ₹0.00.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from bank_simulator import BankAccount

app = Flask(__name__)
app.secret_key = "bank-simulator-demo-key"

account = BankAccount()


@app.get("/")
def index():
    return render_template(
        "index.html",
        balance=account.get_balance(),
        transactions=account.get_transactions(),
    )


@app.post("/deposit")
def deposit():
    try:
        account.deposit(request.form.get("amount", ""))
        flash("Deposit completed successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")
    return redirect(url_for("index"))


@app.post("/withdraw")
def withdraw():
    try:
        account.withdraw(request.form.get("amount", ""))
        flash("Withdrawal completed successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")
    return redirect(url_for("index"))


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
