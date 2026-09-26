from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid using UPI.")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card.")


class DebitCard(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid using Debit Card.")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking.")


def process_payment(payment, amount):
    payment.pay(amount)


payments = [
    UPI(),
    CreditCard(),
    DebitCard(),
    NetBanking()
]

for payment in payments:
    process_payment(payment, 5000)