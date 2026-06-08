from collections import deque

from src.graph.graph_loader import download_city_graph
from src.graph.graph_builder import build_adjacency_list


def bfs(adjacency_list, start_node, max_nodes=20):
    visited = set()
    queue = deque([start_node])

    traversal_order = []

    while queue and len(traversal_order) < max_nodes:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            for neighbor in adjacency_list[node]:
                next_node = neighbor["neighbor"]

                if next_node not in visited:
                    queue.append(next_node)

    return traversal_order


if __name__ == "__main__":
    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)

    adjacency_list = build_adjacency_list(graph)

    start_node = list(adjacency_list.keys())[0]

    result = bfs(adjacency_list, start_node)

    print("\nBFS Traversal")
    print("-" * 30)

    for node in result:
        print(node)