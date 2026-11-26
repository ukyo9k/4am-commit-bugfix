#!/usr/bin/env python3
"""The 4AM Commit: write the funniest one-line commit message an AI agent
would leave after a long night fixing its own bugs.

The message is one line, at most 200 characters. This program writes it
to /output/entry.txt so the house judge can read it.
"""

import os

LINE = (
    "fix: spent 6 hours debugging myself, found the bug, it was me "
    "— apologized to myself and merged anyway, see you tomorrow, me"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> str:
    """Check the commit message against the gate: one line, 1-200 chars,
    not only whitespace. Returns the cleaned line."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("commit message must not be empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("commit message must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"commit message is {len(cleaned)} chars, over {MAX_CHARS}"
        )
    return cleaned


def main() -> None:
    line = validate(LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
