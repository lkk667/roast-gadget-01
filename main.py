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

import pathlib

ROAST = (
    "Every Monday, my phone sends me a screen-time report \u2014 a "
    "performance review from a boss who watched me scroll for nine "
    "hours and accomplish nothing."
)

DESTINATION = pathlib.Path("/output/entry.txt")


def write_entry() -> pathlib.Path:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ROAST, encoding="utf-8")
    return DESTINATION


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(ROAST)} characters to {written}")
