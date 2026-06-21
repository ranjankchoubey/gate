#!/usr/bin/env python3
"""
migrate_pyq.py — Migrate PYQ questions from LaTeX study notes to practice site.

Reads: /Users/vn59a0h/ranjan-learning/study-notes/GATE-DA/**/*-pyq.tex
Writes:
  content/{course}/{chapter}-pyq.md   — new MD files
  lectures/{course}/{chapter}.yaml    — adds PYQ section (or creates for new chapters)

Q-ID allocation:
  Q5001–Q5002 already used in 02-probability-basics-pyq.md (pilot).
  This script starts from Q5003.

Run from: /Users/vn59a0h/preparation/gate-da/practice
  python3 scripts/migrate_pyq.py [--dry-run]
"""

import re
import sys
from pathlib import Path
import yaml

# ─── Directories ────────────────────────────────────────────────────────────
NOTES_DIR = Path("/Users/vn59a0h/ranjan-learning/study-notes/GATE-DA")
PRACTICE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PRACTICE_DIR / "content"
LECTURES_DIR = PRACTICE_DIR / "lectures"

DRY_RUN = "--dry-run" in sys.argv

# ─── Q-ID counter ──────────────────────────────────────────────────────────
_next_qid = 5003  # Q5001–Q5002 used by pilot


def alloc_qid() -> str:
    global _next_qid
    qid = f"Q{_next_qid}"
    _next_qid += 1
    return qid


# ─── Chapter mapping ────────────────────────────────────────────────────────
# Each entry: (tex_rel_path, target_chapter_slug, course, skip_gate_refs)
# skip_gate_refs: set of "GATE YYYY -- Q.NN" strings to skip (duplicates/MTA)
#
# Groups are defined per chapter. Multiple source files → merged output.

