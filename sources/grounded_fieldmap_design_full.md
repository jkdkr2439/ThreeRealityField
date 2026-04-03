# Grounded Fieldmap Design

## 1. Purpose

This document defines a full design for a grounded fieldmap architecture.

The goal is to avoid a floating semantic map with no ontological base. Instead, the system begins from **primordial binary grounding**, then allows later nodes to emerge, connect, polarize, balance, and form semantic structures.

The design is built from five stacked layers:

1. **Existence Core**  
   The substrate that contains the field.
2. **Primordial Axes**  
   Binary grounding axes that define foundational polarity.
3. **Grounded Nodes**  
   Nodes that anchor to at least one primordial axis.
4. **Semantic Planes**  
   Local semantic surfaces formed by ordinary nodes.
5. **BCL Layer**  
   A compression and reasoning layer operating over grounded structure.

---

## 2. Existence Core

Existence is not treated as an ordinary node. It is treated as the **substrate** or **base field** in which all other structures appear.

We denote this substrate by:

\[
\mathcal{E}
\]

This means:

- primordial axes exist *within* the existence core,
- grounded nodes emerge *within* the existence core,
- semantic planes form *within* the existence core,
- BCL compresses structures *within* the existence core.

So the existence core is not one node among many. It is the ontological field in which all grounded entities are defined.

---

## 3. Primordial Binary Grounding

### 3.1 Primordial Binary Axis

A primordial binary axis is a foundational polarity pair:

\[
\mathcal{P}_k = (A_k \leftrightarrow B_k)
\]

Examples include:

- Matter \(\leftrightarrow\) Energy
- Space \(\leftrightarrow\) Time
- Constant \(\leftrightarrow\) Variable

Each primordial pair defines **one axis**. The two poles of the axis are primordial nodes.

### 3.2 Rule of Geometry

A primordial pair always lies on **one axis**. It does **not** generate a plane. It does **not** float as two arbitrary points. It is a polarity line.

Thus:

- primordial geometry is **axis-based**,
- semantic geometry is formed later by ordinary nodes.

### 3.3 Grounding Coordinate

If node \(N_i\) is anchored to primordial axis \(\mathcal{P}_k\), then its grounding coordinate on that axis is:

\[
g_{ik} \in [-1,1]
\]

with:

- \(g_{ik} = -1\): fully polarized toward \(A_k\)
- \(g_{ik} = +1\): fully polarized toward \(B_k\)
- \(g_{ik} = 0\): balanced between the two poles

If a node is anchored to multiple primordial axes, then its grounding vector is:

\[
G_i = \mathbf{g}_i = (g_{i1}, g_{i2}, \dots, g_{im})
\]

This is the node’s ontological grounding position.

### 3.4 Minimum Grounding Rule

Every non-primordial node must anchor to at least one primordial axis.

Formally:

\[
\forall N_i,\ \exists\ \mathcal{P}_k\ \text{such that}\ N_i\ \text{anchors to}\ \mathcal{P}_k
\]

This prevents the fieldmap from producing ungrounded floating nodes.

---

## 4. General Form of Existence

We define existence in its most general form as:

\[
E = \operatorname{Superpose}(K, U)
\]

Where:

- \(K\) — **Grounded Known (Anchor)**  
  The stabilized, anchored component of the system.

- \(U\) — **Structured Unknown**  
  The unresolved, variable, and potentially recursive component, including:
  - observed variation
  - latent (hidden) variation
  - higher-order variation
  - variation of variation

This generalizes the classical form:

\[
A = \text{constant} + \text{variable}
\]

by recognizing that the variable is not a single simple term, but an unresolved structured field.

---

## 5. Relation to Constant–Variable Polarity

Given a primordial binary axis:

\[
\text{Constant} \leftrightarrow \text{Variable}
\]

we reinterpret:

- **Constant** \(\to\) grounded known core \(K\)
- **Variable** \(\to\) structured unknown \(U\)

Thus:

\[
A = K + U
\]

is a more scalable version of:

\[
A = \text{constant} + \text{variable}
\]

We may write the unknown as:

\[
U = \mathcal{V}(K, \Delta_1, \Delta_2, \dots, \Delta_n)
\]

where each \(\Delta_k\) denotes one layer of deviation, perturbation, latent interaction, or unresolved refinement around the current anchor \(K\).

This means:

> the variable is not merely “what changes,” but the unresolved field around what is sufficiently stabilized.

---

## 6. Node Existence: Grounding and Manifestation

A node does not exist in only one sense. It has at least two distinct layers of existence.

### 6.1 Ontological Existence

A node exists if it is grounded:

\[
\text{Existence}(N_i) \Leftrightarrow \|G_i\| > 0
\]

This defines the node’s ontological presence.

### 6.2 Manifested Existence

A node is confirmed, expressed, or made visible in the field through weighted interaction:

\[
\text{Manifestation}(N_i) \propto \sum_{j \in \mathcal{L}_i} w_{ij}
\]

Where:

