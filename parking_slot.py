class ParkingSlot:
    def __init__(self,slot_no):
        self.slot_no=slot_no
        self.vehicle=None
    
    def is_free(self):
        return self.vehicle is None
    
    def park(self,vehicle):
        if self.is_free():
            self.vehicle=vehicle
            return True
        return False
    
    def unpark(self):
        if not self.is_free():
            v=self.vehicle
            self.vehicle=None
            return v
        return None

