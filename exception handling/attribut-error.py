class Student:
    def __init__(self):
        self.name = "Rahul"


student = Student()

try:
    print(student.age)

except AttributeError:
    print("Attribute does not exist")