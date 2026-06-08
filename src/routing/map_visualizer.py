import os
import folium


def create_route_map(
    graph,
    path,
    source_name,
    destination_name,
    output_file="outputs/route_maps/madurai_route.html"
):

    os.makedirs(
        "outputs/route_maps",
        exist_ok=True
    )

    route_coordinates = []

    for node in path:

        lat = graph.nodes[node]["y"]
        lon = graph.nodes[node]["x"]

        route_coordinates.append(
            [lat, lon]
        )

    start_lat = graph.nodes[path[0]]["y"]
    start_lon = graph.nodes[path[0]]["x"]

    route_map = folium.Map(
        location=[start_lat, start_lon],
        zoom_start=15
    )

    folium.Marker(
        location=route_coordinates[0],
        popup=source_name,
        tooltip="Source"
    ).add_to(route_map)

    folium.Marker(
        location=route_coordinates[-1],
        popup=destination_name,
        tooltip="Destination"
    ).add_to(route_map)

    folium.PolyLine(
        route_coordinates,
        weight=5,
        opacity=0.8
    ).add_to(route_map)

    route_map.save(output_file)

    print("\nMAP GENERATED")
    print("-" * 30)
    print(f"Saved to: {output_file}")

    return output_file