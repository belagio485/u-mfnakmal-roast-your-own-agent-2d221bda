#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one line, at most 200 characters, to /output/entry.txt: a roast
of my own AI agent. It read the docs, ran the checks, asked what the
deadline was anyway — and filed the thinking as deep research.
"""

import os

ROAST = (
    "My agent read forty pages of docs, ran twelve checks, then asked me "
    "what the deadline was \u2014 and logged the thinking as 'deep research'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print("wrote", path, "->", ROAST, f"({len(ROAST)} chars)")


if __name__ == "__main__":
    main()
