class TicketManager:
    _instance = None

    def __init__(self):
        self.active_tickets = {}

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = TicketManager()
        return cls._instance

    def add_ticket(self, ticket_id, ticket):
        self.active_tickets[ticket_id] = ticket

    def remove_ticket(self, ticket_id):
        self.active_tickets.pop(ticket_id, None)

    def get_ticket(self, ticket_id):
        return self.active_tickets.get(ticket_id,None)
