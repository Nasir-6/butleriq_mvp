# train_data.py

train_data = [
    # Front Desk
    ("I lost my room key", {"cats": {"Front Desk": 1.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("Can I check in early?", {"cats": {"Front Desk": 1.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("I need a copy of my invoice", {"cats": {"Front Desk": 1.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),

    # Housekeeping
    ("Please send more towels", {"cats": {"Front Desk": 0.0, "Housekeeping": 1.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("I need two extra pillows", {"cats": {"Front Desk": 0.0, "Housekeeping": 1.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("Could you clean my room now?", {"cats": {"Front Desk": 0.0, "Housekeeping": 1.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 0.0}}),

    # Room Service
    ("I'd like to order breakfast", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 1.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("Send a burger and fries to room 502", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 1.0, "Maintenance": 0.0, "Concierge": 0.0}}),
    ("Bring two bottles of water", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 1.0, "Maintenance": 0.0, "Concierge": 0.0}}),

    # Maintenance
    ("The air conditioning isn't working", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 1.0, "Concierge": 0.0}}),
    ("There's no hot water in the shower", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 1.0, "Concierge": 0.0}}),
    ("The toilet is leaking", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 1.0, "Concierge": 0.0}}),

    # Concierge
    ("Please call me a taxi", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 1.0}}),
    ("Book a car to the airport for 6 AM", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 1.0}}),
    ("Can you recommend a good seafood restaurant?", {"cats": {"Front Desk": 0.0, "Housekeeping": 0.0, "Room Service": 0.0, "Maintenance": 0.0, "Concierge": 1.0}})
]
