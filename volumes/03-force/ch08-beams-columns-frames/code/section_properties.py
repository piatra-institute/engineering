"""Section properties for common beam cross-sections.

Computes the second moment of area I, the section modulus S, the area
A, and the radius of gyration r for rectangular, circular, hollow
circular, and built-up I sections. These are the geometric quantities
that turn a bending moment into a stress and a slenderness into a
buckling load.

Run:
    python section_properties.py
"""

from __future__ import annotations

import math


def rectangle(b, h):
    A = b * h
    I = b * h**3 / 12
    S = I / (h / 2)
    r = math.sqrt(I / A)
    return A, I, S, r


def solid_circle(d):
    A = math.pi * d**2 / 4
    I = math.pi * d**4 / 64
    S = I / (d / 2)
    r = math.sqrt(I / A)
    return A, I, S, r


def hollow_circle(do, di):
    A = math.pi * (do**2 - di**2) / 4
    I = math.pi * (do**4 - di**4) / 64
    S = I / (do / 2)
    r = math.sqrt(I / A)
    return A, I, S, r


def i_section(bf, tf, hw, tw):
    """Symmetric I: flange bf x tf (two), web hw x tw."""
    H = hw + 2 * tf
    A = 2 * bf * tf + hw * tw
    # I about centroid (mid-height) = web + two flanges (parallel axis)
    I_web = tw * hw**3 / 12
    d = (hw + tf) / 2
    I_fl = 2 * (bf * tf**3 / 12 + bf * tf * d**2)
    I = I_web + I_fl
    S = I / (H / 2)
    r = math.sqrt(I / A)
    return A, I, S, r


def show(name, A, I, S, r):
    print(f"{name:>22s}: A={A*1e4:8.2f} cm^2  I={I*1e8:10.2f} cm^4  "
          f"S={S*1e6:9.2f} cm^3  r={r*1e3:7.2f} mm")


def main():
    show("rect 100x200", *rectangle(0.100, 0.200))
    show("rect 50x400 (deep)", *rectangle(0.050, 0.400))
    show("solid circle d=100", *solid_circle(0.100))
    show("pipe 100/92", *hollow_circle(0.100, 0.092))
    show("I 150x10 flange, 280x8 web", *i_section(0.150, 0.010, 0.280, 0.008))


if __name__ == "__main__":
    main()
