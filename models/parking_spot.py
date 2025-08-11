class ParkingSpot:
    def __init__(self, spot_id, reserved=False):
        self.spot_id = spot_id
        self.occupied = False
        self.reserved = reserved

    def is_occupied(self):
        return self.occupied

    def occupy(self):
        if self.reserved:
            print(f" Spot {self.spot_id} is reserved and can't be auto-assigned.")
        else:
            self.occupied = True

    def vacate(self):
        self.occupied = False

    def get_type(self):
        return self.__class__.__name__

class HandicappedParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, reserved=True)

class CompactParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)

class LargeParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)

class MotorcycleParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
