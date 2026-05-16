# Data assets — Volume I, Chapter 6 (Time, frequency, signals)

Reference data for chapter exercises and the project. Numbers are
order-of-magnitude or representative values, suitable for
estimation and exercise work; production calculations should
substitute the relevant primary source.

## Files

| File | Source | Used by |
|---|---|---|
| `clock_families.csv` | Editor's reference table for representative fractional accuracy, drift per day, size class, and indicative price class (current as of 2026) for each clock family in Section 6.2. Values are typical bands; specific manufacturer datasheets carry the binding numbers. | Section 6.2, Table 6.1, and `code/clock_comparison.py`. |
| `leap_seconds.csv` | The history of leap-second insertions, from the 1972 start of the leap-second mechanism through the most recent insertion at the end of December 2016. UTC-TAI offset after each insertion is recorded. Source: BIPM Circular T and IERS Bulletin C; verified against `web:nist-leap-seconds`. Current as of 2026. | Section 6.1 (TAI, UTC, leap seconds) and Calculation / Estimation exercises that ask the reader to reconstruct UTC-TAI or count leap seconds. |
| `sample_rates.csv` | Representative sample rates, Nyquist frequencies, and typical signal bandwidths for the application classes a reader will encounter (audio, video, industrial control, power-grid PMU, GPS C/A). Editor's compilation; specific systems vary. | Section 6.4 (Sampling and aliasing) and Design exercises on recording-chain selection. |

## Provenance

The leap-second table is verifiable against the IERS Bulletin C
record and `web:nist-leap-seconds`. The clock-family table reflects
the bands stated in Table 6.1 of the chapter and the public
materials cited at `web:nist-cesium-fountain` and
`web:nist-optical-clock`. The sample-rates table is a working
compilation; the GPS C/A row is included as an example of a code
rate, not a sampled-record rate.
