"""Q13 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "P-Creativity as a Special Function of H-Creativity"
SHOT_LINES = (54, 77)
MAX_OUT_LINES = 26
FLOW_TITLE = "Constrained space -> expand -> eliminate -> combine"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: idea j, pool,\narchives, tau, n", x=0, y=1.3, shape="io"),
    dict(id="init", text="centre = j\nradius r = 1 (small)", x=0, y=2.8),
    dict(id="look", text="States unvisited\ninside radius r", x=0, y=4.3),
    dict(id="elim", text="Eliminate visited and\nlow-value states", x=0, y=5.8),
    dict(id="cap", text="r reached cap?\n(space empty)", x=0, y=7.5, shape="decision"),
    dict(id="grow", text="r = r + 1\n(expand space)", x=4.9, y=7.5, w=3.4),
    dict(id="comb", text="Combine top-n states\n-> new states", x=0, y=9.3),
    dict(id="beyond", text="Any new state\nbeyond covered space?", x=0, y=11.1, shape="decision"),
    dict(id="move", text="Centre moves to best\nnew state (j -> n -> i)", x=0, y=12.9),
    dict(id="ret", text="Return ranked\nfinal states", x=4.9, y=11.1, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="init"), dict(src="init", dst="look"),
    dict(src="look", dst="elim"), dict(src="elim", dst="cap"),
    dict(src="cap", dst="grow", label="No", exit="r", entry="l"),
    dict(src="grow", dst="look", exit="r", entry="r", via=[(7.3, 7.5), (7.3, 4.3)]),
    dict(src="cap", dst="comb", label="Yes"),
    dict(src="comb", dst="beyond"),
    dict(src="beyond", dst="ret", label="No", exit="r", entry="l"),
    dict(src="beyond", dst="move", label="Yes"),
    dict(src="move", dst="look", exit="l", entry="l", via=[(-2.8, 12.9), (-2.8, 4.3)]),
]
