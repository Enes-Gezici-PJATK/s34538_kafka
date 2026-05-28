Write-Host "Starting mock server..."
Start-Process powershell -ArgumentList "python -m uvicorn mock.server.server:app --reload"

Start-Sleep -Seconds 5

Write-Host "Running tests..."
python -m pytest integration/tests