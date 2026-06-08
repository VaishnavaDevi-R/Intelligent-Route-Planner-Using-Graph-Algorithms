def calculate_fuel_cost(
    distance_meters,
    mileage_kmpl=40,
    fuel_price_per_liter=102
):
    """
    Calculate trip fuel cost.
    """

    distance_km = distance_meters / 1000

    fuel_needed = (
        distance_km / mileage_kmpl
    )

    cost = (
        fuel_needed *
        fuel_price_per_liter
    )

    return round(cost, 2)