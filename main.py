#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line aimed at a robot/AI to /output/entry.txt
(honouring MAKEFUN_OUTPUT_DIR). The gate is 1-200 UTF-8 chars, one line,
not only whitespace.
"""

import os
import sys

LINE = "Are you a transformer? Because you've had my undivided attention since the first token."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_line(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, non-blank."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(line: str, out_dir: str) -> str:
    """Write the line to <out_dir>/entry.txt and return the path."""
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
