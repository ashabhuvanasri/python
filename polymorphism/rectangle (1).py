class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()


r1 = Rectangle(10, 5)
r2 = Rectangle(5, 10)

print(r1 == r2)