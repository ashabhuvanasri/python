class InvalidTransactionError(Exception):
    pass


try:
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        raise InvalidTransactionError("Invalid transaction amount")

    print("Transaction successful")

except InvalidTransactionError as e:
    print("Error:", e)