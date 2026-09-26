from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Paid using UPI.")


class Card(Payment):
    def pay(self):
        print("Paid using Card.")


class NetBanking(Payment):
    def pay(self):
        print("Paid using Net Banking.")


payments = [UPI(), Card(), NetBanking()]

for payment in payments:
    payment.pay()