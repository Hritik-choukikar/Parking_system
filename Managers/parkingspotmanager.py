from Strategy.parkingstrategy import BasicParkingStrategy

class ParkingSpotManager:
    _instance = None

    def __init__(self):
        self.spots = {}
        self.available = set()
        self.occupied = set()
        self.parking_strategy = BasicParkingStrategy(self.available)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ParkingSpotManager()
        return cls._instance

    def make_available(self, spot):
        self.occupied.remove(spot)
        self.available.add(spot)

    def make_unavailable(self, spot):
        self.available.remove(spot)
        self.occupied.add(spot)

    def add_spot(self, spot):
        self.spots[spot.get_id()] = spot
        self.available.add(spot)

    def assign_empty_spot(self, spot_type):
        return self.parking_strategy.assign_parking_spot(spot_type)

    def get_all_spots(self):
        return list(self.spots.values())
