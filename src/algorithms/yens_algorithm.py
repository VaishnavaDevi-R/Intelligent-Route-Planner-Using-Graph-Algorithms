import networkx as nx
from itertools import islice

from src.graph.graph_loader import download_city_graph


def get_alternative_routes(
    graph,
    source,
    destination,
    k=3
):
    try:

        print("Converting graph...")

        # Convert OSMnx MultiDiGraph -> DiGraph
        simple_graph = nx.DiGraph()

        for u, v, data in graph.edges(data=True):

            weight = data.get(
                "length",
                1
            )

            if simple_graph.has_edge(u, v):

                current_weight = simple_graph[u][v]["length"]

                if weight < current_weight:
                    simple_graph[u][v]["length"] = weight

            else:

                simple_graph.add_edge(
                    u,
                    v,
                    length=weight
                )

        print("Finding alternative routes...")

        routes = list(
            islice(
                nx.shortest_simple_paths(
                    simple_graph,
                    source,
                    destination,
                    weight="length"
                ),
                k
            )
        )

        return routes

    except Exception as e:

        print(f"Error: {e}")

        return []


if __name__ == "__main__":

    graph = download_city_graph(
        "Madurai, Tamil Nadu, India"
    )

    # Use nodes from your successful Dijkstra test
    source = 314932941
    destination = 1168754478

    routes = get_alternative_routes(
        graph,
        source,
        destination,
        k=3
    )

    print("\nALTERNATIVE ROUTES")
    print("-" * 40)

    for i, route in enumerate(
        routes,
        start=1
    ):

        print(
            f"Route {i}: "
            f"{len(route)} nodes"
        )

    if not routes:
        print(
            "No alternative routes found."
        )