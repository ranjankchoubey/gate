"""
parse.py — Question Bank Parser

Walks content/**/*.md, extracts questions delimited by `## QXXX`.
Returns a registry: { "Q001": { id, type, body, answer, solution, source_file } }
"""

import re
import sys
from pathlib import Path

# Regex: matches ## Q001, ## Q022, etc. (3-5 digits)
QUESTION_HEADER = re.compile(r"^## (Q\d{3,5})\s*$", re.MULTILINE)
# Regex: type tag [MCQ], [NAT], [MSQ], [SUBJ], [CODE], [CASE]
TYPE_TAG = re.compile(r"^\[(\w+)\]$", re.MULTILINE)
# Answer and solution extraction
ANSWER_LINE = re.compile(r"^\*\*Answer:\*\*\s*(.+)$", re.MULTILINE)
SOLUTION_LINE = re.compile(r"^\*\*Solution:\*\*\s*([\s\S]+?)(?=\n---|\Z)", re.MULTILINE)

VALID_TYPES = {"MCQ", "NAT", "MSQ", "SUBJ", "CODE", "CASE"}


def parse_content_dir(content_dir: Path) -> dict:
    """Walk content_dir, parse all .md files, return question registry."""
    registry = {}
    errors = []

    for md_file in sorted(content_dir.rglob("*.md")):
        file_questions, file_errors = parse_file(md_file, content_dir)
        errors.extend(file_errors)
        for qid, qdata in file_questions.items():
            if qid in registry:
                errors.append(
                    f"DUPLICATE ID: {qid} found in both "
                    f"{registry[qid]['source_file']} and {qdata['source_file']}"
                )
            else:
                registry[qid] = qdata

    if errors:
        print("\n[PARSE ERRORS]", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(1)

    print(f"[parse] Loaded {len(registry)} questions from {content_dir}", file=sys.stderr)
    return registry


def parse_file(md_file: Path, base_dir: Path) -> tuple[dict, list]:
    """Parse a single markdown file. Returns (questions_dict, errors_list)."""
    text = md_file.read_text(encoding="utf-8")
    questions = {}
    errors = []
    rel_path = str(md_file.relative_to(base_dir))

    # Split on ## QXXX headers
    splits = QUESTION_HEADER.split(text)
    # splits[0] = content before first Q (file header — skip)
    # splits[1] = "Q001", splits[2] = body, splits[3] = "Q002", ...

    i = 1
    while i < len(splits) - 1:
        qid = splits[i].strip()
        body_raw = splits[i + 1].strip()
        i += 2

        # Extract type tag
        type_match = TYPE_TAG.search(body_raw)
        if not type_match:
            errors.append(f"{rel_path}: {qid} missing type tag [MCQ/NAT/MSQ/...]")
            continue
        qtype = type_match.group(1).upper()
        if qtype not in VALID_TYPES:
            errors.append(f"{rel_path}: {qid} unknown type [{qtype}]")
            continue

        # Remove type tag from body
        body_no_type = TYPE_TAG.sub("", body_raw, count=1).strip()

        # Extract answer and solution
        answer_match = ANSWER_LINE.search(body_no_type)
        solution_match = SOLUTION_LINE.search(body_no_type)

        answer = answer_match.group(1).strip() if answer_match else None
        solution = solution_match.group(1).strip() if solution_match else None

        # Remove answer/solution from student-visible body
        student_body = body_no_type
        if answer_match:
            student_body = student_body[: answer_match.start()].strip()

        questions[qid] = {
            "id": qid,
            "type": qtype,
            "body": student_body,
            "answer": answer,
            "solution": solution,
            "source_file": rel_path,
        }

    return questions, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    registry = parse_content_dir(base / "content")
    for qid, q in sorted(registry.items()):
        print(f"  {qid} [{q['type']}] — {q['source_file']}")
