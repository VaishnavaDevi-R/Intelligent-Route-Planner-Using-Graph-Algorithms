from src.graph.graph_loader import download_city_graph
from src.graph.graph_builder import build_adjacency_list


def dfs(adjacency_list, start_node, visited=None, traversal=None, max_nodes=20):
    if visited is None:
        visited = set()

    if traversal is None:
        traversal = []

    if len(traversal) >= max_nodes:
        return traversal

    visited.add(start_node)
    traversal.append(start_node)

    for neighbor in adjacency_list[start_node]:
        next_node = neighbor["neighbor"]

        if next_node not in visited:
            dfs(
                adjacency_list,
                next_node,
                visited,
                traversal,
                max_nodes
            )

            if len(traversal) >= max_nodes:
                break

    return traversal


if __name__ == "__main__":
    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)

    adjacency_list = build_adjacency_list(graph)

    start_node = list(adjacency_list.keys())[0]

    result = dfs(adjacency_list, start_node)

    print("\nDFS Traversal")
    print("-" * 30)

    for node in result:
        print(node)