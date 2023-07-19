from lib.printer import Printer
from unittest.mock import patch, Mock
from unittest import TestCase
from datetime import date
from io import StringIO


class FakeLogs(TestCase):
    def setUp(self):
        self.fake_log_1 = Mock()
        self.fake_log_1.debit = 0
        self.fake_log_1.credit = 100.50
        self.fake_log_1.balance = 122.569
        self.fake_log_1.date = date.fromisoformat("2000-06-05")

        self.fake_log_2 = Mock()
        self.fake_log_2.debit = 30.20
        self.fake_log_2.credit = 0
        self.fake_log_2.balance = 92.37
        self.fake_log_2.date = date.fromisoformat("2000-06-09")

        self.logs = [self.fake_log_1, self.fake_log_2]


class TestPrinterClass(FakeLogs):
    def test_printer_header(self):
        """
        Tests whether statement header is printed correctly
        """
        with patch("builtins.print") as mock_print:
            Printer.header()
            mock_print.assert_called_with("date || credit || debit || balance")

    def test_print_formatted_deposit_log(self):
        """
        Tests whether the log is printed in the correct format
        """
        with patch("builtins.print") as mock_print:
            Printer.print_formatted_log(self.fake_log_1)
            mock_print.assert_called_with("05/06/2000 || 100.50 ||  || 122.57")

    def test_print_formatted_withdraw_log(self):
        """
        Tests whether the log is printed in the correct format
        """
        with patch("builtins.print") as mock_print:
            Printer.print_formatted_log(self.fake_log_2)
            mock_print.assert_called_with("09/06/2000 ||  || 30.20 || 92.37")

    def test_multiple_logs_in_reverse_chronological_order(self):
        """
        Tests whether logs are printed in reverse order after the header, in the correct format
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            Printer.print_statement(self.logs)
            printed_output = mock_output.getvalue()
            assert printed_output.index(
                "date || credit || debit || balance"
            ) < printed_output.index("09/06/2000 ||  || 30.20 || 92.37")
            assert printed_output.index(
                "09/06/2000 ||  || 30.20 || 92.37"
            ) < printed_output.index("05/06/2000 || 100.50 ||  || 122.57")
