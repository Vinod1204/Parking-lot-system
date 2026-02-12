from level import Level
from parking_slot import ParkingSlot
from ticket import ParkingTicket
class ParkingLot:
    def __init__(self, num_levels, slots_per_level):
        self.levels=[Level(i+1,slots_per_level) for i in range(num_levels)]

    def park(self,vehicle):
        for level in self.levels:
            slot = level.park_vehicle(vehicle)
            if slot:
                print(f"Parked at level {level.level_no} , in slot {slot.slot_no} ")
                return ParkingTicket(level.level_no, slot.slot_no,vehicle)
        print("Parking lot full")
        return None
    
    def unpark(self, level_no, slot_no):
        if 1<=level_no <= len(self.levels):
            vehicle=self.levels[level_no-1].unpark_vehichle(slot_no)
            if vehicle:
                print(f"Vehicle {vehicle.reg_no} exited from Level {level_no} and slot {slot_no}")
            return vehicle
        
        print("Invalid slot or Empty")
        return None
    
    def status(self):
        for level in self.levels:
            print(f"Level {level.level_no}")
            for slot in level.slots:
                if slot.vehicle:
                    print(f" Slot {slot.slot_no} : {slot.vehicle}")

