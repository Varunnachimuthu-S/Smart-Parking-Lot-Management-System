from datetime import datetime
import uuid


class ParkingTicket:

    def __init__(self, vehicle, slot):

        self.ticket_id = str(uuid.uuid4())[:8]

        self.vehicle = vehicle
        self.slot = slot

        self.entry_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        self.exit_time = datetime.now()

    def __str__(self):

        return (
            f"\nTicket ID : {self.ticket_id}\n"
            f"Vehicle   : {self.vehicle.vehicle_number}\n"
            f"Type      : {self.vehicle.vehicle_type}\n"
            f"Floor     : {self.slot.floor_number}\n"
            f"Slot      : {self.slot.slot_id}\n"
            f"Entry     : {self.entry_time}\n"
        )