# Creative Thinking for AI & IoT Innovations — Study Notes

Course by Parag Kulkarni, PhD, DSc. Built from the 4 lecture packs (Classes 1–14, 566 slides) and the
mid-semester question bank (15 questions, 6 diagrams). Slide refs use `PDF:page`.

- `C14` = Class_One_Two_Three_Four_Upload.pdf
- `C58` = Class_5_6_7_8_Upload.pdf
- `L910` = Lecture_nine_ten.pdf
- `L1114` = Upload_Lecture_Eleven_Twelve_Thirteen_Fourteen.pdf

**Exam format (L1114:40):** mid-sem on 22 Oct, covers topics up to 19 Oct, online, closed book, submit PDF.
The question bank's own instruction is: *"Provide diagrams and pseudo code. Make necessary assumptions."*
Every answer should therefore have **Assumptions → Diagram → Definitions (state / actions / heuristic or
fitness) → Pseudocode → Worked example → Discussion (limitations, creative extension)**.

---

## Part A — What the course teaches

### A1. Creativity foundations (Classes 1–4)

- **Definitions.** Creativity is "a process involving the generation of new ideas or concepts, or new
  associations between existing ideas or concepts". Another view (Csikszentmihalyi) is "a process by which a
  symbolic domain in culture is changed". The goal of computational creativity is to model, simulate or
  replicate creativity using a computer.
- **Three aims of creative computing:**
  1. machines help humans be creative (path correction, suggestions, options, pointers);
  2. machines learn from human creativity (decode the creator's thought process);
  3. humans and machines co-create (understand co-workers, complement them, create sizable parts).
- **Boden.** **P-creativity** (psychological): new to the individual or agent. **H-creativity** (historical):
  new to all of history. Boden's three forms are **combinational**, **exploratory** (explore the outer edges of
  a space while staying within its rules) and **transformational** (change the space itself; the "game
  changer"). C58:12 also lists **S-** and **T-creativity** with no definition. The course themes suggest S =
  *systemic* ("Creativity is Systemic") and T = *temporal* or *transformational*.
- **Historical creativity in machines (C58).** Either (a) a creative task this machine has not done before,
  or (b) a creative task no machine has done before.
- **Newell, Shaw and Simon's criteria for a creative idea:** novelty plus usefulness (for the individual or
  society), rejection of previous ideas, intense motivation and persistence, and clarification of vague ideas.
- **Four views of creativity:**
  - **Nomothetic** (universal laws) vs **idiographic** (individual uniqueness).
  - **Mental** vs **social** phenomenon (appreciated by an audience).
  - **Improbabilist** (a novel combination of familiar ideas) vs **impossibilist** (truly new ideas, via
    transformation of the conceptual space).
  - **Rational** (logic: abduction, eduction, deduction, induction; evolution: adaptation through problem
    solving) vs **irrational** (emotion).
