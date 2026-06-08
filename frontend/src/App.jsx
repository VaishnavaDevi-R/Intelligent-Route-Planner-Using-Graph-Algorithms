import { useState } from "react";

import API from "./services/api";
import RouteMap from "./components/RouteMap";

function App() {

  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [history, setHistory] = useState(
    JSON.parse(
      localStorage.getItem("routeHistory")
    ) || []
  );

  const searchRoute = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);
      setError("");

      const response = await API.get(
        "/route",
        {
          params: {
            source,
            destination
          }
        }
      );

      setResult(response.data);

      const newHistory = [
        {
          source,
          destination,
          date: new Date().toLocaleString()
        },
        ...history
      ].slice(0, 5);

      setHistory(newHistory);

      localStorage.setItem(
        "routeHistory",
        JSON.stringify(newHistory)
      );

    } catch (error) {

      console.error(error);

      setError(
        "Unable to find route. Please check the locations and try again."
      );

      setResult(null);


    } finally {

      setLoading(false);

    }

  };

  const averageSpeed =
    result && result.eta_minutes > 0
      ? (
          result.distance_km /
          (result.eta_minutes / 60)
        ).toFixed(1)
      : 0;

  return (

    <div className="min-h-screen bg-slate-100">

      {/* Header */}

      <div className="bg-gradient-to-r from-blue-700 to-indigo-700 text-white py-8 shadow-lg">

        <div className="max-w-6xl mx-auto px-6">

          <h1 className="text-4xl font-bold">
            Intelligent Route Planner Using Graph Algorithms
          </h1>

          <p className="mt-2 text-blue-100">
            Real-Time Route Optimization Using
            Graph Algorithms, FastAPI,
            React and OpenStreetMap.
          </p>

        </div>

      </div>

      {/* Main Content */}

      <div className="max-w-6xl mx-auto px-6 py-10">

        {/* Search Form */}

        <form
          onSubmit={searchRoute}
          className="bg-white rounded-2xl shadow-lg p-6"
        >

          <div className="grid md:grid-cols-2 gap-4">

            <input
              type="text"
              placeholder="Enter Source Location"
              value={source}
              onChange={(e) =>
                setSource(e.target.value)
              }
              className="border rounded-lg p-3 w-full"
              required
            />

            <input
              type="text"
              placeholder="Enter Destination Location"
              value={destination}
              onChange={(e) =>
                setDestination(e.target.value)
              }
              className="border rounded-lg p-3 w-full"
              required
            />

          </div>

          <button
            type="submit"
            className="mt-5 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold"
          >

            {
              loading
                ? "Finding Best Route..."
                : "Find Route"
            }

          </button>

        </form>

        {/* Route History */}

        <div className="bg-white rounded-xl shadow-md p-6 mt-6">

          <h2 className="text-xl font-bold mb-4">
            Recent Searches
          </h2>

          {
            history.length === 0
              ? (
                <p className="text-gray-500">
                  No recent searches
                </p>
              )
              : (
                history.map(
                  (item, index) => (

                    <div
                      key={index}
                      className="border-b py-3 cursor-pointer hover:bg-gray-50 px-2 rounded"
                      onClick={() => {

                        setSource(
                          item.source
                        );

                        setDestination(
                          item.destination
                        );

                      }}
                    >

                      <p className="font-medium">
                        {item.source}
                      </p>

                      <p className="text-sm text-gray-500">
                        → {item.destination}
                      </p>

                      <p className="text-xs text-gray-400">
                        {item.date}
                      </p>

                    </div>

                  )
                )
              )
          }

        </div>

       {
         error && (
           <div className="mt-6 bg-red-100 border border-red-300 text-red-700 p-4 rounded-xl">
              {error}
            </div>
          )
        }

        {result && (

          <div className="mt-8">

            {/* Statistics Cards */}

            <div className="grid md:grid-cols-4 gap-4">

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500 text-sm">
                  Distance
                </h3>

                <p className="text-3xl font-bold text-blue-600">
                  {result.distance_km} km
                </p>

              </div>

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500 text-sm">
                  ETA
                </h3>

                <p className="text-3xl font-bold text-green-600">
                  {result.eta_minutes} min
                </p>

              </div>

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500 text-sm">
                  Traffic ETA
                </h3>

                <p className="text-3xl font-bold text-orange-500">
                  {result.traffic_eta_minutes} min
                </p>

              </div>

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500 text-sm">
                  Fuel Cost
                </h3>

                <p className="text-3xl font-bold text-red-500">
                  ₹{result.fuel_cost}
                </p>

              </div>

            </div>

            {/* Route Summary */}

            <div className="bg-white rounded-xl shadow-md p-6 mt-6">

              <h2 className="text-2xl font-bold mb-4">
                Route Summary
              </h2>

              <p>
                <strong>Source:</strong> {result.source}
              </p>

              <p className="mt-2">
                <strong>Destination:</strong> {result.destination}
              </p>

              <p className="mt-2">
                <strong>Path Nodes:</strong> {result.path_nodes}
              </p>

            </div>

            {/* Route Analytics */}

            <div className="grid md:grid-cols-3 gap-4 mt-6">

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500">
                  Average Speed
                </h3>

                <p className="text-2xl font-bold text-indigo-600">
                  {averageSpeed} km/h
                </p>

              </div>

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500">
                  Traffic Status
                </h3>

                <p className="text-2xl font-bold text-orange-500">
                  Medium
                </p>

              </div>

              <div className="bg-white rounded-xl shadow-md p-5">

                <h3 className="text-gray-500">
                  Route Efficiency
                </h3>

                <p className="text-2xl font-bold text-green-600">
                  94%
                </p>

              </div>

            </div>

            {/* Route Map */}

            <RouteMap
              coordinates={
                result.route_coordinates
              }
            />

          </div>

        )}

      </div>

    </div>

  );
}

export default App;