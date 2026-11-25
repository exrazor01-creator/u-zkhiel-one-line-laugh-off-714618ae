#!/usr/bin/env python3
"""One line for the One-Line Laugh-Off.

The judge reads two lines cold, side by side, and picks the
funnier one. It weighs the laugh first, then the surprise of
the turn, then how tight the wording is, then how fresh the
idea feels. This line is built for that order: it opens on a
familiar virtue purchase — a standing desk bought "to be
healthier" — and the second clause pulls the rug out. Nothing
about the habit changed at all; only the altitude of the
snacking did. "Higher altitude" does the joke's work twice
over: it is literally true of a standing desk, and it is a
mock-grandiose way to describe eating junk food while upright,
so the health framing collapses straight into the punchline.
The angle is fresh because the target is not "standing desks
are silly" — it is the buyer who upgraded the snack instead
of the snacker.

Why LIMIT is 200: the gate scores /output/entry.txt as valid
only at 1 to 200 characters, so 200 is the ceiling the scorer
enforces, not a style choice. The line itself is 80
characters, leaving 120 spare, so validation here only guards
against an edit accidentally pushing it over the ceiling.
Staying short also helps if the rate ever ties: the rules break
an exact tie toward the smaller text.
"""

import os

# The sealed line. One joke, one breath, no setup notes and no
# explanation — the judge only ever sees this text, read cold.
ENTRY = "I bought a standing desk to be healthier; now I just snack at a higher altitude."

LIMIT = 200  # gate: one line, 1-200 characters


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, not another type")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # The gate counts characters, and non-ASCII bytes would make
        # that count differ between platforms, so plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    if text.strip() != text:
        # Leading or trailing spaces would be invisible padding the
        # judge never asked for and the gate would count anyway.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        # Tabs, newlines and other control characters would split
        # the single line or hide bytes inside it.
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a wasted word in a line where every word
        # has to earn its place, and it breaks the clean single line.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
