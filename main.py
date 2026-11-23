"""Make the Judge Smile — one line about a small good thing today.

A stranger's tiny kindness, unexplained: he held the elevator, then pressed
my floor before I could — and smiled like it was nothing. Warm first,
then the small surprise, with one concrete detail (the pressed floor)
to anchor it. The line stops at the kind act itself: no reason is given
for how he knew the floor, so the kindness reads as pure, not watchful.
The gate is 1-200 characters, a single line, verified byte-for-byte on write.
"""

import os
import sys

TEXT = "A stranger held the elevator for me this morning, then pressed my floor before I could \u2014 and smiled like it was nothing."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"gate failed: length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verification failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} characters), verified byte-for-byte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