CHAPTER_GROUPS: dict[tuple[str, str], list[tuple[str, set]]] = {
    # (chapter_slug, course): [(tex_rel, skip_refs), ...]

    ("01-counting-combinatorics", "gate-da-prob-stats"): [
        ("01-probability-statistics/01-counting-combinatorics/01-01-01-permutations-combinations-pyq.tex", set()),
    ],

    # 02-probability-basics: Q5001–Q5002 already done; independence file is empty → skip entirely
    # ("02-probability-basics", "gate-da-prob-stats"): [],  # handled by pilot

    ("03-conditional-probability-bayes", "gate-da-prob-stats"): [
        ("01-probability-statistics/03-conditional-probability-bayes/01-03-01-conditional-joint-marginal-events-pyq.tex", set()),
        ("01-probability-statistics/03-conditional-probability-bayes/01-03-02-bayes-theorem-pyq.tex", set()),
    ],

    ("04-random-variables", "gate-da-prob-stats"): [
        ("01-probability-statistics/04-random-variables/01-04-01-expectation-variance-pyq.tex", set()),
        ("01-probability-statistics/04-random-variables/01-04-02-conditional-expectation-pyq.tex",
         {"GATE 2024 -- Q.59"}),  # MTA — dropped question
    ],

    ("05-discrete-distributions", "gate-da-prob-stats"): [
        ("01-probability-statistics/05-discrete-distributions/01-05-01-uniform-bernoulli-binomial-pyq.tex", set()),
        ("01-probability-statistics/05-discrete-distributions/01-05-02-poisson-geometric-pyq.tex", set()),
    ],

    ("06-continuous-distributions", "gate-da-prob-stats"): [
        ("01-probability-statistics/06-continuous-distributions/01-06-01-pdf-cdf-pyq.tex", set()),
        ("01-probability-statistics/06-continuous-distributions/01-06-02-uniform-exponential-pyq.tex", set()),
        ("01-probability-statistics/06-continuous-distributions/01-06-03-normal-standard-normal-pyq.tex", set()),
        ("01-probability-statistics/06-continuous-distributions/01-06-04-t-chi-squared-pyq.tex", set()),
    ],

    # 07-descriptive-statistics: only Q.34 which is dup of expectation-variance → nothing new
    # ("07-descriptive-statistics", "gate-da-prob-stats"): [],

    ("08-clt-confidence-intervals", "gate-da-prob-stats"): [
        ("01-probability-statistics/10-sampling-distributions-clt/01-10-01-central-limit-theorem-pyq.tex", set()),
        ("01-probability-statistics/11-confidence-intervals-point-estimation/01-11-01-point-estimation-pyq.tex", set()),
    ],

    # 09-hypothesis-testing: all PYQ files empty → skip

    # NEW chapter (no existing filler)
    ("10-covariance-correlation", "gate-da-prob-stats"): [
        ("01-probability-statistics/09-covariance-correlation/01-09-01-covariance-correlation-pyq.tex", set()),
    ],

    # ── ML ──────────────────────────────────────────────────────────────────
    ("01-regression", "gate-da-ml"): [
        ("02-machine-learning/01-regression/02-01-01-simple-linear-regression-pyq.tex", set()),
        # 02-01-02 multiple LR: no PYQs
        ("02-machine-learning/01-regression/02-01-04-gradient-descent-pyq.tex", set()),
    ],

    # practice ch02 = "Ridge Regression and Logistic Regression"
    ("02-classification", "gate-da-ml"): [
        ("02-machine-learning/01-regression/02-01-03-ridge-regression-pyq.tex", set()),
        ("02-machine-learning/02-classification/02-02-01-logistic-regression-pyq.tex", set()),
    ],

    # practice ch03 = "KNN, Naive Bayes, LDA"
    ("03-classification-probabilistic", "gate-da-ml"): [
        ("02-machine-learning/02-classification/02-02-02-naive-bayes-pyq.tex", set()),
        ("02-machine-learning/02-classification/02-02-03-knn-pyq.tex", set()),
        ("02-machine-learning/02-classification/02-02-06-linear-discriminant-analysis-pyq.tex", set()),
    ],

    # practice ch04 = "SVM and Decision Trees"
    ("04-classification-svm-trees", "gate-da-ml"): [
        ("02-machine-learning/02-classification/02-02-04-svm-pyq.tex", set()),
        ("02-machine-learning/02-classification/02-02-05-decision-trees-pyq.tex", set()),
    ],

    ("05-model-evaluation", "gate-da-ml"): [
        # 02-04-01 bias-variance: only Q.37 which is dup of ridge → nothing new
        ("02-machine-learning/04-model-evaluation/02-04-02-cross-validation-pyq.tex", set()),
        ("02-machine-learning/04-model-evaluation/02-04-03-precision-recall-accuracy-pyq.tex", set()),
    ],

    ("06-neural-networks", "gate-da-ml"): [
        ("02-machine-learning/03-neural-networks/02-03-01-perceptron-pyq.tex", set()),
        ("02-machine-learning/03-neural-networks/02-03-02-mlp-feed-forward-pyq.tex", set()),
        # 02-03-03 backpropagation: no PYQs
    ],

    ("07-clustering", "gate-da-ml"): [
        ("02-machine-learning/05-clustering/02-05-01-k-means-k-medoid-pyq.tex", set()),
        ("02-machine-learning/05-clustering/02-05-02-hierarchical-clustering-pyq.tex", set()),
    ],

    ("08-pca", "gate-da-ml"): [
        ("02-machine-learning/06-pca/02-06-01-principal-component-analysis-pyq.tex", set()),
    ],
}

# New chapters that need a YAML created (not just updated)
NEW_CHAPTERS: dict[tuple[str, str], dict] = {
    ("10-covariance-correlation", "gate-da-prob-stats"): {
        "title": "Covariance and Correlation",
        "date": "2026-06-21",
    },
}


# ─── Conversion helpers ─────────────────────────────────────────────────────

