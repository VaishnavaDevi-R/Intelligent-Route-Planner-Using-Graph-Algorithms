import os
import osmnx as ox

CACHE_DIR = "data/osm_cache"
CACHE_FILE = f"{CACHE_DIR}/madurai.graphml"


def download_city_graph(city_name):
    os.makedirs(CACHE_DIR, exist_ok=True)

    if os.path.exists(CACHE_FILE):
        print("Loading cached graph...")
        graph = ox.load_graphml(CACHE_FILE)

    else:
        print(f"Downloading road network for {city_name}...")

        graph = ox.graph_from_place(
            city_name,
            network_type="drive"
        )

        ox.save_graphml(graph, CACHE_FILE)

        print("Graph cached successfully!")

    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")

    return graph