class InsufficientBalanceError(Exception):
    pass


balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= amount
    print("Balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)