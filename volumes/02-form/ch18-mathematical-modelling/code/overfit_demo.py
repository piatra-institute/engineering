"""Overfit demonstration: quadratic ground truth, degree-10 polynomial fit.

Generates 12 training points from y = (x/3)^2 + 0.5 + N(0, 0.1) on
x in [0, 9], fits both a quadratic and a degree-10 polynomial, then
evaluates both on 5 held-out points. The held-out residuals of the
degree-10 fit are typically more than 10x its training residuals,
which is the diagnostic signature of overfitting.

Dependencies: numpy.

Run:
    python overfit_demo.py
"""
from __future__ import annotations

import numpy as np

SEED = 0
N_TRAIN = 12
N_TEST = 5
SIGMA = 0.1


def ground_truth(x: np.ndarray) -> np.ndarray:
    return (x / 3.0) ** 2 + 0.5


def main() -> None:
    rng = np.random.default_rng(SEED)
    x_train = np.sort(rng.uniform(0.0, 9.0, N_TRAIN))
    y_train = ground_truth(x_train) + rng.normal(0.0, SIGMA, N_TRAIN)
    x_test = np.sort(rng.uniform(0.0, 9.0, N_TEST))
    y_test = ground_truth(x_test) + rng.normal(0.0, SIGMA, N_TEST)

    coef_q = np.polyfit(x_train, y_train, 2)
    coef_10 = np.polyfit(x_train, y_train, 10)

    y_train_q = np.polyval(coef_q, x_train)
    y_train_10 = np.polyval(coef_10, x_train)
    y_test_q = np.polyval(coef_q, x_test)
    y_test_10 = np.polyval(coef_10, x_test)

    def rms(r):
        return float(np.sqrt(np.mean(r ** 2)))

    rms_train_q = rms(y_train - y_train_q)
    rms_train_10 = rms(y_train - y_train_10)
    rms_test_q = rms(y_test - y_test_q)
    rms_test_10 = rms(y_test - y_test_10)

    print(f"Ground-truth noise level (sigma): {SIGMA:.3f}")
    print(f"\nFit: degree 2 (correct order)")
    print(f"  training RMS: {rms_train_q:.4f}")
    print(f"  held-out RMS: {rms_test_q:.4f}")
    print(f"  ratio: {rms_test_q / rms_train_q:.2f}")
    print(f"\nFit: degree 10 (overfit)")
    print(f"  training RMS: {rms_train_10:.4f}")
    print(f"  held-out RMS: {rms_test_10:.4f}")
    print(f"  ratio: {rms_test_10 / rms_train_10:.2f}")
    print(f"\nReading: the degree-10 model's training residuals are smaller than the noise,")
    print(f"because the polynomial has interpolated the noise itself. Its held-out residuals")
    print(f"are larger than the quadratic's by a factor that exposes the overfit.")


if __name__ == "__main__":
    main()
