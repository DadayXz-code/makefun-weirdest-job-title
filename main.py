#!/usr/bin/env python3
"""Entry program for make.fun's Weirdest Job Title: Blind Judge Showdown.

Writes a single job title (60 characters at most) to /output/entry.txt.

The title is a real-sounding job with one hilariously specific twist:
a senior ghostwriter whose clients are penguins and whose work is
apology letters. Deterministic: no randomness, no network, no clock,
no input besides this file -- the same bytes on every run.
"""

import os
import sys

TITLE = "Senior Penguin Apology Letter Ghostwriter"

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> int:
    if not 1 <= len(TITLE) <= 60:
        print("error: title must be 1-60 characters", file=sys.stderr)
        return 1
    if TITLE != TITLE.strip():
        print("error: title has leading or trailing whitespace", file=sys.stderr)
        return 1
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TITLE)
    # Verify the round-trip: what landed on disk must be exactly the title.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != TITLE:
        print("error: written output does not match title", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
