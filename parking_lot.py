from datetime import datetime
import heapq
from parking_slot import ParkingSlot
from parking_ticket import ParkingTicket


class ParkingLot:

    def __init__(self):

        self.floors = {}

        self.available_slots = {}

        self.active_tickets = {}

        self.total_revenue = 0

        self.create_parking_lot()

    def create_parking_lot(self):

        vehicle_types = ["Car", "Bike", "Truck"]

        for floor in range(1, 4):

            self.floors[floor] = []

            self.available_slots[floor] = {
                "Car": [],
                "Bike": [],
                "Truck": []
                }

            for slot_id in range(1, 51):

                if slot_id <= 25:
                    slot_type = "Car"

                elif slot_id <= 40:
                    slot_type = "Bike"

                else:
                    slot_type = "Truck"

                slot = ParkingSlot(
                    slot_id,
                    floor,
                    slot_type
                )

                self.floors[floor].append(slot)

                heapq.heappush(
                        self.available_slots[floor][slot_type],
                        slot
                )

    def park_vehicle(self, vehicle):

        for floor in self.available_slots:

            queue = self.available_slots[floor][vehicle.vehicle_type]

            if len(queue) > 0:

                slot = heapq.heappop(queue)

                slot.occupy()

                ticket = ParkingTicket(
                    vehicle,
                    slot
                )

                self.active_tickets[
                    vehicle.vehicle_number
                ] = ticket

                print("\nVehicle Parked Successfully")
                print(ticket)

                return ticket

        print("\nNo Slots Available")

        return None

    def search_vehicle(self, vehicle_number):

        ticket = self.active_tickets.get(
            vehicle_number
        )

        if ticket:

            print("\nVehicle Found")
            print(ticket)

        else:

            print("\nVehicle Not Found")
    def remove_vehicle(self, vehicle_number):
        
        ticket = self.active_tickets.get(vehicle_number)

        if not ticket:
            print("\nVehicle Not Found")
            return

        ticket.close_ticket()

        duration = (
            ticket.exit_time - ticket.entry_time
        ).total_seconds() / 3600

        if duration < 1:
            duration = 1

        rates = {
            "Car": 20,
            "Bike": 10,
            "Truck": 50
        }

        fee = (
            duration *
            rates[ticket.vehicle.vehicle_type]
        )

        slot = ticket.slot

        slot.release()

        heapq.heappush(
            self.available_slots[
                slot.floor_number
            ][slot.slot_type],
            slot
        )

        self.total_revenue += fee

        del self.active_tickets[
            vehicle_number
        ]

        print("\n===== EXIT DETAILS =====")

        print(f"Vehicle : {vehicle_number}")
        print(f"Duration : {duration:.2f} Hours")
        print(f"Fee : Rs.{fee:.2f}")

        print(
            f"Slot Released : Floor {slot.floor_number}"
            f" Slot {slot.slot_id}"
        )

    def show_available_slots(self):

        print("\n===== AVAILABLE SLOTS =====")

        for floor in self.available_slots:

            print(f"\nFloor {floor}")

            for vehicle_type in self.available_slots[floor]:

                count = len(
                    self.available_slots[floor][vehicle_type]
                )

                print(
                    f"{vehicle_type}: {count}"
                )
    def generate_report(self):

        occupied = len(
            self.active_tickets
        )

        available = 0

        for floor in self.available_slots:

            for vehicle_type in self.available_slots[floor]:

                available += len(
                    self.available_slots[floor][vehicle_type]
                )

        print("\n===== REPORT =====")

        print(
            f"Active Vehicles : {occupied}"
        )

        print(
            f"Available Slots : {available}"
        )
        print(
    f"Revenue Generated : "
    f"Rs.{self.total_revenue:.2f}"
)