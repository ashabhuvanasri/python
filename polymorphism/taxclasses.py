from abc import ABC, abstractmethod


class Delivery(ABC):

    @abstractmethod
    def calculate_delivery_charge(self, distance):
        pass


class BikeDelivery(Delivery):
    def calculate_delivery_charge(self, distance):
        return distance * 10


class TruckDelivery(Delivery):
    def calculate_delivery_charge(self, distance):
        return distance * 25


class DroneDelivery(Delivery):
    def calculate_delivery_charge(self, distance):
        return distance * 50


deliveries = [BikeDelivery(), TruckDelivery(), DroneDelivery()]

for delivery in deliveries:
    print("Charge:", delivery.calculate_delivery_charge(10))