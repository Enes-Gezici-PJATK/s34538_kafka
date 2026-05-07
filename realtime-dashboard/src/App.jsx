import { useEffect, useState } from "react";

const API_KEY = import.meta.env.VITE_API_KEY;
const BASE = import.meta.env.VITE_BASE_URL;

export default function App() {
  const [status, setStatus] = useState("connecting...");
  const [rows, setRows] = useState([]);

  useEffect(() => {
    console.log("API KEY:", API_KEY);
    console.log("BASE:", BASE);

    if (!API_KEY || !BASE) {
      setStatus("ENV ERROR (check .env file)");
      return;
    }

    const url = `${BASE}/api/stream?ticker=ACME&api_key=${encodeURIComponent(
      API_KEY
    )}`;

    console.log("Connecting to SSE:", url);

    const es = new EventSource(url);

    es.onopen = () => {
      console.log("SSE CONNECTED");
      setStatus("connected");
    };

    // IMPORTANT: use onmessage (most reliable)
    es.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        console.log("RECEIVED:", data);

        setRows((prev) => [data, ...prev].slice(0, 30));
      } catch (err) {
        console.error("Parse error:", err);
      }
    };

    es.onerror = (err) => {
      console.error("SSE ERROR:", err);
      setStatus("error (check console/network)");
    };

    return () => {
      es.close();
    };
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Realtime Stock Dashboard</h1>

      <p>
        Status: <b>{status}</b>
      </p>

      <p>
        API: {API_KEY ? "loaded ✅" : "missing ❌"}
      </p>

      <table border="1" cellPadding="6">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Price</th>
            <th>Timestamp</th>
            <th>Volume</th>
          </tr>
        </thead>

        <tbody>
          {rows.map((r, i) => (
            <tr key={i}>
              <td>{r.ticker}</td>
              <td>{r.price}</td>
              <td>{r.ts}</td>
              <td>{r.volume}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}