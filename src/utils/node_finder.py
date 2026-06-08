from osmnx.distance import nearest_nodes


def find_nearest_node(
    graph,
    latitude,
    longitude
):

    node = nearest_nodes(
        graph,
        longitude,
        latitude
    )

    return node