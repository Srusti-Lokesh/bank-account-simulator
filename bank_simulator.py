"""
Menu-driven Bank Account Simulator.

This module contains the core account logic and a terminal menu.
The same BankAccount class is used by the Flask web application.
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import List


@dataclass
class BankAccount:
    """Simple in-memory bank account with transaction history."""

    balance: Decimal = Decimal("0.00")
    transactions: List[str] = field(default_factory=list)

    def deposit(self, amount: Decimal) -> str:
        amount = validate_amount(amount)
        self.balance += amount
        message = f"Deposited ₹{amount:.2f}"
        self._record(message)
        return message

    def withdraw(self, amount: Decimal) -> str:
        amount = validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance for this withdrawal.")
        self.balance -= amount
        message = f"Withdrew ₹{amount:.2f}"
        self._record(message)
        return message

    def get_balance(self) -> Decimal:
        return self.balance

    def get_transactions(self) -> List[str]:
        return list(self.transactions)

    def _record(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {message} - Balance: ₹{self.balance:.2f}")


def validate_amount(value) -> Decimal:
    """Convert input to a positive money amount with two decimal places."""
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError("Enter a valid numeric amount.")

    if not amount.is_finite():
        raise ValueError("Enter a finite numeric amount.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount.as_tuple().exponent < -2:
        raise ValueError("Amount can have at most two decimal places.")

    return amount.quantize(Decimal("0.01"))


def run_menu() -> None:
    account = BankAccount()

    while True:
        print("\n=== Bank Account Simulator ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print(f"Current balance: ₹{account.get_balance():.2f}")

        elif choice == "2":
            try:
                amount = input("Enter deposit amount: ").strip()
                print(account.deposit(amount))
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            try:
                amount = input("Enter withdrawal amount: ").strip()
                print(account.withdraw(amount))
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "4":
            history = account.get_transactions()
            if history:
                print("\n--- Transaction History ---")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions yet.")

        elif choice == "5":
            print("Thank you for using the Bank Account Simulator.")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    run_menu()
