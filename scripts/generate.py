"""
generate.py — Practice Set Generator

Reads lecture manifests from lectures/**/*.yaml,
resolves questions from registry,
renders HTML + PDF + QR into docs/{course}/lecture/{slug}/
"""

import sys
import shutil
import subprocess
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from parse import parse_content_dir

try:
    import qrcode
    from PIL import Image
except ImportError:
    qrcode = None

BASE = Path(__file__).parent.parent
CONTENT_DIR = BASE / "content"
LECTURES_DIR = BASE / "lectures"
TEMPLATES_DIR = BASE / "templates"
DOCS_DIR = BASE / "docs"
SCRIPTS_DIR = BASE / "scripts"

# Base URL for published site (no trailing slash)
SITE_BASE_URL = "https://ranjanchoubey.github.io/practice-sets"


def load_manifest(yaml_file: Path) -> dict:
    with open(yaml_file) as f:
        return yaml.safe_load(f)


def render_html(template_name: str, context: dict, env: Environment) -> str:
    tmpl = env.get_template(template_name)
    return tmpl.render(**context)


def generate_qr(url: str, out_path: Path):
    if qrcode is None:
        print(f"  [QR] skipped — install qrcode[pil]: {out_path}", file=sys.stderr)
        return
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)
    print(f"  [QR] {out_path.relative_to(BASE)}", file=sys.stderr)


def generate_pdf(html_file: Path, pdf_file: Path):
    """Use Playwright headless Chromium to print PDF."""
    script = f"""
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file://{html_file.resolve()}", wait_until="networkidle")
        await page.pdf(
            path="{pdf_file.resolve()}",
            format="A4",
            margin={{"top": "20mm", "bottom": "20mm", "left": "18mm", "right": "18mm"}},
            print_background=True,
        )
        await browser.close()

asyncio.run(run())
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  [PDF] ERROR: {result.stderr}", file=sys.stderr)
    else:
        print(f"  [PDF] {pdf_file.relative_to(BASE)}", file=sys.stderr)


def process_lecture(manifest: dict, registry: dict, env: Environment):
    course = manifest["course"]
    slug = manifest["slug"]
    title = manifest["title"]
    question_ids = manifest["questions"]

    # Resolve questions — fail on missing
    questions = []
    for qid in question_ids:
        if qid not in registry:
            print(f"  [ERROR] {slug}: question {qid} not found in registry", file=sys.stderr)
            sys.exit(1)
        questions.append(registry[qid])

    # Output directory
    out_dir = DOCS_DIR / course / "lecture" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    canonical_url = f"{SITE_BASE_URL}/{course}/lecture/{slug}/"
    pdf_filename = f"{slug}.pdf"
    qr_filename = "qr.png"

    # Render HTML
    html_content = render_html(
        "lecture.html",
        {
            "title": title,
            "course": course,
            "slug": slug,
            "questions": questions,
            "canonical_url": canonical_url,
            "pdf_filename": pdf_filename,
            "qr_filename": qr_filename,
            "num_questions": len(questions),
        },
        env,
    )
    html_file = out_dir / "index.html"
    html_file.write_text(html_content, encoding="utf-8")
    print(f"  [HTML] {html_file.relative_to(BASE)}", file=sys.stderr)

    # Render PDF HTML (print-optimized, no nav)
    pdf_html_content = render_html(
        "lecture-print.html",
        {
            "title": title,
            "course": course,
            "slug": slug,
            "questions": questions,
        },
        env,
    )
    pdf_html_file = out_dir / "_print.html"
    pdf_html_file.write_text(pdf_html_content, encoding="utf-8")

    # Generate PDF
    pdf_file = out_dir / pdf_filename
    generate_pdf(pdf_html_file, pdf_file)

    # Generate QR code
    qr_file = out_dir / qr_filename
    generate_qr(canonical_url, qr_file)

    return {
        "course": course,
        "slug": slug,
        "title": title,
        "url": canonical_url,
        "num_questions": len(questions),
    }


def generate_index(all_lectures: list, env: Environment):
    """Generate docs/index.html listing all courses/lectures."""
    # Group by course
    courses = {}
    for lec in all_lectures:
        c = lec["course"]
        courses.setdefault(c, []).append(lec)

    html = render_html("index.html", {"courses": courses, "site_base": SITE_BASE_URL}, env)
    index_file = DOCS_DIR / "index.html"
    index_file.write_text(html, encoding="utf-8")
    print(f"  [INDEX] {index_file.relative_to(BASE)}", file=sys.stderr)


def copy_assets():
    """Copy static assets (CSS, JS) to docs/assets/"""
    src = TEMPLATES_DIR / "assets"
    dst = DOCS_DIR / "assets"
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def main():
    print("[generate] Parsing question bank...", file=sys.stderr)
    registry = parse_content_dir(CONTENT_DIR)

    print("[generate] Loading templates...", file=sys.stderr)
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,  # Markdown content is pre-rendered to HTML
    )

    # Register markdown filter
    try:
        import markdown
        md_extensions = ["tables", "fenced_code", "footnotes"]
        def md_filter(text):
            return markdown.markdown(text, extensions=md_extensions)
        env.filters["markdown"] = md_filter
    except ImportError:
        def md_filter(text):
            return f"<pre>{text}</pre>"
        env.filters["markdown"] = md_filter
        print("  [WARN] markdown package not found — install: pip install markdown", file=sys.stderr)

    DOCS_DIR.mkdir(exist_ok=True)
    copy_assets()

    print("[generate] Processing lectures...", file=sys.stderr)
    all_lectures = []
    for yaml_file in sorted(LECTURES_DIR.rglob("*.yaml")):
        manifest = load_manifest(yaml_file)
        print(f"\n  Lecture: {manifest['slug']} ({manifest['course']})", file=sys.stderr)
        result = process_lecture(manifest, registry, env)
        all_lectures.append(result)

    print("\n[generate] Building index...", file=sys.stderr)
    generate_index(all_lectures, env)

    print(f"\n[generate] Done — {len(all_lectures)} lectures generated → {DOCS_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
