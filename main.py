import sys
from vehicle import Vehicle
from parking_lot import ParkingLot

def process_command(parking_lot, command):
    parts = command.strip().split()

    if parts[0] == "create":
        return ParkingLot(int(parts[1]), int(parts[2]))  # levels, slots per level

    elif parts[0] == "park":
        if parking_lot is None:
            print("Please create a parking lot first using 'create_parking_lot'")
        else:
            vehicle = Vehicle(parts[1], parts[2])
            parking_lot.park(vehicle)

    elif parts[0] == "leave":
        level_no = int(parts[1])
        slot_no = int(parts[2])
        parking_lot.unpark(level_no, slot_no)

    elif parts[0] == "status":
        parking_lot.status()

    else:
        print("Unknown command")

    return parking_lot


def run_file_mode(filename):
    parking_lot = None
    with open(filename) as f:
        for line in f:
            parking_lot = process_command(parking_lot, line)


def run_interactive_mode():
    parking_lot = None
    while True:
        try:
            command = input("Enter command: ")
            if command.lower() in ["exit", "quit"]:
                break
            parking_lot = process_command(parking_lot, command)
        except EOFError:
            break


if __name__ == "__main__":
    '''if len(sys.argv) == 2:
        run_file_mode(sys.argv[1])   # Example: python main.py input.txt
    else: '''
    run_interactive_mode()       # Interactive shell