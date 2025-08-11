import time

class Ticket:
    def __init__(self, ticket_id, spot):
        self.ticket_id = ticket_id
        self.spot_id = spot.spot_id
        self.spot_type = spot.get_type()
        self.spot = spot
        self.issue_time = time.time()
        self.exit_time = None
        self.paid = False
