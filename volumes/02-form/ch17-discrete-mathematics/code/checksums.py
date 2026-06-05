# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Checksum and hashing arithmetic for section 17.7.

The Luhn check digit (credit-card and IMEI numbers), a modulus-11
check digit (ISBN-10), and a bit-wise CRC are all modular-arithmetic
error-detection schemes. The point of the chapter's number-theory
section is that these are not folklore: each detects a characterised
class of transcription error, and the modulus is chosen to do so.

Run: uv run code/checksums.py
"""

from __future__ import annotations


def luhn_is_valid(number: str) -> bool:
    """Validate a digit string by the Luhn (mod 10) algorithm."""
    digits = [int(c) for c in number if c.isdigit()]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def luhn_check_digit(payload: str) -> int:
    """Return the digit that makes payload + digit a valid Luhn number."""
    for d in range(10):
        if luhn_is_valid(payload + str(d)):
            return d
    raise AssertionError("unreachable: a valid digit always exists")


def isbn10_is_valid(code: str) -> bool:
    """Validate an ISBN-10 by its weighted mod-11 checksum."""
    chars = [c for c in code if c.isdigit() or c in "Xx"]
    if len(chars) != 10:
        return False
    total = 0
    for i, c in enumerate(chars):
        value = 10 if c in "Xx" else int(c)
        total += (10 - i) * value
    return total % 11 == 0


def crc8(data: bytes, poly: int = 0x07) -> int:
    """Compute an 8-bit CRC (polynomial division over GF(2))."""
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ poly) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return crc


if __name__ == "__main__":
    # A canonical Luhn test number (passes) and a single-digit error (fails).
    print(f"79927398713 valid (Luhn): {luhn_is_valid('79927398713')}")
    print(f"79927398710 valid (Luhn): {luhn_is_valid('79927398710')}")
    print(f"check digit for 7992739871: {luhn_check_digit('7992739871')}")

    # ISBN-10 of a classic discrete-math text (mod-11 catches more errors).
    print(f"0262033844 valid (ISBN-10): {isbn10_is_valid('0262033844')}")

    # A CRC-8 over a short message and a corrupted copy.
    msg = b"engineering"
    corrupt = b"enginaering"
    print(f"CRC-8('{msg.decode()}') = 0x{crc8(msg):02X}")
    print(f"CRC-8('{corrupt.decode()}') = 0x{crc8(corrupt):02X} (detects flip)")
