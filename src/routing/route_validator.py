def validate_nodes(graph, source, destination):

    if source not in graph.nodes:
        raise ValueError(
            f"Source node {source} not found"
        )

    if destination not in graph.nodes:
        raise ValueError(
            f"Destination node {destination} not found"
        )

    return True