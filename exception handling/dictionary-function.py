

def find_key(data, key):
    try:
        return data[key]

    except KeyError:
        return "Key not found"


students = {
    "101": "Rahul",
    "102": "Priya"
}

key = input("Enter key: ")

print(find_key(students, key))