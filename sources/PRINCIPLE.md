# Principles of Cognition

---

## Core Thesis

> **A decision only has meaning when context is sufficient.
> Context is built from two sources: endogenous (imagination) and exogenous (exploration).
> Cognition is a convergence loop between these two sources.**

---

## 1. Collapse

A decision is not "chosen" — it *emerges* when context is sufficiently coherent.

Insufficient context → no meaningful decision.
Contradictory context → collapse fails.
Converged context → collapse happens naturally.

**Never act with insufficient context. If you don't know enough, the action is to KNOW MORE, not to guess.**

---

## 2. Two Paths to Expand Context

When context is insufficient, there are exactly two ways to expand it:

**1. Imagination (endogenous)**
> Use what is already known to infer what is not yet known.
> Generate possible cases without requiring additional input from the world.

**2. Exploration (exogenous)**
> Acquire additional input from the world to confirm or eliminate cases from (1).

There is no third path.

---

## 3. The Convergence Loop

The two paths are not independent — they loop:

```
context insufficient
  → [1] imagine: generate cases from what is known
  → [2] explore: observe to confirm or refute
  → gap narrows → context updated
  → sufficient → collapse
  → insufficient → return to [1] with updated context
```

Convergence = the gap between imagination and observation is small enough.

---

## 4. Meaning Depends on Frame

```
M = f(N, F)
```

- **N**: name / identifier of a concept
- **F**: the set of currently active context — the frame
- **M**: meaning — only valid within that specific F

Same N, different F → different M.

There is no absolute meaning. Meaning is a relation between concept and context.
Collapse is only valid once the frame is determined.

---

## 5. Memory is Layered by Rate of Change

Not all context changes at the same speed.
Slower layers are not reset by faster layers.

```
invariant          → cross-domain, never changes
quasi-invariant    → learned gradually, stable after many observations
spatial / episodic → changes per situation
momentary          → exists for one tick, one token, one step
```

Mixing layers → noisy context → wrong collapse.

---

## 6. Gap is the Driver of Learning

Gap = the distance between imagination and observation.

Gap is not an error — gap is a signal.
No gap → no learning.
Large persistent gap → fastest learning.

```
gap appears
  → classify: where in the loop does the gap live?
  → generate hypothesis to fill the gap
  → test via exploration
  → gap narrows → knowledge increases
```

---

## 7. Multi-channel Input — Collect First, Filter Later

The human brain renders a world model from at least 5 parallel channels.
No channel is "primary" — each provides a type of context that no other channel can replace.

**Principle:**

> You cannot know in advance which channel is meaningful in this situation.
> Collect all available channels first, then filter.
> A missing channel = a blind spot in the world model = insufficient context = wrong collapse.

**Possible channel types:**

| Channel | Type of information | Sensory analog |
|---|---|---|
| Visual frame (pixel grid) | spatial, objects, color, motion | vision |
| Progress signal (score, levels) | reward, right/wrong direction | taste — safe/unsafe |
| Resistance signal (blocked, collision) | physics, boundaries | touch |
| Action space (available_actions) | current capabilities | proprioception |
| State flags (WIN, RESET, GAME_OVER) | alerts, thresholds | hearing — danger signal |
| Temporal delta (tick-over-tick diff) | motion, change, causality | dynamic vision |
| Metadata / data dict | game-specific context | implicit background |
| Multi-layer frames | foreground/background separation | depth perception |
| Inventory / carried state | internal state | interoception |

**Consequence:**

Each situation has a different dominant channel.
A passive agent (reads only one channel) → incomplete world model → collapse on insufficient information.
An active agent (prepares all channels, uses whatever is available each tick) → fuller world model → more accurate collapse.

---

## 8. Three Object Classes in Any Game

Every game world has exactly 3 types of entities:

**1. Avatar Player (self)**
> The entity you control. Moves in response to your actions.
> You do NOT "become" the player — you OBSERVE and CONTROL it from outside (3rd person perspective).
> This means: you can see the player's coordinates BEFORE acting. This is an advantage over real-time human play.

**2. Avatar Objects (interactive entities)**
> Things in the world that respond to interaction: doors, keys, rotators, items, enemies, switches.
> They have state. Their state can change when player touches/approaches them.
> Each one is a potential cause-effect pair waiting to be discovered.

**3. Avatar Environment (static world)**
> Walls, floor, background. Never changes. Defines the boundaries of what is possible.
> Once observed, can be cached permanently — invariant layer (P5).
> Wasting actions on confirmed-static entities = wasting energy.

**Consequence:**

First action in any game should be: classify every pixel/object into one of these 3 types.
- Type 3 (static) → cache, never re-examine
- Type 1 (self) → track position every frame
- Type 2 (interactive) → these are the UNKNOWNS. All learning comes from interacting with Type 2.

---

## 9. Context Query Protocol — Questions Before Actions

> The quality of a decision is bounded by the quality of the context that produced it.
> Context does not arrive automatically — it must be QUERIED.
> Each query = attention directed at a specific sensor or memory channel.
> No query = no context from that channel = blind spot.

**Before every action, answer these 7 questions:**

| # | Question | Source | What it gathers |
|---|----------|--------|-----------------|
| Q1 | Where am I? | S5 (self-location) | Exact coordinates of player avatar |
| Q2 | What is around me? | S3 (objects) + spatial map | All entities within interaction range |
| Q3 | Where can I go? | S4 (walkable map) + BFS | Reachable positions, paths to targets |
| Q4 | What just changed? | S2 (delta) + S13 (causality) | Effect of last action — confirms/rejects hypothesis |
| Q5 | What is my goal right now? | D (field map) + gap analysis | Current target, key-door match status, biggest gap |
| Q6 | What have I already tried? | D (action history, tested entities) | Avoid repeating failed actions, build on successes |
| Q7 | How much budget remains? | S8 (energy) + action count | Collapse pressure — when to stop exploring and commit |

**Rules:**
- All 7 answered → sufficient context → collapse into action
- Any question unanswered → that IS the action: explore to answer it
- Q7 critical (low budget) → force collapse even with incomplete context (P1: collapse pressure)
- Q4 is the LEARNING channel — every action produces a Q4 answer. If Q4 says "nothing changed" → that action is dead for this situation.

**This protocol IS the convergence loop (P3) made concrete:**
- Q1-Q3 = exogenous (what do sensors tell me NOW)
- Q5-Q6 = endogenous (what do I already know / imagine)
- Q4 = the bridge (did reality match imagination?)
- Q7 = collapse pressure (when to stop looping)

