"""Q8 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Multi-Agent Creative Drawing by Combining Two Patterns"
SHOT_LINES = (126, 146)
MAX_OUT_LINES = 22
FLOW_TITLE = "Multi-agent loop for a new creative drawing"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: pattern A (spiral)\n+ pattern B (star)", x=0, y=1.3, shape="io"),
    dict(id="pick", text="Each agent picks one\naction from each parent", x=0, y=2.8),
    dict(id="comb", text="Combine them: compose,\nblend, nest or interleave", x=0, y=4.3),
    dict(id="draw", text="Repeat the new action\nn times = new drawing", x=0, y=5.8),
    dict(id="fit", text="Fitness = novelty +\naesthetics + inheritance", x=0, y=7.3),
    dict(id="new", text="New state vs\narchive?", x=0, y=8.9, shape="decision"),
    dict(id="arch", text="Add to shared\narchive", x=4.9, y=8.9, shape="data", w=3.2),
    dict(id="best", text="Update the agent's\nbest drawing", x=0, y=10.5),
    dict(id="more", text="More\nrounds?", x=0, y=12.1, shape="decision"),
    dict(id="out", text="Show best\ndrawings", x=4.9, y=12.1, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="pick"), dict(src="pick", dst="comb"),
    dict(src="comb", dst="draw"), dict(src="draw", dst="fit"), dict(src="fit", dst="new"),
    dict(src="new", dst="arch", label="Yes", exit="r", entry="l"),
    dict(src="new", dst="best", label="No"),
    dict(src="arch", dst="best", exit="b", entry="r", via=[(4.9, 10.5)]),
    dict(src="best", dst="more"),
    dict(src="more", dst="out", label="No", exit="r", entry="l"),
    dict(src="more", dst="pick", label="Yes", exit="l", entry="l",
         via=[(-2.8, 12.1), (-2.8, 2.8)], label_at=(-2.35, 11.75)),
]
