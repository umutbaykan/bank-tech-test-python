class Printer:
    def header():
        print("date || credit || debit || balance")

    def print_formatted_log(log):
        date = log.date.strftime("%d/%m/%Y")
        credit = "" if log.credit == 0 else "{:.2f}".format(log.credit)
        debit = "" if log.debit == 0 else "{:.2f}".format(log.debit)
        balance = "{:.2f}".format(log.balance)
        print(f"{date} || {credit} || {debit} || {balance}")

    def print_statement(logs):
        Printer.header()
        for i in reversed(range(len(logs))):
            Printer.print_formatted_log(logs[i])
