from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json
import time

app = FastAPI()

with open("mock/fixtures/ticks.json", "r", encoding="utf-8") as f:
    TICKS = json.load(f)


@app.get("/api/tickers")
def get_tickers():
    return ["AAPL"]


@app.get("/api/latest")
def get_latest(ticker: str):
    return TICKS[0]


@app.get("/api/stream")
def stream(ticker: str):

    def event_stream():
        while True:
            data = json.dumps(TICKS[0])
            yield f"data: {data}\n\n"
            time.sleep(2)

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream"
    )