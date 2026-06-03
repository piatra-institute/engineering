# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""Fit the Hill equation to oxygen-saturation curves for haemoglobin
and myoglobin, returning the Hill coefficient and P50 for each.

Reads ../data/hemoglobin_oxygen_binding.csv.

Engineering reading: the Hill coefficient n parametrises cooperativity
empirically. n approx 1 corresponds to non-cooperative binding (myoglobin);
n approx 2.7 to 3.0 corresponds to the strongly cooperative tetramer of
haemoglobin. The mechanistic MWC and KNF models give n a physical
interpretation in terms of conformational equilibria.
"""

from __future__ import annotations

import csv
import pathlib

import numpy as np
from scipy.optimize import curve_fit


HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "hemoglobin_oxygen_binding.csv"


def hill(po2: np.ndarray, p50: float, n: float) -> np.ndarray:
    return po2**n / (p50**n + po2**n)


def load(path: pathlib.Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    po2_list: list[float] = []
    hb_list: list[float] = []
    mb_list: list[float] = []
    with path.open() as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            po2_list.append(float(row["po2_mmHg"]))
            hb_list.append(float(row["saturation_Hb"]))
            mb_list.append(float(row["saturation_Mb"]))
    return np.asarray(po2_list), np.asarray(hb_list), np.asarray(mb_list)


def fit(po2: np.ndarray, theta: np.ndarray) -> tuple[float, float]:
    popt, _ = curve_fit(hill, po2, theta, p0=(20.0, 2.0), bounds=(0, np.inf))
    return float(popt[0]), float(popt[1])


def main() -> None:
    po2, hb, mb = load(DATA)
    p50_hb, n_hb = fit(po2, hb)
    p50_mb, n_mb = fit(po2, mb)

    print("Hill fit:")
    print(f"  Haemoglobin:  P50 = {p50_hb:5.2f} mmHg, n = {n_hb:4.2f}")
    print(f"  Myoglobin:    P50 = {p50_mb:5.2f} mmHg, n = {n_mb:4.2f}")
    print()
    print("Lungs at 100 mmHg, tissues at 26 mmHg:")
    delta_hb = hill(np.array([100.0]), p50_hb, n_hb)[0] - hill(
        np.array([26.0]), p50_hb, n_hb
    )[0]
    delta_mb = hill(np.array([100.0]), p50_mb, n_mb)[0] - hill(
        np.array([26.0]), p50_mb, n_mb
    )[0]
    print(f"  Hb releases  {100 * delta_hb:4.1f}% of bound O2 between lung and tissue.")
    print(f"  Mb releases  {100 * delta_mb:4.1f}% of bound O2 between lung and tissue.")
    print()
    print(
        "The cooperative Hb releases an order of magnitude more bound oxygen"
        " across the lung-to-tissue PO2 range than the non-cooperative Mb."
    )


if __name__ == "__main__":
    main()
