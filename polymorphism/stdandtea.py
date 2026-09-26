class Student:
    def display(self):
        print("I am a Student.")


class Teacher:
    def display(self):
        print("I am a Teacher.")


people = [Student(), Teacher()]

for person in people:
    person.display()