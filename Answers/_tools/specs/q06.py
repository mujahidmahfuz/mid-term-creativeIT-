"""Q6 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Creative Product Agent: GA + Semi-Supervised Learning"
SHOT_LINES = (133, 154)
MAX_OUT_LINES = 30
FLOW_TITLE = "Creative agent: learn, evolve, share, test"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: current product,\nfew labelled launches", x=0, y=1.3, shape="io"),
    dict(id="ssl", text="Self-training on labelled\n+ unlabelled ideas", x=0, y=2.8),
    dict(id="init", text="Each agent starts an\nisland of random ideas", x=0, y=4.3),
    dict(id="fit", text="Score ideas: success\n+ novelty - cost", x=0, y=5.8),
    dict(id="ops", text="Select, crossover,\nmutate (3 agents)", x=0, y=7.3),
    dict(id="mig", text="Every 5 generations:\nshare best genes", x=0, y=8.8, shape="data"),
    dict(id="done", text="Generations\ndone?", x=0, y=10.45, shape="decision"),
    dict(id="top", text="Show top 3 ideas\n(choices, not answers)", x=0, y=12.2, shape="terminal", w=3.8),
    dict(id="fb", text="Market test results\nbecome new labels", x=4.9, y=12.2, shape="data", w=3.8),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="ssl"), dict(src="ssl", dst="init"),
    dict(src="init", dst="fit"), dict(src="fit", dst="ops"), dict(src="ops", dst="mig"),
    dict(src="mig", dst="done"),
    dict(src="done", dst="fit", label="No", exit="l", entry="l", via=[(-2.8, 10.45), (-2.8, 5.8)]),
    dict(src="done", dst="top", label="Yes"),
    dict(src="top", dst="fb", exit="r", entry="l"),
    dict(src="fb", dst="ssl", exit="r", entry="r", via=[(7.6, 12.2), (7.6, 2.8)],
         label="learn set evolves", label_at=(7.6, 7.5)),
]
