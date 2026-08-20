try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))

    result = a / b
    print(result)

except ValueError:
    print("ValueError: Invalid input")

except TypeError:
    print("TypeError: Invalid data type")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")