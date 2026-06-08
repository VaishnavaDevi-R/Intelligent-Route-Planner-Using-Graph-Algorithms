import heapq

from src.graph.graph_loader import download_city_graph
from src.routing.route_validator import validate_nodes


def dijkstra(graph, source, destination):

    validate_nodes(
        graph,
        source,
        destination
    )

    distances = {
        node: float("inf")
        for node in graph.nodes
    }

    previous = {}

    distances[source] = 0

    priority_queue = [
        (0, source)
    ]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_node == destination:
            break

        for neighbor in graph.neighbors(
            current_node
        ):

            edge_data = graph.get_edge_data(
                current_node,
                neighbor
            )

            weight = edge_data[0].get(
                "length",
                1
            )

            distance = (
                current_distance
                + weight
            )

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (
                        distance,
                        neighbor
                    )
                )

    path = []

    current = destination

    while current in previous:

        path.append(current)

        current = previous[current]

    path.append(source)

    path.reverse()

    return path, distances[destination]


if __name__ == "__main__":

    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)

    nodes = list(graph.nodes())

    source = nodes[0]

    destination = nodes[500]

    path, distance = dijkstra(
        graph,
        source,
        destination
    )

    print("\nDIJKSTRA RESULT")
    print("-" * 30)

    print(f"Source: {source}")

    print(f"Destination: {destination}")

    print(f"Path Nodes: {len(path)}")

    print(f"Distance: {distance:.2f} meters")