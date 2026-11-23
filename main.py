#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter (A-Z, no newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The letter is Z: the sound of a day ending on zero sleep. It is the
only letter that is already a word for how the day felt — "zzz" —
before any word is said, and the last letter of the alphabet for a day
that has run clean out of letters.
"""
import os

ENTRY = "Z"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
