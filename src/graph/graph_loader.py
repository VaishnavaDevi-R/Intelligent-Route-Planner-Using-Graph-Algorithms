import os
import osmnx as ox

GRAPH_FILE = "data/madurai_graph.graphml"


def download_city_graph(city_name):

    if os.path.exists(GRAPH_FILE):

        print("Loading cached graph...")

        graph = ox.load_graphml(
            GRAPH_FILE
        )

    else:

        print(
            "Downloading graph..."
        )

        graph = ox.graph_from_place(
            city_name,
            network_type="drive"
        )

        os.makedirs(
            "data",
            exist_ok=True
        )

        ox.save_graphml(
            graph,
            GRAPH_FILE
        )

    print(
        f"Nodes: {len(graph.nodes)}"
    )

    print(
        f"Edges: {len(graph.edges)}"
    )

    return graph

if __name__ == "__main__":

    download_city_graph(
        "Madurai, Tamil Nadu, India"
    )