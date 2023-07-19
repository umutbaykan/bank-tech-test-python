from lib.printer import Printer
from unittest.mock import patch, Mock
from unittest import TestCase
from datetime import date


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
        self.fake_log_2.balance = 70.30
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

    def test_print_formatted_log(self):
        """
        Tests whether the log is printed in the correct format
        """
        with patch("builtins.print") as mock_print:
            Printer.print_formatted_log(self.fake_log_1)
            mock_print.assert_called_with("05-06-2000 || 100.50 ||  || 122.57")
