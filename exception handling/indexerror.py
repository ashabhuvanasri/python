numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Index is out of range")
except ValueError:
    print("Enter a valid index")