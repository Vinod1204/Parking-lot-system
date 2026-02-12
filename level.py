from parking_slot import ParkingSlot
class Level:

    def __init__(self,level_no,num_slots):
        self.level_no=level_no
        self.slots=[ParkingSlot(i+1) for i in range(num_slots)]

    def  park_vehicle(self,vehicle):
        for slot in self.slots:
            if slot.is_free():
                slot.park(vehicle)
                return slot
        return None
    
    def unpark_vehichle(self,slot_no):
        if 1 <= slot_no <= len(self.slots):
            return self.slots[slot_no-1].unpark()
        return None
    
    def available_slots(self):
        return [self.slot_no for slot in self.slots if slot.is_free()]
       
