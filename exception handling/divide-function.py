def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(divide(a, b))