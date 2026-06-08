TRAFFIC_FACTORS = {
    "low": 1.0,
    "medium": 1.3,
    "heavy": 1.8,
    "severe": 2.5
}


def apply_traffic(
    eta_minutes,
    traffic_level="medium"
):

    factor = TRAFFIC_FACTORS.get(
        traffic_level,
        1.0
    )

    return round(
        eta_minutes * factor,
        2
    )

if __name__ == "__main__":

    eta = 3.4

    print(
        f"Normal ETA: {eta} min"
    )

    print(
        f"Heavy Traffic ETA: "
        f"{apply_traffic(eta,'heavy')} min"
    )

    print(
        f"Severe Traffic ETA: "
        f"{apply_traffic(eta,'severe')} min"
    )