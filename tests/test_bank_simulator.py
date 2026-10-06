from decimal import Decimal
import pytest
from bank_simulator import BankAccount, validate_amount


def test_deposit_updates_balance():
    account = BankAccount()
    account.deposit("100.00")
    assert account.get_balance() == Decimal("100.00")


def test_withdraw_updates_balance():
    account = BankAccount(Decimal("200.00"))
    account.withdraw("75.50")
    assert account.get_balance() == Decimal("124.50")


def test_withdraw_more_than_balance_is_rejected():
    account = BankAccount(Decimal("50.00"))
    with pytest.raises(ValueError, match="Insufficient balance"):
        account.withdraw("50.01")


@pytest.mark.parametrize("value", ["0", "-10", "abc", "1.234"])
def test_invalid_amounts_are_rejected(value):
    with pytest.raises(ValueError):
        validate_amount(value)


def test_transaction_history_is_recorded():
    account = BankAccount()
    account.deposit("25")
    account.withdraw("5")
    history = account.get_transactions()
    assert len(history) == 2
    assert "Deposited ₹25.00" in history[0]
    assert "Withdrew ₹5.00" in history[1]
