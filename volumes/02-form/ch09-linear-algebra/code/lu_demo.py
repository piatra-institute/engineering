# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""LU factorisation by Doolittle elimination on the section 9.3 example.

Verifies L U = A and back-solves A x = b for b = (4, 10, 30).
"""

from __future__ import annotations

import numpy as np


def lu_doolittle(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = A.shape[0]
    L = np.eye(n)
    U = A.astype(float).copy()
    for j in range(n - 1):
        pivot = U[j, j]
        if abs(pivot) < 1e-14:
            raise ValueError(f"zero pivot at column {j}; partial pivoting required")
        for i in range(j + 1, n):
            m = U[i, j] / pivot
            L[i, j] = m
            U[i, j:] -= m * U[j, j:]
    return L, U


def forward_solve(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - L[i, :i] @ y[:i]
    return y


def back_solve(U: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x


def main() -> None:
    A = np.array([[2.0, 1.0, 1.0],
                  [4.0, 3.0, 3.0],
                  [8.0, 7.0, 9.0]])
    b = np.array([4.0, 10.0, 30.0])

    L, U = lu_doolittle(A)
    print("L =")
    print(L)
    print("U =")
    print(U)
    print("L U =")
    print(L @ U)
    print("max |L U - A| =", float(np.max(np.abs(L @ U - A))))

    y = forward_solve(L, b)
    x = back_solve(U, y)
    print("x =", x)
    print("A x =", A @ x, "vs b =", b)


if __name__ == "__main__":
    main()
