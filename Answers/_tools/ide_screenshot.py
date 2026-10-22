"""Render an IDE-style screenshot of a real code run: editor pane + terminal pane.

The code shown is the actual file and the terminal text is the actual captured output,
so the image documents a genuine run (only the window frame is drawn).
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

FONT_DIR = Path("C:/Windows/Fonts")
MONO = str(FONT_DIR / "consola.ttf")
UI = str(FONT_DIR / "segoeui.ttf")

WIDTH = 1100
CODE_SIZE, CODE_LINE_H = 15, 21
TERM_SIZE, TERM_LINE_H = 14, 19
TITLE_H, TAB_H, STATUS_H, TERM_HEAD_H = 34, 34, 24, 34
ACTIVITY_W, GUTTER_W = 46, 62

BG = "#1e1e1e"
COLORS = {
    "title_bg": "#3c3c3c", "title_fg": "#cccccc", "activity": "#333333",
    "tab_bar": "#252526", "tab_active": "#1e1e1e", "tab_fg": "#ffffff",
    "gutter_fg": "#858585", "text": "#d4d4d4", "term_head": "#e7e7e7",
    "term_fg": "#cccccc", "prompt": "#3b8eea", "status": "#007acc", "status_fg": "#ffffff",
    "divider": "#454545",
}
TOKEN_COLORS = [
    (Token.Comment, "#6a9955"),
    (Token.Literal.String, "#ce9178"),
    (Token.Literal.Number, "#b5cea8"),
    (Token.Keyword.Constant, "#569cd6"),
    (Token.Keyword.Namespace, "#c586c0"),
    (Token.Keyword, "#c586c0"),
    (Token.Name.Function, "#dcdcaa"),
    (Token.Name.Class, "#4ec9b0"),
    (Token.Name.Builtin.Pseudo, "#569cd6"),
    (Token.Name.Builtin, "#dcdcaa"),
    (Token.Name.Decorator, "#dcdcaa"),
    (Token.Operator.Word, "#569cd6"),
    (Token.Name, "#9cdcfe"),
]
DEF_KEYWORDS = {"def", "class", "lambda"}


def token_color(ttype, value):
    if ttype in Token.Keyword and value in DEF_KEYWORDS:
        return "#569cd6"
    for base, color in TOKEN_COLORS:
        if ttype in base:
            return color
    return COLORS["text"]


def highlighted_lines(code):
    """Split pygments tokens into per-line lists of (text, color)."""
    lines, current = [], []
    for ttype, value in lex(code, PythonLexer()):
        parts = value.split("\n")
        for i, part in enumerate(parts):
            if part:
                current.append((part, token_color(ttype, part)))
            if i < len(parts) - 1:
                lines.append(current)
                current = []
    if current:
        lines.append(current)
    return lines


def render(code_path, output_text, out_png, line_range=None, max_out_lines=26, cwd_label=None):
    code_path = Path(code_path)
    code = code_path.read_text(encoding="utf-8")
    all_lines = highlighted_lines(code)
    start, end = line_range or (1, len(all_lines))
    shown = all_lines[start - 1:end]

    out_lines = output_text.rstrip("\n").splitlines()
    if len(out_lines) > max_out_lines:
        head = max_out_lines - 4
        out_lines = out_lines[:head] + ["   ..."] + out_lines[-3:]
    cwd_label = cwd_label or str(code_path.parent)
    prompt = f"PS {cwd_label}> "
    command = f"python {code_path.name}"
    term_rows = [("prompt", prompt + command)] + [("out", ln) for ln in out_lines] + [("prompt", prompt)]

    editor_h = len(shown) * CODE_LINE_H + 16
    term_h = TERM_HEAD_H + len(term_rows) * TERM_LINE_H + 12
    height = TITLE_H + TAB_H + editor_h + term_h + STATUS_H

    img = Image.new("RGB", (WIDTH, height), BG)
    d = ImageDraw.Draw(img)
    mono = ImageFont.truetype(MONO, CODE_SIZE)
    mono_term = ImageFont.truetype(MONO, TERM_SIZE)
    ui = ImageFont.truetype(UI, 14)
    ui_small = ImageFont.truetype(UI, 13)

    # title bar with window controls
    d.rectangle([0, 0, WIDTH, TITLE_H], fill=COLORS["title_bg"])
    title = f"{code_path.name} - {code_path.parent.name} - Python IDE"
    tw = d.textlength(title, font=ui)
    d.text(((WIDTH - tw) / 2, 8), title, fill=COLORS["title_fg"], font=ui)
    for i, sym in enumerate(["\u2014", "\u25a1", "\u2715"]):
        d.text((WIDTH - 130 + i * 44, 7), sym, fill=COLORS["title_fg"], font=ui)
    d.text((14, 8), "File  Edit  View  Run  Terminal  Help", fill="#bbbbbb", font=ui_small)

    # activity bar
    top = TITLE_H
    d.rectangle([0, top, ACTIVITY_W, height - STATUS_H], fill=COLORS["activity"])
    for i in range(4):
        y = top + 18 + i * 46
        d.rounded_rectangle([13, y, 33, y + 20], radius=4, outline="#858585", width=2)

    # tab bar
    d.rectangle([ACTIVITY_W, top, WIDTH, top + TAB_H], fill=COLORS["tab_bar"])
    tab_w = d.textlength(code_path.name, font=ui) + 60
    d.rectangle([ACTIVITY_W, top, ACTIVITY_W + tab_w, top + TAB_H], fill=COLORS["tab_active"])
    d.line([ACTIVITY_W, top, ACTIVITY_W + tab_w, top], fill="#007acc", width=2)
    d.text((ACTIVITY_W + 30, top + 8), code_path.name, fill=COLORS["tab_fg"], font=ui)
    d.ellipse([ACTIVITY_W + 12, top + 13, ACTIVITY_W + 20, top + 21], fill="#3e9bd6")

    # editor
    y = top + TAB_H + 8
    x0 = ACTIVITY_W + GUTTER_W + 14
    for offset, segments in enumerate(shown):
        num = str(start + offset)
        nw = d.textlength(num, font=mono)
        d.text((ACTIVITY_W + GUTTER_W - nw - 6, y), num, fill=COLORS["gutter_fg"], font=mono)
        x = x0
        for text, color in segments:
            text = text.replace("\t", "    ")
            if x > WIDTH - 20:
                break
            d.text((x, y), text, fill=color, font=mono)
            x += d.textlength(text, font=mono)
        y += CODE_LINE_H

    # terminal
    ty = top + TAB_H + editor_h
    d.line([ACTIVITY_W, ty, WIDTH, ty], fill=COLORS["divider"], width=1)
    labels = ["PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL"]
    lx = ACTIVITY_W + 16
    for lab in labels:
        color = COLORS["term_head"] if lab == "TERMINAL" else "#969696"
        d.text((lx, ty + 8), lab, fill=color, font=ui_small)
        w = d.textlength(lab, font=ui_small)
        if lab == "TERMINAL":
            d.line([lx, ty + 29, lx + w, ty + 29], fill="#e7e7e7", width=1)
        lx += w + 26
    yy = ty + TERM_HEAD_H + 4
    for kind, text in term_rows:
        if kind == "prompt":
            d.text((ACTIVITY_W + 16, yy), prompt, fill=COLORS["prompt"], font=mono_term)
            pw = d.textlength(prompt, font=mono_term)
            d.text((ACTIVITY_W + 16 + pw, yy), text[len(prompt):], fill="#ffffff", font=mono_term)
        else:
            d.text((ACTIVITY_W + 16, yy), text, fill=COLORS["term_fg"], font=mono_term)
        yy += TERM_LINE_H

    # status bar
    sy = height - STATUS_H
    d.rectangle([0, sy, WIDTH, height], fill=COLORS["status"])
    py = f"Python {sys.version.split()[0]}"
    d.text((12, sy + 3), "\u2387 main", fill=COLORS["status_fg"], font=ui_small)
    right = f"Ln {end}, Col 1    Spaces: 4    UTF-8    CRLF    {py}"
    rw = d.textlength(right, font=ui_small)
    d.text((WIDTH - rw - 16, sy + 3), right, fill=COLORS["status_fg"], font=ui_small)

    img.save(out_png)
    return out_png
