from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class FixedDeposit(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDeposit()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))