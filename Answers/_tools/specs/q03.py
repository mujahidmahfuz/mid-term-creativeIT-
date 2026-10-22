"""Q3 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Hill Climbing for Airport Design and Gate Arrangement"
SHOT_LINES = (65, 86)
MAX_OUT_LINES = 28
FLOW_TITLE = "Steepest-ascent hill climbing for the airport"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: blueprint A,\nactions a-e, score C", x=0, y=1.3, shape="io"),
    dict(id="cur", text="current = blueprint A", x=0, y=2.7),
    dict(id="gen", text="B: apply every legal\naction a-e -> neighbours", x=0, y=4.2),
    dict(id="pick", text="best = neighbour with\nthe highest score C", x=0, y=5.7),
    dict(id="dec", text="score(best) >\nscore(current)?", x=0, y=7.3, shape="decision"),
    dict(id="move", text="current = best\n(take one small step)", x=0, y=8.9),
    dict(id="stop", text="Return current\n(peak / local max)", x=4.9, y=7.3, shape="terminal",
         w=3.0, h=1.0),
    dict(id="rr", text="Random restart:\nnew blueprint", x=4.9, y=2.7, shape="data", w=3.2),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="cur"), dict(src="cur", dst="gen"),
    dict(src="gen", dst="pick"), dict(src="pick", dst="dec"),
    dict(src="dec", dst="move", label="Yes"),
    dict(src="dec", dst="stop", label="No", exit="r", entry="l"),
    dict(src="move", dst="gen", exit="l", entry="l", via=[(-2.8, 8.9), (-2.8, 4.2)]),
    dict(src="rr", dst="cur", exit="l", entry="r", label="optional"),
]
