export default function RouteResult({
  result
}) {

  if (!result) return null;

  return (

    <div>

      <h2>Route Summary</h2>

      <p>
        Distance:
        {result.distance_km} km
      </p>

      <p>
        ETA:
        {result.eta_minutes} min
      </p>

      <p>
        Traffic ETA:
        {result.traffic_eta_minutes} min
      </p>

      <p>
        Fuel Cost:
        ₹{result.fuel_cost}
      </p>

      <p>
        Path Nodes:
        {result.path_nodes}
      </p>

    </div>

  );
}