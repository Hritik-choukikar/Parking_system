class ParkingStrategy:
    def assign_parking_spot(self, requested_type):
        raise NotImplementedError

    def release_parking_spot(self, spot):
        raise NotImplementedError

class BasicParkingStrategy(ParkingStrategy):
    def __init__(self, available_spots):
        self.available_spots = available_spots

    def assign_parking_spot(self, requested_type):
        for spot in self.available_spots:
            if not spot.is_occupied() and spot.get_type() == requested_type:
                return spot
        print(f"No available {requested_type} spots.")
        return None

    def release_parking_spot(self, spot):
        spot.vacate()
