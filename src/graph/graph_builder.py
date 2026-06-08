from src.graph.graph_loader import download_city_graph


def build_adjacency_list(graph):
    adjacency_list = {}

    for node in graph.nodes():
        adjacency_list[node] = []

    for u, v, data in graph.edges(data=True):
        distance = data.get("length", 1)

        adjacency_list[u].append(
            {
                "neighbor": v,
                "distance": distance
            }
        )

    return adjacency_list


if __name__ == "__main__":
    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)

    adjacency_list = build_adjacency_list(graph)

    print("\nADJACENCY LIST SAMPLE")
    print("-" * 30)

    count = 0

    for node, neighbors in adjacency_list.items():
        print(f"\nNode: {node}")

        for neighbor in neighbors[:5]:
            print(
                f" -> {neighbor['neighbor']} "
                f"(Distance: {neighbor['distance']:.2f}m)"
            )

        count += 1

        if count == 5:
            break