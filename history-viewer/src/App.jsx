import { useEffect, useState } from "react";

const API_KEY = import.meta.env.VITE_API_KEY;
const BASE = import.meta.env.VITE_BASE_URL;

export default function App() {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("ACME");

  useEffect(() => {
    const es = new EventSource(
      `${BASE}/api/stream?ticker=${ticker}&api_key=${API_KEY}`
    );

    es.addEventListener("tick", (event) => {
      const tick = JSON.parse(event.data);

      setData((prev) => [...prev.slice(-99), tick]);
    });

    return () => es.close();
  }, [ticker]);

  const downloadJSON = () => {
    const blob = new Blob(
      [JSON.stringify(data, null, 2)],
      { type: "application/json" }
    );

    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "history.json";
    a.click();
  };

  const downloadCSV = () => {
    const header = "ticker,price,timestamp,volume";

    const rows = data.map(
      (d) =>
        `${d.ticker},${d.price},${d.ts},${d.volume}`
    );

    const csv = [header, ...rows].join("\n");

    const blob = new Blob([csv], {
      type: "text/csv",
    });

    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "history.csv";
    a.click();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>History Viewer</h1>

      <select
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      >
        <option>ACME</option>
        <option>ALFA</option>
        <option>BETA</option>
        <option>GAME</option>
      </select>

      <button onClick={downloadJSON}>
        Download JSON
      </button>

      <button onClick={downloadCSV}>
        Download CSV
      </button>

      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Price</th>
            <th>Timestamp</th>
            <th>Volume</th>
          </tr>
        </thead>

        <tbody>
          {data.map((d, idx) => (
            <tr key={idx}>
              <td>{d.ticker}</td>
              <td>{d.price}</td>
              <td>{d.ts}</td>
              <td>{d.volume}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

