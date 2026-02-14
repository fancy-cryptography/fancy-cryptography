#!/usr/bin/env python3

# vibe coded.

"""Check that README.md list entries are properly formatted.

Checks:
1. Trailing spaces: every line within a list entry block that is followed by
   another line must end with two trailing spaces ('  ') or '<br>' to produce
   a line break in rendered markdown. Lines ending with a comma (continuation
   lines for multi-link Reading entries) are exempt.
2. Required fields: every list entry must contain a 'Reading:' line and a
   'Fully PQ:' line.
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


def check_required_fields(lines, start, end):
    """Check that a block contains 'Reading:' and 'Fully PQ:' lines.

    Returns a list of (line_number, entry_name, missing_field) for any missing
    required fields.
    """
    import re

    # Extract entry name from the first line: * **Name**
    first_line = lines[start].strip()
    match = re.search(r"\*\*(.+?)\*\*", first_line)
    name = match.group(1) if match else first_line

    block_text = [lines[i] for i in range(start, end + 1)]

    errors = []
    has_reading = any("Reading:" in line for line in block_text)
    has_fully_pq = any("Fully PQ:" in line for line in block_text)

    if not has_reading:
        errors.append((start + 1, name, "Reading:"))
    if not has_fully_pq:
        errors.append((start + 1, name, "Fully PQ:"))

    return errors


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"

    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    blocks = list(find_blocks(lines))

    trailing_errors = []
    field_errors = []
    for start, end in blocks:
        trailing_errors.extend(check_block(lines, start, end))
        field_errors.extend(check_required_fields(lines, start, end))

    ok = True

    if trailing_errors:
        ok = False
        print(
            f"ERROR: {len(trailing_errors)} line(s) missing trailing "
            f"double-space for line break:\n"
        )
        for lineno, text in trailing_errors:
            print(f"  Line {lineno}: {text.strip()}")
        print(
            f"\nAdd two trailing spaces ('  ') at the end of each flagged "
            f"line to create a proper line break in rendered markdown.\n"
        )

    if field_errors:
        ok = False
        print(f"ERROR: {len(field_errors)} missing required field(s):\n")
        for lineno, name, field in field_errors:
            print(f"  Line {lineno} ({name}): missing '{field}'")
        print(f"\nEvery entry must contain a 'Reading:' line and a 'Fully PQ:' line.\n")

    if ok:
        print("README formatting check passed.")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
