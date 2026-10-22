"""Q14 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "K-means + KNN Semi-Supervised Learning for Cultural Tourism"
SHOT_LINES = (85, 112)
MAX_OUT_LINES = 28
FLOW_TITLE = "Semi-supervised cultural tour planner"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="20 cities: numeric +\n8 cultural bits, 4 seeds", x=0, y=1.3, shape="io"),
    dict(id="dist", text="d = a*Euclid +\n(1-a)*Hamming/m", x=0, y=2.75),
    dict(id="km", text="K-means (k=4) with d\n-> 4 clusters", x=0, y=4.2),
    dict(id="name", text="Seeds name clusters\n-> pseudo-labels", x=0, y=5.65),
    dict(id="knn", text="KNN (k=3) re-checks\neach pseudo-label", x=0, y=7.1),
    dict(id="chg", text="Any label\nchanged?", x=0, y=8.75, shape="decision"),
    dict(id="new", text="KNN labels new\ncities (Kyoto, Lisbon)", x=4.9, y=2.75),
    dict(id="pick", text="Pick cluster that best\nmatches the traveller", x=4.9, y=4.2),
    dict(id="route", text="Nearest-neighbour route\n+1 cross-cluster stop", x=4.9, y=5.65),
    dict(id="end", text="Cultural tour", x=4.9, y=7.1, shape="terminal", w=2.9),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="dist"), dict(src="dist", dst="km"),
    dict(src="km", dst="name"), dict(src="name", dst="knn"), dict(src="knn", dst="chg"),
    dict(src="chg", dst="knn", label="Yes", exit="l", entry="l", via=[(-2.8, 8.75), (-2.8, 7.1)]),
    dict(src="chg", dst="new", label="No", exit="r", entry="t",
         via=[(2.7, 8.75), (2.7, 1.55), (4.9, 1.55)]),
    dict(src="new", dst="pick"), dict(src="pick", dst="route"), dict(src="route", dst="end"),
]
