from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid through UPI.")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid through Credit Card.")


class DebitCard(Payment):
    def pay(self, amount):
        print(f"₹{amount} paid through Debit Card.")


class CashOnDelivery(Payment):
    def pay(self, amount):
        print(f"₹{amount} will be paid on delivery.")


def checkout(payment, amount):
    payment.pay(amount)


checkout(UPI(), 1500)
checkout(CreditCard(), 2500)
checkout(DebitCard(), 3000)
checkout(CashOnDelivery(), 1000)