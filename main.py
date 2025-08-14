from Factory.parkingspotfactory import ParkingSpotFactory
from Components.terminal import EntryTerminal,ExitTerminal
from Managers.parkingspotmanager import ParkingSpotManager
from Managers.ticketmanager import TicketManager
from Strategy.paymentstrategy import Cash,CreditCard

class ParkingLot:
    def __init__(self):
        self.factory = ParkingSpotFactory()
        self.entry_terminal = EntryTerminal("EntryTerminal")
        self.exit_terminal = ExitTerminal("ExitTerminal")
        self.manager = ParkingSpotManager.get_instance()
        self.ticketmanager = TicketManager.get_instance()
        self.initialize()

    def initialize(self):
         
        for i in range(8):
            spot = self.factory.create_spot(str(i), "HandicappedParkingSpot")
            self.manager.add_spot(spot)
        for i in range(8, 15):
            spot = self.factory.create_spot(str(i), "BikeParkingSpot")
            self.manager.add_spot(spot)
        for i in range(15, 28):
            spot = self.factory.create_spot(str(i), "CompactParkingSpot")
            self.manager.add_spot(spot)
        for i in range(28, 100):
            spot = self.factory.create_spot(str(i), "LargeParkingSpot")
            self.manager.add_spot(spot)

    def park_vehicle(self, spot_type, vehicle_no):
        ticket = self.entry_terminal.issue_ticket(spot_type,vehicle_no)
        if ticket:
            print("🚗 Vehicle parked.")
            return ticket
        else:
            print("❌ Parking failed.")
            return None

    def unpark_vehicle(self, ticket_id, payment_method):
         
        ticket=self.ticketmanager.get_ticket(ticket_id)
        if payment_method == "Cash":
            self.exit_terminal.set_payment_strategy(Cash())
             
        elif payment_method == "CreditCard":
            self.exit_terminal.set_payment_strategy(CreditCard())
            payt=True
        elif payment_method == None:
            
            print("⚠️ Unsupported payment method.")
            return "Invalid payment"
            
        
         
         
        temp=self.exit_terminal.accept_ticket(ticket_id)
        return temp 
