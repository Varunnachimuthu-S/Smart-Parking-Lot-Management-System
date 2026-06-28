from vehicle import Vehicle
from parking_lot import ParkingLot

parking_lot = ParkingLot()

while True:

    print("\n===== PARKING LOT SYSTEM =====")

    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicle")
    print("4. Show Available Slots")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        vehicle_number = input(
            "Enter Vehicle Number: "
        )

        vehicle_type = input(
            "Enter Vehicle Type (Car/Bike/Truck): "
        )

        vehicle = Vehicle(
            vehicle_number,
            vehicle_type
        )

        parking_lot.park_vehicle(
            vehicle
        )

    elif choice == "2":

        vehicle_number = input(
            "Enter Vehicle Number: "
        )

        parking_lot.remove_vehicle(
            vehicle_number
        )

    elif choice == "3":

        vehicle_number = input(
            "Enter Vehicle Number: "
        )

        parking_lot.search_vehicle(
            vehicle_number
        )

    elif choice == "4":

        parking_lot.show_available_slots()

    elif choice == "5":

        parking_lot.generate_report()

    elif choice == "6":

        print(
            "\nThank You For Using The System"
        )

        break

    else:

        print(
            "\nInvalid Choice"
        )