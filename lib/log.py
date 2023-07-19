class Log:
    def __init__(self, debit=0, credit=0, balance=0, date=None) -> None:
        self.debit = debit
        self.credit = credit
        self.balance = balance - debit + credit
        self.date = date
