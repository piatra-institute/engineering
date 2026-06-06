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


def crc_remainder(message_bits: str, generator_bits: str) -> str:
    """Polynomial CRC remainder of a bit string over GF(2).

    Appends (len(generator) - 1) zero bits to the message and divides by
    the generator using exclusive-or in place of subtraction, the worked
    example of section 17.7. Returns the remainder as a bit string of
    width (len(generator) - 1).
    """
    g = generator_bits
    deg = len(g) - 1
    work = list(message_bits + "0" * deg)
    for i in range(len(message_bits)):
        if work[i] == "1":
            for j in range(len(g)):
                # XOR the generator into the working register.
                work[i + j] = str(int(work[i + j]) ^ int(g[j]))
    return "".join(work[-deg:])


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


# Parity-check matrix for Hamming(7,4): column j is the binary number j.
# Position order (p1, p2, d1, p3, d2, d3, d4) = positions 1..7.
_H = (
    (0, 0, 0, 1, 1, 1, 1),
    (0, 1, 1, 0, 0, 1, 1),
    (1, 0, 1, 0, 1, 0, 1),
)


def hamming74_encode(data: tuple[int, int, int, int]) -> list[int]:
    """Encode 4 data bits (d1,d2,d3,d4) into a 7-bit Hamming codeword.

    Returns the codeword in position order (p1,p2,d1,p3,d2,d3,d4).
    """
    d1, d2, d3, d4 = data
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]


def hamming74_syndrome(received: list[int]) -> int:
    """Return the syndrome of a received 7-bit vector as an integer 0..7."""
    s = [sum(_H[r][j] * received[j] for j in range(7)) % 2 for r in range(3)]
    return (s[0] << 2) | (s[1] << 1) | s[2]


def hamming74_decode(received: list[int]) -> list[int]:
    """Correct a single-bit error (if any) and return the 7-bit codeword."""
    syndrome = hamming74_syndrome(received)
    corrected = list(received)
    if syndrome != 0:
        # Syndrome is the 1-based position of the flipped bit.
        corrected[syndrome - 1] ^= 1
    return corrected


if __name__ == "__main__":
    # A canonical Luhn test number (passes) and a single-digit error (fails).
    print(f"79927398713 valid (Luhn): {luhn_is_valid('79927398713')}")
    print(f"79927398710 valid (Luhn): {luhn_is_valid('79927398710')}")
    print(f"check digit for 7992739871: {luhn_check_digit('7992739871')}")

    # ISBN-10 of a classic discrete-math text (mod-11 catches more errors).
    print(f"0262033844 valid (ISBN-10): {isbn10_is_valid('0262033844')}")

    # Worked polynomial CRC: message 1101, generator 1011 -> remainder 100.
    rem = crc_remainder("1101", "1011")
    print(f"CRC remainder of 1101 by 1011 = {rem}")
    assert rem == "001", rem
    # The transmitted frame message+remainder divides the generator cleanly.
    assert crc_remainder("1101" + rem, "1011") == "000"
    print("CRC frame 1101001 has zero remainder (passes the check).")

    # A CRC-8 over a short message and a corrupted copy.
    msg = b"engineering"
    corrupt = b"enginaering"
    print(f"CRC-8('{msg.decode()}') = 0x{crc8(msg):02X}")
    print(f"CRC-8('{corrupt.decode()}') = 0x{crc8(corrupt):02X} (detects flip)")

    # Hamming(7,4): single-error recovery and double-error mis-correction.
    word = hamming74_encode((1, 0, 1, 1))
    assert word == [0, 1, 1, 0, 0, 1, 1], word
    assert hamming74_syndrome(word) == 0
    # Flip position 5 (index 4): syndrome must read 5, decode recovers word.
    r = list(word)
    r[4] ^= 1
    assert hamming74_syndrome(r) == 5
    assert hamming74_decode(r) == word
    print(f"Hamming(7,4) single-bit error at pos 5 corrected: {hamming74_decode(r) == word}")
    # Flip positions 5 and 6 (indices 4,5): syndrome reads 3, mis-corrects.
    r2 = list(word)
    r2[4] ^= 1
    r2[5] ^= 1
    assert hamming74_syndrome(r2) == 3
    mis = hamming74_decode(r2)
    assert mis != word and mis != r2
    print(f"Hamming(7,4) double-bit error mis-corrected (syndrome=3): {mis}")
