class Person:
    def role(self):
        print("I am a person.")


class Student(Person):
    def role(self):
        print("I am a Student.")


class Teacher(Person):
    def role(self):
        print("I am a Teacher.")


class Doctor(Person):
    def role(self):
        print("I am a Doctor.")


people = [Student(), Teacher(), Doctor()]

for person in people:
    person.role()