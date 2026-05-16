# Data assets — Volume I, Chapter 8 (Statistics for engineers)

## Files

| File | Purpose | Used by |
|---|---|---|
| `commute_minutes.csv` | The thirty-day commute series of section 8.1, in machine-readable form. Columns: `day`, `minutes`, `weekday`, `notes`. | Section 8.1 worked example; bootstrap, CI, prediction-interval, and Q-Q-plot exercises. |
| `wafer_defects.csv` | Twenty wafer defect counts including one out-of-distribution wafer (W017, 42 defects against a nominal Poisson mean of 30). Columns: `wafer_id`, `defect_count`, `inspector`, `date`, `lot`. | Section 8.3 engineering example; chi-square-equivalent and Poisson-mean exercises. |

## Conventions

- All values typed by hand from the chapter's worked examples; provenance is editorial.
- Dates are illustrative (the project is dated 2026); no claim is made that these data come from a specific physical experiment.
- `notes` columns record collection conditions that would otherwise be lost from the numerical record.

## Provenance

Editor's reference data, constructed to match the chapter's narrative. A reader running the chapter's project replaces these files with their own thirty-trial dataset.
