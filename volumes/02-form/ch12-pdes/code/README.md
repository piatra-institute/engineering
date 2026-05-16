# Volume II Chapter 12: PDEs, supporting code

Three reference implementations for the chapter's worked examples
and project. Written for the project's working environment
(Python 3, NumPy, SciPy, matplotlib). Each script is self-contained
and runnable directly (`python3 <name>.py`); each writes a CSV
under `../data/` and a PNG plot beside it.

| Script                       | Purpose                                                     | Output                                            |
| ---------------------------- | ----------------------------------------------------------- | ------------------------------------------------- |
| `heat_ftcs.py`               | FTCS explicit solver for the 1D heat equation               | `../data/heat_ftcs.csv`, `../data/heat_ftcs.png`  |
| `wave_explicit.py`           | Centred-time-centred-space solver for the 1D wave equation  | `../data/wave_pulse.csv`, `../data/wave_pulse.png` |
| `laplace_jacobi.py`          | Jacobi relaxation for Laplace's equation on the unit square | `../data/laplace_jacobi.csv`, `../data/laplace.png`|

The scripts implement exactly what the chapter's project block
asks the reader to write. They are not packaged as a library; each
file fits in a screen and is meant to be read alongside the
chapter prose.

## Reproducibility

Random number generation is not used. The numerical output is
fully determined by the grid choices, the boundary data, and the
floating-point arithmetic of the host machine. A reasonable
NumPy build (1.20 or later) produces bitwise-identical CSVs on
x86_64 and arm64.

## Half-life

Working code at this depth is durable across NumPy and SciPy
major versions on a decade scale. The CSV outputs are committed
under `../data/` so the chapter's tables and figures do not depend
on the reader re-running the scripts.
