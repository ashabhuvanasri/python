class BikeDelivery:
    def deliver(self):
        print("Delivery by bike.")


class TruckDelivery:
    def deliver(self):
        print("Delivery by truck.")


class DroneDelivery:
    def deliver(self):
        print("Delivery by drone.")


def process_delivery(delivery):
    delivery.deliver()


process_delivery(BikeDelivery())
process_delivery(TruckDelivery())
process_delivery(DroneDelivery())