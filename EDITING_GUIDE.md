# Editing Guide — GATE Practice Sets

Quick reference for adding questions, images, and new lectures.

---

## Directory Structure

```
practice/
├── content/
│   └── gate-da-prob-stats/
│       ├── 01-counting-combinatorics-demo.md   ← question bank
│       └── img/
│           ├── q013-diagram.png                ← images go here
│           └── q014-table.png
├── lectures/
│   └── gate-da-prob-stats/
│       └── 01-counting-basics.yaml             ← lecture manifest
├── scripts/
│   └── generate.py                             ← run this to rebuild
└── docs/                                       ← generated output (GitHub Pages)
```

---

## Adding a Text Question

Edit the content file: `content/{course}/{file}.md`

**MCQ format** (multiple choice, one correct answer):
```markdown
## Q013

[MCQ]

A coin is tossed 3 times. What is the total number of outcomes?

- **(A)** 3
- **(B)** 6
- **(C)** 8
- **(D)** 9

**Answer:** C
```

**NAT format** (numerical answer type):
```markdown
## Q014

[NAT]

How many ways can 3 books be arranged on a shelf?

**Answer:** 6
```

**MSQ format** (multiple select, more than one correct):
```markdown
## Q015

[MSQ]

Which of the following are prime numbers? (Select all that apply)

- **(A)** 2
- **(B)** 4
- **(C)** 7
- **(D)** 9

**Answer:** A, C
```

**Rules:**
- Question IDs (`Q013`, `Q014`, …) must be unique across the entire content file.
- The `[MCQ]` / `[NAT]` / `[MSQ]` tag must be on its own line right after the `##` heading.
- `**Answer:**` must be the last line before the `---` separator.
- You can use `$...$` for inline math and `$$...$$` for display math (MathJax renders it).

---

## Adding a Question with an Image

1. **Save the image** in `content/{course}/img/`:
   ```
   content/gate-da-prob-stats/img/q013-venn.png
   ```
   Use descriptive filenames. PNG or JPG, keep under 200KB.

2. **Reference in markdown** using a relative path from `img/`:
   ```markdown
   ## Q013

   [MCQ]

   The Venn diagram below shows sets A and B. How many elements are in A ∪ B?

   ![Venn diagram showing sets A and B](img/q013-venn.png)

   - **(A)** 5
   - **(B)** 8
   - **(C)** 10
   - **(D)** 12

   **Answer:** C
   ```

3. **Rebuild** — `generate.py` automatically copies `content/{course}/img/` into each lecture output folder, so the `img/filename.png` path works in the browser and PDF.

---

## Adding a Question to a Lecture

After adding the question to the content file, reference it in the YAML manifest:

**File:** `lectures/{course}/{slug}.yaml`

```yaml
sections:
  - heading: "Combinations"
    questions:
      - Q009
      - Q010
      - Q013    ← add your new question ID here
```

Order matters — questions appear in the order listed.

---

## Adding a New Section to a Lecture

```yaml
sections:
  - heading: "Product Rule & Multiplication Principle"
    questions: [Q001, Q002, Q003, Q004]

  - heading: "Permutations"
    questions: [Q005, Q006, Q007]

  - heading: "My New Section"      ← add a new section block
    questions: [Q013, Q014, Q015]
```

The new section will automatically appear in the sidebar navigation.

---

## Creating a New Lecture

1. **Create a content file** in `content/{course}/`:
   ```
   content/gate-da-prob-stats/02-probability-basics.md
   ```
   Follow the same `## QXXX` + `[TYPE]` + `**Answer:**` format.

2. **Create a YAML manifest** in `lectures/{course}/`:
   ```yaml
   # lectures/gate-da-prob-stats/02-probability-basics.yaml
   title: "Probability Basics"
   course: gate-da-prob-stats
   slug: 02-probability-basics
   date: "2026-06-21"

   sections:
     - heading: "Sample Space & Events"
       questions: [Q101, Q102, Q103]
     - heading: "Conditional Probability"
       questions: [Q104, Q105]
   ```

3. **Rebuild** (see below).

---

## Rebuilding the Site

```bash
cd /Users/vn59a0h/preparation/gate-2026/practice
python scripts/generate.py
```

Output goes to `docs/`. Open `docs/{course}/lecture/{slug}/index.html` in a browser to preview.

**Dependencies** (one-time setup):
```bash
pip install pyyaml jinja2 markdown
pip install playwright && playwright install chromium   # for PDF generation
pip install "qrcode[pil]"                              # for QR codes
```

---

## Math Syntax Quick Reference

| What you type | Renders as |
|---|---|
| `$x^2 + y^2$` | inline math |
| `$$\binom{n}{r} = \frac{n!}{r!(n-r)!}$$` | display (centered) math |
| `$P(A \cup B)$` | P(A ∪ B) |
| `$\frac{1}{2}$` | ½ |

---

## Common Mistakes

| Problem | Fix |
|---|---|
| Question not showing | Check the Q-ID in YAML matches exactly (case-sensitive: `Q013` not `q013`) |
| Math not rendering | Ensure `$` delimiters are closed and no space after opening `$` |
| Image not loading | Filename in markdown must match exactly (case-sensitive on Linux) |
| Options on one line | Options must be `- **(A)**` list format, NOT `A. text` inline |
