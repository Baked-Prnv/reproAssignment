from api.models import Rooms


def run():
    room_data = [
        # DELUX ROOMS
        {'room_type': 'Delux', 'room_no': 'A1', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'A2', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'A3', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'A4', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'A5', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'B1', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'B2', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'B3', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'B4', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'B5', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'C1', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'C2', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'C3', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'C4', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'C5', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'D1', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'D2', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'D3', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'D4', 'room_price': 7000},
        {'room_type': 'Delux', 'room_no': 'D5', 'room_price': 7000},
        # Luxury ROOMS
        {'room_type': 'Luxury', 'room_no': 'A6', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'A7', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'A8', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'A9', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'A10', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'B6', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'B7', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'B8', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'B9', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'B10', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'C6', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'C7', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'C8', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'C9', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'C10', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'D6', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'D7', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'D8', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'D9', 'room_price': 8500},
        {'room_type': 'Luxury', 'room_no': 'D10', 'room_price': 8500},
        # Luxury Suite
        {'room_type': 'Luxury Suite', 'room_no': 'D11', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D12', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D13', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D14', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D15', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D16', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D17', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D18', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D19', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'D20', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'E1', 'room_price': 12000},
        {'room_type': 'Luxury Suite', 'room_no': 'E2', 'room_price': 12000},
        # Presidential Suite
        {'room_type': 'Presidential Suite', 'room_no': 'E3', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E4', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E5', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E6', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E7', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E8', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E9', 'room_price': 20000},
        {'room_type': 'Presidential Suite', 'room_no': 'E10', 'room_price': 20000}
    ]
    
    for room_info in room_data:
        room = Rooms(**room_info)
        room.save()