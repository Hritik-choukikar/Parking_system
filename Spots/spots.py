class ParkingSpot:
    def __init__(self, id, occupied=False, reserved=False):
        self.spot_id = id
        self.occupied = occupied
        self.reserved = reserved

    def get_type(self):
        return self.__class__.__name__

    def is_occupied(self):
        return self.occupied

    def is_reserved(self):
        return self.reserved

    def get_id(self):
        return self.spot_id

    def vacate(self):
        self.occupied = False

    def occupy(self):
        self.occupied = True


class LargeParkingSpot(ParkingSpot):
    def __init__(self, id, occupied=False, reserved=False):
        super().__init__(id, occupied, reserved)
class CompactParkingSpot(ParkingSpot):
    def __init__(self, id, occupied=False, reserved=False):
        super().__init__(id, occupied, reserved)

class HandicappedParkingSpot(ParkingSpot):
    def __init__(self, id, occupied=False, reserved=True):
        super().__init__(id, occupied, reserved)

class BikeParkingSpot(ParkingSpot):
    def __init__(self, id, occupied=False, reserved=False):
        super().__init__(id, occupied, reserved)
