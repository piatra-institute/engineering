# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Working number-theory toolkit for section 17.7.

Extended Euclidean algorithm, modular inverse, the Chinese remainder
theorem, modular exponentiation, and a toy RSA round trip on small
primes. The toy RSA is for pedagogy only; a deployed system uses a
vetted library and primes of thousands of bits, per the recognition-
level discussion in the chapter.

Run: uv run code/number_theory.py
"""

from __future__ import annotations


def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, x, y) with a*x + b*y = g = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a: int, n: int) -> int:
    """Return a^{-1} mod n. Raise ValueError if gcd(a, n) != 1."""
    g, x, _ = ext_gcd(a % n, n)
    if g != 1:
        raise ValueError(f"{a} has no inverse mod {n}: gcd = {g}")
    return x % n


def crt(residues: list[int], moduli: list[int]) -> int:
    """Solve x = residues[i] (mod moduli[i]) for pairwise-coprime moduli."""
    total = 0
    prod = 1
    for m in moduli:
        prod *= m
    for r_i, m_i in zip(residues, moduli):
        p = prod // m_i
        total += r_i * mod_inverse(p, m_i) * p
    return total % prod


def toy_rsa_roundtrip(p: int, q: int, e: int, message: int) -> dict[str, int]:
    """Encrypt then decrypt a single integer message with toy RSA."""
    n = p * q
    phi = (p - 1) * (q - 1)
    if message >= n:
        raise ValueError("message must be smaller than n = p*q")
    d = mod_inverse(e, phi)
    cipher = pow(message, e, n)
    recovered = pow(cipher, d, n)
    return {"n": n, "phi": phi, "d": d, "cipher": cipher, "recovered": recovered}


if __name__ == "__main__":
    # Exercise 17.8: gcd(2024, 1547) and the Bezout coefficients.
    g, x, y = ext_gcd(2024, 1547)
    print(f"gcd(2024, 1547) = {g}; 2024*{x} + 1547*{y} = {2024 * x + 1547 * y}")

    # Modular inverse used by RSA key generation.
    print(f"inverse of 7 mod 40 = {mod_inverse(7, 40)}")

    # CRT: smallest x with x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7).
    x = crt([2, 3, 2], [3, 5, 7])
    print(f"CRT solution = {x}  (Sun-tzu's classical problem)")

    # Toy RSA on primes 61 and 53 with public exponent 17.
    result = toy_rsa_roundtrip(p=61, q=53, e=17, message=65)
    print(
        f"RSA toy: n={result['n']} d={result['d']} "
        f"cipher={result['cipher']} recovered={result['recovered']}"
    )
    assert result["recovered"] == 65, "RSA round trip failed"
    print("RSA round trip recovered the message.")
