from .log import Log
from datetime import datetime


class Account:
    def __init__(self, logs=[], logger=Log) -> None:
        self.balance = self.get_balance()
        self.logger = logger
        self.logs = logs if logs is not None else []

    def get_balance(self):
        for log in self.logs:
            pass

    def deposit(self, amount, date=datetime.today()):
        log = self.logger(credit=amount, date=date)
        self.logs.append(log)
