from Spots.spots import LargeParkingSpot,CompactParkingSpot,BikeParkingSpot,HandicappedParkingSpot
class ParkingSpotFactory:
    @staticmethod
    def create_spot(ide, type_):
        if type_ == "LargeParkingSpot":
            return LargeParkingSpot(ide)
        elif type_ == "CompactParkingSpot":
            return CompactParkingSpot(ide)
        elif type_ == "BikeParkingSpot":
            return BikeParkingSpot(ide)
        elif type_ == "HandicappedParkingSpot":
            return HandicappedParkingSpot(ide)
        else:
            return None