from lib.account import Account
from lib.printer import Printer
import pytest
from datetime import date
from unittest.mock import patch, Mock
from unittest import TestCase
from io import StringIO


class FakeLogs(TestCase):
    def setUp(self):
        self.fake_deposit = Mock()
        self.fake_deposit.credit = 200
        self.fake_deposit.balance = 300


def test_account_creation():
    """
    Upon initiation, account has no logs and 0 balance.
    """
    account = Account()
    assert account.get_balance() == 0
    assert account.logs == []


def test_account_deposit_amount():
    """
    Creates and adds a deposit log object to the account logs.
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


def test_depositing_0_into_account():
    """
    Throws a ValueError if user tries to deposit anything <= 0 into account.
    """
    account = Account()
    with pytest.raises(ValueError) as e:
        account.deposit(0)
    assert str(e.value) == "You need to deposit an amount higher than 0."


class TestWithdrawals(FakeLogs):
    def test_account_withdraw_amount(self):
        """
        Creates and adds a withdrawal log object to the account logs.
        """
        account = Account(logs=[self.fake_deposit])
        fake_date = date.fromisoformat("2000-06-05")
        account.withdraw(30, date=fake_date)
        assert len(account.logs) == 2
        assert account.logs[-1].date == fake_date
        assert account.logs[-1].balance == 270
        assert account.logs[-1].debit == 30

    def test_account_withdraw_when_balance_is_insufficient(self):
        """
        Throws a ValueError if withdrawn amount is higher than account balance
        """
        account = Account()
        with pytest.raises(ValueError) as e:
            account.withdraw(100)
        assert str(e.value) == "Insufficient funds."
        assert len(account.logs) == 0
        assert account.get_balance() == 0

    def test_multiple_withdrawals(self):
        """
        Returns the final balance after multiple withdrawals are made
        """
        account = Account(logs=[self.fake_deposit])
        account.withdraw(30)
        account.withdraw(25)
        assert len(account.logs) == 3
        assert account.logs[-1].balance == 245
        assert account.logs[-1].debit == 25
        assert account.get_balance() == 245


class TestInvalidDataTypes:
    @pytest.mark.parametrize(
        "data, expected_error",
        [
            (False, "Invalid data."),
            (True, "Invalid data."),
            (None, "Invalid data."),
            ({}, "Invalid data."),
            (["something"], "Invalid data."),
            ("string", "Invalid data."),
        ],
    )
    def test_invalid_data_types_for_withdrawal_method(self, data, expected_error):
        """
        Tests whether the method throws errors if data type is incorrect.
        """
        account = Account()
        with pytest.raises(ValueError) as e:
            account.withdraw(data)
        assert str(e.value) == expected_error

    @pytest.mark.parametrize(
        "data, expected_error",
        [
            (False, "Invalid data."),
            (True, "Invalid data."),
            (None, "Invalid data."),
            ({}, "Invalid data."),
            (["something"], "Invalid data."),
            ("string", "Invalid data."),
        ],
    )
    def test_invalid_data_types_for_deposit_method(self, data, expected_error):
        """
        Tests whether the method throws errors if data type is incorrect.
        """
        account = Account()
        with pytest.raises(ValueError) as e:
            account.deposit(data)
        assert str(e.value) == expected_error


def test_feature_acceptance_test_specified_in_brief():
    account = Account()
    account.deposit(1000, date=date.fromisoformat("2023-01-10"))
    account.deposit(2000, date=date.fromisoformat("2023-01-13"))
    account.withdraw(500, date=date.fromisoformat("2023-01-14"))
    assert account.get_balance() == 2500
    assert len(account.logs) == 3
    with patch("sys.stdout", new=StringIO()) as mock_output:
        Printer.print_statement(account.logs)
        printed_output = mock_output.getvalue()
        assert printed_output.index(
            "date || credit || debit || balance"
        ) < printed_output.index("14/01/2023 ||  || 500.00 || 2500.00")
        assert printed_output.index(
            "14/01/2023 ||  || 500.00 || 2500.00"
        ) < printed_output.index("13/01/2023 || 2000.00 ||  || 3000.00")
        assert printed_output.index(
            "13/01/2023 || 2000.00 ||  || 3000.00"
        ) < printed_output.index("10/01/2023 || 1000.00 ||  || 1000.00")
