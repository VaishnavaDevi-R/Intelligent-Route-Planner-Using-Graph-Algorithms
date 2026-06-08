import os
import osmnx as ox

CACHE_FILE = "data/osm_cache/madurai.graphml"

def download_city_graph(city_name):
    if os.path.exists(CACHE_FILE):
        print("Loading cached graph...")
        graph = ox.load_graphml(CACHE_FILE)
    else:
        print(f"Downloading road network for {city_name}...")

        graph = ox.graph_from_place(
            city_name,
            network_type="drive"
        )

        os.makedirs("data/osm_cache", exist_ok=True)

        ox.save_graphml(graph, CACHE_FILE)

        print("Graph saved to cache.")

    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")

    return graph


if __name__ == "__main__":
    graph = download_city_graph(
        "Madurai, Tamil Nadu, India"
    )