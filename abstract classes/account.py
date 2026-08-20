from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def display_account(self):
        pass


class SavingsAccount(Account):

    def display_account(self):
        print("Account Type: Savings Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class CurrentAccount(Account):

    def display_account(self):
        print("Account Type: Current Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


savings = SavingsAccount("SA1001", 25000)
current = CurrentAccount("CA2001", 50000)

savings.display_account()
print()

current.display_account()