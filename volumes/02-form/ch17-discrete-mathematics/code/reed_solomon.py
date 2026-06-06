# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Reed-Solomon over GF(2^4) for the section 17.7 case study.

Builds the field GF(16) from the irreducible polynomial
p(x) = x^4 + x + 1, generates the log/antilog tables driven by the
primitive element alpha = x, encodes an RS(7, 3) codeword by polynomial
evaluation, then recovers the message from any k = 3 surviving symbols
by Lagrange interpolation over the field. The recovery from two
erasures is the worked correction in the chapter.

Run: uv run code/reed_solomon.py
"""

from __future__ import annotations

# --- Field GF(2^4) with modulus x^4 + x + 1 (bit pattern 0b10011). ---
PRIM_POLY = 0b10011  # x^4 + x + 1
FIELD_SIZE = 16

# antilog[j] = alpha^j as a 4-bit symbol; log[s] = exponent of symbol s.
antilog = [0] * (FIELD_SIZE - 1)
log = [0] * FIELD_SIZE
x = 1
for j in range(FIELD_SIZE - 1):
    antilog[j] = x
    log[x] = j
    x <<= 1
    if x & FIELD_SIZE:          # degree reached 4: reduce by the modulus
        x ^= PRIM_POLY
        x &= FIELD_SIZE - 1


def gf_add(a: int, b: int) -> int:
    """Field addition is bitwise exclusive-or (no carries)."""
    return a ^ b


def gf_mul(a: int, b: int) -> int:
    """Field multiplication via the log table: add exponents mod 15."""
    if a == 0 or b == 0:
        return 0
    return antilog[(log[a] + log[b]) % (FIELD_SIZE - 1)]


def gf_inv(a: int) -> int:
    """Multiplicative inverse: negate the exponent mod 15."""
    if a == 0:
        raise ZeroDivisionError("0 has no inverse in GF(16)")
    return antilog[(-log[a]) % (FIELD_SIZE - 1)]


def poly_eval(coeffs: list[int], point: int) -> int:
    """Horner evaluation of a polynomial (low degree first) at a point."""
    acc = 0
    for c in reversed(coeffs):
        acc = gf_add(gf_mul(acc, point), c)
    return acc


def rs_encode(message: list[int], n: int) -> list[int]:
    """Encode k message symbols into n codeword symbols by evaluation."""
    return [poly_eval(message, antilog[i]) for i in range(n)]


def lagrange_interpolate(points: list[int], values: list[int]) -> list[int]:
    """Recover polynomial coefficients (low degree first) from k samples."""
    k = len(points)
    coeffs = [0] * k
    for i in range(k):
        # Build the i-th Lagrange basis polynomial, scaled by values[i].
        basis = [1]
        denom = 1
        for j in range(k):
            if j == i:
                continue
            # multiply basis by (x - points[j]) = (x + points[j]) in GF(2^k)
            new = [0] * (len(basis) + 1)
            for d, c in enumerate(basis):
                new[d] = gf_add(new[d], gf_mul(c, points[j]))
                new[d + 1] = gf_add(new[d + 1], c)
            basis = new
            denom = gf_mul(denom, gf_add(points[i], points[j]))
        scale = gf_mul(values[i], gf_inv(denom))
        for d, c in enumerate(basis):
            coeffs[d] = gf_add(coeffs[d], gf_mul(c, scale))
    return coeffs


if __name__ == "__main__":
    # alpha^j table check: alpha^4 must be 0b0011 from x^4 = x + 1.
    assert antilog[4] == 0b0011, "field table wrong at alpha^4"
    assert gf_mul(antilog[7], antilog[11]) == antilog[3], "log-add mul wrong"

    # Worked message: m(x) = alpha^4 x^2 + alpha^0 x + alpha^1.
    message = [antilog[1], antilog[0], antilog[4]]  # coeffs low-degree first
    n, k = 7, 3
    codeword = rs_encode(message, n)
    print("codeword symbols:", codeword)
    assert codeword[0] == 0, "c0 should vanish for this message"

    # Two erasures at positions 2 and 4: recover from any 3 survivors.
    survivors = [0, 1, 3]  # use the values at alpha^0, alpha^1, alpha^3
    pts = [antilog[i] for i in survivors]
    vals = [codeword[i] for i in survivors]
    recovered = lagrange_interpolate(pts, vals)
    print("recovered coeffs:", recovered)
    assert recovered == message, "RS erasure recovery failed"
    print("Reed-Solomon recovered the message from two erasures.")
