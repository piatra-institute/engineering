# Data assets — Volume I, Chapter 9 (The discipline of estimation)

Each file is a small reference table. CSV format; first row is the header.

## Files

| File | Purpose | Source |
|---|---|---|
| `anchor_points.csv` | Order-of-magnitude anchor points for masses, lengths, times, energies, and powers. Used as the reader's reference for internal-ruler benchmarks. | Editorial compilation from primary references. |
| `chicago_piano_factors.csv` | Per-factor low / nominal / high inputs for the canonical Chicago piano-tuner Fermi problem. | Reproduces `code/piano_tuners.py`. |
| `fermi50_ground_truth.csv` | Selected reference values for the fifty Fermi problems in section 9.9, where a defensible source exists. Used after the reader has recorded their own estimates. | Citation noted per row. |

## Conventions

- Numerical columns use SI base units unless otherwise noted in the header.
- The `year` column gives the dated reference year for time-varying quantities.
- `nan` (or empty) marks a value not applicable; for example, deep-uncertainty Fermi problems where no defensible point ground truth exists.

## Provenance

Editorial compilation. Verify all entries against the cited sources before use in any reportable analysis.
