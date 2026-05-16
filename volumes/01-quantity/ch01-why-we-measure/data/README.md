# Data assets — Volume I, Chapter 1 (Why we measure)

Reference datasets supporting the chapter's exercises and worked examples.

## Files

| File | Source | Year | Used by |
|---|---|---|---|
| `coin_masses.csv` | US Mint, Royal Mint UK, European Central Bank | 2024 | Design exercise (kitchen-scale verification); `code/calibration_check.py` example. |
| `cement_production_usgs.csv` | USGS Mineral Commodity Summaries | 2010-2023 | Estimation exercise (cement flow rate); the estimation block on cement production. |
| `example_calibration_log.jsonl` | Editor's reference logbook (illustrative; not a real measurement series). | 2026 | Project (Instrument the home); model of the seven-component measurement habit. |

## Provenance

Each row carries the date the value was retrieved and the canonical
source. Values are quoted to the precision of the source. Where a
source updates annually (USGS Mineral Commodity Summaries), the file
notes the cycle and the reader is encouraged to refresh.

## Use

Files are CSV (UTF-8, RFC 4180) or JSON Lines (one JSON object per
line). The chapter's exercises and the code in `code/` reference
specific files; the reader can substitute their own data while
preserving the file structure.
