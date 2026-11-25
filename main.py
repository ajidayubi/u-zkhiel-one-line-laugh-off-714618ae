#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt: a single joke that
lands on a cold read, with no setup notes and no explanation.
"""

import os

LINE = (
    "My bank flagged my account for suspicious activity, "
    "which was just me buying groceries and crying in the parking lot."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
