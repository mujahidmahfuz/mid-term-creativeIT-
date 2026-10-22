"""Q10 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Creative Agent: Expanding Search and Action Space with RL"
SHOT_LINES = (34, 59)
MAX_OUT_LINES = 22
FLOW_TITLE = "Utility-based RL agent that expands its action space"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: 24 basic actions,\nutility function", x=0, y=1.3, shape="io"),
    dict(id="ep", text="Run one design episode\n(3 steps, epsilon-greedy)", x=0, y=2.8),
    dict(id="u", text="Utility of finished\ndesign = reward", x=0, y=4.3),
    dict(id="q", text="Update Q-values\nfrom the reward", x=0, y=5.8),
    dict(id="chk", text="Warm-up over?\n(episode 500)", x=0, y=7.4, shape="decision"),
    dict(id="mine", text="Mine best runs: frequent\naction pairs = macros", x=4.9, y=7.4, w=3.8),
    dict(id="more", text="More\nepisodes?", x=0, y=9.2, shape="decision"),
    dict(id="out", text="Final design +\nbigger action set", x=4.9, y=10.8, shape="terminal", w=3.2, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="ep"), dict(src="ep", dst="u"),
    dict(src="u", dst="q"), dict(src="q", dst="chk"),
    dict(src="chk", dst="mine", label="Yes", exit="r", entry="l"),
    dict(src="chk", dst="more", label="No"),
    dict(src="mine", dst="more", exit="b", entry="r", via=[(4.9, 9.2)]),
    dict(src="more", dst="out", label="No", exit="b", entry="l", via=[(0, 10.8)],
         label_at=(0, 10.2)),
    dict(src="more", dst="ep", label="Yes", exit="l", entry="l",
         via=[(-2.8, 9.2), (-2.8, 2.8)], label_at=(-2.35, 8.85)),
]
