# practice-sets

Distraction-free student practice sets — auto-generated from a Markdown question bank.

Published at: **https://ranjanchoubey.github.io/practice-sets/**

## Structure

```
content/
  discrete-math/counting.md      # question bank — ## Q001 delimited
  gate-da/                       # add more courses here
lectures/
  discrete-math/counting-basics.yaml  # one file per lecture
scripts/
  parse.py                       # extracts questions from Markdown
  generate.py                    # renders HTML + PDF + QR
templates/
  lecture.html                   # student web view
  lecture-print.html             # PDF print view
  index.html                     # course listing
docs/                            # generated output (GitHub Pages root)
.github/workflows/build.yml      # CI/CD
```

## Adding a question

Open any file in `content/` and add:

```markdown
## Q025

[MCQ]

Your question text here. Math works: $n!$ and $\binom{n}{k}$.

A. Option A
B. Option B
C. Option C
D. Option D

**Answer:** B

**Solution:** Brief explanation.

---
```

**Question ID rules:** `Q` + 3–5 digits, globally unique across ALL content files.

**Type tags:** `[MCQ]` `[NAT]` `[MSQ]` `[SUBJ]` `[CODE]` `[CASE]`

## Adding a lecture

Create `lectures/<course>/<slug>.yaml`:

```yaml
title: "My Lecture Title"
course: discrete-math
slug: my-lecture-slug     # immutable — used in URL and QR code
date: "2026-06-21"

questions:
  - Q001
  - Q025
  - Q003
```

**Warning:** Never rename `slug` after publishing — QR codes will break.

## Local build

```bash
pip install -r requirements.txt
playwright install chromium
./build.sh
# Open docs/discrete-math/lecture/counting-basics/index.html
```

## CI/CD

Push to `main` → GitHub Actions builds everything → deploys to GitHub Pages automatically.

Enable GitHub Pages in repo settings: **Source → GitHub Actions**.
