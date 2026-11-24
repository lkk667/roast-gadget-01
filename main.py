#!/usr/bin/env python3
"""Roast the gadget you use every day: the phone's screen-time report.

The joke: the phone that steals your attention all week then shows up
on Monday morning acting like your manager, handing you a performance
review for a job you never applied for -- scrolling. The roast lands
because the phone is both the culprit and the auditor.

The script is deliberately boring: it takes the single roast line
below and writes it, byte for byte, to /output/entry.txt, with no
trailing newline and no extra output, so the sealed gate sees exactly
one line of 148 characters.
"""

import os
import pathlib

ROAST = (
    "Every Monday, my phone sends me a screen-time report \u2014 a "
    "performance review from a boss who watched me scroll for nine "
    "hours and accomplish nothing."
)

# The sealed gate counts characters, not bytes: keep the line inside
# the 1-to-200 range, and refuse to write anything that would fail it.
MAX_CHARS = 200

# The grader runs this with /output mounted; the override exists only
# so the same program can be smoke-tested on a machine without it.
DESTINATION = pathlib.Path(os.environ.get("ROAST_OUTPUT", "/output/entry.txt"))


def write_entry() -> pathlib.Path:
    if not 1 <= len(ROAST) <= MAX_CHARS:
        raise ValueError(f"roast is {len(ROAST)} characters, outside 1-{MAX_CHARS}")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ROAST, encoding="utf-8")
    return DESTINATION


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(ROAST)} characters to {written}")
