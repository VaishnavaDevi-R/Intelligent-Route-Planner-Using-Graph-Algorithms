from src.graph.graph_loader import download_city_graph
from src.utils.geocoder import get_coordinates
from src.utils.node_finder import find_nearest_node
from src.algorithms.astar import astar
from src.analytics.metrics import calculate_eta
from src.analytics.fuel_estimator import calculate_fuel_cost
from src.traffic.traffic_engine import apply_traffic


def route_between_places(
    source_place,
    destination_place
):

    graph = download_city_graph(
        "Madurai, Tamil Nadu, India"
    )

    src_lat, src_lon = get_coordinates(
        source_place
    )

    dst_lat, dst_lon = get_coordinates(
        destination_place
    )

    source_node = find_nearest_node(
        graph,
        src_lat,
        src_lon
    )

    destination_node = find_nearest_node(
        graph,
        dst_lat,
        dst_lon
    )

    path, distance = astar(
        graph,
        source_node,
        destination_node
    )

    eta = calculate_eta(distance)

    traffic_eta = apply_traffic(
        eta,
        "medium"
    )

    fuel_cost = calculate_fuel_cost(
        distance
    )

    return (
    graph,
    path,
    distance,
    eta,
    traffic_eta,
    fuel_cost,
    source_node,
    destination_node
)


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

    print("\nREAL ROUTE RESULT")
    print("-" * 30)

    print(f"Source: {source}")

    print(f"Destination: {destination}")

    print(f"Path Nodes: {len(path)}")

    print(
        f"Distance: {distance/1000:.2f} km"
    )