def apply_macros(text: str) -> str:
    """Replace custom LaTeX macros with MathJax-compatible equivalents."""
    replacements = [
        # Custom DeclareMathOperator → MathJax
        (r'\\Prob(?=[^a-zA-Z]|$)', r'P'),
        (r'\\Exp(?=[^a-zA-Z]|$)', r'E'),
        (r'\\Var(?=[^a-zA-Z]|$)', r'\\text{Var}'),
        (r'\\Cov(?=[^a-zA-Z]|$)', r'\\text{Cov}'),
        # Vector / matrix macros
        (r'\\vw(?=[^a-zA-Z]|$)', r'\\mathbf{w}'),
        (r'\\vy(?=[^a-zA-Z]|$)', r'\\mathbf{y}'),
        (r'\\vx(?=[^a-zA-Z]|$)', r'\\mathbf{x}'),
        (r'\\mX(?=[^a-zA-Z]|$)', r'\\mathbf{X}'),
        (r'\\mI(?=[^a-zA-Z]|$)', r'\\mathbf{I}'),
        (r'\\T(?=[^a-zA-Z]|$)', r'^\\top'),
        # Number sets
        (r'\\R(?=[^a-zA-Z]|$)', r'\\mathbb{R}'),
        # \norm{...} → \|...\|  (up to 1-level nested braces)
        (r'\\norm\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', r'\\|\\1\\|'),
        # Display math \[...\] → $$...$$
        (r'\\\[([\s\S]*?)\\\]', lambda m: '$$' + m.group(1) + '$$'),
    ]
    for pat, repl in replacements:
        text = re.sub(pat, repl, text)
    return text


def clean_body(text: str) -> str:
    """Remove structural LaTeX; convert text-mode markup to Markdown."""
    # Remove comments
    text = re.sub(r'%.*$', '', text, flags=re.MULTILINE)
    # Remove structural environments we don't need
    for env in ['practicesection', 'sectionindex']:
        text = re.sub(r'\\' + env + r'\{[^}]*\}', '', text)
    # \textbf{X} → **X** (outside math — approximate)
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)
    # \emph{X} or \textit{X} → *X*
    text = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', text)
    text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', text)
    # \rule{...}{...} (blank line in NAT) → ______
    text = re.sub(r'\\rule\{[^}]+\}\{[^}]+\}', '______', text)
    # Collapse 3+ blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def convert_enumerate(text: str) -> str:
    """Convert LaTeX enumerate with lettered items to Markdown MCQ options."""
    def replace_enum(m):
        inner = m.group(1)
        inner = re.sub(r'\\item\[\(([A-Z])\)\]\s*', r'\n- **(\1)** ', inner)
        return inner.strip()

    text = re.sub(
        r'\\begin\{enumerate\}(?:\[[^\]]*\])?\s*([\s\S]*?)\\end\{enumerate\}',
        replace_enum,
        text,
    )
    return text


def convert_table(text: str) -> str:
    """Convert LaTeX tabular (inside center env) to Markdown table."""
    def replace_center_tabular(outer):
        # Column spec may contain nested {} like {@ {}l l@{}} — use balanced match
        inner = re.search(
            r'\\begin\{tabular\}\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}([\s\S]*?)\\end\{tabular\}',
            outer.group(0),
        )
        if not inner:
            return outer.group(0)
        table_body = inner.group(1)
        lines = table_body.split('\n')
        rows = []
        for line in lines:
            line = re.sub(r'\\(toprule|midrule|bottomrule|hline)\b', '', line).strip()
            line = re.sub(r'\\\\$', '', line).strip()
            if not line:
                continue
            cells = [c.strip() for c in line.split('&')]
            rows.append(cells)
        if not rows:
            return ''
        header = rows[0]
        md = '| ' + ' | '.join(header) + ' |\n'
        md += '| ' + ' | '.join(['---'] * len(header)) + ' |\n'
        for row in rows[1:]:
            while len(row) < len(header):
                row.append('')
            md += '| ' + ' | '.join(row[:len(header)]) + ' |\n'
        return md.strip()

    text = re.sub(
        r'\\begin\{center\}[\s\S]*?\\end\{center\}',
        replace_center_tabular,
        text,
    )
    return text


# ─── Answer key parsing ─────────────────────────────────────────────────────

