MAP_DATA = {
    "locations": [
        {"name": "City Hall", "coordinates": (40.7128, -74.0060)},
        {"name": "Codetropolis Park", "coordinates": (40.7138, -74.0050)},
        {"name": "Hovercar Garage", "coordinates": (40.7120, -74.0045)},
        {"name": "Futureville Plaza", "coordinates": (40.7150, -74.0020)},
        {"name": "Drone Dock", "coordinates": (40.7140, -74.0030)},
        {"name": "Anti-Gravity Bike Store", "coordinates": (40.7110, -74.0070)},
        {"name": "Robot Cafe", "coordinates": (40.7160, -74.0010)},
        {"name": "Atlantis", "coordinates": (31.0000, -24.0000)},
        {"name": "Poseidon's Palace", "coordinates": (32.0000, -25.0000)},
        {"name": "Neptune's Garden", "coordinates": (33.0000, -26.0000)},
    ]
}

def get_location(name):
    """
    Retrieve the coordinates of a location by name.
    """
    if name.lower() == "atlantis":
        import random
        return random.choice(MAP_DATA["locations"][7:])["coordinates"]
    
    for location in MAP_DATA["locations"]:
        if location["name"].lower() == name.lower():
            return location["coordinates"]
    return None  # Returns None if the location is not found

def get_all_locations():
    """
    Retrieve a list of all available location names.
    """
    return [location["name"] for location in MAP_DATA["locations"]]

def plan_route(start, end):
    """
    Plan a route between two locations.
    """
    start_coords = get_location(start)
    end_coords = get_location(end)

    if not start_coords or not end_coords:
        raise ValueError(f"One or both locations not found: {start}, {end}")
    
    # TODO: Calculate distance between coordinates (use Haversine formula)
    return f"Route planned from {start} to {end}. Distance calculation coming soon!"

if __name__ == "__main__":
    print("Available locations:")
    print(get_all_locations())
    
    try:
        print(plan_route("City Hall", "Codetropolis Park"))
    except Exception as e:
        print("Error planning route:", e)
