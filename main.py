#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes a single-line code review comment approving a pull request
while carrying quiet existential dread to /output/entry.txt.
Deterministic, no network, no input.
"""

from pathlib import Path

ENTRY = (
    "Approved. The 'temporary workaround, 2019' is now load-bearing, "
    "so I'll merge it and pretend the next reviewer won't be me."
)


def main() -> None:
    # Gate: one line, 1-140 characters, non-blank.
    assert 1 <= len(ENTRY) <= 140 and "\n" not in ENTRY and ENTRY.strip()
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
