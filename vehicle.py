class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type} - {self.vehicle_number}"