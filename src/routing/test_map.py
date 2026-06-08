from src.routing.route_engine import route_between_places
from src.routing.map_visualizer import create_route_map


if __name__ == "__main__":

    source = (
        "Meenakshi Amman Temple, Madurai"
    )

    destination = (
        "Madurai Junction Railway Station"
    )

    graph, path, distance, source_node, destination_node = (
        route_between_places(
            source,
            destination
        )
    )

    create_route_map(
        graph,
        path,
        source,
        destination
    )

    print(
        f"\nDistance: {distance/1000:.2f} km"
    )