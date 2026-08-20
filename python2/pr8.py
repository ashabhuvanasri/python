class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car:", self.brand, self.model)


class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Bike:", self.brand, self.model)


class Truck:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Truck:", self.brand, self.model)


vehicles = [
    Car("Toyota", "Camry"),
    Bike("Honda", "Shine"),
    Truck("Tata", "Prima")
]

for vehicle in vehicles:
    vehicle.display()