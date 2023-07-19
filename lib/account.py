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
        log = self.logger(credit=amount, balance=self.get_balance(), date=date)
        self.logs.append(log)
