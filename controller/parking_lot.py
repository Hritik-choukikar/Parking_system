from models.parking_spot import *
from models.terminal import EntryTerminal, ExitTerminal

class ParkingLot:
    def __init__(self, processor, calculator):
        self.spots = [
            HandicappedParkingSpot("H1"),
            CompactParkingSpot("C1"),
            CompactParkingSpot("C2"),
            LargeParkingSpot("L1"),
            MotorcycleParkingSpot("M1")
        ]
        from strategy.parking_strategy import BasicParkingStrategy
        self.strategy = BasicParkingStrategy(self.spots)
        self.entry_terminal = EntryTerminal("E-Terminal", self.strategy)
        self.exit_terminal = ExitTerminal("X-Terminal", processor, calculator, self.strategy)
        self.active_tickets = {}

    def park_vehicle(self, spot_type):
        ticket = self.entry_terminal.issue_ticket(spot_type)
        if ticket:
            self.active_tickets[ticket.ticket_id] = ticket
            return ticket
        return None

    def exit_vehicle(self, ticket_id):
        ticket = self.active_tickets.get(ticket_id)
        if ticket:
            self.exit_terminal.accept_ticket(ticket)
            del self.active_tickets[ticket_id]
