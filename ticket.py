import time

class ParkingTicket:
    def __init__(self,level_no,slot_no,vehicle):
        self.level_no=level_no
        self.slot_no=slot_no
        self.vechile=vehicle
        self.start_time=time.time()

    def calculate_price(self,rate_per_hr=20):
        duration=(time.time() - self.start_time) / 3600

        return round(duration*rate_per_hr,2)
    
    def __str__(self):
        print(f"Ticket : Level {self.level_no}, Slot {self.slot_no}, Vehicle number {self.vechile.reg_no}")