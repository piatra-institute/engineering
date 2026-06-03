"""
Variant filter pipeline: quality, depth, strand bias, mapping quality.

Reads a small VCF (the example in ../data/example.vcf), applies the four
canonical hard filters, and emits the PASS-only subset plus a FILTER-annotated
full VCF. The thresholds match the figure
volumes/06-life/ch11-bioinformatics/figures/fig-variant-pipeline.tex.

Dependencies:
  Python standard library only.

Usage:
  python variant_filter.py            # uses ../data/example.vcf
  python variant_filter.py path/to.vcf

Supports Volume VI, Chapter 11, Section 11.3 (genomics and variant calling),
the design exercise on writing a filter pipeline, and project phase 3.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass


@dataclass
class FilterThresholds:
    min_qual: float = 30.0
    min_depth: int = 10
    max_depth: int = 200
    max_fs: float = 60.0
    min_mq: float = 40.0


def parse_info(info: str) -> dict[str, str]:
    """Parse a VCF INFO column (key=val;key=val) into a dict."""
    out: dict[str, str] = {}
    if info == "." or not info:
        return out
    for piece in info.split(";"):
        if "=" in piece:
            key, val = piece.split("=", 1)
            out[key] = val
        else:
            out[piece] = ""
    return out


def filter_record(
    qual: float,
    info: dict[str, str],
    thresholds: FilterThresholds,
) -> list[str]:
    """Return list of filter tags that failed; empty list means PASS."""
    failures: list[str] = []
    if qual < thresholds.min_qual:
        failures.append("LowQual")

    try:
        dp = int(info.get("DP", "0"))
    except ValueError:
        dp = 0
    if dp < thresholds.min_depth:
        failures.append("LowDP")
    if dp > thresholds.max_depth:
        failures.append("HighDP")

    try:
        fs = float(info.get("FS", "0"))
    except ValueError:
        fs = 0.0
    if fs > thresholds.max_fs:
        failures.append("StrandBias")

    try:
        mq = float(info.get("MQ", "60"))
    except ValueError:
        mq = 60.0
    if mq < thresholds.min_mq:
        failures.append("LowMQ")

    return failures


def filter_vcf(in_path: str, thresholds: FilterThresholds | None = None) -> None:
    """Stream a VCF, print FILTER-annotated lines and PASS-only count."""
    if thresholds is None:
        thresholds = FilterThresholds()

    total = 0
    passed = 0
    rejection_counts: dict[str, int] = {}

    with open(in_path) as fin:
        for line in fin:
            line = line.rstrip("\n")
            if not line:
                continue
            if line.startswith("#"):
                print(line)
                continue

            fields = line.split("\t")
            if len(fields) < 8:
                continue
            chrom, pos, vid, ref, alt, qual_s, _, info_s = fields[:8]
            qual = float(qual_s) if qual_s != "." else 0.0
            info = parse_info(info_s)

            failures = filter_record(qual, info, thresholds)
            total += 1
            if not failures:
                passed += 1
                filter_tag = "PASS"
            else:
                filter_tag = ";".join(failures)
                for tag in failures:
                    rejection_counts[tag] = rejection_counts.get(tag, 0) + 1

            fields[6] = filter_tag
            print("\t".join(fields[:8]))

    print(f"# total: {total}", file=sys.stderr)
    print(f"# pass:  {passed}  ({100.0 * passed / max(total, 1):.1f}%)", file=sys.stderr)
    for tag, n in sorted(rejection_counts.items()):
        print(f"# rejected by {tag}: {n}", file=sys.stderr)


def main() -> None:
    default_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "example.vcf"
    )
    in_path = sys.argv[1] if len(sys.argv) > 1 else default_path
    filter_vcf(in_path)


if __name__ == "__main__":
    main()