- \(\mathcal{L}_i\) = linked-node neighborhood
- \(w_{ij}\) = interaction weight between node \(i\) and node \(j\)

### 6.3 Combined Principle

> A node exists by grounding, and is confirmed by interaction.

Grounding gives ontological legitimacy. Interaction gives field reality.

---

## 7. Minimal Grounded Node Form

A minimal grounded node is:

\[
N_i = [G_i, T_i, S_i, W_i, X_i]
\]

Where:

- \(G_i\) — **Grounding**  
  Primordial axes and polarity coordinates.

- \(T_i\) — **Temporal Trace**  
  The time signature of the node.

- \(S_i\) — **Manifested State**  
  The node’s current expression in the field.

- \(W_i\) — **Field Weight**  
  The node’s intensity, influence, and preservation strength.

- \(X_i\) — **Open Extension Variable**  
  An unbounded slot for future attributes.

The extension slot remains open:

\[
X_i = \{x_{i1}, x_{i2}, x_{i3}, \dots\}
\]

Possible future additions include:

- uncertainty
- momentum
- memory trace
- confidence
- modality
- symbolic payload
- cluster identity
- resonance signature

---

## 8. State as Manifestation

State is not the same as grounding. Grounding is the anchor. State is the current expression.

We define:

\[
S_i(t) = \mathcal{F}(G_i, \mathcal{L}_i(t), T_i, W_i)
\]

Thus:

- grounding defines what the node is anchored to,
- links define how the node is pulled or reinforced,
- time defines when the state is evaluated,
- weight defines how strongly the node acts and is acted upon,
- state is the resulting manifested condition.

State is therefore derived, not primitive.

---

## 9. Polarization and Field Dynamics

A grounded node may shift under field interaction.

Its grounding vector may evolve as:

\[
\mathbf{g}_i(t+1) = \mathbf{g}_i(t) + \Delta \mathbf{g}_i(\mathcal{L}_i, W_i, T_i)
\]

Its state updates accordingly:

\[
S_i(t+1) = \mathcal{F}(G_i(t+1), \mathcal{L}_i(t), T_i, W_i(t))
\]

Its weight may also evolve:

\[
W_i(t+1) = \mathcal{H}(S_i(t+1), \mathcal{L}_i(t), T_i)
\]

This means fieldmap is not merely a static graph. It is a grounded field system in which:

- nodes anchor,
- links exert pressure,
- states manifest,
- weights shift,
- grounding itself may move toward polarization or balance.

---

## 10. Semantic Plane Formation

Primordial pairs do not create semantic planes. They remain axis-based.

Semantic planes are formed only by **ordinary nodes**.

### 10.1 Rule of Semantic Plane

Three non-collinear ordinary nodes create one semantic plane.

Given three nodes:

\[
N_i, N_j, N_k
\]

if they are not collinear, then they define a semantic plane:

\[
\Pi_{ijk}
\]

### 10.2 Meaning of Semantic Plane

A semantic plane is a local semantic surface in which:

- context stabilizes,
- local meaning is interpreted relationally,
- nodes are no longer read only as isolated points,
- semantic direction and semantic neighborhood become readable.

### 10.3 Two Geometries

The architecture therefore has two distinct geometries:

#### Ontological Geometry

- primordial pairs
- axis-based
- grounding-oriented
- rigid polarity structure

#### Semantic Geometry

- ordinary nodes
- plane-forming
- context-oriented
- local semantic structure

This means a node has two simultaneous positions:

1. **Grounding position** on primordial axes
2. **Semantic position** through the semantic planes it participates in

We may write:

\[
N_i = (\mathbf{g}_i, \{\Pi_{i*}\})
\]

where:

- \(\mathbf{g}_i\) = grounding vector
- \(\{\Pi_{i*}\}\) = set of semantic planes containing node \(N_i\)

---

## 11. Relational Structure

A node may also carry explicit relational links:

\[
\mathcal{L}_i = \{N_j \mid N_j\ \text{linked to}\ N_i\}
\]

These links are not identical to grounding.

- **Grounding** anchors the node to primordial ontology.
- **Links** connect the node to field interaction and semantic formation.

This distinction is essential. A node may be strongly grounded but weakly linked, or strongly linked but weakly grounded.

---

## 12. Grounded State Space

We define the grounded state space as:

\[
\mathcal{S} = \{s_i \mid s_i = (G_i, T_i, S_i, W_i, X_i)\}
\]

This is stronger than a flat state space of arbitrary symbolic or semantic configurations. A state is now a grounded field entity.

---

## 13. BCL Integration

### 13.1 Why BCL Needs Grounding

BCL is powerful for branch-rich data because it supports:

- shared-state branching
- multi-view encoding
- fractal refinement
- entropy-governed stopping

But without grounding, its shared core remains underdefined. A core may be detected statistically or structurally while still lacking ontological interpretation.

The grounded fieldmap architecture strengthens BCL by giving the codec a grounded substrate.

### 13.2 Grounded Shared Core

A BCL shared core should be interpreted as a grounded known core:

