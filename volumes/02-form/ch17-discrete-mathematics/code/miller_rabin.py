# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Miller-Rabin probabilistic primality test.

Reference: Rabin, 'Probabilistic algorithm for testing primality,'
J. Number Theory 12, 1980. The implementation is the standard form
described in section 17.7; for n above 3,317,044,064,679,887,385,961,981
the deterministic witness set used here (the first 13 primes) is
known to give a correct answer (Sorenson and Webster, 2017), so the
test is deterministic in the working range below that bound.

Run: uv run code/miller_rabin.py
"""

from __future__ import annotations

import time

_WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)


def _miller_check(n: int, a: int, d: int, r: int) -> bool:
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _WITNESSES:
        if a >= n:
            continue
        if not _miller_check(n, a, d, r):
            return False
    return True


def first_k_primes_above(threshold: int, k: int) -> list[int]:
    found: list[int] = []
    candidate = threshold + 1 if (threshold + 1) % 2 else threshold + 2
    while len(found) < k:
        if is_prime(candidate):
            found.append(candidate)
        candidate += 2
    return found


if __name__ == "__main__":
    threshold = 10**18
    target = 100
    t0 = time.time()
    primes = first_k_primes_above(threshold, target)
    elapsed = time.time() - t0
    print(f"first {target} primes above 10^18 (elapsed {elapsed:.2f} s)")
    print(f"smallest: {primes[0]}")
    print(f"largest:  {primes[-1]}")
    print(f"gap mean: {(primes[-1] - primes[0]) / (target - 1):.1f}")
