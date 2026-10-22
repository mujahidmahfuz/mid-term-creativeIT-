"""Q9 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "P-creativity to H-creativity with an Evolutionary Algorithm"
SHOT_LINES = (45, 75)
MAX_OUT_LINES = 20
FLOW_TITLE = "Evolutionary loop with P- and H-creativity checks"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: 300 known designs\n(history), own archive empty", x=0, y=1.3, shape="io", w=4.0),
    dict(id="init", text="Random population\nof vehicle designs", x=0, y=2.8),
    dict(id="eval", text="Fitness = usefulness\n+ novelty", x=0, y=4.3),
    dict(id="label", text="Label each design:\nP-creative / H-creative", x=0, y=5.8),
    dict(id="arch", text="Own archive P +\nhistory archive H", x=4.9, y=5.8, shape="data", w=3.4),
    dict(id="low", text="H-creative\nrate too low?", x=0, y=7.4, shape="decision"),
    dict(id="exp", text="Expand space: global\narchive + new gene", x=4.9, y=7.4, w=3.6),
    dict(id="sel", text="Select, crossover,\nmutate: next generation", x=0, y=9.0),
    dict(id="done", text="Last\ngeneration?", x=0, y=10.6, shape="decision"),
    dict(id="out", text="Report P- and\nH-creative designs", x=4.9, y=10.6, shape="terminal", w=3.2, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="init"), dict(src="init", dst="eval"),
    dict(src="eval", dst="label"),
    dict(src="arch", dst="label", exit="l", entry="r"),
    dict(src="label", dst="low"),
    dict(src="low", dst="exp", label="Yes", exit="r", entry="l"),
    dict(src="low", dst="sel", label="No"),
    dict(src="exp", dst="sel", exit="b", entry="r", via=[(4.9, 9.0)]),
    dict(src="sel", dst="done"),
    dict(src="done", dst="out", label="Yes", exit="r", entry="l"),
    dict(src="done", dst="eval", label="No", exit="l", entry="l",
         via=[(-2.8, 10.6), (-2.8, 4.3)], label_at=(-2.35, 10.25)),
]