def normalize_answer(s: str) -> str:
    s = s.strip()
    s = s.replace(';', ', ')               # B;C → B, C
    s = re.sub(r'--+', ' to ', s)          # 0.062--0.063 → 0.062 to 0.063
    return s


def parse_answerkey(ak_str: str, n_questions: int) -> dict[int, str]:
    """Return {0-based-index: answer_str}. Handles position-based and label-based keys."""
    if not ak_str:
        return {}
    results: dict[int, str] = {}
    parts = [p.strip() for p in ak_str.split(',') if p.strip()]
    for i, part in enumerate(parts):
        if '/' not in part:
            results[i] = normalize_answer(part)
            continue
        key, _, val = part.rpartition('/')
        key = key.strip()
        val = normalize_answer(val)
        if re.match(r'^\d+$', key):
            idx = int(key) - 1
            results[idx] = val
        elif re.match(r'^GATE \d{4}', key):
            # label-based: map by position in parts (less reliable; use as fallback)
            results[i] = val
        else:
            results[i] = val
    return results


# ─── Question extraction ─────────────────────────────────────────────────────

Q_MARKER = re.compile(r'\\pq(mcq|n|msq|NAT|MCQ|MSQ)\[([^\]]+)\]', re.IGNORECASE)


def extract_from_tex(tex_path: Path, skip_refs: set) -> list[dict]:
    """
    Parse one *-pyq.tex file. Returns list of question dicts:
      {gate_ref, type, pyq_tag, body, answer}
    """
    text = tex_path.read_text(encoding='utf-8')

    # Extract between \begin{practicequestions} ... \end{practicequestions}
    pq = re.search(
        r'\\begin\{practicequestions\}([\s\S]*?)\\end\{practicequestions\}', text
    )
    if not pq:
        return []
    pq_content = pq.group(1)

    # Answer key (outside practicequestions)
    ak = re.search(r'\\answerkey\{([^}]+)\}', text)
    ak_str = ak.group(1) if ak else ''

    # Split on question markers
    parts = Q_MARKER.split(pq_content)
    # parts = [before_q1, type1, ref1, body1, type2, ref2, body2, ...]

    raw_qs: list[dict] = []
    i = 1
    while i + 2 < len(parts):
        qtype_code = parts[i].lower()
        gate_ref = parts[i + 1].strip()
        body_raw = parts[i + 2]
        i += 3

        qtype = {'mcq': 'MCQ', 'n': 'NAT', 'msq': 'MSQ'}.get(qtype_code, qtype_code.upper())
        year_m = re.match(r'GATE (\d{4})', gate_ref)
        year = year_m.group(1) if year_m else '????'

        raw_qs.append({
            'gate_ref': gate_ref,
            'type': qtype,
            'pyq_tag': f'GATE DA {year}',
            'body_raw': body_raw.strip(),
        })

    answers = parse_answerkey(ak_str, len(raw_qs))

    questions = []
    for j, rq in enumerate(raw_qs):
        if rq['gate_ref'] in skip_refs:
            print(f'    [SKIP] {rq["gate_ref"]}', file=sys.stderr)
            continue

        body = rq['body_raw']
        body = convert_table(body)
        body = convert_enumerate(body)
        body = apply_macros(body)
        body = clean_body(body)

        # Flag figure-dependent questions
        if re.search(r'figure|Figure|diagram|Diagram|graph|plot|image', body):
            body = '<!-- FIGURE NEEDED: Original question references a figure from the GATE paper -->\n\n' + body

        questions.append({
            'gate_ref': rq['gate_ref'],
            'type': rq['type'],
            'pyq_tag': rq['pyq_tag'],
            'body': body,
            'answer': answers.get(j),
        })

    return questions


# ─── Output writers ─────────────────────────────────────────────────────────

def format_md_block(qid: str, q: dict) -> str:
    lines = [f'## {qid}', '', f'[{q["type"]}]', f'[PYQ: {q["pyq_tag"]}]', '']
    lines.append(q['body'])
    if q['answer']:
        lines += ['', f'**Answer:** {q["answer"]}']
    lines += ['', '---', '']
    return '\n'.join(lines)


