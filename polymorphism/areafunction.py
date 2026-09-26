class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


def calculate_area(shape):
    print("Area:", shape.area())


calculate_area(Circle(5))
calculate_area(Rectangle(10, 5))
calculate_area(Square(4))