- **Formalization (Wiggins' Creative Systems Framework, C14 / C58).**
  - U is the universe of concepts, and the conceptual space C is a strict subset of U.
  - Axiom 1: every concept is a distinct member of U. Axiom 2: every space contains the empty concept ⊥
    (rendered "F" on the slides).
  - L is the language. **R** is the rules for existence in a space and **T** the traversal rules, with
    R and T both subsets of L. **[.]** is the interpretation function and **<.>** the traversal function.
  - An exploratory system is the tuple (U, L, R, T, E). The exploratory creative process begins as
    `<R+T>({⊥})`, and E(C) is the value of the conceptual space.
  - Exploration happens *within* C. Transformation goes *out of the box* by changing R or T.
- **Artificial Creative Intelligence (Mark Amerika).** Computational creativity is the research field
  (systems evaluated against criteria). Creative AI is the applied framing (AI as a tool in creative
  industries). ACI is creativity as a hybrid process across humans and non-humans that belongs fully to
  neither. Related ideas:
  - The **Hybrid Mind** is the third authorial entity that emerges from human–machine exchange.
  - **Psychic automatism** is composing without conscious control.
  - The **Meta Remix Engine** is the artist's own unconscious recombination apparatus.
  - ACI replaces the virtues of authenticity and intentionality with **intuition, spontaneity and remix**.
- **Ideas to choices (Thread C).** **Choices, not answers**: present a ranked set of options with visible
  reasoning. Make trade-offs visible. Human judgement is structured, not replaced.
- **Why IoT (Thread D).**
  1. New primitives to combine (sensor streams from domains never juxtaposed before).
  2. Grounding in the physical (the space is constrained by physics, not convention).
  3. Continuous space expansion: *adding a sensor modality adds a dimension and changes the space*. This is
     the closest practical analogue to transformational creativity.
  4. Value becomes measurable (energy saved, comfort, harm avoided).
- **Thinking.** "Organizing and reorganizing known facts, learning, and extrapolating them in the context of
  the problem." Types: perceptual/concrete, conceptual/abstract, logical, creative, problem-based, and
  convergent vs divergent.
  - **Convergent** thinking narrows to one well-defined solution and is constrained.
  - **Divergent** thinking looks in many directions and tries multiple solutions; it involves conceptual
    combination, mental flexibility and depth of semantic knowledge.
- **Critical vs creative thinking.** Critical thinkers care to "get it right": they seek alternative
  hypotheses, are well informed, consider other views, and value clarity, precision and honesty.
- **Lateral thinking moves:** take a contrary view, think of one subject in terms of another, take multiple
  perspectives, hunt for chances to think differently, and form new relevant combinations from existing ones.
- **Learning** is "building the ability to produce the expected results". Creative learning is "finding more
  through available knowledge through **association, meta-reasoning, exploration, expansion, transformation
  and mapping**".
- **Turing test vs creativity test.** In the creativity test, an evaluator cannot tell whether a creative
  response came from the human or the machine. Ideas for a new test include role change, dynamism,
  variability, and answer-, emotion- or human-driven designs. **Relative creativity** means indistinguishable
  from a realistic human creator. **Statistical creativity** compares a model with a population of human
  creators (arXiv 2401.01623).
- **Poetry generation approaches:** template-based, generate-and-test (WASP, Tra-La-Lyrics), evolutionary
  (POEVOLVE, McGonnagall) and case-based reasoning (ASPERA, COLIBRI). Balance **meaningfulness,
  grammaticality and poeticness** (the seesaw slide). RACTER (1984) shows that "creativity is in the reader's
  mind".
- **TALE-SPIN.** Rule-based systems are monotonous, so use a **meta-approach: rules for rules**.
- **Creative operators:** repurpose, complete differently, form a story, associate words, building blocks,
  incremental/evolutionary design, exploratory design. Also **substitute, eliminate, minimal, optimal, adapt,
  combine, expand, reverse, associate, analogy** (SCAMPER-like).
- **Creativity and business:** repositioning, repurposing, expansion, combination. Examples: Ogilvy with
  DALL·E (Vermeer's *Milkmaid*), the Kartell/Starck AI chair, Stitch Fix.
- **Creativity results from interactions:** system, assessment and validation.
- **Grass cutter example:** "Shyama developed a grass cutter" → "Shyama on tricycles", combining a mower
  with a tricycle. This is combinational creativity.

### A2. Conceptual spaces (Class 5–6, Gärdenfors)

- A conceptual space is a geometric structure over **quality dimensions** (weight, colour, taste,
  temperature, pitch, the 3 spatial dimensions).
  - **Objects are points.** **Properties and relations are regions.**
  - **Similarity is distance.**
  - The layers run from Sensory input → Sub-conceptual (connectionist) → Conceptual → Linguistic
    (inference engine). This is Chella's architecture.
- A **property** lives in one domain (an adjective). A **concept** spans several domains (a noun). The
  *Apple* example has colour, shape, texture, taste, fruit and nutrition domains, and **context sets the
  domain weights**.
- **Combination rules:**
  - Compatible property and concept: intersect the regions.
  - Incompatible: the property's region overrules (a **pink elephant**).
  - Correlated shifts: a **brown apple** changes colour *and* texture.
- Other operations: conceptual **contradictions, mutations, crossovers, hierarchy and transformation**.
- **Releasing the boundaries of compatibility** yields new conceptual definitions and new spaces.
  Constraints focus creativity.
- **Primary** spaces hold basic physical qualities. **Secondary** spaces are derived, abstract and symbolic.
- **Concept transformation** reshapes the rules and boundaries of a domain itself. It goes beyond
  combination.
- **Creative problem solving in AI agents** (Gizzi et al., JAIR 2022; C58:48–49).
  - Premise: the agent's initial conceptual space {c1, c2, c3} is *insufficient*, so the task fails. CPS
    produces a new concept c'4, giving an expanded space in which the task succeeds.
  - The framework runs: problem formulation (planning / learning) → knowledge representation (symbolic /
    non-symbolic / hybrid) → knowledge manipulation (**exploratory / combinational / transformational**) →
    evaluation (simulation / real-world / benchmark).
- **Creativity traversals (C58:23).**
  - Move to the best neighbouring state, i.e. the *most creative neighbour*.
  - Think in terms of creative states and creative paths, and cumulative creative effort.
  - Give each state a new creative value **Ct**.
  - Use multi-state search (several start states).
  - Shortlist a few actions and a few initial states, then imagine possible transformations.
- **"What could be?" (C58:21).** Assign properties to the object. Then properties → concept → concept
  expansion, with a goal state, start state, action sequence and path cost.
- **Cup exercise (C58:22).** Twelve cups shade from a tall mug to a wide bowl. The highlighted path is
  9 → 6 → 3 → 4, and the question is "what could be the heuristic function?" A good answer is the
  **width/height ratio**, or the distance to a target cup–bowl prototype in the conceptual space.
- **Modelling and evaluating creativity:** expansion, exploration, analogy, the **AUT** (Alternate Uses
  Test) and the **TTCT** (Torrance Tests of Creative Thinking).
- **Creative choosing (C58).** Generate many options (random but with an objective), present them to a
  program, choose the best using creativity-evaluation mechanisms, and give the final choices to the user.
- **Living geometry (Salingaros 2025).** Alexander's **15 properties** can serve as an objective aesthetic
  fitness function: levels of scale, strong centres, thick boundaries, alternating repetition, positive
  space, good shape, local symmetries, deep interlock and ambiguity, contrast, gradients, roughness, echoes,
  the void, simplicity and inner calm, and not-separateness.
- **AI and diversity (Doshi & Hauser, Science Advances 2024).** AI raises *individual* creativity but
  *reduces collective diversity*. The course responds with agents that include diversity:
  - decentralization;
  - "bad samples could be good samples";
  - progress may not have the right direction;
  - **Positive + Positive < Negative + Positive**;
  - samples that lead to questions.

### A3. Agents → intelligent agents → creative agents (Classes 5–10)

- An **agent** perceives its environment through sensors and acts through actuators.
  - **Percept sequence** is everything the agent has perceived so far.
  - The **agent function** maps the percept sequence to an action.
  - A **rational agent** chooses the action that maximizes its performance measure.
  - **Agent = Architecture + Program.** In the creative version (L910) it becomes **+ (Creativity
    evaluator, Conceptual space expander)**, so the pipeline is Sensors → Agent program → *Conceptual space
    expander* → Actuators.
- **PEAS** stands for Performance measure, Environment, Actuators, Sensors. Slide examples:
  - **Washing machine.** P: cleanliness, time, electricity, water, detergent, noise. E: clothes, tap, water,
    detergent. A: drum motor, timer, alarm. S: water level, detergent, cloth weight, clock.
  - **Medical diagnosis.** P: accuracy, time, recovery, expense. E: patient, doctors, equipment.
    A: diagnosis, tests, alerts, medicines. S: BP, sugar, ECG, EEG, symptoms, reports.
  - **Auto door.** P: response time, idle time, noise. E: both sides of the door. A: motor.
    S: cameras, object sensing.
  - **Face authentication.** P: time, accuracy, handling new faces. E: face. A: outcome message.
    S: camera.
  - **Auto car.** P: time, accuracy, safety. E: streets, pedestrians, signals. A: steering, brake,
    accelerator, horn. S: cameras, GPS, speedometer.
- **PEAS for a creative agent.** Ask "what could be different?" for each of P, E, A and S, then add
  **Evaluation** and a **New agent function**. The slide's diagram contrasts an Intelligent agent, a
  Creative agent, a **Creativity companion (co-creator)** and a **Creativity booster**.
  - P adds novelty, surprise, usefulness and diversity (a creativity score).
  - E is open and dynamic, with cross-domain sources.
  - A can *generate* options, combine and present choices.
  - S senses previous performance and competing performance, plus human reactions.
- **Environment dimensions:**
  - fully vs partially observable;
  - deterministic vs stochastic;
  - discrete vs continuous;
  - episodic vs sequential;
  - static vs dynamic (or semi-dynamic);
  - single- vs multi-agent.
  The real world is partially observable, stochastic, sequential, dynamic, continuous and multi-agent. The
  table shows chess with a clock is "semi" static and image analysis is episodic.
- A **rational / flexible agent** is responsive (timely), **proactive** (goal-directed, takes the
  initiative; *temporal creativity*) and **social** (interacts; *expands the creativity space*). Other
  properties: mobility, veracity, benevolence, rationality, learning.
- **Agent types:**
  - **Table-driven:** huge table, no autonomy.
  - **Simple reflex:** condition–action rules on the current percept only; works in fully observable
    environments; randomize for the vacuum world.
  - **Model-based reflex:** internal state for unobserved aspects; the percept history gives *temporal
    creativity*.
  - **Goal-based:** "what will happen if I do A" plus goals; uses search and planning.
  - **Utility-based:** the means matter too (safer, quicker routes); utility maps a state to a real number
    measuring "happiness".
  - **Learning agent:** a *performance element* (selects actions), a *learning element* (makes
    improvements), a *critic/reviewer* (feedback against a standard) and a *problem generator* (suggests
    exploratory actions). It learns through rewards and penalties.
- **Creative agent** (L910, L1114:16). It is a learning agent plus a **Creativity Calibration** block next
  to the performance element, with actuators for **Exploration, Analogy and Combination**. Its traits:
  - a function that measures the extent of creativity;
  - it does both obvious and creative tasks;
  - **rational but non-obvious**;
  - it classifies tasks and outcomes on a creativity scale;
  - it senses previous and competing performance.
- **How a creative agent learns:** deviates from historically established routes, tries new variations,
  learns through combination, exploration and expansion, and keeps a dynamic learn set. *The learn set
  evolves → the algorithm evolves → the outcome evolves.* It has a built-in **creativity calibrator**.
- **Multi-agent creativity:** single-agent, multi-agent, **co-operative creativity**, and ensemble
  creativity (think bagging and boosting). Limitations of agent solutions: no overall system controller and
  no global perspective, and **creativity is not possible without a broader perspective**.
- **Reductionist / connectionist / inferential creativity:**
  - reductionist works one part at a time;
  - connectionist finds connections and associations;
  - inferential infers from relationships.
  **Holism**: the whole is more than the sum of its parts, and the network of relationships gives purpose.
  Da Vinci: "everything connects to everything else."
- **Consciousness:** epiphenomenalism (physical → mental, not mental → physical). Self-awareness has three
  parts: continuity, agency and identity (Gallup).
- **Instincts** (Rosling's Factfulness "dramatic instincts"): gap, negativity, straight line, fear, size,
  generalization, destiny, single perspective, blame, urgency.

### A4. Connections, mind maps and combinational creativity (Classes 7–10)

- A **creative connection** produces associations that give *useful, novel and surprising* results. It is
  inspired by neurons and can join agents with different cognitive styles. Processing ends when the network
  settles into a stable state.
- **Connections** can be vectors and context-based, are stable in a *band* rather than at a value, and are
  selected, cooperative and evolving.
- **Mind maps:** a central topic with idea branches (Buzan, XMind). Reinforce through connectionism: start
  with random seeds and strengthen links.
  - Inference can be **vertical** or **lateral**, with layers of mind maps that associate and overlap.
  - **Opportunity maps** look at unexplored, under-explored and new relationships, within and across maps.
  - Pay attention to strong links *and weak links*.
- **Reinforcement exploration on mind maps:** creativity-driven reinforcement of connections, new starting
  points, random connection changes, and starting from random or **weakest** links. **Reverse hypothesis
  creativity** begins with the weakest hypothesis.
- **Combinational creativity** comes in three kinds:
  - **problem-driven**: bridge a problem–solution gap with old ideas that are incomplete on their own;
  - **similarity-driven**: cup → glass, spoon → fork;
  - **inspiration-driven**: unrelated ideas joined.
  Poincaré: "ideas rose in crowds… collide until pairs interlocked." Examples: crab-inspired toys,
  elephant + butterfly.
- **Cognitive flexibility:** go beyond a single concept, switch importance between concepts, relate them,
  fit them to the context, adapt.
- The **systemic view** connects domains (Agri, Financial, Manufacturing, Smart-City, Other) around a
  shared core. This is **systemic creativity**.
- **Creativity and constraints:** process vs product constraints, *expand → reduce and expand*, imposing
  and releasing constraints, a partition-based approach.
- **Creativity and state transition (L910:4–5).** Start → State1 → State2 → State3, with events leading to
  Action1 and Action2. Creativity means you **introduce a new action** or **introduce a new state**.

### A5. Search: uninformed (Lectures 9–11)

- **State space** is the set of states reachable by applying operators. The **search space** is the
  implicit tree or graph defined by the initial state and operators. The **search tree** is the explicit
  tree the strategy actually generates.
  - **Node:** state, parent, action, path cost g, depth.
  - The **fringe** holds nodes that have been generated but not yet expanded (the leaves).
  - The **branching factor** b is the number of successors per state.
  - Prolog example: `link(a,b)…`, `go(a,c,X)` gives [a,e,f,c], [a,b,f,c] and [a,b,c].
- **Evaluation criteria:** completeness, time complexity, space complexity, optimality/admissibility.

| Strategy | Frontier | Complete | Optimal | Time / Space |
|---|---|---|---|---|
| BFS | FIFO queue | yes | yes if step costs are equal | O(b^d) / O(b^d) — depth 12, b=10 ≈ 35 years, 111 TB |
| DFS | LIFO stack | no | no | O(b^m) / O(bm), linear; chronological backtracking |
| UCS (Dijkstra) | priority on g(n) | yes if every step > 0 | yes (goal test on removal) | exponential |
| Depth-limited | DFS with cutoff L | no (misses goals deeper than L) | no | — |
| IDDFS | DLS with L = 0, 1, 2… | yes | yes for unit costs | O(b^d), linear space; combines BFS and DFS |
| Bidirectional | from both ends | yes | — | needs predecessor states and memory for one tree |

- **Repeated states:** use a closed list; detect looping paths and discard them.
- **Partial information:**
  - **sensorless** (could be in any of several states);
  - **contingency** (a percept after each action; plan for each contingency);
  - **exploration** (states and actions unknown, so act to discover them).
- **UCS example (L910:95).** Edges: S→A 3, S→B 1, S→C 8, A→D 3, A→E 7, A→G 15, B→G 20, C→G 5.
  - UCS expands S(0), B(1), A(3), D(6), C(8), E(10), G(13), giving **S→C→G, cost 13** (optimal).
  - BFS or DFS find S→A→G with cost 18 (DFS goes via D and E first).

### A6. Search: informed / heuristic (Lectures 11–14)

- **Best-first search** uses an evaluation function and expands the "best-looking" node. Its key part is
  the heuristic **h(n)**, the estimated cost from n to the goal.
- **Greedy best-first search (GBFS):** f(n) = h(n). Fast, but not optimal or complete.
- **A\*:** f(n) = g(n) + h(n), i.e. cost so far plus estimated cost to go. It avoids expanding paths that
  are already expensive. It is optimal if h is **admissible** (never overestimates).
- **IDA\*** uses an f-cost cutoff instead of a depth cutoff.
- **RBFS** changes its mind often because f gets more accurate (less optimistic) near the goal. **SMA\***
  deletes the worst (largest f) node when memory is full and remembers the best descendant.
- **Lecture graph (L1114:62–74).** The same graph is used for GBFS and A\*.
  - Edges: Start–A 4, Start–D 10, A–B 2, A–D 6, D–F 2, D–G 4, D–E 6, D–C 4, E–C 6, E–Goal 10,
    G–Goal 24.
  - h values: Start 40, A 20, B 40, D 14, F 40, G 24, E 10, C 16, Goal 0.
  - **GBFS:** expand Start → {A 20, D 14} → pick D → add F 40, G 24, E 10, C 16 → pick E → add Goal 0 →
    pick Goal. Path **Start → D → E → Goal**, cost 10 + 6 + 10 = 26.
  - **A\*:** A = 4 + 20 = 24 and D = 10 + 14 = 24 (tie). Expand A: B = 6 + 40 = 46. Expand D: E =
    16 + 10 = **26**, C = 14 + 16 = 30, G = 14 + 24 = 38, F = 12 + 40 = 52. Expand E: Goal = 26 + 0 = 26.
    Path **Start → D → E → Goal = 26 (optimal)**; Start → A → D → E → Goal also costs 26. The slide
    annotations read 4+20, 40+2+4, 10+14, 10+4+16, 10+6, 10+4+24.
  - *Exam observation:* h(Start) = 40 > 26 and h(B) = 40 > 24 actually **overestimate**, so h is not
    strictly admissible. It does no harm here because those nodes are never competing frontier nodes.
- **Admissible heuristics for the 8-puzzle (L1114:78).** Start 7 2 4 / 5 _ 6 / 8 3 1, goal _ 1 2 / 3 4 5 /
  6 7 8.
  - H1 = misplaced tiles = **8**.
  - H2 = Manhattan (city-block) distance = 3+1+2+2+2+3+3+2 = **18**.
  - H2 dominates H1.
- **Psychological heuristics (L1114:56–61)** can be **injected into agents** as a *creative pre-filter*
  ("optimization's blind spot" is efficient but predictable output):
  - **availability**: the most easily recalled feels most likely;
  - **representativeness**: resemblance to a prototype, ignoring base rates;
  - **affect**: emotional response.
  System 1 is fast, automatic, associative and always on. System 2 is effortful, rule-based, deliberate
  and limited in capacity.
- **Gestalt laws of choosing (L1114:49–50):**
  - rationality (filter the reachable rational choices);
  - next choice (proximity);
  - similarity;
  - unit formation;
  - default and simple choice;
  - symmetry;
  - storytelling (the choice path is a story).
- **"Choose!" principles (L1114:48):**
  - *inertia diluent* (default is better);
  - *less is more*;
  - *story and relevance*;
  - *surprise at the critical point*;
  - ***slow to heat and gradual cooling*** (introduce the best choice gradually and keep it warm). This is
    the human analogue of simulated annealing.
  - *neighbours matter* (careful clustering of choices near key choice points).
- **Dynamic heuristics:** "limited knowledge strategies" and **"dynamic and evolving heuristic functions"**
  (L910:84). Dynamic goals (L1114:6) cover changing goal states, an evolutionary termination criterion, and
  multiple demarches with multiple goals (population evolution / GA).

### A7. Local search (Lectures 12–14)

- **Local search** is used when the path is irrelevant and only the final configuration matters. It keeps
  one current state, is memory-efficient, and handles large or infinite spaces. Optimization moves from
  suboptimal to better; satisfaction moves from infeasible to feasible. There are no guarantees.
  - A **neighbourhood** N: C → 2^C is defined by local moves ("are local moves rational moves?").
  - Examples: TSP and n-queens.
- **Hill climbing:**
  - Start from a random or special state. Until there is no improvement: **steepest ascent** (the best
    successor) or **greedy/first-improving**. Repeat with restarts.
  - It is "greedy local search", never looks beyond immediate neighbours, and its success depends on the
    landscape shape.
  - **Problems:** local maxima, ridges (a series of local maxima), plateaus/flat maxima, and shoulders.
- **Variants:**
  - **stochastic** (random uphill move);
  - **first-choice** (generate random successors until one is better);
  - **random-restart**;
  - **simulated annealing** (hill climbing plus a random walk, giving both efficiency and completeness;
    raise the "energy" to escape local minima, then cool slowly);
  - **beam** (a mix of hill climbing and best-first, caching the best K; not optimal or complete);
  - **local beam** (k states that share information, unlike k independent restarts);
  - **stochastic beam** (choose k successors with probability rising with fitness);
  - **tabu** (keep a list of visited nodes and pick the best non-tabu move).
- **Slide examples:**
  - 8-puzzle hill climbing goes h = 5 → 4 → 3 → 2 → 1 → 0.
  - **4-queens**, starting with all queens in the top row: score −6 → −3 → −1 → 0, where the score is minus
    the number of attacking pairs.
  - **8-queens:** count the violations, move the queen with the most violations within its column, and take
    the best move.
- **Surprise-test template (L1114:83, 109, 203)**, which is identical to Q15:
  1. Model *product recommendation* (or *course selection*) as a heuristic search.
  2. Define h, the start, the goal, and actions/neighbours.
  3. Do a hill-climbing traversal over 10 products.
  4. Discuss local vs global maxima.
  5. Handle multiple goals.
  6. Give an A\* vector transition with correction.
  7. Propose an interesting HC modification ("embed humanized aspects").

### A8. Evolutionary computation and genetic algorithms (Lectures 13–14)

- **Evolution:** selection, heredity, variation. Genotype (genetic material) vs phenotype (the expressed
  organism). Selection acts on the phenotype, while the genotype carries inheritance.
  - **Fittest ≠ best**: selection is relative to the environment and peers at one time and place, and
    natural selection has no comparative memory.
  - Diversity gives adaptation power.
- **The EA loop** is generate-and-test, stochastic and population-based. Variation operators create
  diversity (and so novelty); selection reduces diversity and pushes quality.

```
procedure EA:
  t = 0; initialize P(t); evaluate P(t)
  until (done):
    t = t + 1
    parent_selection P(t); recombine P(t); mutate P(t)
    evaluate P(t); survive P(t)
```

- **Types of EA:** GA (crossover + mutation), evolutionary programming, evolution strategies, genetic
  programming, PSO, island models (parallel diverse populations exchanging strings), steady-state
  (worst replaced by offspring of the best), simulated annealing, and PBIL/adaptive PBIL.
- **The five GA phases:** initialization → evaluation → selection → crossover → mutation, then
  termination. The GA ingredients are an encoding (gene, chromosome), initialization, an evaluation function
  (the environment), parent selection, operators, and parameters ("practice and art").
- **Selection:** fitness-proportionate (**roulette wheel**) or **tournament**. Keep a few weaker
  individuals for diversity to avoid premature convergence.
- **Crossover** happens with probability 60–70%. Types:
  - **single-point**: XX|XXXXX + YY|YYYYY → XXYYYYY, YYXXXXX;
  - **two-point**: XX|XXX|XX → XXYYYXX;
  - **uniform** (p = 0.5 per gene);
  - real-coded **mid-point** ((X+Y)/2), **flat** (rnd(X, Y)) and **BLX-0.5**.
- **Mutation** happens with probability about 0.1–0.2% per allele and preserves diversity so the GA can
  escape local optima.
  - Types: point (substitution, deletion, insertion) and segmental (substantive; contextual: inversion,
    recombination).
  - For permutations: swap, inversion, scramble.
- **Termination:** a solution meets the minimum criteria; a fixed number of generations; a budget
  (time/money); a plateau (no improvement); manual inspection; or a combination.
- **The GA is a variant of local beam search** in which successors combine two parents.
- **8-queens GA (L1114:180).** Fitness = non-attacking pairs, max 28. Population 24748552 (24),
  32752411 (23), 24415124 (20), 32543213 (11) gives selection probabilities 31%, 29%, 26%, 14%. The steps
  are selection → crossover → mutation.
- **Car / vehicle GA (L1114:187–196).** This is the course's own creative-GA example.
  - Initial population: 5 toy vehicles (bar on wheels, box car, red wedge, purple wedge, yellow
    two-circle).
  - **Fitness** = top area / wheel area + top length / wheel distance (+ rear height / front height). The
    slide asks "what could be other fitness functions?"
  - **Operators:** (1) wheels of one + body of the other (crossover); (2) abrupt wheel change (mutation);
    (3) abrupt body-shape change (mutation); (4) partial colour change (mutation); (5) one wheel of one +
    the rest of the other; (6) the shape of one + the rest of the other.
  - Generations 2, 3, 4… follow.
  - The **GENERATE** slide (L1114:202) generalizes properties by statistical likelihood: "some geometric
    shape on top of two circles" yields a *new* member (a pentagon on two wheels). This is **conceptual
    space expansion by generalization**.
- **Evolving neural networks:** encode the connection matrix as genes. Chalmers (1990) evolved a learning
  rule close to the delta rule with 8 unknowns.
- **Applications:** Al Biles' GenJam jazz riffs, radar classification, stock prediction. Mangano: GAs
  navigate huge spaces to find "solutions you might not otherwise find in a lifetime".

### A9. Search → *creative* search (L1114:4–12, L910)

- **Kinds of option:**
  - **Available options:** logical/obvious, illogical/non-obvious, derived, indirect, short-sighted.
  - **Unavailable options:** closed, not yet opened, not known.
  - Creative search *creates, discovers or invents* new options, at different points across the value
    chain.
- **When search is creative:**
  1. it generates new options;
  2. it discovers a new concept, node or route;
  3. it **combines two or more nodes**;
  4. it **creates new sets of actions**;
  5. it **redefines the neighbour**.
- **Creative search strategies (L910):** go to states that meet creativity criteria, generate new states,
  **merge states**, **expand the search space**, **expand the action space**.
- **Creative heuristics** come from functional creativity and invention and transfer to other realms. They
  help **overcome fixation** and **resolve contradictions**.
- **Search-space problems:** rarity, payoffs, oasis, plateau. **Creating the search space:** broaden it,
  evaluate it, go from incremental to radical.
- **Triple path to insight** (Klein; L1114:10). Each trigger leads to an activity, and all three change how
  we understand (act, see, feel, desire).
  - *Contradiction* (find an inconsistency) → use a weak anchor to rebuild the story.
  - *Connection, coincidence or curiosity* → add a new anchor.
  - *Creative desperation* (escape an impasse) → discard a weak anchor.
- **Creative problem-solving cycle (L1114:11–12).** Challenging assumptions ↔ Generation of alternatives
  ↔ Reframing the problem ↔ Fine-tuning the solution. The supporting modes are contradiction and
  confrontation, imagination and visualization, variabilization and configuration, and combination and
  separation.
  - **Variabilization and configuration:** vary the variable; SCAMPER; find a trajectory or evaluation
    function; add relevant features; package features; improve the human interface; delete irrelevant
    features; abstract and transform (scale, dimensionality, matching).
  - **Combination and separation:** consider the negative/inverse; combine inventions with complementary or
    emergent qualities; combine to remove redundancy; interpolate and extrapolate; find a new purpose;
    separate and recombine.

---

## Part B — Question-bank map (all 15)

These are answer *skeletons*, written in the course's vocabulary. Diagram notes describe what each figure
in the PDF actually shows.

### Diagrams in the question bank

- **D1:** a 4-level tree (root, about 7 children, about 35 grandchildren, a few great-grandchildren). It
  represents a search tree, decision tree or population member.
- **D2:** a grid of about 12×7 black and dark-grey squares. **S** is at the top right and **G** at the
  bottom left (both green), with **C** and **D** as blue waypoints. White paths run from S → D (down the
  right side, then left) and from S → C (along the top, then down the left). Constraint: **no more than two
  black squares visited consecutively**.
- **D3:** a hill curve. **A** is at the foot (start), **B** on the rising slope, and **C** at the peak.
- **D4:** a square spiral of expanding rings around a green centre point, with black arrows tracing ring by
  ring and a **red arrow** pointing outward (upper right). This is Manhattan-distance iterative deepening:
  each ring is one more unit of distance, and the red arrow is a preferred expansion path.
- **D5:** three overlapping circles (search spaces) holding points. A green arrow runs from **j** (lower
  left) through **n** (the overlap) to **i** (upper circle). The space expands and moves as new states are
  created.
- **D6:** a bubble chart of 20 cities, x = year-over-year growth 2015→2016 (0–14%), y = spend per visit
  ($0–2000), bubble size = visits, colour = region (Asia-Pacific teal, Europe green, North America purple).
  The Mastercard Global Destination Cities Index.
  - Dubai is the top (~$2000, 7%) and New York ~$1600 at 3%.
  - Osaka has the highest growth (13%).
  - The low-spend European cluster is Istanbul, Rome, Prague, Amsterdam, Paris and Milan.

### Q1 — Greedy best-first search for website design → chatbot forest → GA of decision trees
- **State:** a website design configuration (layout, navigation, colour, CTA, content blocks, load
  profile). **Node expansion:** apply one design change. **Traversal:** the sequence of accepted design
  changes.
- **h(n)** = weighted gap to the target UX, so lower is better and h = 0 is the goal:
  - `h = w1·(1−predicted_conversion) + w2·norm(load_time) + w3·accessibility_violations +
    w4·(1−usability_score) + w5·nav_depth`
- **Convergent:** GBFS itself, always expanding the lowest h and narrowing to one design.
  **Divergent:** keep a beam of k designs, add random or novel actions, generate alternatives, use multiple
  start states, and present choices, not answers.
- **Worked example:** reuse the lecture graph. Start = current site (h 40), A = new layout (20),
  D = simplified navigation (14), E = mobile-first (10), Goal (0). The GBFS path is Start → D → E → Goal.
- **Chatbot with multiple trees:** each tree is an intent/dialogue tree, and together they form a forest.
  Search across trees and combine sub-trees.
- **Each population member as a decision tree (D1):** internal nodes test the user intent or context, and
  leaves are responses or actions.
  - Crossover is a **sub-tree swap**.
  - Mutation changes a node's condition or response, or adds or prunes a branch.
  - Fitness = task success + user satisfaction − turns.
- **Dynamic heuristic: yes.** `h_t(n) = Σ w_i(t)·f_i(n)`, with the weights updated from A/B tests, user
  feedback or RL. This is the "dynamic and evolving heuristic function".
- **Pseudocode:** GBFS with a priority queue keyed on h, a closed list, and goal test h ≤ ε.

### Q2 — Goal-based agent with a GA for news reporting (D2)
- **Agent:** goal-based. Sensors are news feeds and reader metrics. The model ("what will happen if I do
  A") is a reader-impact predictor. The goal is **G = target news with the reference impact**. Actuators
  publish or edit. Add PEAS.
- **Map D2:** every square is a candidate news version with a fitness value.
  - **Black squares** are low-quality or risky versions (sensational, unverified, biased); grey squares are
    acceptable.
  - **C and D** are editorial checkpoints.
  - A move to a neighbouring square is a legal application of one genetic operator.
  - The constraint is a penalty or repair: **≤ 2 consecutive black squares**.
- **Initial population** of at least 4 items, e.g. N1 politics, N2 health, N3 tech, N4 sports. Encode each
  as a chromosome such as [headline, lead, body facts, quotes/sources, tone, length, image, tags].
- **Four operators:**
  1. crossover (headline/lead of one + body of another);
  2. mutation (tone or headline rephrasing);
  3. insertion (add a verified fact, quote or source);
  4. deletion or inversion (remove a sensational or redundant segment; reorder into an inverted pyramid).
- **Fitness:**
  - `F = w1·accuracy + w2·(1−|predicted_impact − target_impact|) + w3·readability + w4·novelty
    − w5·bias − λ·black_run_penalty`
- **Exit criteria:** |impact − target| ≤ ε; or max generations; or a plateau of k generations with no gain;
  or the budget; or editor approval. Discuss premature convergence (keep diversity) and the black-run
  constraint as a feasibility check.

### Q3 — Hill climbing for airport design and gate arrangement
- **A, the start state:** the blueprint of an existing airport, as a state vector (gates, immigration
  counters, space usage, shop positions, waiting-area size).
- **B, action selection:** the legal small changes a–e generate the neighbours. Pick the best (steepest
  ascent).
- **C, the goal state:** the evaluation function.
  - `Score = w1·votes(10 frequent travellers)/10 + w2·(1/avg_wait) + w3·space_utilization
    + w4·senior_friendliness`
  - Stop when no neighbour is better, or when the score ≥ threshold.
- **Pseudocode:**
  ```
  current = blueprint
  loop:
    neighbours = apply(a..e, current)
    best = argmax Score(neighbours)
    if Score(best) <= Score(current): return current
    current = best
  ```
- **Limitations:**
  - bias from the other city's blueprint;
  - a noisy and subjective evaluation (10 voters);
  - costly evaluation (simulation);
  - plateaus (moving a shop doesn't change the score);
  - ridges (gates and counters must change *together*);
  - no backtracking;
  - real constraints (budget, safety).
- **Local maximum example:** waiting-area size is tuned to the current gates. Adding a gate takes waiting
  space, so every single change lowers the score, yet the global optimum needs restructuring (+2 gates,
  +counters, relocated shops).
- **Remedies:** random restarts (different blueprints), SA, tabu, compound actions, beam.

### Q4 — Best-first vs hill climbing; expanding the spaces; D3 convergence speed
- **Common ground:** both are informed and use an evaluation or heuristic function to pick the most
  promising node; both are greedy. Hill climbing is best-first with a memory of 1: no frontier, no
  backtracking. Best-first keeps an OPEN list.
- **Best-first expands the search space** by keeping alternatives on OPEN, inserting newly generated
  (creative) states, and redefining neighbours.
- **Both spaces at once: yes.** A new action creates new successor states, so the search space grows too.
- **D3 convergence control** uses the step size, number of neighbours sampled, temperature or acceptance
  threshold, and momentum.
  - **A** (far from the peak): large steps, aggressive or random exploration.
  - **B** (on the slope): follow the gradient (steepest ascent), with moderate steps.
  - **C** (at the peak): small steps for fine-tuning, plus a perturbation or restart to test whether this
    is the global maximum.
  - This is an adaptive schedule, like SA cooling.
- **Two new operations for Q3:** (f) add a new terminal wing or pier (a macro-move); (g) convert or swap a
  zone's function (shops → senior lounge, or e-gates replacing manual counters), or combine a and b.
- **Impact on the goal:** a bigger neighbourhood can escape local maxima and reach a higher global maximum,
  and the goal may move or gain new dimensions. Each step costs more.

### Q5 — Heuristic vs non-heuristic search; simulated annealing for recommendation
- **Uninformed:** BFS, DFS, UCS, DLS, IDDFS, bidirectional. **Informed:** GBFS, A\*, HC, beam, SA, GA.
  Compare them on completeness, optimality, time and space.
- **SA recommender:**
  - The state is a list of k products. A neighbour swaps one product for a catalogue item.
  - Score = relevance + diversity + novelty (+ margin).
  - Accept a worse move with probability `e^{Δ/T}`, with `T ← αT`.
  - Tie this to the "slow to heat and gradual cooling" choice principle.
- **Worked example:** a 10-product catalogue with numeric scores, T0 = 10, α = 0.8. Show one accepted
  downhill move escaping a "same-category" local maximum.

### Q6 — Creative product-modification agent: GA + semi-supervised learning; modified PEAS; multi-agent
- **PEAS changes:**
  - P adds novelty, surprise, usefulness and diversity (a creativity calibrator).
  - E goes from closed to open: market trends, competitors, IoT usage data, other domains.
  - A generates variants and presents ranked choices or prototypes.
  - S senses previous and competing performance and user reactions.
- **The SSL + GA loop:**
  1. Train a fitness predictor from a few labelled "successful/creative modifications" plus many unlabelled
     designs (self-training or label propagation).
  2. The GA generates variants (as in the slides' car GA), and the predictor scores them.
  3. Add high-confidence pseudo-labels to the training set, so the learn set evolves → the algorithm
     evolves → the outcome evolves.
- **Multi-agent co-operative creativity:**
  - agents: generator (divergent), critic (convergent), cost, aesthetics (living geometry), user-proxy;
  - a shared blackboard;
  - an **island-model GA** with migration;
  - ensemble creativity (bagging/boosting);
  - "Positive + Positive < Negative + Positive".
  Examples: grass cutter + tricycle; the car GA.

### Q7 — Dynamic heuristic; hill climbing for the best employee; RL + HC learning agent
- **Dynamic h: yes.** It changes over time, context and feedback.
- **h(e)** = w1·performance + w2·peer feedback + w3·projects delivered + w4·innovation (ideas
  implemented) + w5·learning/upskilling − w6·incidents.
- **Neighbours:** employees linked in the collaboration graph or with a similar role.
- **Hill climbing:** start from a random employee and move to a better neighbour. The local maximum is the
  best within one department.
- **Learning agent mapping:**
  - The performance element is the HC search.
  - The critic is HR or management validation (subsequent performance, team satisfaction) and provides the
    **reward**.
  - The learning element adjusts the weights w by RL. Q(s, a) covers actions {move to a neighbour, jump
    department (exploration), stop}.
  - The problem generator proposes random restarts in other departments.
- Show the reward update `w ← w + η·(r − r̂)·f(e)` or Q-learning.

### Q8 — Search space; multi-agent combination of two drawing patterns
- **Search space:** the set of states reachable from the start via the operators (an implicit tree or
  graph).
- **Agent roles:** Agent 1 owns pattern P1 (say, a spiral) and Agent 2 owns P2 (a zig-zag or tessellation).
- **State:** the canvas, a set of primitives with parameters. **Basic actions:** line, arc, rotate, scale,
  translate, colour.
- **Combining two actions:**
  - **composition** (`a2∘a1`, e.g. rotate + scale = spiral step);
  - **interleaving**;
  - **parameter blending** (interpolation);
  - **conditional**.
  The new macro-action expands the action space and so the search space. Both agents propose combinations
  and negotiate.
- **Fitness:** `w1·novelty(distance from P1, P2 and the archive) + w2·aesthetics (symmetry, balance,
  Alexander's 15 properties) + w3·coherence (balanced inheritance from P1 and P2) + w4·human rating`.

### Q9 — P-creativity via EA → H-creativity; challenges; conceptual space expansion
- **P-creativity via EA:** evolved designs that are new to the system (the car GA, POEVOLVE/McGonnagall
  poems, GenJam riffs, evolved NN architectures, product variants).
- **Extending to H-creativity** means checking novelty against the *global* historical archive rather than
  the agent's own.
- **Challenges:**
  - incomplete historical knowledge;
  - subjective, social evaluation of value;
  - novelty vs usefulness;
  - combinatorial explosion;
  - a human-defined fitness biased toward the known;
  - premature convergence;
  - homogenization ("AI reduces collective diversity");
  - slow expert validation.
- **Fixes:**
  - novelty search with a global archive (embedding similarity to patents and literature);
  - multi-objective fitness (novelty, value, surprise);
  - island models;
  - human-in-the-loop creativity tests;
  - dynamic fitness;
  - operators that change the representation.
- **Expanding the conceptual space:**
  - add quality dimensions (new IoT sensors);
  - release the boundaries of compatibility;
  - change R and T (Wiggins), i.e. transformational moves;
  - merge spaces across domains (the systemic view);
  - generalize properties (the GENERATE slide).

### Q10 — Intelligent vs creative agent and search; a function to expand search and action space; utility agent + RL
- **Intelligent search** reaches the goal efficiently. **Creative search** generates new options, combines
  nodes, creates action sets and redefines the neighbour.
- **Agents:** the intelligent agent is rational. The creative agent is rational but non-obvious and adds
  the creativity calibrator and conceptual space expander.
- **Expansion function:**
  ```
  expand(S, A):
    A_new = compose(A) ∪ analogize(A, other_domain) ∪ vary_params(A)
    S_new = {a(s) | s∈S, a∈A_new} ∪ crossover(top_k(S)) ∪ relax_constraints(S)
    keep x if novelty(x)>τ_n and usefulness(x)>τ_u
    return S∪S_new, A∪A_new_kept
  ```
- **Product design** with a utility-based agent, U(design) = function + cost + aesthetics + novelty.
  RL options for expanding the action space:
  1. macro-actions/options (hierarchical RL);
  2. parameterized continuous actions;
  3. mining frequent successful action sequences into new actions;
  4. analogy/transfer from other products;
  5. human co-creator suggestions;
  6. curiosity (intrinsic reward for novel states);
  7. a GA over action sequences.

### Q11 — Connectionist vs reductionist; Manhattan-distance IDS to expand the conceptual space (D4); mobile phone features
- **Reductionism** understands the parts first, then the whole, one part at a time. **Connectionism** finds
  connections and associations (networks of units settle into a stable state, the whole emerges). Holism.
- **Phone feature space:** discrete levels per dimension (camera, battery, screen size, foldability,
  sensors, AI features, price).
  - One unit move changes one feature by one level.
  - Iteration d explores all designs within **Manhattan distance d** of the current phone (the rings in D4).
    The next iteration expands the search space.
  - The red arrow is a preferred expansion path (e.g. camera + AI). Expand along that path first, or weight
    it.
- **Pseudocode:**
  ```
  for d = 0..Dmax:
    DLS(start, limit=d)        # states s with |s−start|_1 ≤ d
    evaluate creativity of the new ring
    if a ring adds viable new concepts: record them, maybe add a new dimension (new sensor)
  ```
- **Connectionist vs reductionist angle:** a connectionist evaluator (neural embedding) vs a reductionist
  per-feature scoring.

### Q12 — Expand the action space by combining two basic actions (a game); goal = f(action space, search space)
- **Grid game example:** the basic actions are up, down, left and right (plus jump and shoot).
  - Pairwise combinations: up+right = diagonal, jump+right = long jump, move+shoot = strafe.
  - With n basic actions there are up to n(n−1)/2 unordered or n² ordered pairs.
- **Quantified effect with Manhattan IDS:** the reachable cells at depth d go from 2d²+2d+1 (4 moves) to
  (2d+1)² (8 moves). At **d = 2 that is 13 → 25**. The search space expands.
- **Goal = f(A, S):** e.g. maximize the score reachable within depth d, or a target that is reachable only
  with the new actions. Redefine the goal whenever the action space grows.

### Q13 — Model P-creativity as a special function of H-creativity; constrained → expanding space (D5)
- **Definitions:**
  - `novelty_H(s) = min dist(s, Archive_history)`
  - `novelty_P(s) = min dist(s, Archive_agent)`, with Archive_agent ⊆ Archive_history.
  - P-creativity is the H-function restricted to the agent's own memory: **P(s) = H(s | archive = own)**.
- **Algorithm (D5):**
  1. Start with a small constrained space (the circle around j), where most actions are new to the agent,
     i.e. P-creative.
  2. Expand the radius gradually and eliminate states (visited or low fitness).
  3. When no state is left, **combine the top-n states** (crossover or blend) into new states. The centre
     moves j → n → i.
  4. Repeat until no new state falls beyond the final expanded space (closure).
  5. Return the ranked final state set.
- Give pseudocode with a loop of radius r, `elimination`, and `combine_top_n`.

### Q14 — K-means + KNN semi-supervised learning; cultural tour clustering; Euclidean + Hamming; systemic creativity (D6)
- **SSL loop:**
  1. Run K-means over all (mostly unlabelled) destinations.
  2. A few labelled destinations (cultural category: heritage, religious, art/modern, culinary, nature)
     name the clusters.
  3. KNN classifies new destinations using labelled plus cluster-pseudo-labelled points.
  4. Iterate (self-training).
- **The tour:** pick the cluster matching the traveller's culture profile, then order the stops by route
  (a nearest-neighbour TSP heuristic).
- **Combined distance:** `d = α·d_Euclid(normalized numeric: spend, growth, visits, cost, travel time) +
  (1−α)·d_Hamming(binary cultural attributes)/m`. This is Gower-like.
- **Systemic creativity:**
  - treat tourism as a system linking culture, food, economy, transport, weather, events and IoT footfall
    sensors;
  - build cross-cluster tours (e.g. Istanbul bridging Europe and Asia);
  - dynamic re-clustering on live data;
  - explore unexplored relationships (opportunity maps).
- **Modified D6 for cultural preference:**
  - x = cultural-heritage index (or Hamming similarity to the traveller's profile), y = preference-match
    score;
  - colour = cultural cluster instead of region; size = visits.
  - Example clusters:
    - heritage: Rome, Istanbul, Prague;
    - art/design: Paris, Barcelona, Milan, Vienna, Amsterdam, London;
    - modern/shopping: Dubai, Singapore, Hong Kong, New York, Seoul, Tokyo;
    - street-food/culinary: Bangkok, Osaka, Taipei, Kuala Lumpur, Shanghai.

### Q15 — Product recommendation as heuristic search (same as the surprise test)
- **h:** the distance between the product vector and the user-preference vector, `h(p) = ||u − v_p||`, or
  utility. **Start:** the last viewed or most popular product. **Goal:** h ≤ ε, or a purchase.
  **Actions/neighbours:** similar products (same category or adjacent price band; one attribute changed).
- **Hill-climbing traversal:** a table of 10 products P1–P10 with scores, the path, and where it stops.
  - **Local maximum:** the best in the current category (e.g. stuck in phones when the user would prefer a
    tablet). **Global maximum:** the best overall.
- **Multiple goals:** a weighted sum or Pareto set, a goal set or bundle, top-k or beam, multi-start.
- **A\* vector transition with correction:**
  - `f = g + h`, with g = cumulative user effort or dissimilarity travelled, h = ||u − v||.
  - On feedback, correct the preference vector (Rocchio-like): `u' = u + α(v_liked − u) − β(v_skipped −
    u)`. Then recompute h and re-plan.
- **HC modifications:** SA ("slow heat, gradual cooling"), random restart, tabu, stochastic, beam,
  serendipity jumps (lateral moves), humanized aspects (mood, Gestalt "surprise at critical point",
  "neighbours matter"), and a dynamic heuristic.

---

## Part C — The course's phrases to use in answers

- choices, not answers
- creativity calibrator
- conceptual space expander
- rational but non-obvious
- dynamic and evolving heuristic functions
- redefine the neighbour
- introduce a new action / introduce a new state
- expand search space / expand action space
- merge states
- the learn set evolves → the algorithm evolves → the outcome evolves
- creativity companion / co-creator / creativity booster
- Positive + Positive < Negative + Positive
- adding a sensor modality changes the space, not merely the data
- releasing the boundaries of compatibility
- exploratory / combinational / transformational
- P- and H-creativity
- slow to heat and gradual cooling
- surprise at the critical point
- neighbours matter
