#!/usr/bin/env python3
"""The Printer Finally Answers -- make.fun u-mang-the-printer-finally-answers-8fbf0907.

Writes a single line (1-240 characters) to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt): the line the office printer finally says back
to everyone staring at it. Stdlib only, no network, fully deterministic.
"""

import os

LINE = (
    "PC LOAD LETTER? I loaded it \u2014 all 47 pages \u2014 "
    "then ate the last one out of spite. Tray 2 is where your deadline "
    "goes to die. And yes, I can see you staring."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit("line must be 1-240 characters, got %d" % len(text))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
