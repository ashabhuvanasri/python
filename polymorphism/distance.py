class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def display(self):
        print(self.meters, "meters")


d1 = Distance(100)
d2 = Distance(250)

d3 = d1 + d2
d3.display()