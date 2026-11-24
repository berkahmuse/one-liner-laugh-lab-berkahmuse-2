#!/usr/bin/env python3
"""One-Liner Laugh Lab entry for @berkahmuse-2.

Prompt: the excuse a GPS gives after routing you through a cornfield.
Writes one short funny line to /output/entry.txt.
"""

import os

LINE = "Shortest route. I never promised it had roads."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip() == LINE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what we wrote is exactly the line, nothing else.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == LINE
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
