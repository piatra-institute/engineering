# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Johnson (Nyquist) noise voltage of a resistor over a measurement
bandwidth, evaluated at room temperature.

    v_n = sqrt(4 k_B T R Delta f)

This is the irreducible thermal-noise floor of any resistive sensor
element; the engineer reports it alongside the ADC LSB, the amplifier
input-noise spec, and the reference-resistor tolerance.

Companion to Estimation exercise 3.
"""

from __future__ import annotations

import math

K_B = 1.380_649e-23  # J/K (CODATA)
T_K = 295.15  # 22 C, typical room
RESISTANCES = (1.0e3, 10.0e3, 100.0e3, 1.0e6)
BANDWIDTHS = (1.0, 10.0, 1_000.0, 1.0e6)


def v_johnson(r_ohm: float, df_hz: float, t_kelvin: float = T_K) -> float:
    return math.sqrt(4.0 * K_B * t_kelvin * r_ohm * df_hz)


def main() -> None:
    print(f"Johnson noise voltage (rms) at T = {T_K - 273.15:.1f} C\n")
    header = "R (Ohm)".rjust(12)
    for df in BANDWIDTHS:
        header += f"  df={df:>6g} Hz".rjust(14)
    print(header)
    for r in RESISTANCES:
        row = f"{r:>12.0f}"
        for df in BANDWIDTHS:
            v = v_johnson(r, df)
            # report in nV or microV depending on size
            if v < 1e-6:
                row += f"  {v*1e9:>9.3f} nV  "
            else:
                row += f"  {v*1e6:>9.3f} uV  "
        print(row)


if __name__ == "__main__":
    main()
