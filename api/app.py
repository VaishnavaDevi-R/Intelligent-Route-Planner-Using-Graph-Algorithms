from fastapi import FastAPI

from src.routing.route_engine import (
    route_between_places
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Intelligent Route Planner API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message":
        "Intelligent Route Planner API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/route")
def get_route(
    source: str,
    destination: str
):

    (
        graph,
        path,
        distance,
        eta,
        traffic_eta,
        fuel_cost,
        source_node,
        destination_node
    ) = route_between_places(
        source,
        destination
    )

    route_coordinates = []

    for node in path:

        route_coordinates.append(
            {
                "lat": graph.nodes[node]["y"],
                "lng": graph.nodes[node]["x"]
            }
        )

    return {

        "source":
        source,

        "destination":
        destination,

        "distance_km":
        round(
            distance / 1000,
            2
        ),

        "eta_minutes":
        eta,

        "traffic_eta_minutes":
        traffic_eta,

        "fuel_cost":
        fuel_cost,

        "path_nodes":
        len(path),

        "route_coordinates":
        route_coordinates
    }