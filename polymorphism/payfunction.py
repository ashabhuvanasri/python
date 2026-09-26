class UPI:
    def pay(self):
        print("Paid using UPI.")


class Card:
    def pay(self):
        print("Paid using Card.")


class Cash:
    def pay(self):
        print("Paid using Cash.")


def process_payment(payment):
    payment.pay()


process_payment(UPI())
process_payment(Card())
process_payment(Cash())