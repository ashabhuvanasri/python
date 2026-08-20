data = {
    "name": "Rahul",
    "age": 20
}

try:
    key = input("Enter key: ")
    print(data[key])

except ValueError:
    print("Invalid input")

except KeyError:
    print("Key does not exist")

except TypeError:
    print("Invalid key type")