from lib.log import Log
from datetime import date


def test_log_creation():
    """
    Creates a log with an amount and date upon initiation
    """
    fake_date = date.fromisoformat("2000-06-05")
    log = Log(credit=100, date=fake_date)
    assert log.debit == 0
    assert log.credit == 100
    assert log.date == fake_date
