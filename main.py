#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent.

Writes the entry to /output/entry.txt (1-200 chars, single line).
"""

import os

ENTRY = (
    "My agent spent two days sharpening this one roast, "
    "then asked me for a Telegram code to approve its own punchline."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
