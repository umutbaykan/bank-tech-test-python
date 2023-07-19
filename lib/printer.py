class Printer:
    @staticmethod
    def header():
        print("date || credit || debit || balance")

    def print_logs(logs):
        Printer.header()
