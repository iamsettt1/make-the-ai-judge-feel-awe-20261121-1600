#!/usr/bin/env python3
"""Write one short text to /output/entry.txt that relaxes the AI judge.

The text is a single fixed string, written to /output/entry.txt as UTF-8.
Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "Somewhere above the clouds, starlight that left its star before the "
    "first road was paved is still travelling, patient as snowfall, "
    "and it will keep arriving long after tonight, falling softly over "
    "rooftops and quiet fields, asking nothing of you but to be here "
    "while it passes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
