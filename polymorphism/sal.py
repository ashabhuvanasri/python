from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 80000


class Developer(Employee):
    def calculate_salary(self):
        return 60000


class Tester(Employee):
    def calculate_salary(self):
        return 50000


class Intern(Employee):
    def calculate_salary(self):
        return 20000


employees = [
    Manager(),
    Developer(),
    Tester(),
    Intern()
]

for employee in employees:
    print("Salary:", employee.calculate_salary())