class BankAccount:
    def calculate_interest(self, amount):
        return amount * 0.03


class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.07


class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.04


accounts = [
    SavingsAccount(),
    CurrentAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))