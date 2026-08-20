
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        radius = 5
        result = 3.14 * radius * radius
        print("Color:", self.color)
        print("Circle Area:", result)


class Rectangle(Shape):

    def area(self):
        length = 10
        width = 5
        result = length * width
        print("Color:", self.color)
        print("Rectangle Area:", result)


circle = Circle("Red")
rectangle = Rectangle("Blue")

circle.area()
print()

rectangle.area()