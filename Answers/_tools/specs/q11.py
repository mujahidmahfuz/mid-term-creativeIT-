"""Q11 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Manhattan-Distance Iterative Deepening for Mobile Phone Features"
SHOT_LINES = (53, 81)
MAX_OUT_LINES = 24
FLOW_TITLE = "Manhattan IDS with conceptual space expansion"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: phone S0,\nscore = utility + novelty", x=0, y=1.3, shape="io"),
    dict(id="init", text="d = 0, best = S0,\nstale = 0", x=0, y=2.7),
    dict(id="dls", text="DLS over the ball\n|s - S0| <= d, score ring", x=0, y=4.2),
    dict(id="gain", text="Ring beats best\nby >= 1 point?", x=0, y=5.9, shape="decision"),
    dict(id="upd", text="best = ring top,\nstale = 0", x=4.9, y=5.9, w=3.4),
    dict(id="stale", text="stale = stale + 1", x=0, y=7.5),
    dict(id="inc", text="d = d + 1\n(next ring)", x=4.9, y=7.5, w=3.4),
    dict(id="plat", text="stale = 2?\n(plateau)", x=0, y=9.1, shape="decision"),
    dict(id="newdim", text="New feature\nto add?", x=0, y=10.9, shape="decision"),
    dict(id="add", text="Add dimension (sensor),\nreset d = 0", x=0, y=12.5),
    dict(id="ret", text="Return best\ndesigns", x=4.9, y=10.9, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="init"), dict(src="init", dst="dls"),
    dict(src="dls", dst="gain"),
    dict(src="gain", dst="upd", label="Yes", exit="r", entry="l"),
    dict(src="gain", dst="stale", label="No"),
    dict(src="upd", dst="inc"),
    dict(src="stale", dst="plat"),
    dict(src="plat", dst="inc", label="No", exit="r", entry="b", via=[(4.9, 9.1)],
         label_at=(2.6, 9.1)),
    dict(src="plat", dst="newdim", label="Yes"),
    dict(src="inc", dst="dls", exit="r", entry="r", via=[(7.3, 7.5), (7.3, 4.2)]),
    dict(src="newdim", dst="ret", label="No", exit="r", entry="l"),
    dict(src="newdim", dst="add", label="Yes"),
    dict(src="add", dst="dls", exit="l", entry="l", via=[(-2.8, 12.5), (-2.8, 4.2)]),
]
