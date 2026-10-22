"""Build one question folder: run code -> output.txt -> IDE screenshot -> flowchart -> notebook -> PDF.

Usage:  python _tools/build.py Q01_GreedyBFS_Website_Chatbot [--preview DIR] [--skip-nb]
Spec:   _tools/specs/qNN.py defines FLOW_NODES, FLOW_EDGES, FLOW_TITLE, SHOT_LINES, MAX_OUT_LINES.
"""
import argparse
import glob
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from flowchart import draw_flowchart  # noqa: E402
from ide_screenshot import render  # noqa: E402

CHROME = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
EDGE = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")


def load_spec(num: str):
    path = TOOLS / "specs" / f"q{num}.py"
    spec = importlib.util.spec_from_file_location(f"spec_q{num}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_code(folder: Path, code: Path) -> str:
    result = subprocess.run([sys.executable, code.name], cwd=folder, capture_output=True,
                            text=True, encoding="utf-8", timeout=600)
    if result.returncode != 0:
        raise SystemExit(f"Code failed:\n{result.stdout}\n{result.stderr}")
    return result.stdout


def build_notebook(folder: Path, code: Path, num: str, title: str) -> Path:
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor

    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_markdown_cell(
            f"# Q{num} - {title}\n\nSame code as `{code.name}`. Works locally in Jupyter or on Google Colab "
            "(upload this notebook, then *Runtime -> Run all*)."),
        nbformat.v4.new_code_cell(code.read_text(encoding="utf-8")),
        nbformat.v4.new_code_cell(
            "from IPython.display import Image, display\nimport glob\n"
            f"for p in sorted(glob.glob('images/q{num}_chart*.png')):\n    display(Image(p))"),
    ]
    ExecutePreprocessor(timeout=600, kernel_name="python3").preprocess(nb, {"metadata": {"path": str(folder)}})
    out = folder / f"q{num}_code.ipynb"
    nbformat.write(nb, out)
    return out


def html_to_pdf(html: Path, pdf: Path) -> None:
    browser = CHROME if CHROME.exists() else EDGE
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([str(browser), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={profile}", "--virtual-time-budget=4000",
                        f"--print-to-pdf={pdf}", html.resolve().as_uri()],
                       check=True, capture_output=True, timeout=180)


def preview(pdf: Path, out_dir: Path, num: str) -> list:
    import fitz
    from PIL import Image

    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    pages = []
    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
        pages.append(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
    paths = []
    for i in range(0, len(pages), 3):
        group = pages[i:i + 3]
        sheet = Image.new("RGB", (sum(p.width for p in group) + 12 * (len(group) - 1), group[0].height), "#888888")
        x = 0
        for p in group:
            sheet.paste(p, (x, 0))
            x += p.width + 12
        path = out_dir / f"q{num}_preview_{i // 3 + 1}.png"
        sheet.save(path)
        paths.append(str(path))
    return [len(pages)] + paths


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--preview")
    ap.add_argument("--skip-nb", action="store_true")
    args = ap.parse_args()

    folder = (ROOT / args.folder).resolve()
    num = folder.name[1:3]
    code = folder / f"q{num}_code.py"
    spec = load_spec(num)
    (folder / "images").mkdir(exist_ok=True)

    output = run_code(folder, code)
    (folder / f"q{num}_output.txt").write_text(output, encoding="utf-8")
    print(f"[run] ok, {len(output.splitlines())} output lines")

    draw_flowchart(spec.FLOW_NODES, spec.FLOW_EDGES, str(folder / "images" / f"q{num}_flowchart.png"),
                   title=getattr(spec, "FLOW_TITLE", ""), scale=getattr(spec, "FLOW_SCALE", 1.0))
    render(code, output, folder / "images" / f"q{num}_ide_run.png",
           line_range=getattr(spec, "SHOT_LINES", None), max_out_lines=getattr(spec, "MAX_OUT_LINES", 26),
           cwd_label=f"C:\\Users\\USER\\questions\\Answers\\{folder.name}")
    print("[figures] flowchart + IDE screenshot written")

    if not args.skip_nb:
        build_notebook(folder, code, num, getattr(spec, "TITLE", folder.name))
        print("[notebook] executed and saved")

    html = folder / f"Q{num}_Answer.html"
    pdf = folder / f"Q{num}_Answer.pdf"
    html_to_pdf(html, pdf)
    print(f"[pdf] {pdf.name}")
    if args.preview:
        info = preview(pdf, Path(args.preview), num)
        print(f"[preview] {info[0]} pages ->", *info[1:], sep="\n  ")
    for p in sorted(glob.glob(str(folder / "images" / "*.png"))):
        print("  img:", Path(p).name)


if __name__ == "__main__":
    main()
