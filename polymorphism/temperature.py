class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __gt__(self, other):
        return self.celsius > other.celsius


t1 = Temperature(40)
t2 = Temperature(30)

print(t1 > t2)