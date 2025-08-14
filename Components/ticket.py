import time
class Ticket:
    def __init__(self, id, spot, vehicle_no):
        self.ticket_id = id
        self.spot_id = spot.get_id()
        self.spot = spot
        self.vehicle_no = vehicle_no
        self.spot_type = spot.get_type()
        self.paid = False
        self.entering_time = time.time()
        self.leaving_time = None

    def get_id(self):
      return self.spot_id    
