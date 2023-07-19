from lib.printer import Printer
import unittest
from unittest.mock import patch, Mock


def test_printer_header():
    """
    Tests whether statement header is printed correctly
    """
    with patch("builtins.print") as mock_print:
        Printer.header()
        mock_print.assert_called_with("date || credit || debit || balance")
