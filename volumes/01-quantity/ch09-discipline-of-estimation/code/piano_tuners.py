# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Reference Fermi-decomposition calculator for the Chicago piano-tuner problem.

Reproduces the canonical Fermi estimate with explicit low/nominal/high ranges
for each factor; reports a product range and identifies the dominant
uncertainty contributor by ratio of log-widths.

Ground truth, per BLS OEWS May 2023 for the Chicago-Naperville-Elgin
metropolitan area, occupation code 49-9063 (musical instrument repairers
and tuners): approximately 350 workers, RSE 24.6 percent.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Factor:
    name: str
    low: float
    nominal: float
    high: float

    def log_width(self) -> float:
        return math.log(self.high / self.low)


FACTORS = [
    Factor("Metro population", 8.0e6, 9.0e6, 1.0e7),
    Factor("Pianos per person", 1 / 200, 1 / 100, 1 / 50),
    Factor("Tunings per piano-year", 0.5, 1.0, 2.0),
    Factor("Tuner annual throughput (tunings/yr)", 500, 750, 1000),
]


def main() -> None:
    low = 1.0
    nom = 1.0
    high = 1.0
    for i, f in enumerate(FACTORS):
        op = "/" if i == 3 else "*"
        if op == "*":
            low *= f.low
            nom *= f.nominal
            high *= f.high
        else:
            low /= f.high
            nom /= f.nominal
            high /= f.low
    print(f"{'factor':<40} {'low':>10} {'nominal':>10} {'high':>10} {'log width':>10}")
    for f in FACTORS:
        print(f"{f.name:<40} {f.low:>10.3g} {f.nominal:>10.3g} {f.high:>10.3g} {f.log_width():>10.2f}")
    print()
    print(f"Estimate range: {low:.0f} to {high:.0f} (nominal {nom:.0f})")
    print(f"BLS OEWS 2023 ground truth: 350 (RSE 24.6 percent)")
    print(f"Ratio of nominal estimate to truth: {nom / 350:.2f}")
    # Identify dominant contributor by log width
    widths = [f.log_width() for f in FACTORS]
    dom = max(range(len(widths)), key=lambda i: widths[i])
    print(f"Dominant uncertainty factor: {FACTORS[dom].name} (log width {widths[dom]:.2f})")


if __name__ == "__main__":
    main()
