class Payment:
    def pay(self):
        print("Processing payment.")


class UPI(Payment):
    def pay(self):
        print("Payment through UPI.")


class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card.")


class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking.")


payments = [UPI(), CreditCard(), NetBanking()]

for payment in payments:
    payment.pay()