class Account():
    def __init__(self, balance=0 , logs=[]) -> None:
        self.balance = 0 or balance
        self.logs = logs if logs is not None else []