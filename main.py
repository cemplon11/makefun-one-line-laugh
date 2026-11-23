#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Pure Python stdlib, deterministic, no network. The line is a single sentence
of at most 200 characters.
"""

import os

LINE = "My calendar just reminded me to relax, so I've scheduled worrying about it for Thursday."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
