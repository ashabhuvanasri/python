try:
    value = input("Enter a number: ")
    number = int(value)

    print("Integer:", number)

except ValueError:
    print("Invalid integer")