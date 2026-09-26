class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


e1 = Employee("John", 60000)
e2 = Employee("David", 50000)

print(e1 > e2)