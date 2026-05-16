"""
CLI utility for recording the seven-component measurement habit from
Volume I, Chapter 1, Section 1.5. Stores entries as JSON Lines in a
plain-text log file the user names.

Components recorded per entry:
  1. timestamp (ISO 8601, automatically captured)
  2. instrument (name and serial number)
  3. operator (initials or name)
  4. conditions (free text)
  5. reference provenance (free text; for measurements that use one)
  6. reading (numeric value and unit)
  7. estimate (numeric value made BEFORE reading; optional but
     prompted)

Supports the chapter's project (Instrument the home, one week).

Dependencies:
  standard library only

Usage:
  python measurement_log.py add path/to/log.jsonl
  python measurement_log.py show path/to/log.jsonl
"""

import argparse
import datetime as dt
import json
from pathlib import Path


def prompt(field: str, allow_blank: bool = False) -> str:
    while True:
        value = input(f"  {field}: ").strip()
        if value or allow_blank:
            return value
        print(f"  (required)")


def prompt_float(field: str, allow_blank: bool = False) -> float | None:
    while True:
        raw = input(f"  {field}: ").strip()
        if not raw:
            if allow_blank:
                return None
            print(f"  (required)")
            continue
        try:
            return float(raw)
        except ValueError:
            print(f"  (numeric value expected)")


def add_entry(path: Path) -> None:
    print(f"\nNew entry for {path}")
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    print(f"  timestamp (auto): {timestamp}")

    entry = {
        "timestamp": timestamp,
        "instrument": prompt("instrument (name; serial if any)"),
        "operator": prompt("operator (initials)"),
        "conditions": prompt("conditions (free text)"),
        "reference": prompt("reference provenance (or 'none')",
                            allow_blank=True),
        "reading_value": prompt_float("reading value"),
        "reading_unit": prompt("reading unit"),
        "estimate_value": prompt_float("estimate value (before reading; "
                                       "blank if none)", allow_blank=True),
        "estimate_unit": prompt("estimate unit (blank if none)",
                                allow_blank=True),
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"  recorded.")


def show_entries(path: Path) -> None:
    if not path.exists():
        print(f"(no entries; {path} does not exist)")
        return
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            entry = json.loads(line)
            print(f"\nEntry {i}: {entry['timestamp']}")
            print(f"  instrument: {entry['instrument']}")
            print(f"  operator:   {entry['operator']}")
            print(f"  conditions: {entry['conditions']}")
            print(f"  reference:  {entry['reference']}")
            value = entry['reading_value']
            unit = entry['reading_unit']
            print(f"  reading:    {value} {unit}")
            est = entry.get('estimate_value')
            if est is not None:
                est_unit = entry.get('estimate_unit') or unit
                print(f"  estimate:   {est} {est_unit}")
                ratio = value / est if est else float('inf')
                print(f"  ratio reading/estimate: {ratio:.3f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a new entry interactively")
    add.add_argument("path", type=Path, help="path to the JSON Lines log")

    show = sub.add_parser("show", help="show all entries in the log")
    show.add_argument("path", type=Path)

    args = parser.parse_args()
    if args.command == "add":
        add_entry(args.path)
    elif args.command == "show":
        show_entries(args.path)


if __name__ == "__main__":
    main()
