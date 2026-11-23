#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt.

Stdlib only: no third-party imports, no network, no file reads outside
this repository. The joke is a constant in this file, so the program is
fully deterministic -- the same bytes on every run.
"""

import os

JOKE = "I set my out-of-office reply to 'per my last email' — now even my holiday sounds passive-aggressive."

# The sealed gate only accepts 1 to 199 characters; refuse to write
# anything that could never be judged instead of shipping it silently.
assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
assert "\n" not in JOKE, "joke must be a single line"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print("wrote %d characters to %s" % (len(JOKE), path))


if __name__ == "__main__":
    main()
