class Employee:
    def calculate_salary(self):
        return 30000


class Manager(Employee):
    def calculate_salary(self):
        return 80000


class Developer(Employee):
    def calculate_salary(self):
        return 60000


employees = [Manager(), Developer()]

for employee in employees:
    print("Salary:", employee.calculate_salary())