numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Invalid index")

except IndexError:
    print("Index out of range")

except TypeError:
    print("Invalid type")

except Exception as e:
    print("Other error:", e)