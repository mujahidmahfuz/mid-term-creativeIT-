"""Q1 flowchart + screenshot spec (loaded by _tools/build.py)."""
TITLE = "Greedy Best-First Search for Website & Chatbot Design"
SHOT_LINES = (46, 65)
MAX_OUT_LINES = 30
FLOW_TITLE = "GBFS loop for website design"
FLOW_NODES = [
    dict(id="s", text="Start", x=0, y=0, shape="terminal"),
    dict(id="in", text="Input: live site S0,\nh(n), goal h <= 20", x=0, y=1.3, shape="io"),
    dict(id="init", text="OPEN = {S0} (sorted by h)\nVISITED = { }", x=0, y=2.7),
    dict(id="empty", text="OPEN\nempty?", x=0, y=4.3, shape="decision"),
    dict(id="pop", text="n = design in OPEN\nwith the lowest h(n)", x=0, y=5.9),
    dict(id="goal", text="h(n) <= 20 ?", x=0, y=7.5, shape="decision"),
    dict(id="exp", text="Expand n: one design\nchange -> child designs", x=0, y=9.1),
    dict(id="add", text="Score children with h,\nadd unseen ones to OPEN", x=0, y=10.6),
    dict(id="upd", text="Re-weight h from\nnew analytics", x=5.3, y=10.6, shape="data", w=3.4),
    dict(id="ok", text="Return design\n+ change path", x=4.9, y=7.5, shape="terminal", w=2.9, h=1.0),
    dict(id="fail", text="No design\nmeets goal", x=4.9, y=4.3, shape="terminal", w=2.9, h=1.0),
]
FLOW_EDGES = [
    dict(src="s", dst="in"), dict(src="in", dst="init"), dict(src="init", dst="empty"),
    dict(src="empty", dst="pop", label="No"),
    dict(src="empty", dst="fail", label="Yes", exit="r", entry="l"),
    dict(src="pop", dst="goal"),
    dict(src="goal", dst="ok", label="Yes", exit="r", entry="l"),
    dict(src="goal", dst="exp", label="No"),
    dict(src="exp", dst="add"),
    dict(src="upd", dst="add", exit="l", entry="r", label="dynamic h"),
    dict(src="add", dst="empty", exit="l", entry="l", via=[(-2.8, 10.6), (-2.8, 4.3)]),
]