def write_pyq_md(chapter: str, course: str, questions: list[dict]) -> list[str]:
    """Write content/{course}/{chapter}-pyq.md. Returns list of assigned Q-IDs."""
    if not questions:
        return []
    out_path = CONTENT_DIR / course / f'{chapter}-pyq.md'
    qids = []
    blocks = [
        f'# {chapter.replace("-", " ").title()} — PYQ\n\nSource: GATE DA Previous Year Questions\n\n---\n'
    ]
    for q in questions:
        qid = alloc_qid()
        qids.append(qid)
        blocks.append(format_md_block(qid, q))

    content = '\n'.join(blocks)
    print(f'  [MD] {out_path.relative_to(PRACTICE_DIR)} ({len(qids)} questions)', file=sys.stderr)
    if not DRY_RUN:
        out_path.write_text(content, encoding='utf-8')
    return qids


def update_yaml(chapter: str, course: str, qids: list[str], new_chapter_meta: dict | None = None):
    """Add PYQ section to existing YAML, or create new YAML for new chapters."""
    yaml_path = LECTURES_DIR / course / f'{chapter}.yaml'

    if new_chapter_meta and not yaml_path.exists():
        # Create new chapter YAML
        data = {
            'title': new_chapter_meta['title'],
            'course': course,
            'slug': chapter,
            'date': new_chapter_meta['date'],
            'sections': [{'heading': 'PYQ — ' + new_chapter_meta['title'], 'questions': qids}],
        }
        print(f'  [YAML-NEW] {yaml_path.relative_to(PRACTICE_DIR)}', file=sys.stderr)
        if not DRY_RUN:
            yaml_path.write_text(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False), encoding='utf-8')
        return

    if not yaml_path.exists():
        print(f'  [WARN] YAML not found: {yaml_path}', file=sys.stderr)
        return

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    sections = data.get('sections', [])

    # Find existing PYQ section
    pyq_section = None
    for sec in sections:
        heading = (sec.get('heading') or '').lower()
        if 'pyq' in heading:
            pyq_section = sec
            break

    if pyq_section:
        # Append new Q-IDs (avoid duplicates)
        existing = set(pyq_section.get('questions', []))
        new_ids = [q for q in qids if q not in existing]
        pyq_section['questions'] = list(pyq_section.get('questions', [])) + new_ids
        print(f'  [YAML-UPD] {yaml_path.relative_to(PRACTICE_DIR)} (+{len(new_ids)} IDs)', file=sys.stderr)
    else:
        # Get chapter title for heading
        title = data.get('title', chapter)
        sections.append({'heading': f'PYQ — {title}', 'questions': qids})
        data['sections'] = sections
        print(f'  [YAML-ADD] {yaml_path.relative_to(PRACTICE_DIR)} (new PYQ section, {len(qids)} IDs)', file=sys.stderr)

    if not DRY_RUN:
        with open(yaml_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print(f'[migrate_pyq] DRY_RUN={DRY_RUN}', file=sys.stderr)
    total_q = 0

    for (chapter, course), sources in CHAPTER_GROUPS.items():
        print(f'\n── {course}/{chapter} ──', file=sys.stderr)

        all_questions = []
        for tex_rel, skip_refs in sources:
            tex_path = NOTES_DIR / tex_rel
            if not tex_path.exists():
                print(f'  [MISSING] {tex_rel}', file=sys.stderr)
                continue
            qs = extract_from_tex(tex_path, skip_refs)
            print(f'  [TEX] {tex_path.name}: {len(qs)} questions', file=sys.stderr)
            all_questions.extend(qs)

        if not all_questions:
            print('  [SKIP] no questions', file=sys.stderr)
            continue

        qids = write_pyq_md(chapter, course, all_questions)
        new_meta = NEW_CHAPTERS.get((chapter, course))
        update_yaml(chapter, course, qids, new_meta)
        total_q += len(qids)

    print(f'\n[migrate_pyq] Done — {total_q} questions written (next Q-ID: Q{_next_qid})', file=sys.stderr)


if __name__ == '__main__':
    main()
