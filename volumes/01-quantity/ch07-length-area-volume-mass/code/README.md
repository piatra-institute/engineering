# Code assets — Volume I, Chapter 7 (Length, area, volume, mass)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `gauge_block_stack.py` | Combined standard uncertainty of a stack of wrung gauge blocks (calibration and wringing components). | Section 7.1 worked example; Calculation exercise on length-standard build-up. |
| `displacement_volume.py` | Combined Type A (repeatability) and Type B (resolution) uncertainty on a water-displacement volume reading. | Section 7.5 worked example; Calculation exercise on graduated-cylinder uncertainty. |
| `density_propagation.py` | Density rho = m / V propagated by both the product-of-powers rule and Monte Carlo; alloy identification table. | Section 7.2 worked example; Calculation and Diagnosis exercises on metal-sample identification. |
| `ellipsoid_volume_mc.py` | Monte Carlo distribution of a triaxial-ellipsoid volume; comparison to the linear-propagation result. | Simulation exercise on ellipsoid Monte Carlo. |

## Conventions

- Random-number generator seeded per script for reproducibility.
- Sample counts are at the low end of practical Monte Carlo
  ($10^{4}$ to $2 \times 10^{5}$); production work would increase
  by an order of magnitude.
- Output is human-readable text on stdout, not files.
- All scripts use `uv run`-compatible PEP 723 inline metadata.

## Provenance

Editors' reference implementations. The illustrative numerical
inputs (gauge-block calibration uncertainty, graduated-cylinder
graduation interval, sample mass and volume readings, ellipsoid
semi-axes) are documented at the top of each script and should be
replaced by the reader's own values for working a real measurement.
