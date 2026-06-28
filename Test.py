from vehicle import Vehicle
from parking_lot import ParkingLot

parking_lot = ParkingLot()

v1 = Vehicle("TN38AB1234", "Car")
v2 = Vehicle("TN38AB5678", "Car")
v3 = Vehicle("TN38AB9999", "Car")

parking_lot.park_vehicle(v1)
parking_lot.park_vehicle(v2)
parking_lot.park_vehicle(v3)

parking_lot.show_available_slots()

parking_lot.remove_vehicle("TN38AB5678")

v4 = Vehicle("TN38AB7777", "Car")
parking_lot.park_vehicle(v4)