import time
from payment.processor import CreditCardProcessor
from payment.calculator import FlatRateCalculator
from controller.parking_lot import ParkingLot

def main():
    rate_table = {
        "HandicappedParkingSpot": 20,
        "CompactParkingSpot": 30,
        "LargeParkingSpot": 50,
        "MotorcycleParkingSpot": 15
    }
    processor = CreditCardProcessor()
    calculator = FlatRateCalculator(rate_table)
    lot = ParkingLot(processor, calculator)

    print("\n🚙 Request: Compact")
    ticket1 = lot.park_vehicle("CompactParkingSpot")

    print("\n🏍️ Request: Motorcycle")
    ticket2 = lot.park_vehicle("MotorcycleParkingSpot")

    print("\n♿ Request: Handicapped (should be reserved)")
    ticket3 = lot.park_vehicle("HandicappedParkingSpot")

    time.sleep(2)

    print("\n🚗 Exit: Compact")
    if ticket1:
        lot.exit_vehicle(ticket1.ticket_id)

    print("\n🏁 Exit: Motorcycle")
    if ticket2:
        lot.exit_vehicle(ticket2.ticket_id)

if __name__ == "__main__":
    main()
