class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)

    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge

bus = Bus()
print(f"The total fare for the bus ride is INR {bus.fare()}")