\[
s^\star \rightsquigarrow K^\star
\]

Thus shared core is no longer merely latent overlap. It becomes anchored common structure.

### 13.3 Branches as Known Plus Unknown

A realized branch may be written as:

\[
A = K^\star + U_A,
\qquad
B = K^\star + U_B
\]

Thus the shared-state branch unit becomes:

\[
B = (K^\star, U_A, U_B)
\]

This is conceptually stronger than a merely latent branch relation.

### 13.4 Multi-View Representation

A canonical BCL view set may be written as:

\[
V = \{S, F, P, T, B, U\}
\]

where views may stand for:

- Skeleton
- Flow
- Pattern
- Semantic Type
- Binding
- Surface

Each view is a projection over grounded structure:

\[
\Pi_v : \mathcal{S} \to \mathcal{S}_v
\]

### 13.5 Fractal Refinement as Unknown Resolution

Given:

\[
A = K + U
\]

fractal refinement through layers:

\[
f_0, f_1, \dots, f_k
\]

may be interpreted as progressive resolution of \(U\) relative to \(K\).

At shallow depth:

\[
A \approx K + U^{(0)}
\]

At deeper depth:

\[
A \approx K + U^{(k)}
\]

Entropy stopping means refinement halts when the remaining unresolved structure is not worth the additional representational cost.

### 13.6 Grounded Runtime Node

A conceptual grounded BCL runtime node may be represented as:

```python
@dataclass
class GroundedNode:
    node_id: int
    grounding: dict
    time_trace: any
    state: any
    weight: float
    extra: dict

    shared_core_ref: int | None
    local_delta_ref: int | None
    view_states: dict[str, any]
    entropy: float
    readiness: float
```

This unifies:

- grounded field nodes,
- node runtime architecture,
- BCL branch and view handling.

---

## 14. Collapse in the Unified System

A path or structure collapses when grounded nodes align sufficiently under field, weight, resonance, and multi-view consistency.

Let \(\pi\) be a path of grounded nodes. Then a path score may be written as:

\[
J(\pi) = \sum_{u_i \in \pi} \Bigl(
\kappa_1 \mathrm{Res}_i
+ \kappa_2 W_i
+ \kappa_3 r_i
- \kappa_4 \mathrm{Ent}_i
- \kappa_5 \mathrm{Inhib}_i
- \kappa_6 \mathrm{Dist}_{\text{view}}(u_i)
\Bigr)
\]

The collapsed path is:

\[
\pi^\star = \arg\max_{\pi} J(\pi)
\]

The key difference here is that each node in the path is not an abstract codec state alone. It is a grounded field entity.

---

## 15. Full Design Stack

The architecture can be summarized as a five-layer stack.

### Layer 0 — Existence Core

\[
\mathcal{E}
\]

The substrate of the field.

### Layer 1 — Primordial Axes

\[
\mathcal{P}_k = (A_k \leftrightarrow B_k)
\]

Binary grounding axes.

### Layer 2 — Grounded Nodes

\[
N_i = [G_i, T_i, S_i, W_i, X_i]
\]

Grounded field entities.

### Layer 3 — Semantic Planes

\[
\Pi_{ijk}
\]

Local semantic surfaces created by ordinary nodes.

### Layer 4 — BCL Layer

- shared-state branching
- multi-view encoding
- fractal refinement
- entropy-governed stopping
- grounded collapse

---

## 16. Core Principles

The full system follows these principles:

1. **Grounding precedes relation**  
   A node must anchor before it can meaningfully drift.

2. **Primordial pairs define axes, not planes**  
   Their geometry is linear and polar.

3. **Three ordinary nodes define a semantic plane**  
   Semantic context emerges relationally.

4. **Existence and manifestation are distinct**  
   Grounding gives existence; interaction gives field confirmation.

5. **State is derived**  
   State is the expression of grounding under interaction.

6. **Unknown is structured**  
   Variation is not mere noise but organized incompletion.

7. **Compression should preserve grounding**  
   BCL must compress grounded structure, not floating fragments.

---

## 17. Final Summary

The architecture proposed here turns fieldmap into a grounded representational regime.

- Existence is a substrate, not an ordinary node.
- Primordial pairs are axis-based polarity anchors.
- Every ordinary node must anchor to at least one primordial axis.
- Each node has a minimal grounded form:

\[
N_i = [G_i, T_i, S_i, W_i, X_i]
\]

- Existence in general is:

\[
E = \operatorname{Superpose}(K, U)
\]

- Three ordinary nodes form one semantic plane.
- BCL operates as a grounded compression and reasoning layer above this field structure.

This yields a single system in which:

- ontology is grounded,
- nodes are dynamic,
- meaning is planar and relational,
- variation is structured,
- and compression preserves rather than destroys the field.

---

## 18. Closing Insight

> A node is not merely a point in a graph.  
> It is a grounded entity inside an existence field,  
> positioned between primordial poles,  
> manifested through interaction,  
> and interpreted through semantic planes.

That is the shift from an ungrounded semantic map to a grounded field architecture.

