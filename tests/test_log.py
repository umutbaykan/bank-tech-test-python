from lib.log import Log
from datetime import date


def test_log_creation():
    """
    Creates a log with an amount and date upon initiation
    """
    fake_date = date.fromisoformat("2000-06-05")
    log = Log(credit=100, balance=0, date=fake_date)
    assert log.debit == 0
    assert log.credit == 100
    assert log.balance == 100
    assert log.date == fake_date


def test_log_credit_to_increase_available_balance():
    """
    Adds the deposited amount on top of the balance
    """
    log = Log(credit=100, balance=300)
    assert log.credit == 100
    assert log.balance == 400


def test_log_debit_to_decrease_available_balance():
    """
    Removes the deposited amount from the account balance
    """
    log = Log(debit=100, balance=300)
    assert log.debit == 100
    assert log.balance == 200
