from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


def get_coordinates(place_name):
    """
    Convert a place name into latitude and longitude.
    """

    geolocator = Nominatim(
        user_agent="intelligent_route_planner"
    )

    search_queries = [
        place_name,
        f"{place_name}, Madurai",
        f"{place_name}, Tamil Nadu",
        f"{place_name}, India"
    ]

    for query in search_queries:
        try:
            location = geolocator.geocode(
                query,
                exactly_one=True,
                timeout=10
            )

            if location:
                print("\nLOCATION FOUND")
                print("-" * 40)
                print(f"Query: {query}")
                print(f"Address: {location.address}")
                print(f"Latitude: {location.latitude}")
                print(f"Longitude: {location.longitude}")

                return (
                    location.latitude,
                    location.longitude
                )

        except (
            GeocoderTimedOut,
            GeocoderServiceError
        ) as e:

            print(
                f"Geocoder error for '{query}': {e}"
            )

    raise ValueError(
        f"Location not found: {place_name}"
    )


if __name__ == "__main__":

    print("\nTesting Geocoder\n")

    places = [
        "Meenakshi Amman Temple",
        "Madurai Junction Railway Station",
        "Madurai Airport",
        "Thirumalai Nayakkar Mahal"
    ]

    for place in places:

        try:
            lat, lon = get_coordinates(place)

            print(
                f"\nSUCCESS: {place}"
            )

            print(
                f"Coordinates: ({lat}, {lon})"
            )

        except Exception as e:

            print(
                f"\nFAILED: {place}"
            )

            print(e)

        print("\n" + "=" * 50)