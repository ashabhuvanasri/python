balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance -= amount
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)

finally:
    print("Transaction completed")