# 📈 Kafka Real-Time Stock Dashboard (React + Vite)

This project is a real-time stock data dashboard built with React + Vite. It consumes live stock data via SSE and REST API for 50 fictional companies.

## 🔑 API Setup

API key from:
https://add.piotrkojalowicz.dev/

Required header:
X-API-Key: YOUR_KEY

or query param:
?api_key=YOUR_KEY

---

## 📡 API Endpoints

- GET /api/tickers → list all tickers  
- GET /api/latest?ticker=ACME → latest price  
- GET /api/stream?ticker=ACME → live SSE stream  

---

## 📊 App 1 — Realtime Dashboard (React + Vite)

Built with React + Vite using EventSource (SSE).

Features:
- Live stock price updates
- Multiple ticker selection
- Price + timestamp display
- Small live history

Run:
cd realtime-dashboard
npm install
npm run dev

Env:
VITE_API_KEY=your_key

---

## 📈 App 2 — History Viewer (React + Vite)

Fetches and displays historical stock data.

Features:
- Select tickers + time range
- Fetch latest or polling updates
- Table / chart view
- Export CSV / JSON

Run:
cd history-viewer
npm install
npm run dev

---

## 💾 Notes

- Data stored ~10 minutes only
- Rate limit: 1 request / 10s after free tier
- API key excluded via .gitignore

---

## 🧠 Tech Stack

React + Vite • SSE • REST API • JavaScript

---

## 👤 Author

s34538
