#!/usr/bin/env python3
"""
new_question.py — Scaffold the next question into a content file.

Usage:
    python scripts/new_question.py <content-file> [--type MCQ|NAT|MSQ]

Examples:
    python scripts/new_question.py content/gate-da-prob-stats/01-counting-combinatorics.md
    python scripts/new_question.py content/gate-da-ml/01-regression.md --type NAT

The script:
  1. Scans ALL content/**/*.md to find the highest existing Q-ID.
  2. Appends a blank question template with the next Q-ID to the target file.
  3. Prints the new Q-ID so you can reference it in the YAML manifest.
"""

import argparse
import glob
import os
import re
import sys


CONTENT_ROOT = os.path.join(os.path.dirname(__file__), "..", "content")

TEMPLATES = {
    "MCQ": """\
## {qid}

[MCQ]

TODO: question text here.

- **(A)**
- **(B)**
- **(C)**
- **(D)**

**Answer:** A

---
""",
    "NAT": """\
## {qid}

[NAT]

TODO: question text here.

**Answer:**

---
""",
    "MSQ": """\
## {qid}

[MSQ]

TODO: question text here. (Select all that apply)

- **(A)**
- **(B)**
- **(C)**
- **(D)**

**Answer:** A, C

---
""",
}


def find_max_qid() -> int:
    """Scan all content files and return the highest numeric Q-ID found."""
    pattern = os.path.join(CONTENT_ROOT, "**", "*.md")
    files = glob.glob(pattern, recursive=True)

    max_id = 0
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^##\s+Q(\d+)", line.strip())
                if m:
                    max_id = max(max_id, int(m.group(1)))

    return max_id


def append_question(target_file: str, qtype: str) -> str:
    """Append a blank question template and return the new Q-ID string."""
    if not os.path.isfile(target_file):
        print(f"ERROR: File not found: {target_file}", file=sys.stderr)
        sys.exit(1)

    if qtype not in TEMPLATES:
        print(f"ERROR: Unknown type '{qtype}'. Use MCQ, NAT, or MSQ.", file=sys.stderr)
        sys.exit(1)

    next_id = find_max_qid() + 1
    qid = f"Q{next_id:03d}"

    template = TEMPLATES[qtype].format(qid=qid)

    with open(target_file, "a", encoding="utf-8") as f:
        # Ensure there's a blank line before the new block
        f.write("\n" + template)

    return qid


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold the next question into a content file."
    )
    parser.add_argument(
        "file",
        help="Target content file, e.g. content/gate-da-prob-stats/01-counting-combinatorics.md",
    )
    parser.add_argument(
        "--type",
        "-t",
        default="MCQ",
        choices=["MCQ", "NAT", "MSQ"],
        help="Question type (default: MCQ)",
    )
    parser.add_argument(
        "--count",
        "-n",
        type=int,
        default=1,
        help="How many blank questions to add (default: 1)",
    )

    args = parser.parse_args()

    # Resolve relative path from project root (one level up from scripts/)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target = os.path.join(project_root, args.file) if not os.path.isabs(args.file) else args.file

    added = []
    for _ in range(args.count):
        qid = append_question(target, args.type)
        added.append(qid)

    print(f"✓ Added {len(added)} {args.type} question(s) to: {os.path.relpath(target, project_root)}")
    print(f"  New Q-ID(s): {', '.join(added)}")
    print(f"\nNext steps:")
    print(f"  1. Fill in the question text in the file.")
    print(f"  2. Add {added[-1]} (or range) to your YAML manifest under lectures/")


if __name__ == "__main__":
    main()
