class InsufficientStockError(Exception):
    pass


stock = 10

try:
    quantity = int(input("Enter quantity: "))

    if quantity > stock:
        raise InsufficientStockError("Not enough stock")

    stock -= quantity
    print("Remaining stock:", stock)

except InsufficientStockError as e:
    print("Error:", e)