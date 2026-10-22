"""Q5 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Simulated Annealing for Product Recommendation"
SHOT_LINES = (82, 102)
MAX_OUT_LINES = 30
FLOW_TITLE = "Simulated annealing for a recommendation slate"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: start slate S,\nT0 = 0.10, alpha = 0.97", x=0, y=1.3, shape="io"),
    dict(id="stop", text="T small or\niterations done?", x=0, y=2.95, shape="decision"),
    dict(id="nb", text="Make neighbour S':\nswap one product", x=0, y=4.6),
    dict(id="d", text="delta = score(S')\n- score(S)", x=0, y=6.05),
    dict(id="better", text="delta > 0 ?", x=0, y=7.6, shape="decision"),
    dict(id="prob", text="rand < e^(delta/T) ?", x=0, y=9.3, shape="decision", w=3.9),
    dict(id="acc", text="Accept: S = S',\nupdate best", x=4.9, y=9.3, w=3.4),
    dict(id="cool", text="Cool down:\nT = alpha * T", x=0, y=10.95),
    dict(id="out", text="Return best\nslate", x=4.9, y=2.95, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="stop"),
    dict(src="stop", dst="out", label="Yes", exit="r", entry="l"),
    dict(src="stop", dst="nb", label="No"),
    dict(src="nb", dst="d"), dict(src="d", dst="better"),
    dict(src="better", dst="acc", label="Yes", exit="r", entry="t", via=[(4.9, 7.6)]),
    dict(src="better", dst="prob", label="No"),
    dict(src="prob", dst="acc", label="Yes", exit="r", entry="l"),
    dict(src="prob", dst="cool", label="No (keep S)"),
    dict(src="acc", dst="cool", exit="b", entry="r", via=[(4.9, 10.95)]),
    dict(src="cool", dst="stop", exit="l", entry="l", via=[(-2.8, 10.95), (-2.8, 2.95)]),
]
