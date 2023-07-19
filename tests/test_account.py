from lib.account import Account


def test_account_creation():
    """
    Upon initiation, account has no logs and 0 balance.
    """
    account = Account()
    assert account.balance == 0
    assert account.logs == []


def test_account_balance_override():
    """
    Account balance can be overridden upon initiation.
    """
    account = Account(balance=100)
    assert account.balance == 100
