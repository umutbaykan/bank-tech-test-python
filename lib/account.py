from .log import Log
from datetime import datetime


class Account:
    def __init__(self, balance=0, logs=[], logger=Log) -> None:
        self.balance = 0 or balance
        self.logger = logger
        self.logs = logs if logs is not None else []

    def deposit(self, amount, date=datetime.today()):
        log = self.logger(credit=amount, date=date)
        self.logs.append(log)
