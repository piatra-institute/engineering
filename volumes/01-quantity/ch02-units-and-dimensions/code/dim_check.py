"""
Symbolic dimensional-consistency checker.

Each engineering quantity is represented by a tuple of base-dimension
exponents (M, L, T, I, Theta, N, J). The checker takes an expression
in such quantities and returns the resulting dimensional signature,
or flags an inconsistency when a sum of terms with different
signatures is attempted.

Supports Volume I, Chapter 2, Diagnosis exercises on incorrect-
equation detection.

Dependencies:
  standard library only.

Usage:
  python dim_check.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Dim:
    """A dimensional signature in the seven SI base dimensions."""
    M: float = 0.0
    L: float = 0.0
    T: float = 0.0
    I: float = 0.0
    Theta: float = 0.0
    N: float = 0.0
    J: float = 0.0

    def __mul__(self, other: "Dim") -> "Dim":
        return Dim(self.M + other.M, self.L + other.L, self.T + other.T,
                  self.I + other.I, self.Theta + other.Theta,
                  self.N + other.N, self.J + other.J)

    def __truediv__(self, other: "Dim") -> "Dim":
        return Dim(self.M - other.M, self.L - other.L, self.T - other.T,
                  self.I - other.I, self.Theta - other.Theta,
                  self.N - other.N, self.J - other.J)

    def __pow__(self, p: float) -> "Dim":
        return Dim(self.M * p, self.L * p, self.T * p,
                  self.I * p, self.Theta * p, self.N * p, self.J * p)

    def __str__(self) -> str:
        parts = []
        for name, val in [("M", self.M), ("L", self.L), ("T", self.T),
                          ("I", self.I), ("Theta", self.Theta),
                          ("N", self.N), ("J", self.J)]:
            if val != 0:
                parts.append(f"[{name}]^{val:g}" if val != 1
                             else f"[{name}]")
        return " ".join(parts) if parts else "[dimensionless]"


# Common quantities
M_ = Dim(M=1)
L_ = Dim(L=1)
T_ = Dim(T=1)

length = L_
mass = M_
time = T_
velocity = L_ / T_
acceleration = velocity / T_
force = mass * acceleration       # M L T^-2
energy = force * length            # M L^2 T^-2
power = energy / T_                # M L^2 T^-3
pressure = force / (L_ ** 2)       # M L^-1 T^-2
density = mass / (L_ ** 3)         # M L^-3
viscosity = pressure * time        # M L^-1 T^-1


def check_sum(*terms: Dim) -> None:
    """Verify that all terms in a sum have the same dimensional
    signature; raise ValueError otherwise."""
    first = terms[0]
    for i, t in enumerate(terms[1:], start=1):
        if t != first:
            raise ValueError(
                f"dimensional mismatch in sum: term[0]={first}, "
                f"term[{i}]={t}")


def main() -> None:
    print("Examples:")
    print(f"  force         = {force}")
    print(f"  energy        = {energy}")
    print(f"  pressure      = {pressure}")
    print(f"  power         = {power}")
    print(f"  Reynolds (Re) = {density * velocity * length / viscosity}")

    # Verify F = ma:
    print()
    print("Check F = ma:")
    check_sum(force, mass * acceleration)
    print(f"  PASS: both sides are {force}")

    # Verify the bad equation sigma = F^2 L / (A E):
    print()
    print("Check sigma = F^2 L / (A E):")
    sigma_correct = force / (L_ ** 2)
    area = L_ ** 2
    modulus = pressure
    bad_rhs = (force ** 2) * length / (area * modulus)
    print(f"  LHS (stress) = {sigma_correct}")
    print(f"  RHS          = {bad_rhs}")
    try:
        check_sum(sigma_correct, bad_rhs)
    except ValueError as e:
        print(f"  FAIL: {e}")


if __name__ == "__main__":
    main()
