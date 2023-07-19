from lib.account import Account
from datetime import date


def test_account_creation():
    """
    Upon initiation, account has no logs and 0 balance.
    """
    account = Account()
    assert account.get_balance() == 0
    assert account.logs == []


def test_account_deposit_amount():
    """
    Creates and adds a log object to the account logs.
    """
    account = Account()
    fake_date = date.fromisoformat("2000-06-05")
    account.deposit(100, date=fake_date)
    assert len(account.logs) == 1
    assert account.logs[0].date == fake_date
    assert account.logs[0].balance == 100


def test_account_balance_after_deposit():
    """
    Returns the current balance in the account based on log history.
    """
    account = Account()
    account.deposit(100)
    assert account.logs[0].balance == 100
    assert account.get_balance() == 100


def test_account_balance_after_multiple_deposits():
    """
    Returns the current balance in the account after multiple deposits.
    """
    account = Account()
    account.deposit(100)
    account.deposit(150)
    assert account.logs[0].balance == 100
    assert account.get_balance() == 250
