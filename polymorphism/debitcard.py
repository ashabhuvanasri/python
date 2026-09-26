class DebitCard:
    def pay(self):
        print("Payment using Debit Card.")


class CreditCard:
    def pay(self):
        print("Payment using Credit Card.")


def card_payment(card):
    card.pay()


card_payment(DebitCard())
card_payment(CreditCard())