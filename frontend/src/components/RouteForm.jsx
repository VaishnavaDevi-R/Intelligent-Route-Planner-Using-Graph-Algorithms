import { useState } from "react";

export default function RouteForm({ onSearch }) {

  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    onSearch(
      source,
      destination
    );
  };

  return (
    <form onSubmit={handleSubmit}>

      <input
        type="text"
        placeholder="Enter Source"
        value={source}
        onChange={(e) =>
          setSource(e.target.value)
        }
      />

      <input
        type="text"
        placeholder="Enter Destination"
        value={destination}
        onChange={(e) =>
          setDestination(e.target.value)
        }
      />

      <button type="submit">
        Find Route
      </button>

    </form>
  );
}