# Code for Chapter 8: Beams, columns, frames

Standalone Python scripts supporting the worked examples, figures, and
exercises. Each script writes its CSV output into the sibling `data/`
folder (paths are relative, so run each from inside this `code/` folder).

| script | what it does |
| --- | --- |
| `shear_moment.py` | shear and bending-moment diagrams for a simple beam under mixed point and line loads; writes `data/shear_moment_profile.csv` |
| `beam_deflection.py` | finite-difference solver for the Euler-Bernoulli equation; verifies the midspan deflection against `5 w0 L^4 / 384 EI`; writes `data/deflection_profile.csv` |
| `euler_buckling.py` | Euler critical loads for the four end conditions and the column strength curve; writes `data/column_strength_curve.csv` |
| `frame_stiffness.py` | direct (matrix) stiffness method for a 2D frame member; checks a propped-cantilever rotation against closed form |
| `section_properties.py` | second moment of area, section modulus, area, radius of gyration for rectangular, circular, hollow, and built-up I sections |

Dependencies: `numpy` only. Run with `python <script>.py`.
