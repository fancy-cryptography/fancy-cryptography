#!/usr/bin/env python3

# vibe coded.

"""Check that README.md list entries have proper trailing spaces for line breaks.

Each list entry (starting with '* **') is a block of lines. Every line within a
block that is followed by another line in the same block must end with two
trailing spaces ('  ') or '<br>' to produce a line break in rendered markdown.

Lines ending with a comma are considered continuation lines (e.g. multi-link
Reading entries) and are exempt from this check.
"""

import sys


def find_blocks(lines):
    """Yield (start, end) line ranges for each list entry block.

    A block starts at a line beginning with '* **' and continues until the next
    blank line, heading, or another top-level list item ('* ').
    Lines starting with '* (...)' are skipped (placeholder entries).
    """
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Start of a list entry
        if stripped.startswith("* **"):
            start = i
            i += 1
            # Collect all continuation lines (indented, non-empty, not a new
            # top-level list item, not a heading)
            while i < len(lines):
                s = lines[i].strip()
                if s == "":
                    break
                if s.startswith("## ") or s.startswith("# "):
                    break
                # A new top-level list item that isn't a nested sub-item
                if s.startswith("* ") and not lines[i].startswith("  "):
                    break
                i += 1
            yield (start, i - 1)  # end is inclusive
        else:
            i += 1


def check_block(lines, start, end):
    """Check a single block for missing trailing spaces.

    Returns a list of (line_number, line_text) for lines that are missing
    trailing spaces.
    """
    errors = []
    for i in range(start, end):  # skip the last line (index `end`)
        line = lines[i].rstrip("\n")

        # Comma-continuation lines are exempt
        if line.rstrip().endswith(","):
            continue

        # Line must end with two trailing spaces or <br>
        if line.endswith("  ") or line.rstrip().endswith("<br>"):
            continue

        errors.append((i + 1, line))  # 1-indexed line numbers
    return errors


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"

    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    all_errors = []
    for start, end in find_blocks(lines):
        all_errors.extend(check_block(lines, start, end))

    if all_errors:
        print(
            f"ERROR: {len(all_errors)} line(s) missing trailing double-space "
            f"for line break:\n"
        )
        for lineno, text in all_errors:
            print(f"  Line {lineno}: {text.strip()}")
        print(
            f"\nAdd two trailing spaces ('  ') at the end of each flagged "
            f"line to create a proper line break in rendered markdown."
        )
        sys.exit(1)
    else:
        print("README formatting check passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
