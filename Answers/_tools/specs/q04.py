"""Q4 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Best-First vs Hill Climbing, Expanding Search and Action Space"
SHOT_LINES = (107, 133)
MAX_OUT_LINES = 20
FLOW_TITLE = "Best-first search with an expandable action space"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: design S0,\nactions a-e, score C", x=0, y=1.3, shape="io"),
    dict(id="init", text="OPEN = {S0}\nSEEN = {S0}", x=0, y=2.7),
    dict(id="empty", text="OPEN empty or\nbudget used?", x=0, y=4.3, shape="decision"),
    dict(id="pop", text="n = best-scoring\ndesign in OPEN", x=0, y=5.9),
    dict(id="exp", text="Apply every action:\nnew designs -> OPEN", x=0, y=7.4),
    dict(id="best", text="Keep the best design\nseen so far", x=0, y=8.9),
    dict(id="new", text="Add new actions\nf, g (bigger action space)", x=4.9, y=7.4, shape="data", w=3.8),
    dict(id="out", text="Return best\ndesign", x=4.9, y=4.3, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="init"), dict(src="init", dst="empty"),
    dict(src="empty", dst="pop", label="No"),
    dict(src="empty", dst="out", label="Yes", exit="r", entry="l"),
    dict(src="pop", dst="exp"),
    dict(src="exp", dst="best"),
    dict(src="new", dst="exp", exit="l", entry="r", label="optional"),
    dict(src="best", dst="empty", exit="l", entry="l", via=[(-2.8, 8.9), (-2.8, 4.3)]),
]