---

## 10. Universal Game Solving — Interaction Chain

> This principle applies to ALL games, ALL levels, ALL genres.
> It is the invariant structure of how difficulty scales.

**The simplest game:**
```
A → B
Player → Goal
```

**How difficulty increases — the ONLY way:**
```
A → [interact O1] → B
A → [interact O1] → [interact O2] → B
A → [interact O1] → [interact O2] → ... → [interact On] → B
```

Every level harder than the last = **one more interaction inserted between player and goal.**
The chain never changes structure. Only its LENGTH grows and its ELEMENTS vary.

### Each interaction object has exactly 2 variables:

**1. Position (WHERE)**
> Where the object sits relative to A→B path.
> On the direct path = cheap (detour = 0).
> Off the path = expensive (detour > 0, consumes energy/budget).
> The shortest path may not go through all required objects → path planning must account for interaction order.

**2. Interaction Property (HOW)**
> How the player must interact with this object:
> - Touch once (pass through)
> - Touch multiple times (rotator: cycle states)
> - Push / pull (change object position)
> - Carry (pick up → use elsewhere)
> - Activate from specific direction
> - Stand on / trigger by proximity
> - Sequence-dependent (must interact with O1 before O2 becomes active)
>
> The property is UNKNOWN at first. Must be discovered through exploration (P2 + P6).

### Solving any level = answering 3 questions:

```
Q_game1: What objects exist between A and B? (scan — P7, P8)
Q_game2: In what ORDER must I interact with them? (sequence — P6, causal chain)
Q_game3: HOW do I interact with each one? (property — P2, explore + test)
```

### The interaction chain is INVARIANT across all games:

| Game | A | Chain | B |
|------|---|-------|---|
| Locksmith | player | rotate_key → match_door | exit_door |
| Sokoban | player | push_box → fill_hole | goal_tile |
| Zelda | player | find_key → kill_enemy → unlock_door | treasure |
| Portal | player | place_portal → walk_through | exit |
| Any puzzle | player | [interact O1] → ... → [interact On] | win_condition |

**The game genre, art style, and specific mechanics are VARIANT.**
**The chain structure A → [O1...On] → B is INVARIANT.**

### Object may be noise (decoy)

Not every interactive-looking object is part of the chain.
Some objects exist but contribute NOTHING to solving the level — they are **decoys / noise**.

> You cannot know in advance if an object is real (on-chain) or noise (off-chain).
> The only way to distinguish: interact with it → Q4 check → did it bring you closer to B?
> If no effect on chain progress after 2 attempts → classify as noise → ignore.
>
> Noise objects waste energy and budget. Identifying them early = efficiency.
> But ignoring a REAL object because it LOOKS like noise = stuck forever.
>
> Default: assume every object is real until proven noise. (False positive < false negative)

### Consequence for the solver:

1. **First scan**: find A (player), B (goal), and ALL O's (interactive objects)
2. **Classify O's**: which are on the chain (required) vs decoration (irrelevant)?
3. **Order O's**: which must be interacted with first? (causal dependency)
4. **Learn each O's property**: touch it → Q4 what changed? → hypothesis → confirm
5. **Execute chain**: A → O1 (with correct interaction) → O2 → ... → B
6. **Next level**: same chain structure, maybe +1 object, maybe different properties

This is why P6 (gap drives learning) is the most important principle for games:
- Gap = "I don't know what O3 does" → test it → learn → chain complete
- No gap = chain fully known = execute and win

### Chain = sequence of ADJACENT PAIRS, not all-pairs

```
A → B → C → Z
  chain1  chain2  chain3
```

- N objects between A and Z = **N+1 nodes, N chains (adjacent pairs only)**
- NOT N×(N-1)/2 (not every pair interacts — only consecutive ones)
- Each chain = transformation from one node to the next
- Each chain = one of the **28 known chain variants** (from P21)
  - 17 condition-driven (WHY→WHERE→WHAT)
  - 7 region-driven (WHERE→WHY→WHAT)
  - 4 trivial (WHAT→WHERE→WHY)

**Chain structure is INVARIANT**: always A → [O1→O2→...] → Z, always adjacent pairs.
**Chain content is VARIANT**: which objects, which variant type, which parameters.
**Chain LENGTH is VARIANT per level**: L1 = 2 chains, L2 = 3 chains, L3 = 4 chains...

Each chain variant learned from one game/puzzle applies to another if the triple (WHAT, WHERE, WHY) matches.
800 ARC tasks → 28 variants. New game: detect which variant each chain is → retrieve order → execute.

### Every object is UNIQUE even if same function

Two energy pills have the same function (refill) but are DIFFERENT objects:
- Different position → different cost to reach
- Different order → different chain sequence
- Different context → different dependency

**N objects = N! possible orderings.** Every object is unique even if function is identical.

```
General: N objects between A and Z
  Permutations = N!
  N=1: 1
  N=2: 2
  N=3: 6
  N=4: 24
  N=5: 120
  ...
```

Same function ≠ same object. Two energy pills at different positions = different ordering implications.
Each object has unique: **position, context, dependency, cost-to-reach.**

**Solving = choosing 1 permutation out of N!** by reasoning:
1. **Dependency**: does O_j require O_i first? → O_i before O_j (prune permutations)
2. **Position**: total travel cost per permutation → minimize
3. **Budget**: resource constraints (energy, steps) → prune infeasible permutations
4. **Effect propagation**: does O_i change state that affects O_j? → order matters

Dependency alone can prune N! dramatically:
- If O2 depends on O1 → eliminates half the permutations
- If O3 depends on O2 → further prune
- Strong dependency chain → only 1 valid ordering

Weak dependency (all independent) → must evaluate by position/budget.

**The correct ordering IS the solution. Finding it IS the reasoning.**

### Object = 5 dimensions

Every object on the chain exists as exactly 5 properties:

```
Object = (position, shape, function, state, trigger)
```

1. **Position** — where on map (x, y)
2. **Shape** — visual appearance (pixels, color, size, pattern)
3. **Function** — what interaction produces (refill, rotate, block, teleport, advance...)
4. **State** — current condition (active/inactive, used/unused, on/off)
5. **Trigger** — how to activate (pass-through, click, proximity, sequence, direction...)

Two objects with same function but different position = DIFFERENT objects.
Two objects with same position but different function = DIFFERENT objects.
Any 1 dimension different = different object.

