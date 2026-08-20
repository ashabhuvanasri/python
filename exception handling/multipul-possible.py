try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))

    numbers = [10, 20, 30]

    print("Division:", a / b)
    index = int(input("Enter index: "))
    print("List value:", numbers[index])

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except IndexError:
    print("Index out of range")