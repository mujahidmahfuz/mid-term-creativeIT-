"""Q12 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Expanding the Action Space by Combining Two Basic Actions"
SHOT_LINES = (68, 88)
MAX_OUT_LINES = 28
FLOW_TITLE = "Expand action space, then iterative deepening"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: game map,\nbasic actions A0", x=0, y=1.3, shape="io"),
    dict(id="pair", text="Pair every two basic\nactions -> new actions", x=0, y=2.8),
    dict(id="drop", text="Drop pairs that\ncancel (Up+Down)", x=0, y=4.3),
    dict(id="a", text="A = basic + combined\n(4 -> 12 actions)", x=0, y=5.8),
    dict(id="d", text="d = 1", x=0, y=7.2),
    dict(id="dls", text="Depth-limited search\nwith A, depth d", x=0, y=8.6),
    dict(id="g", text="G(A, d) = best value\nfound (coins + exit)", x=0, y=10.1),
    dict(id="done", text="d = max depth?", x=0, y=11.8, shape="decision"),
    dict(id="inc", text="d = d + 1", x=-4.9, y=11.8, w=3.0),
    dict(id="ret", text="Return best path\nand G(A, d)", x=4.9, y=11.8, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="pair"), dict(src="pair", dst="drop"),
    dict(src="drop", dst="a"), dict(src="a", dst="d"), dict(src="d", dst="dls"),
    dict(src="dls", dst="g"), dict(src="g", dst="done"),
    dict(src="done", dst="ret", label="Yes", exit="r", entry="l"),
    dict(src="done", dst="inc", label="No", exit="l", entry="r"),
    dict(src="inc", dst="dls", exit="t", entry="l", via=[(-4.9, 8.6)]),
]