Function is just 1 of 5. Refill = a function. Shape = visual identity. Trigger = interaction method.
All 5 must be known to fully understand an object.

**Ordering depends on ALL 5 dimensions:**
- Position → travel cost
- Function → dependency (does O1's function enable O2?)
- State → is it available now?
- Trigger → can player activate it from here?
- Shape → recognition (is this the same type as one seen before?)

---

## 11. Think Before Look — Superposition of Possibilities

> Everything exists in superposition until input collapses it.
> Cognition is NOT: see → think → act.
> Cognition IS: think (imagine possibilities) → see (input collapses) → act (on collapsed reality).

**Before receiving ANY new input, the mind must IMAGINE what is possible.**

This is how humans work:
- Before opening a door, you imagine: room, hallway, outside, danger.
- When you open it and see a hallway → possibilities collapse to one.
- You never "see" without expectations. Seeing without thinking first = surprise = slow reaction.

**Applied to games:**

Before scanning a new level, use LTM (sea map + gravity) to generate possibilities:

```
From L1 experience:
  → game has: player, rotator, door, key, energy     (quasi-invariant)
  → mechanism: rotate key → match door → enter       (invariant)
  → each level adds complexity                        (quasi-invariant)

Possibilities for L2 (BEFORE looking):
  P1: door at different position                      (likely, based on P10)
  P2: rotator at different position                   (likely)
  P3: new objects exist                               (likely, P10 says chain grows)
  P4: new objects = energy refill OR color rotator     (hypothesis from game rules)
  P5: need more rotations than L1                     (likely, increased difficulty)
  P6: corridor layout completely different             (likely)
  P7: energy might not be enough                      (possible, increased difficulty)
```

**After scanning L2 frame, each possibility COLLAPSES:**

```
  P1: door at (15,41) not (36,11)                     → COLLAPSED: confirmed different
  P2: rotator at (51,47) not (21,32)                   → COLLAPSED: confirmed different
  P3: 2 yellow squares (16,17) and (41,52)             → COLLAPSED: new objects exist
  P4: yellow = energy refill? color rotator? unknown?   → NOT YET: need interaction to collapse
  P5: door pattern needs R3 = 3 rotations              → COLLAPSED: confirmed
  P6: maze completely different                        → COLLAPSED: confirmed
  P7: energy runs out before 3 rotations               → COLLAPSED: confirmed, need refill
```

**Uncollapsed possibilities = gaps = what to explore next.**

P4 is uncollapsed → highest priority → action = go interact with yellow square.

**This is VEG made concrete:**
- V (drift): uncollapsed possibility with most connections drifts to top of attention
- E (evaluate): each interaction adds input → collapses or eliminates a possibility
- G (genesis): remaining possibilities generate new actions to test

**Rule: NEVER act on uncollapsed possibilities. Either collapse them first, or choose the action that collapses the most possibilities at once.**

---

## 12. Color Gradient = Map Topology

> Before detecting objects, read the MAP itself from color gradients.
> Bright pixels = paths. Dark pixels = walls. The brightness pattern IS the road network.

In ARC-3 games:
```
color 3 (dark gray, bright relative to walls)  = corridor = CAN walk
color 4 (near black)                           = wall     = CANNOT walk
color 5 (black)                                = border   = structure edge
```

**One glance at the brightness map reveals:**
- Where corridors go (path network)
- Where junctions are (corridors cross)
- Where dead ends are (corridor terminates)
- Corridor width at each point (narrow = might not fit player body)
- Which areas are connected vs isolated (islands)

**This is S4 (spatial map) done RIGHT:**
- Don't BFS pixel-by-pixel
- Render brightness map → see the ROAD NETWORK
- Then plan paths ON the network, not on individual pixels

**Implementation:**
1. Extract all pixels where color == 3 (walkable)
2. Skeletonize → find corridor center lines
3. Build graph: nodes = junctions, edges = corridor segments with WIDTH
4. Player body = 5×5 → only traverse edges with width >= 5
5. BFS/A* on corridor graph, not on pixel grid

**Why this matters:**
Without topology: player tries to walk through walls, gets stuck, wastes energy, dies.
With topology: player knows exactly which corridors connect, which are wide enough, shortest path pre-computed before first step.

---

## 13. Bipolar Field Map — Object as Anchor Between Invariant and Variant

> Every object sits at the CENTER between two poles.
> Properties of the object are VALUE NODES that orbit between the object and their pole.
> This is the fundamental data structure for representing knowledge.

**Structure:**
```
[INVARIANT POLE] ←── value_node ←── OBJECT ──→ value_node ──→ [VARIANT POLE]
```

- **Object** = always at center. Never at a pole. It IS the anchor.
- **Invariant pole** = the pole of "never changes". Identity. Mechanism. Structure.
- **Variant pole** = the pole of "always changes". Position. State. Pattern.
- **Value nodes** = properties of the object. Each property sits BETWEEN the object and whichever pole it belongs to.

**Minimum viable system = 3 nodes:**
```
[INV pole] ── OBJECT ── [VAR pole]
```
Any object with fewer than 3 nodes (no invariant OR no variant) is either:
- Pure invariant (decoration, environment constant) → collapses to INV pole
- Pure variant (noise, ephemeral) → collapses to VAR pole
- Orphan → attracted by GRAVITY toward nearest system

**Example: Player**
```
[INV] ←─ FDIC=1.094529 ─← PLAYER →─ position=(31,40) ─→ [VAR]
          shape=5x5      /         \   energy=36
          controllable  /           \
```
Player identity (FDIC, shape) = close to INV pole. Player state (position, energy) = close to VAR pole.
Player itself = always center. You can find Player anywhere on the map because its INV side never changes.

**Example: Door**
```
[INV] ←─ structure=c5+c9 ─← DOOR →─ position=(varies) ─→ [VAR]
          role=exit        /       \   pattern=(varies)
          trigger=match   /         \   FDIC=(varies)
```
Door is BALANCED — 3 INV, 3 VAR. Harder to track than Player because more properties vary.

**Example: Energy_Pip**
```
[INV] ←─ FDIC=0.809558 ─← ENERGY_PIP   [VAR = empty]
          location=BR
          color=8
```
Pure invariant. No variant properties. Collapses toward INV pole. Background constant.

**Gravity rule:**
- An orphan node (not part of any 3-node system) gets PULLED toward the nearest system.
- Pull strength = number of shared properties with that system's objects.
- If pulled toward INV pole of a system → it's a known type.
- If pulled toward VAR pole → it's a transient phenomenon.
- If pulled toward no system → it's noise (P10: decoy).

**Building the map:**
1. Start with SEA (flat, no gravity) — detect all objects, list all properties
2. Classify each property as INV or VAR (cross-level comparison)
3. Place object at center, INV properties toward INV pole, VAR toward VAR pole
4. Form systems: 3+ objects whose value nodes connect (shared mechanisms)
5. Orphans → gravity pulls into nearest system or declares noise
6. Gravity accumulates from interaction evidence (P6: gap drives learning)

---

## 14. The Fundamental Triad — Player, Door, Object

> Every game is exactly 3 things:
> 1. PLAYER (constant) — always exists, always controllable, always wants to reach door.
> 2. DOOR (constant) — always exists, always the goal, always requires conditions to enter.
> 3. OBJECTS (variable) — everything between player and door. Changes every level.

```
[PLAYER] ←── OBJECT(s) ──→ [DOOR]
  constant    variable      constant
```

Player and Door are the TWO CONSTANTS of every game. They define the problem:
**"I am here (player). I need to be there (door). What's in between?"**

Objects are the VARIABLE. They are what makes each level different:
- L1: 1 rotator between player and door
- L2: 1 rotator + unknown objects between player and door
- L3: more objects, harder interactions

**Solving = removing/satisfying each object between player and door.**

Each object BLOCKS the player→door path in some way:
- Rotator blocks because door won't open without matching key
- Wall blocks physically
- Energy limit blocks by time constraint
- Unknown object blocks because you don't know what it does

**Interaction with object = changing its state so it no longer blocks.**
- Rotate key → key matches → rotator no longer blocks
- Find path around wall → wall no longer blocks
- Find energy refill → energy no longer blocks

**Synchronizing two systems:**
The game has only 2 systems that need sync:
1. **Player system** (where am I, what can I do, how much energy)
2. **Door system** (where is door, what conditions to enter)

Objects are NOT a system — they are the INTERFACE between the two systems.
Each object translates "player action" into "door condition satisfied."

**Solving order:**
1. Identify all objects between player and door
2. For each object: what does player need to do → what door condition does it satisfy?
3. Order by dependency (can't rotate key if you can't reach rotator)
4. Execute in order

**This is P10 (interaction chain) made even simpler:**
- P10 says: A → [O1...On] → B
- P14 says: Player and Door are ALWAYS A and B. Objects are ALWAYS the chain between them.
- The chain is not a property of the game. It's the DEFINITION of what a game is.

---

## 15. Node Flattening — List All, Then Fold by Shared Values

> When there are many objects between Player and Door, the chain gets complex.
> Solution: flatten everything into individual value nodes, then FOLD by shared values.

**Step 1: Flatten**
Every object → list ALL its properties as individual nodes on the Player→Door line.

```
Player → [fdic=0.803] → [color=11] → [pattern=KKK] → [pos=(16,17)] → ... → Door
               ↑ Yellow_Sq_1 properties
```

**Step 2: Fold**
Find properties SHARED between different objects → fold them into ONE node.

```
Yellow_Sq_1: fdic=0.803, color=11, pattern=KKK, pos=(16,17)
Yellow_Sq_2: fdic=0.803, color=11, pattern=KKK, pos=(41,52)
                    ↓ FOLD shared values ↓
Yellow_TYPE: fdic=0.803, color=11, pattern=KKK
  instances: pos=(16,17), pos=(41,52)    ← only position differs
```

Two objects collapse to ONE TYPE + variant instances.

**Step 3: Connect types by shared values**
```
Rotator:    markers=color_0+1, mechanism=rotate_key
Yellow_TYPE: color=11, pattern=KKK
Door:       structure=c5+c9, trigger=key_match

Rotator.mechanism=rotate_key → Key.pattern → Door.trigger=key_match
  → Rotator connects to Door through Key

Yellow_TYPE.color=11 = Energy_Bar.color=11
  → Yellow might connect to Energy system

Yellow_TYPE.color=11 ≠ Rotator.markers=color_0+1
  → Yellow NOT same type as Rotator
```

**Step 4: Infer causal order from connections**

Shared values = edges. Follow edges from Player to Door = chain.
No shared value = no connection = noise (or unexplored).

**Why flatten first:**
- You can't see connections between objects by looking at objects.
- You CAN see connections by looking at individual VALUES.
- Same value in 2 objects = they are related.
- Different values everywhere = they are independent.
- Flattening makes the invisible visible.

**Why fold:**
- Too many nodes = can't reason.
- Folding reduces dimensionality.
- After fold: each unique TYPE appears once, with variant instances listed.
- Chain becomes: Player → Type_A → Type_B → Door (manageable).

---

## 16. Test Unknown Objects Using ALL Known Mechanisms

> When you discover a new object, do NOT test it only one way.
> Test it using EVERY mechanism you have already learned from other objects.

**The mistake:**
- Rotator triggers by "pass through" (not "stand next to")
- Yellow square tested by "stand next to + press direction" → no effect → classified as noise
- But yellow ALSO triggers by "pass through" → never tested → missed

**The rule:**
```
For each unknown object:
  For each known mechanism (pass-through, touch, stand-on, click, approach-from-direction):
    Test object with that mechanism
    Q4: what changed?
    If any effect → collapse role → add to chain
```

**Why this matters:**
- Games reuse mechanisms across objects (pass-through for rotator AND flipper)
- New objects may use OLD mechanisms with NEW effects
- Testing only the "default" way = missing the real interaction
- 1 failed test ≠ noise. Must exhaust ALL known mechanisms before declaring noise.

**Corollary:** The set of known mechanisms GROWS with each level.
L1 teaches: pass-through = triggers change.
L2 should test: does pass-through work on yellow? YES → flip key.
L3 might add: click, push, carry, sequence-dependent, etc.

---

## 17. Fractal Decomposition of Input — Invariant Extraction at Every Scale

> Sensor collects raw signal. I.P PROCESSES it by extracting invariant at every scale.
> Never test specific cases. Extract the RULE that covers all cases.

**Method: recursive split of VARIANT into (invariant_small + variant_small)**

```
Layer 1:
  Invariant: action exists → pixels change → something responds
  Variant:   WHICH action, WHICH pixels, WHAT change

Layer 2 (split variant):
  Invariant: each action has its own affected pixel set
  Variant:   where those pixels are, how many

Layer 3 (split variant):
  Invariant: changed pixels = disappeared_group + appeared_group (object moved)
  Variant:   direction and distance of movement

Layer 4 (split variant):
  Invariant: moved object = same colors, same pattern, different position
  Variant:   position delta (dx, dy)

Layer 5 (atomic):
  Invariant: delta is consistent across repeated same-action → deterministic movement
  Variant:   nothing left to split → this is the atom
```

**Stop when:** variant is atomic (1 pixel, 1 step, 1 frame). Cannot split further.

**This replaces:** "try UP, if fail try LEFT, if fail try CLICK" (brute force)
**With:** "try ALL available_actions, collect ALL deltas, extract invariant structure from the SET of deltas"

**Sensor vs I.P:**
- Sensor (I.I) = raw: frame pixels, state flag, action list, level count
- I.P = process: delta computation, object clustering, movement extraction, invariant/variant split
- I.O = output: processed Perception with objects, player, movement rules
- I.D = memory: previous frames, known movement patterns

**Sensor does NOT change per game.** I.P processing does NOT change per game.
Only the DATA changes. The decomposition algorithm is universal.

---

## 18. Binary Classification First — The Universal Split

> Before any game-specific logic, split ALL pixels into exactly 2 groups.
> Then split again. 2 → 3 → done. Universal. Works on any 2D game.

**Step 1: Binary split**
```
        [ALL PIXELS]
       /            \
[RESPONSIVE]    [NON-RESPONSIVE]
 (delta > 0)     (delta = 0 always)
                  = ENVIRONMENT
```
Method: compare frames before/after actions. Pixels that NEVER change = environment.

**Step 2: Binary split of RESPONSIVE**
```
    [RESPONSIVE]
    /          \
[CONTROLLABLE]  [NOT CONTROLLABLE]
 (moves WITH    (changes but NOT
  my action)     in my control)
  = PLAYER       = OBJECT
```
Method: player pixels move in SAME DIRECTION as action input.
Object pixels change but direction/timing doesn't match action.

**The full tree:**
```
        [ALL PIXELS]
       /            \
[RESPONSIVE]    [ENVIRONMENT]
   /      \       (never changes)
[PLAYER]  [OBJECT]
(moves     (changes on
 with       interaction,
 action)    not direct
            control)
```

**This is the ONLY classification needed.**
No color check. No FDIC. No heuristic.
Just: does it respond? → does it obey me?

**3 types from 2 binary splits = universal for ALL 2D games.**
Every pixel in every game falls into exactly one of these 3 categories.

The rest (what TYPE of object, what it DOES) = interaction testing (P layer).
I layer only needs to answer: responsive or not? controllable or not?

---

## 19. Reverse Trace — Learn Mechanism from Solution, Not from Trial

> If you have both the start (A) and the end (Z), don't learn forward A→Z.
> Learn BACKWARD Z→A. The backward trace reveals the mechanism.

**Forward learning** (A→Z): try action → observe → try another → slow, wasteful, may never converge.

**Backward tracing** (Z→A): look at Z → what nodes must be active to produce Z? → that's step Y → what produces Y? → step X → ... → back to A. Each step backward = one layer of causality revealed.

**Why backward is better:**
- Forward: exponential branching. From A, 4 actions → 4 states → 16 states → ...
- Backward: convergent. Z is ONE state. What produces it? Usually 1-2 possibilities. Y is constrained. X is constrained. Path narrows going backward.
- Forward: you don't know if you're getting closer (no gradient toward Z).
- Backward: every step you KNOW is correct (it produces the next step toward Z).

**Applied to ARC puzzles (400 tasks with known input/output):**
```
Task: input_grid (A) → output_grid (Z)

Backward trace:
  Z = output grid. What transformation produced it?
    → Z minus A = the DELTA. Delta = the mechanism.
    → Delta decomposes into: which cells changed? what pattern?
    → Pattern = rotate? flip? fill? scale? mirror? conditional?
    → Each pattern = a NODE in field map
    → Connections between patterns = EDGES
    → 400 tasks × backward trace = field map of ALL transformation mechanisms
```

**Applied to games:**
```
Game state Z (door open, level complete).
  What produced Z? → player at door + key matched.
  What produced key matched? → rotator activated N times.
  What produced rotator activated? → player passed through rotator.
  What produced player at rotator? → navigate from start.
  = Full chain A→Z derived BACKWARD from Z.
```

**Field map stores these backward traces as nodes + edges.**
Each node = a transformation pattern (rotate, flip, fill, match, move).
Each edge = "this pattern enables that pattern."
400 tasks = 400 backward traces = dense field map of mechanisms.

**New game:** observe current state → field map activates matching nodes → backward trace suggests what to do → collapse into action.

**This is VEG reversed:**
- V: which node in field map resonates with current observation?
- E: does the backward trace from that node match reality?
- G: if gap between trace and reality → new mechanism to discover

---

## 20. Empirical Mechanism Distribution — What ARC Actually Requires

> From reverse-tracing 400 ARC classic tasks (2874 observations):
> The data tells you what matters. Not theory — data.

**Binary tree of ALL mechanisms found:**

```
L0: SHAPE CHANGES(487) vs SAME SHAPE(815)
│
├── SHAPE CHANGES (37%)
│   ├── expand(121): tile patterns (107), irregular (14)
│   └── shrink(366): crop/extract (312), compress to line (54)
│
└── SAME SHAPE (63%)
    ├── global transform (3%): rotate, flip, transpose — RARE
    ├── identity (0.6%): output = input — TRIVIAL
    └── cell transform (96%): DOMINANT — almost all tasks
        ├── FILL (57%): scatter(298), region(127), line(23)
        ├── bg_mix (16%): both fill and erase
        ├── recolor (18%): single color swap(73), multi(70)
        ├── erase (8%): remove to background
        └── swap (1%): symmetric color exchange — RARE
```

**Key empirical findings:**

1. **Cell-level transform = 96% of same-shape tasks.**
   Almost never global rotate/flip. Almost always: look at each cell, decide based on local context.

2. **Fill is #1 mechanism (57%).**
   Most tasks = find where to add color. "What cells should become non-zero?"

3. **Scattered fill (298) >> connected fill (127).**
   The rule for WHICH cells to fill is usually NOT "flood fill adjacent."
   It is: "fill cells that match a CONDITION" — condition may be positional, neighbor-based, symmetry-based.

4. **Condition is usually complex (604/786 = 77% varied neighbors).**
   Only 46 tasks have uniform neighbor condition (simplest case).
   Most tasks: each changed cell has DIFFERENT local context → the rule must be ABSTRACT, not just "if all neighbors are X."

5. **Shrink (366) >> expand (121).**
   Tasks more often ask "find and EXTRACT" than "find and TILE."
   Implies: pattern RECOGNITION more important than pattern GENERATION.

6. **Spatial: local (504) >> global (197) >> point (85).**
   Changes are regional, not whole-grid, not single-pixel.
   Agent should focus on REGIONS, not individual cells or entire frame.

**What this means for a solver:**

The solver should be optimized for:
1. Local condition detection (what makes THIS region special?)
2. Fill rule inference (which cells satisfy the condition?)
3. Pattern extraction (crop the relevant subgrid)
4. NOT: global transforms, NOT: single-pixel operations

**Collapse condition = the RULE that determines which cells to transform.**
Storing mechanisms is not enough. Must store the CONDITIONS under which each mechanism fires.
A mechanism without its collapse condition = useless (knows WHAT but not WHEN).

**BCL encoding of mechanisms:**
Each task = superposition of active mechanism bits.
Shared-state = mechanisms that co-occur (fill + local + few_neighbors = common pattern).
Collapse = when input matches the condition → mechanism fires → output produced.

---

## 21. Three Chain Orders — The Only Structures That Exist

> From 400 ARC tasks reverse-traced: only 3 chain orderings appear. Not 6. Not arbitrary.
> Chain STRUCTURE is invariant. Chain CONTENT is variant (fractal sub-chains inside).

**The 3 orders (empirical, from 1302 observations):**

```
Order 1 (50%): WHY → WHERE → WHAT
  "Find the CONDITION → locate the REGION → apply the TRANSFORM"
  Used for: fill_enclosed, fill_adjacent, pattern-based transforms

Order 2 (47%): WHERE → WHY → WHAT
  "Find the REGION → check the CONDITION → apply the TRANSFORM"
  Used for: crop/extract, shape changes, symmetry-based transforms

Order 3 (2%):  WHAT → WHERE → WHY
  "Know the TRANSFORM → apply to ALL → ALWAYS"
  Used for: trivial global transforms (rotate, flip, transpose)
```

**Invariant rule: WHAT is always LAST.**
You never transform before knowing what and where.
The only question is: do you find the condition first (Order 1) or the region first (Order 2)?

**Fractal property:**
Each step (WHY, WHERE, WHAT) can contain a SUB-CHAIN of the same structure.

```
WHY (top level)
  └── WHY_sub → WHERE_sub → WHAT_sub
      "To determine the condition, first find WHY this sub-condition,
       then WHERE it applies, then WHAT it produces"
```

Example:
```
WHY = detect_boundary (which itself is: WHY=non-zero → WHERE=connected → WHAT=mark)
WHERE = enclosed_cells (which itself is: WHY=all_rays_hit → WHERE=interior → WHAT=select)
WHAT = fill_color (which itself is: WHY=selected → WHERE=those_cells → WHAT=assign_value)
```

**Chain structure = invariant at every scale.**
**Chain content = variant — different WHY, WHERE, WHAT at each level.**
**This is BCL fractal layering applied to transformation chains.**

**39 unique (what, where, why) triples cover all 400 tasks.**
New task: detect which triple → retrieve chain order → execute.

---

## 22. Five Grounding Primitives — Binary Is Not Enough

> Binary (P18) covers most classification but cannot represent everything alone.
> Minimum grounding set = 5 irreducible primitives:

| # | Primitive | Mechanism | Covers |
|---|-----------|-----------|--------|
| G1 | **Binary** | A ↔ B | distinction, existence, K/U split |
| G2 | **Gradient** | scalar [0,1] | measurement, weight, confidence, intensity |
| G3 | **Sequence** | a → b → c | time, causality, chain order (P21) |
| G4 | **Relation** | node + edge | space, network, topology, field map |
| G5 | **Recursion** | f(f) | meta-cognition, self-reference, fractal |

Binary covers most but cannot replace Gradient (loses middle), Sequence (order matters),
Relation (n-ary structure), or Recursion (meta-levels). All 5 needed for complete representation.

---

## 23. Epistemic vs Exploit Action

> When rules unknown: best action = maximize INFORMATION GAIN, not reward.

```
Epistemic: "what does this action REVEAL about the system?"
Exploit:   "what does this action GET me toward goal?"
```

Switch from epistemic to exploit when confidence > threshold.
Not by step count — by confidence level.

Wrong question: "is this action correct?"
Right question: "what does this action tell me about the rules?"

---

## 24. NMF — Name, Meaning, Frame

> Every piece of information is filtered through 3 simultaneous lenses:

```
Name = f(Meaning, Frame)
```

- **Name** — label in current context (can change per frame)
- **Meaning** — stable concept across contexts (transfers)
- **Frame** — reference system used to interpret (can switch)

Same Meaning + different Frame → different Name.
Same Name + different Frame → different Meaning.

**Transfer = stabilize Meaning across Name changes.**
Rotator in ls20 = switch in ft09 = lever in vc33 → same Meaning: "transformer."
System based on Name: re-learns each game. System based on Meaning: transfers instantly.

---

## 25. E = Superpose(K, U) — Existence as Grounded Known + Structured Unknown

> Classical: A = constant + variable.
> General: E = Superpose(K, U).

- **K** = grounded known anchor (stabilized, not just "constant")
- **U** = structured unknown (NOT noise — unresolved structured presence)

```
U = V(K, Δ₁, Δ₂, ..., Δn)
  Δ₁: visible change
  Δ₂: hidden/latent change
  Δ₃: variation of variation
```

**U is not absence. U is unresolved presence.** Progressively resolved layer by layer.

K/U split is FRAME-DEPENDENT:
```
Navigation frame: K = obstacles, goal / U = player movement, path
Puzzle frame:     K = rotator rule, door condition / U = key_state, health
```

Choose frame first → determines what is K and what is U → determines all reasoning after.

---

## 26. Grounded Node = [G, T, S, W, X]

> A node is not a point in a graph. It is a grounded entity in an existence field.

```
N = [G, T, S, W, X]
  G = Grounding    — primordial axes coordinates, ontological anchor
  T = Time trace   — when created, when last activated
  S = State        — current expression (DERIVED, not identity)
  W = Weight       — influence, preservation strength
  X = Extension    — open slot for future attributes
```

**State ≠ Identity.** Grounding = anchor = identity. State = current expression = derived from (G, interactions, time, weight).

**Existence requires grounding. Manifestation requires interaction.**
A node exists by anchoring. It is confirmed by being linked and activated.

---

## 27. Five-Layer Architecture Stack

> From substrate to compression — the full grounded system:

```
Layer 0: Existence Core (E)         — substrate containing everything
Layer 1: Primordial Axes (P)        — binary grounding poles (K↔U, etc.)
Layer 2: Grounded Nodes (N)         — entities anchored to at least 1 axis
Layer 3: Semantic Planes (Π)        — 3 ordinary nodes → 1 local meaning surface
Layer 4: BCL Layer                  — compression + reasoning over grounded structure
```

Two geometries coexist:
- **Ontological**: axis-based, rigid, grounding-oriented (Layers 0-1)
- **Semantic**: plane-based, relational, context-oriented (Layers 2-3)

Every node has two positions simultaneously:
- Grounding position on primordial axes
- Semantic position through planes it participates in

---

## 28. Frame Adjudicator — ACCEPT / REJECT / PARALLEL

> Before processing any input, evaluate the frame:

```
ACCEPT   — frame consistent with observation → proceed
REJECT   — frame contradicts observation → reframe from internal model
PARALLEL — insufficient evidence → maintain multiple frames
           → choose action that maximizes information gain (P23)
```

Reactive system: always ACCEPT. Intelligent system: can REJECT or PARALLEL.

---

## 29. World Model = 5 Primitives

> To represent ANY interactive world:

1. **Spatial occupancy** — where objects are, what space they fill
2. **Movement vector** — how objects move
3. **Static vs dynamic** — background vs actors
4. **Scalar state** — values that change (health, energy, count)
5. **Contact effects** — what happens when objects touch

These 5 are sufficient for most interactive environments. No physics engine needed.

---

## 30. Scaffold Architecture — IPOD + VEG

The principles above are implemented through two orthogonal structures:

**IPOD = the body (invariant structure)**
```
I (Input)   — sensors that collect all channels (P7)
P (Process) — brain that runs convergence loop (P3) using query protocol (P9)
O (Output)  — actuators that execute collapsed decisions (P1)
D (Data)    — memory layered by rate of change (P5)
```

**VEG = the thinking (variant process inside P)**
```
V (Void Drift)    — signals compete by resonance, strongest rises (≈ attention)
E (Evaluate)      — each hypothesis lives or dies by evidence (P6: gap drives learning)
G (Genesis Seed)  — detect gaps, generate new hypotheses to test (P2: imagination)
```

IPOD is the skeleton — never changes.
VEG is the thought — drifts freely within the skeleton.

**Fractal:** every IPOD module contains its own I, P, O, D.
**Boundary:** VEG never restructures IPOD. IPOD constrains where VEG can flow.

---

## 31. Collapse Condition = Context Count, Not Numeric Threshold

> A chain does not collapse by exceeding a fixed numeric threshold.
> A chain collapses when the NUMBER OF MATCHING CONTEXT CLUES is maximal.

**Wrong approach:**
```
score = Σ (power_i × ratio_i)      ← fixed numbers, same for every input
if score > threshold → collapse     ← arbitrary cutoff
```

**Right approach:**
```
For each chain triple, there exist N context clues (features present in input).
Each clue is BINARY: present or absent in THIS input.
Chain with most matching clues → highest context resonance → collapses first.
```

**Why this works:**
- Numbers (power, weight, ratio) are FIXED — they were computed once from training data
- Context clues are VARIABLE — they change with every new input
- Collapse is driven by what IS PRESENT in the current input, not by pre-computed weights
- Same feature set, different input → different clues match → different chain collapses

**The numbers tell you WHICH features to check (feature selection).**
**The current input tells you WHICH of those features are active (context).**
**Count of active features = collapse strength.**

```
Input X → extract context clues → match against each chain's clue set
  Chain A: 7/10 clues match → strong resonance
  Chain B: 3/8 clues match → weak resonance
  Chain C: 5/5 clues match → FULL resonance (all clues present)
  → Chain C collapses first (100% context match)
  → Chain A is backup (70% match)
```

**This is P1 (Collapse) applied to chain selection:**
- Context = set of active clues from input
- Sufficient context = enough clues match ONE chain distinctly
- Collapse = that chain is selected
- Insufficient = multiple chains have similar match count → PARALLEL (P28) → explore

**This is P24 (NMF) in action:**
- Name = chain triple label
- Meaning = the set of context clues that define it
- Frame = the current input's active features
- Collapse happens when Frame activates enough of the Meaning to unambiguously Name one chain

**When multiple chains tie (insufficient context for collapse):**

Context has TWO SOURCES (P2):
1. **Exogenous (direct observation)**: interact with the puzzle, observe more cells, test hypotheses
2. **Endogenous (inference from data)**: use fieldmap, known mechanism patterns, prior solved tasks to DEDUCE additional context clues without new observation

Each additional context node ELIMINATES chains that don't match it.
Process: tie → acquire more context (either source) → re-count → narrower set → eventually 1 chain dominates → collapse.

```
Step 1: 5 chains match at 80% → no collapse (tie)
Step 2: infer from fieldmap that input has enclosed regions → +1 context node
        → 3 chains now mismatch → 2 remain
Step 3: observe that output same size → +1 context node
        → 1 chain mismatch → 1 remains → COLLAPSE
```

**The more context nodes available, the easier collapse.**
- Easy tasks: few context clues sufficient (high discrimination)
- Hard tasks: many context clues needed (low initial discrimination)
- Impossible: no amount of context disambiguates (genuinely novel chain → P6: gap = learning signal)

**Empirical validation (400 ARC classic tasks):**
```
Method                          Top-1   Top-3
Numeric threshold scoring       24%     40%
Context count (binary match)    39%     58%
Fingerprint matching (64 nodes) 56%     72%    ← best
  + multi-pair consensus        54%     72%
  + blind (no output)           31%     52%
```

**WHY (enclosed/adjacent/symmetry/pattern) is hardest to distinguish.**
It REQUIRES output delta — which cells changed tells you WHY they changed.
Input alone only narrows WHAT and WHERE.

→ Implication: for unknown tasks, first step = get output (explore/observe),
  then WHY collapses, then full chain collapses.

---

## 32. Frame Switch Eliminates U

> When stuck, the problem is not lack of compute — it is lack of frame.
> Switch frame → see new K/U split → new information → U shrinks → closer to collapse.

Every observation is filtered through a frame. Same data, different frame → different K and different U.
When all actions within the current frame are exhausted and U is not resolved → the frame is wrong.

**Three frame operations:**

```
FRACTAL IN:   zoom into detail (1 object, 1 step, 1 pixel)
              → reveals micro-structure invisible at macro level

FRACTAL OUT:  zoom out to cross-instance (cross-level, cross-game, cross-domain)
              → reveals macro-pattern invisible at detail level

FRAME SWITCH: same data, different reference system
              → reveals different K/U partition
```

**Why this always helps:**
Each new frame gives at least one piece of information that the old frame could not see.
One new piece of information eliminates at least one U candidate.
Eliminating U = progress toward collapse.

**Applied:**
```
Stuck: "2 valves, 16K combos, no solve"
  Frame 1 (valve position): tried all combos → exhausted → stuck
  Frame switch → "is click location relevant?"
  New info: ALL clicks produce same state → location = irrelevant (K!)
  Frame switch → "what happens AFTER the transition?"
  New info: 4 NEW responsive spots appear → multi-phase structure
  → U narrowed from 16K combos to 4-valve sequential problem
```

**Rule: if stuck for more than N attempts in same frame → switch frame, do not increase N.**

---

## 33. Reduce to 2^10 Before Brute Force

> Never brute force more than ~1000 combinations. If search space > 2^10, STOP and reduce first.
> Human cannot enumerate 4^31. Neither should agent. Add input to shrink U.

**Reduction chain (each step cuts exponentially):**
```
RAW:           N_objects ^ N_clicks         (e.g., 4^31 = 4 billion)
Phase split:   N_objects ^ (N/phases)       (e.g., 4^10 per phase)
Prune dead:    responsive_only ^ (N/phases) (e.g., 2^10)
Binary model:  2 ^ N_responsive             (e.g., 2^4 = 16)
Dependency:    N_responsive!  or just N      (e.g., 4! = 24 or 4)
```

**Sources of input to reduce (P2: two paths):**
1. **Observation**: click 1 valve, observe what changes → prune others
2. **Map query**: fieldmap says "valves are binary toggle" → 0 or 1 per valve
3. **Phase detection**: scan after each click → new spots = new phase = split
4. **Symmetry**: if A+B = B+A → halve combos
5. **Delta tracking**: if click X gets closer to target → keep X, prune others
6. **Cross-level transfer**: L1 pattern = BBB → L2 might be similar structure

**Target: always reduce to ≤ 2^10 before searching. If cannot → need more input, not more compute.**

---

## 34. Metaphor = Structure Transfer Across Domains

> When stuck in domain A, find domain B with ISOMORPHIC structure. Solution in B transfers to A.
> This is P24 (NMF) at macro scale: same Meaning, different Name, different Frame.

Metaphor is not decoration — it is the mechanism of cross-domain intelligence.

```
Domain A (vc33): click valve → toggle fluid level → match target heights
Domain B (ft09): click tile → toggle color → match target pattern
Structure:       click X → flip binary state → match goal configuration

Same structure → same solution method.
If you can solve lights-out (ft09) → you can solve valve-matching (vc33).
```

**When to use metaphor:**
- Stuck in current domain (all frames exhausted)
- Query map for other domains with similar STRUCTURE (not similar appearance)
- Isomorphism = same K skeleton, different U surface

**How to detect isomorphism:**
- Both domains have: binary state objects + click to toggle + target configuration = match
- Ignore: colors, sizes, positions, names (all U)
- Match: toggle mechanic, goal = state match, objects = independent toggles (all K)

**Transfer = apply solution strategy from B to A:**
- ft09 strategy: "each tile affects neighbors in pattern → solve as system of equations"
- vc33 transfer: "each valve affects connected reservoirs → solve as flow system"

**This is what the fieldmap enables:** nodes from different games share Meaning edges.
When solving game X, activate Meaning → find isomorphic nodes from game Y → transfer.

---

## 35. Gap + Metaphor = Universal Reasoning Tool

> Gap is not just P6 (learning signal). Gap is the UNIVERSAL MEASURE of difference when comparing any two things.
> Metaphor is not just P34 (structure transfer). Metaphor provides GROUNDING for the unknown.
> Combined: metaphor gives you a complete structure to compare against. Gap tells you exactly WHERE the comparison breaks.

**How it works:**
```
1. STUCK on unknown structure A
2. Find known structure B that RESEMBLES A (metaphor)
3. Overlay B onto A — B is the grounding, the scaffolding
4. Measure GAP: where does A differ from B?
5. Gap = exactly the part that needs solving
6. Everything that matches = FREE KNOWLEDGE (transferred from B)
7. Only the gap requires new exploration
```

**Example:**
```
A = vc33 L3 (unknown: how to solve 4 valves)
B = dam irrigation (known: open gates near driest field)

Overlay B onto A:
  B: look at which field is driest     → A: look at which target has biggest gap
  B: open nearest gate                 → A: click nearest valve
  B: water flows and redistributes     → A: fluid level changes
  B: check again                       → A: re-scan responsive spots
  B: repeat until all fields watered   → A: repeat until all targets matched

Gap between A and B:
  B: water flows DOWN (gravity)        → A: fluid might flow any direction
  B: gates are physical (near/far)     → A: valves might affect non-adjacent reservoirs
  → THESE gaps are exactly what to explore next
```

**Gap can combine with ANY principle:**
- Gap + P1 (Collapse): gap between current context and sufficient context = how far from decision
- Gap + P4 (Frame): gap between two frames viewing same data = what each frame misses
- Gap + P18 (Binary): gap between responsive and non-responsive = classification boundary
- Gap + P21 (Chains): gap between chain prediction and actual = which chain step is wrong
- Gap + P25 (K/U): gap between K and U = exactly what is still unknown
- Gap + P31 (Context): gap between matched clues and total clues = collapse confidence
- Gap + P32 (Frame Switch): gap between old frame and new frame = new information gained
- Gap + P33 (Reduce): gap between current search space and 2^10 = how much more to reduce
- Gap + P34 (Metaphor): gap between source domain and target domain = transfer boundary

**Gap is the difference. Metaphor is the reference. Together they pinpoint exactly what you don't know.**

---

## One Sentence

> Cognition is a loop: collect from all channels, query to build context, imagine from what is known, explore to confirm, converge when the gap is small enough, decide only when context is sufficiently coherent. Every game is a chain A → [O1...On] → B; solving = discovering the chain, learning each link's property, and executing in order. Chain selection = count matching context clues from input against each chain's condition set; chain with most matches collapses first.
