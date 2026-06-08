def calculate_eta(distance_meters, average_speed_kmph=30):
    """
    Calculate ETA in minutes.
    """

    distance_km = distance_meters / 1000

    eta_hours = distance_km / average_speed_kmph

    eta_minutes = eta_hours * 60

    return round(eta_minutes, 2)