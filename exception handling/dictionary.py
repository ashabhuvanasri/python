students = {
    "101": "Rahul",
    "102": "Amit",
    "103": "Priya"
}

try:
    key = input("Enter student ID: ")
    print("Student:", students[key])

except KeyError:
    print("Student ID not found")