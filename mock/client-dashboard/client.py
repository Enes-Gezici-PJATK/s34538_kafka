import requests
from sseclient import SSEClient

url = "http://127.0.0.1:8000/api/stream?ticker=AAPL"

messages = SSEClient(url)

print("Listening for stock updates...")

for msg in messages:
    print(msg.dat)