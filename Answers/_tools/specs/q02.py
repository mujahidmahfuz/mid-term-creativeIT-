"""Q2 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Goal-Based News Agent with a Genetic Algorithm"
SHOT_LINES = (59, 81)
MAX_OUT_LINES = 20
FLOW_TITLE = "Genetic algorithm inside the news agent"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="init", text="Population: 60 operator\nsequences from story S", x=0, y=1.4, shape="io"),
    dict(id="eval", text="Fitness of each:\nimpact gap, quality, rule", x=0, y=2.9),
    dict(id="exit", text="Goal met and\nplateau 15 gens?", x=0, y=4.5, shape="decision"),
    dict(id="sel", text="Select parents\n(tournament of 3)", x=0, y=6.1),
    dict(id="cross", text="Crossover: swap\noperator sequences", x=0, y=7.5),
    dict(id="mut", text="Mutate: random\noperator (4% per gene)", x=0, y=9.0),
    dict(id="elite", text="Keep 2 best (elitism)\nform new generation", x=0, y=10.5),
    dict(id="out", text="Return best path\nS to G", x=4.9, y=4.5, shape="terminal", w=2.9, h=1.0),
    dict(id="lim", text="Or stop at the\ngeneration limit", x=4.9, y=2.9, shape="data", w=3.4),
]
FLOW_EDGES = [
    dict(src="s", dst="init"), dict(src="init", dst="eval"), dict(src="eval", dst="exit"),
    dict(src="exit", dst="sel", label="No"),
    dict(src="exit", dst="out", label="Yes", exit="r", entry="l"),
    dict(src="lim", dst="out", exit="b", entry="t"),
    dict(src="sel", dst="cross"), dict(src="cross", dst="mut"), dict(src="mut", dst="elite"),
    dict(src="elite", dst="eval", exit="l", entry="l", via=[(-2.8, 10.5), (-2.8, 2.9)]),
]
