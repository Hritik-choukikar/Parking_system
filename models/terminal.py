import time
from models.ticket import Ticket

class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id

class EntryTerminal(Terminal):
    def __init__(self, terminal_id, strategy):
        super().__init__(terminal_id)
        self.strategy = strategy

    def issue_ticket(self, requested_type):
        spot = self.strategy.assign_parking_spot(requested_type)
        if not spot:
            return None
        ticket_id = f"T{int(time.time())}"
        ticket = Ticket(ticket_id, spot)
        spot.occupy()
        print(f"🎫 Ticket Issued: {ticket.ticket_id} | Type: {ticket.spot_type} | Spot ID: {ticket.spot_id}")
        return ticket

class ExitTerminal(Terminal):
    def __init__(self, terminal_id, processor, calculator, strategy):
        super().__init__(terminal_id)
        self.processor = processor
        self.calculator = calculator
        self.strategy = strategy

    def accept_ticket(self, ticket):
        ticket.exit_time = time.time()
        amount = self.calculator.calculate_tariff(ticket.issue_time, ticket.exit_time, ticket.spot_type)
        self.processor.process(amount)
        self.strategy.release_parking_spot(ticket.spot)
        ticket.paid = True
        print(f"🚗 Spot {ticket.spot_id} ({ticket.spot_type}) is now available.")
        return amount
