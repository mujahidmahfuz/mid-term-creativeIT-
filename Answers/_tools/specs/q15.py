"""Q15 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Product Recommendation as Heuristic Search (Hill Climbing + A*)"
SHOT_LINES = (59, 88)
MAX_OUT_LINES = 30
FLOW_TITLE = "Hill climbing for recommendation"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Start product, user\nvector u, product list", x=0, y=1.3, shape="io"),
    dict(id="cur", text="current = start", x=0, y=2.7),
    dict(id="nb", text="List same-category\nneighbours of current", x=0, y=4.15),
    dict(id="best", text="best = neighbour with\nlowest h = ||p - u||", x=0, y=5.65),
    dict(id="cmp", text="h(best) <\nh(current)?", x=0, y=7.3, shape="decision"),
    dict(id="mv", text="current = best", x=0, y=9.1, w=3.2),
    dict(id="out", text="Recommend\ncurrent product", x=4.9, y=7.3, shape="terminal", w=3.2, h=1.0),
    dict(id="fix", text="Fix: random restart,\nannealing, jumps", x=4.9, y=5.65, shape="data"),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="cur"), dict(src="cur", dst="nb"),
    dict(src="nb", dst="best"), dict(src="best", dst="cmp"),
    dict(src="cmp", dst="mv", label="Yes"),
    dict(src="cmp", dst="out", label="No", exit="r", entry="l"),
    dict(src="out", dst="fix", exit="t", entry="b"),
    dict(src="mv", dst="nb", exit="l", entry="l", via=[(-2.8, 9.1), (-2.8, 4.15)]),
]
