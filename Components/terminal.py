import time
from Managers.parkingspotmanager import ParkingSpotManager
from Managers.ticketmanager import TicketManager
from Components.ticket import Ticket
from Components.calculator import TariffCalculator
class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id
        self.spot_manager = ParkingSpotManager.get_instance()
        self.ticket_manager = TicketManager.get_instance()

class EntryTerminal(Terminal):
    def issue_ticket(self, spot_type,vehicle_no):
        spot = self.spot_manager.assign_empty_spot(spot_type)
        if spot:
            ticket_id = f"T{int(time.time())}{spot_type}"
            ticket = Ticket(ticket_id, spot, vehicle_no)
            self.ticket_manager.add_ticket(ticket_id, ticket)
            self.spot_manager.make_unavailable(spot)
            spot.occupy()
            print(f"✅ Ticket Issued: {ticket.ticket_id}")
            return ticket
        else:
            print("🚫 No valid spots available.")
            return None


class ExitTerminal(Terminal):
    def __init__(self, terminal_id):
        super().__init__(terminal_id)
        self.calculator = TariffCalculator()
        self.payment_strategy = None

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def pay(self, amount):
        if self.payment_strategy:
            self.payment_strategy.process_payment(amount)
        else:
            print("⚠️ No payment method selected.")

    def accept_ticket(self, ticket_id):
        ticket = self.ticket_manager.get_ticket(ticket_id)
        if ticket:
            leaving_time = time.time()
            amount = self.calculator.calculate(ticket.entering_time, leaving_time, ticket.spot_type)
            print(f"💰 Parking Fee: ₹{amount}")
            self.pay(amount)
            ticket.spot.vacate()
            self.ticket_manager.remove_ticket(ticket_id)
            self.spot_manager.make_available(ticket.spot)
            print("✅ Vehicle unparked successfully.")
            return True
        else:
            print("🚫 Invalid ticket ID.")
            return 'invalid ticketid'
           