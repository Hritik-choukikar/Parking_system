from abc import ABC,abstractmethod
class ParkingStrategy(ABC):
    @abstractmethod
    def assign_parking_spot(self, type_):
        pass

    @abstractmethod
    def release_parking_spot(self, spot):
        pass


class BasicParkingStrategy(ParkingStrategy):
    def __init__(self, spots):
        self.available_spots = spots

    def assign_parking_spot(self, type_):
        for spot in self.available_spots:
            if spot.get_type() == type_ and not spot.is_occupied():
                return spot
        return None

    def release_parking_spot(self, spot):
        spot.vacate()