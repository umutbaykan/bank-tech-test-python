from .log import Log
from datetime import datetime


class Account:
    def __init__(self, logs=None, logger=Log) -> None:
        self.logs = [] if logs is None else logs
        self.logger = logger

    def get_balance(self):
        if len(self.logs) == 0:
            return 0
        else:
            return self.logs[-1].balance

    def deposit(self, amount, date=datetime.today()):
        self._validate_input(amount)
        if amount <= 0:
            raise ValueError("You need to deposit an amount higher than 0.")
        log = self.logger(credit=amount, balance=self.get_balance(), date=date)
        self.logs.append(log)

    def withdraw(self, amount, date=datetime.today()):
        self._validate_input(amount)
        current_balance = self.get_balance()
        if amount > current_balance:
            raise ValueError("Insufficient funds.")
        log = self.logger(debit=amount, balance=current_balance, date=date)
        self.logs.append(log)

    @staticmethod
    def _validate_input(amount):
        if not isinstance(amount, (float, int)) or isinstance(amount, bool):
            raise ValueError("Invalid data.")
