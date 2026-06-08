import heapq

from src.graph.graph_loader import download_city_graph
from src.routing.route_validator import validate_nodes
from src.utils.haversine import haversine


def heuristic(graph, node, destination):

    lat1 = graph.nodes[node]["y"]
    lon1 = graph.nodes[node]["x"]

    lat2 = graph.nodes[destination]["y"]
    lon2 = graph.nodes[destination]["x"]

    return haversine(
        lat1,
        lon1,
        lat2,
        lon2
    )


def astar(graph, source, destination):

    validate_nodes(
        graph,
        source,
        destination
    )

    g_score = {
        node: float("inf")
        for node in graph.nodes
    }

    g_score[source] = 0

    f_score = {
        node: float("inf")
        for node in graph.nodes
    }

    f_score[source] = heuristic(
        graph,
        source,
        destination
    )

    previous = {}

    open_set = []

    heapq.heappush(
        open_set,
        (
            f_score[source],
            source
        )
    )

    while open_set:

        _, current = heapq.heappop(
            open_set
        )

        if current == destination:
            break

        for neighbor in graph.neighbors(current):

            edge_data = graph.get_edge_data(
                current,
                neighbor
            )

            weight = edge_data[0].get(
                "length",
                1
            )

            tentative_g = (
                g_score[current]
                + weight
            )

            if tentative_g < g_score[neighbor]:

                previous[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score[neighbor] = (
                    tentative_g
                    + heuristic(
                        graph,
                        neighbor,
                        destination
                    )
                )

                heapq.heappush(
                    open_set,
                    (
                        f_score[neighbor],
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

    return path, g_score[destination]

if __name__ == "__main__":

    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)

    nodes = list(graph.nodes())

    source = nodes[0]

    destination = nodes[500]

    path, distance = astar(
        graph,
        source,
        destination
    )

    print("\nA* RESULT")
    print("-" * 30)

    print(f"Source: {source}")

    print(f"Destination: {destination}")

    print(f"Path Nodes: {len(path)}")

    print(f"Distance: {distance:.2f} meters")