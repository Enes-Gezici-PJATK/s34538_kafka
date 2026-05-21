@'
# Consolidation Notes

This repository consolidates the Phase 2 additional assignments for student s34538.

## Merged repositories

AA1 Local Data Anonymizer was moved from `s34538_anonymize` into this repository under `anonymizer/`.

AA2 stock applications remain in their original folders:

- `realtime-dashboard/`
- `history-viewer/`

The `history-viewer` folder name was kept from the original AA2 submission. It is the historical stock viewer/downloader application for Phase 2.

## Final repository

The final Phase 2 repository is `s34538_kafka`.

The final work is on the `main` branch.

## Security

No real API keys, passwords, `.env` files, tokens, or cloud credentials are committed.

API keys must be provided through environment variables.
'@ | Set-Content -Encoding UTF8 .\consolidation\CONSOLIDATION.md