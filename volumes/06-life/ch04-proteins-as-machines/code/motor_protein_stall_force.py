# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Brownian-ratchet model for motor-protein force-velocity behaviour.

A processive motor steps forward against load F. We use the Howard 1996
linear approximation
    v(F) = v0 * (1 - F / F_stall)        for 0 <= F <= F_stall
augmented with the Bell-model exponential slow-down to capture the
near-stall regime:
    v(F) = v0 * exp(-F * delta / kBT)    for F approaching F_stall.

Engineering reading: the linear regime is a useful classroom
approximation; the Bell exponential captures the near-stall behaviour
observed in optical-trap single-molecule experiments. The model
explains the broad "force-velocity curve" measured for kinesin
(8 nm step, 7 pN stall) and myosin V (36 nm step, 3 pN stall).
"""

from __future__ import annotations

import math


KBT_pN_nm = 4.114  # k_B T at 310 K, in pN*nm


def linear_velocity(force_pN: float, v0_um_s: float, fstall_pN: float) -> float:
    if force_pN >= fstall_pN:
        return 0.0
    return v0_um_s * (1.0 - force_pN / fstall_pN)


def bell_velocity(force_pN: float, v0_um_s: float, delta_nm: float) -> float:
    return v0_um_s * math.exp(-force_pN * delta_nm / KBT_pN_nm)


def main() -> None:
    motors = [
        {"name": "kinesin-1", "v0": 0.80, "fstall": 7.0, "delta": 1.3},
        {"name": "myosin-V", "v0": 0.50, "fstall": 3.0, "delta": 2.4},
        {"name": "cytoplasmic_dynein", "v0": 0.50, "fstall": 1.1, "delta": 3.0},
    ]

    print(f"Force-velocity curves at 310 K (kBT = {KBT_pN_nm:.3f} pN*nm)")
    for motor in motors:
        print(f"\n{motor['name']}: v0 = {motor['v0']:.2f} um/s, "
              f"Fstall = {motor['fstall']:.1f} pN, delta = {motor['delta']:.1f} nm")
        print(f"  {'F (pN)':>7} {'v_linear (um/s)':>18} {'v_Bell (um/s)':>15}")
        for f in [0.0, 1.0, 2.0, 3.0, 5.0, 7.0]:
            v_lin = linear_velocity(f, motor["v0"], motor["fstall"])
            v_bell = bell_velocity(f, motor["v0"], motor["delta"])
            print(f"  {f:7.1f} {v_lin:18.3f} {v_bell:15.3f}")


if __name__ == "__main__":
    main()
