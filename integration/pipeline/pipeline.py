import json
from pathlib import Path

sample_data = {
    "ticker": "AAPL",
    "price": 185.22,
    "trader_email": "john@broker.test",
    "operator_name": "John Smith"
}

export_path = Path("integration/pipeline/export.json")

with export_path.open("w", encoding="utf-8") as f:
    json.dump(sample_data, f, indent=2)

print("Export created.")