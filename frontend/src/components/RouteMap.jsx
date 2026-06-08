import {
  MapContainer,
  TileLayer,
  Polyline,
  Marker,
  Popup
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

export default function RouteMap({
  coordinates
}) {

  if (
    !coordinates ||
    coordinates.length === 0
  ) {
    return null;
  }

  const route = coordinates.map(
    (point) => [
      point.lat,
      point.lng
    ]
  );

  return (

    <div className="bg-white rounded-xl shadow-md p-6 mt-6">

      <div className="flex items-center justify-between mb-4">

        <h2 className="text-2xl font-bold">
          Interactive Route Map
        </h2>

        <span className="text-sm text-gray-500">
          OpenStreetMap Visualization
        </span>

      </div>

      <MapContainer
        center={route[0]}
        zoom={15}
        scrollWheelZoom={true}
        style={{
          height: "550px",
          width: "100%",
          borderRadius: "12px"
        }}
      >

        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {/* Source Marker */}

        <Marker
          position={route[0]}
        >
          <Popup>
            <strong>Source Location</strong>
          </Popup>
        </Marker>

        {/* Destination Marker */}

        <Marker
          position={
            route[
              route.length - 1
            ]
          }
        >
          <Popup>
            <strong>Destination Location</strong>
          </Popup>
        </Marker>

        {/* Route Polyline */}

        <Polyline
          positions={route}
          pathOptions={{
            color: "#2563eb",
            weight: 7,
            opacity: 0.9
          }}
        />

      </MapContainer>

    </div>

  );
}