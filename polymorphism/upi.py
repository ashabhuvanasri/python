class UPIPayment:
    def pay(self):
        print("Paid using UPI.")


class CardPayment:
    def pay(self):
        print("Paid using Card.")


def process_payment(payment):
    payment.pay()


process_payment(UPIPayment())
process_payment(CardPayment())