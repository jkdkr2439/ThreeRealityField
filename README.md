# Three-Reality Field

A spatial model of knowledge organized into three layers of reality, visualized as concentric and offset spheres in 3D.

**Author**: Kevin T.N. — jkdkr2439@gmail.com
**License**: [AGPL-3.0](LICENSE)

## Structure

```
                        ╭── PYRAMID (meta-framework) ──╮
                        │                               │
    ╭───────────────────┼───────────────────╮           │
    │  SUBJECTIVE       │                   │           │
    │  ╭─────────╮      │                   │           │
    │  │ EXISTENCE│      │    VOID           │           │
    │  │  gates   │      │    (absolute      │           │
    │  │  layers  │      │     objective —   │           │
    │  │principles│      │     what no one   │           │
    │  │ topics   │      │     knows)        │           │
    │  │  docs    │      │                   │           │
    │  ╰─────────╯      │                   │           │
    │           ╲       │                   │           │
    │         overlap = attention            │           │
    │             ╲     │                   │           │
    │    ╭─────────────────────╮            │           │
    │    │   INTERSUBJECTIVE   │            │           │
    │    │   (shared, social,  │            │           │
    │    │    consensus)       │            │           │
    │    ╰─────────────────────╯            │           │
    ╰───────────────────────────────────────╯           │
                        ╰───────────────────────────────╯
```

### Three Realities

**Subjective** — the inner sphere, centered. Personal memory, unconscious patterns, long-term knowledge. Everything you know, including things you don't know you know. Layered from general (center) to specific (surface).

**Intersubjective** — the outer sphere, offset. Shared consensus, social knowledge, language, culture. Much larger than subjective. Only partially overlaps — that overlap is attention: the part of shared reality you are currently aware of.

**Absolute Objective** — the void outside both spheres. What exists regardless of any observer. No one knows it directly. It can only be approximated through the gap between subjective and intersubjective.

### Inside the Subjective Sphere

Knowledge is layered concentrically — the more general, the closer to center:

```
center    EXISTENCE (substrate, 1 node)
  r~30    Filter Gates (5) — binary, gradient, sequence, relation, recursion
  r~60    Framework Layers (6) — NMF, K/U, Collapse, IPOD, GAP, Superpose
  r~100   Principles (35) — general rules discovered through practice
  r~140   Discoveries + Design (37) — specific insights
  r~180   Topics (191) — branching knowledge clusters
surface   Documents (760) — papers, code, texts, most specific
```

### The Pyramid

Four vertices wrapping everything — meta-methods for viewing the field:

- **NMF** — Name = f(Meaning, Frame). How to read any node.
- **SDC(D/H)V** — Sinh/Dan/Chuyen/(Dung or Hoai)/Vo. Lifecycle of every node. Born fragile, grow connections, transform, stabilize (Dung) or fade (Hoai), die.
- **Phap Luan** — Two methods: trace to essence + transform through resonance.
- **3 Reality Layers** — Subjective / Intersubjective / Absolute.

The pyramid is not inside the field. It is the frame through which the field is observed.

### Gap = Existence

The model encodes one key insight: gap and existence are the same thing. Without difference, nothing can be detected. Without detection, nothing exists for any observer. EXISTENCE node carries two names — "existence" (object frame) and "gap" (observer frame). Same meaning, different frame, different name. NMF describing itself.

## Current State

This is a proof-of-concept built from one person's knowledge base (~760 documents, ~33K nodes). The subjective sphere is sparsely populated. A real deployment would have orders of magnitude more nodes — every memory, every experience, every learned pattern.

The intersubjective sphere is represented structurally but not yet populated with external knowledge.

## Files

```
ThreeRealityField/
├── build_fieldmap.py        # Build grounded fieldmap from documents
├── gen_3d.py                # Generate 3D orbital visualization
├── kevin_fieldmap.db        # Example fieldmap (33K nodes, 17MB)
├── kevin_fieldmap_3d.html   # Interactive 3D visualization (open in browser)
├── LICENSE
└── .gitignore
```

## Usage

### View the visualization
Open `kevin_fieldmap_3d.html` in a browser. Drag to rotate, scroll to zoom, hover for details.

### Build from your own data
Place documents (PDF, TXT, DOCX, PY, JS, MD, TEX) in subfolders, then:
```bash
pip install pymupdf python-docx
python build_fieldmap.py
python gen_3d.py
```

### Requirements
- Python 3.10+
- `pymupdf` (PDF reading)
- `python-docx` (DOCX reading)
- A modern browser with WebGL (for 3D visualization)

## License

[GNU Affero General Public License v3.0](LICENSE)