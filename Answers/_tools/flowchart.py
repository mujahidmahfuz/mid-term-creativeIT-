"""Draw clean, conventional flowcharts with matplotlib.

Spec format (coordinates are in abstract grid units, y grows downward):
    nodes = [dict(id="start", text="Start", x=0, y=0, shape="terminal"), ...]
    edges = [dict(src="start", dst="init", label="", exit="b", entry="t", via=[(x, y)]), ...]
Shapes: terminal, process, decision, io, data.  Sides: t, b, l, r.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

STYLE = {
    "terminal": {"fc": "#d9f2ea", "ec": "#2a9d8f"},
    "process": {"fc": "#e6eefa", "ec": "#3a6ea5"},
    "decision": {"fc": "#fff1d0", "ec": "#d98e04"},
    "io": {"fc": "#f1e6fa", "ec": "#7b5ea7"},
    "data": {"fc": "#fde8e4", "ec": "#c8553d"},
}
SIZE = {"terminal": (2.6, 0.8), "process": (3.8, 0.95), "decision": (3.6, 1.5),
        "io": (3.8, 0.95), "data": (3.6, 0.95)}
TEXT = "#1f2937"
LINE = "#4b5563"


def _size(node: dict) -> tuple[float, float]:
    w, h = SIZE[node.get("shape", "process")]
    return node.get("w", w), node.get("h", h)


def _anchor(node: dict, side: str) -> tuple[float, float]:
    w, h = _size(node)
    x, y = node["x"], node["y"]
    return {"t": (x, y - h / 2), "b": (x, y + h / 2), "l": (x - w / 2, y), "r": (x + w / 2, y)}[side]


def _draw_node(ax, node: dict) -> None:
    shape = node.get("shape", "process")
    style = STYLE[shape]
    w, h = _size(node)
    x, y = node["x"], node["y"]
    kw = dict(facecolor=style["fc"], edgecolor=style["ec"], linewidth=2.2, zorder=2)
    if shape == "terminal":
        patch = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.33", **kw)
    elif shape == "decision":
        patch = Polygon([(x, y - h / 2), (x + w / 2, y), (x, y + h / 2), (x - w / 2, y)], closed=True, **kw)
    elif shape == "io":
        s = 0.22
        patch = Polygon([(x - w / 2 + s, y - h / 2), (x + w / 2 + s, y - h / 2),
                         (x + w / 2 - s, y + h / 2), (x - w / 2 - s, y + h / 2)], closed=True, **kw)
    else:
        patch = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.06", **kw)
    ax.add_patch(patch)
    weight = "bold" if shape == "terminal" else "normal"
    ax.text(x, y, node["text"], ha="center", va="center", fontsize=node.get("fs", 14.5),
            color=TEXT, zorder=3, fontweight=weight, linespacing=1.25)


def _draw_edge(ax, nodes: dict, edge: dict) -> None:
    src, dst = nodes[edge["src"]], nodes[edge["dst"]]
    pts = [_anchor(src, edge.get("exit", "b"))] + list(edge.get("via", [])) + [_anchor(dst, edge.get("entry", "t"))]
    for (x1, y1), (x2, y2) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x1, x2], [y1, y2], color=LINE, lw=2.0, zorder=1, solid_capstyle="round")
    ax.annotate("", xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle="-|>", color=LINE, lw=2.0, mutation_scale=22), zorder=1)
    label = edge.get("label")
    if label:
        (x1, y1), (x2, y2) = pts[0], pts[1]
        lx, ly = edge.get("label_at", ((x1 + x2) / 2, (y1 + y2) / 2))
        ax.text(lx, ly, label, fontsize=12.5, color="#111827", ha="center", va="center", zorder=4,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none"))


def draw_flowchart(nodes: list, edges: list, out_path: str, title: str = "", scale: float = 1.0) -> str:
    by_id = {n["id"]: n for n in nodes}
    xs = [n["x"] for n in nodes]
    ys = [n["y"] for n in nodes]
    pad_x, pad_y = 2.2, 1.0
    x_min, x_max = min(xs) - pad_x, max(xs) + pad_x
    y_min, y_max = min(ys) - pad_y, max(ys) + pad_y
    for e in edges:
        for vx, vy in e.get("via", []):
            x_min, x_max = min(x_min, vx - 0.6), max(x_max, vx + 0.6)
            y_min, y_max = min(y_min, vy - 0.6), max(y_max, vy + 0.6)
    width, height = (x_max - x_min) * 0.95 * scale, (y_max - y_min) * 0.95 * scale
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_max, y_min)
    ax.set_aspect("equal")
    ax.axis("off")
    for e in edges:
        _draw_edge(ax, by_id, e)
    for n in nodes:
        _draw_node(ax, n)
    if title:
        ax.set_title(title, fontsize=16, fontweight="bold", color=TEXT, pad=10)
    fig.savefig(out_path, dpi=110, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path
