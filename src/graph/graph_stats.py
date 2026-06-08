from graph_loader import download_city_graph

city = "Madurai, Tamil Nadu, India"

graph = download_city_graph(city)

print("\nGRAPH STATISTICS")
print("-" * 30)

print(f"Nodes: {graph.number_of_nodes()}")
print(f"Edges: {graph.number_of_edges()}")

avg_degree = (
    sum(dict(graph.degree()).values())
    / graph.number_of_nodes()
)

print(f"Average Degree: {avg_degree:.2f}")