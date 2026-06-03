# Vol VI Ch 8 — Data assets

Datasets supporting the chapter and the project track.

## Files

- `pandemic_mortality.csv` — Historical influenza pandemics and major
  respiratory-pathogen outbreaks 1918--2023, with estimated global
  mortality and pathogen subtype. Sources: Johnson and Mueller 2002,
  Dawood et al.\ 2012, WHO excess-mortality estimate 2023.
- `covid_nz_first_wave.csv` — Synthetic daily case counts patterned
  on the New Zealand first wave (Feb--May 2020), suitable for the
  project-track SIR fit. The file is illustrative; production work
  should use Johns Hopkins CSSE archive or country-specific official
  sources.
- `resistance_prevalence.csv` — Antibiotic-resistance prevalence by
  drug class and year, in clinical isolates. Source: stylised
  composite of WHO Antimicrobial Resistance surveillance reports
  2014--2022 and Murray et al.\ 2022 *Lancet* AMR burden estimate.
- `iucn_redlist_categories.csv` — Category definitions and the
  approximate number of species in each category as of 2023, from
  IUCN Red List Version 2023-1.
- `boarding_school_flu_1978.csv` — Daily case counts from the
  classic 1978 UK boarding-school influenza outbreak
  (Communicable Disease Surveillance Centre, BMJ 1978). The
  textbook SIR teaching dataset.

## Notes

All CSVs use UTF-8, comma-separated, with a single header row.
Numeric values are integers or floats; no localised currency or
thousands separators. Date fields are ISO 8601 (YYYY-MM-DD).

`pandemic_mortality.csv` and `boarding_school_flu_1978.csv` are
canonical reference datasets; `covid_nz_first_wave.csv` is
illustrative and should be replaced with an authoritative source
for the project-track deliverable.
