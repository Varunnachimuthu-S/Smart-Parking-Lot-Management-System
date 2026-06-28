class ParkingSlot:
    def __init__(self, slot_id, floor_number, slot_type):
        self.slot_id = slot_id
        self.floor_number = floor_number
        self.slot_type = slot_type
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def release(self):
        self.is_occupied = False

    def __lt__(self, other):
        return self.slot_id < other.slot_id

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"

        return (
            f"Floor: {self.floor_number} | "
            f"Slot: {self.slot_id} | "
            f"Type: {self.slot_type} | "
            f"Status: {status}"
        )