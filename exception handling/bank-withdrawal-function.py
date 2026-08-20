def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient balance")

        balance -= amount
        return balance

    except ValueError as e:
        return str(e)


balance = 5000
amount = float(input("Enter amount: "))

print(withdraw(balance, amount))