import osmnx as ox

def download_city_graph(city_name):
    print(f"Downloading road network for {city_name}...")

    graph = ox.graph_from_place(
        city_name,
        network_type="drive"
    )

    print("Download completed!")
    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")

    return graph


if __name__ == "__main__":
    city = "Madurai, Tamil Nadu, India"

    graph = download_city_graph(city)