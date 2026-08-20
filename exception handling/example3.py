data = {
    "name": "Rahul",
    "age": 20
}

try:
    key = input("Enter key: ")
    print(data[key])

except KeyError:
    print("Key not found")

except TypeError:
    print("Invalid key type")