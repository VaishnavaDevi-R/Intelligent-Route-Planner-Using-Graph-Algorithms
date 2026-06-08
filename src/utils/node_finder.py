from osmnx.distance import nearest_nodes


def find_nearest_node(graph, longitude, latitude):
    return nearest_nodes(
        graph,
        longitude,
        latitude
    )