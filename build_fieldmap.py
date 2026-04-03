"""
Build a grounded fieldmap.db from the Kevin_TN folder.

Architecture:
  EXISTENCE (substrate)
    └── Filter Gates (5 primordial axes)
        ├── Binary, Gradient, Sequence, Relation, Recursion
    └── Framework Layers (built on gates)
        ├── NMF, K/U, Collapse, IPOD, GAP, Superpose
    └── All content nodes anchor to gates + layers

Every document/concept must ground to at least one filter gate.
"""

import hashlib
import json
import os
import re
import sqlite3
import sys
import zipfile
import tempfile
import shutil
from collections import defaultdict
from pathlib import Path

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

ROOT_DIR = Path(__file__).resolve().parent
DB_PATH = ROOT_DIR / 'kevin_fieldmap.db'
CHUNK_SIZE = 500


# === Hashing ===

def nh(s: str) -> str:
    return '0x' + hashlib.md5(s.encode('utf-8')).hexdigest()[:12]


# === Text Extraction ===

def read_text_file(path: Path) -> str:
    for enc in ['utf-8', 'utf-16', 'cp1252', 'latin-1']:
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, UnicodeError):
            continue
    return ''


def read_pdf(path: Path) -> str:
    try:
        import fitz
        doc = fitz.open(str(path))
        text = '\n'.join(page.get_text() for page in doc)
        doc.close()
        return text
    except Exception:
        return ''


def read_docx(path: Path) -> str:
    try:
        import docx
        doc = docx.Document(str(path))
        return '\n'.join(p.text for p in doc.paragraphs)
    except Exception:
        return ''


def extract_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in ('.txt', '.md', '.tex', '.py', '.js', '.json', '.csv', '.html', '.css'):
        return read_text_file(path)
    elif ext == '.pdf':
        return read_pdf(path)
    elif ext == '.docx':
        return read_docx(path)
    return ''


# === Keyword / Gate Detection ===

GATE_KEYWORDS = {
    'binary': ['binary', 'polarity', 'true/false', 'yes/no', 'exist', 'non-exist', 'k/u', 'invariant', 'variant', 'split', 'classify', 'boolean'],
    'gradient': ['gradient', 'weight', 'confidence', 'threshold', 'scalar', 'intensity', 'activation', 'decay', 'energy', 'score', 'probability', 'continuous'],
    'sequence': ['sequence', 'temporal', 'causal', 'chain', 'order', 'step', 'cycle', 'loop', 'before', 'after', 'process', 'pipeline', 'flow'],
    'relation': ['relation', 'graph', 'network', 'edge', 'node', 'topology', 'connection', 'link', 'neighbor', 'field', 'spatial', 'structure'],
    'recursion': ['recursion', 'self-reference', 'fractal', 'meta', 'self-apply', 'self-similar', 'scale-invariant', 'emergence', 'consciousness'],
}

LAYER_KEYWORDS = {
    'nmf': ['nmf', 'name', 'meaning', 'frame', 'context', 'perspective', 'identity', 'transfer'],
    'ku': ['invariant', 'variant', 'k/u', 'constant', 'variable', 'skeleton', 'flesh', 'stable', 'change'],
    'collapse': ['collapse', 'decision', 'convergence', 'sufficient', 'emerge', 'superposition', 'resolve'],
    'ipod': ['ipod', 'input', 'process', 'output', 'data', 'perception', 'action', 'memory'],
    'gap': ['gap', 'difference', 'learning', 'signal', 'comparison', 'imagination', 'exploration', 'hypothesis'],
    'superpose': ['superpose', 'superposition', 'coexist', 'potential', 'unresolved', 'existence'],
}

FRAMEWORK_KEYWORDS = list(set(
    kw for kws in list(GATE_KEYWORDS.values()) + list(LAYER_KEYWORDS.values()) for kw in kws
))


def extract_keywords(text: str, max_kw: int = 20) -> list[str]:
    text_lower = text.lower()
    found = [t for t in FRAMEWORK_KEYWORDS if t in text_lower]
    phrases = re.findall(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+', text[:2000])
    for p in phrases[:10]:
        if p.lower() not in found:
            found.append(p.lower())
    return found[:max_kw]


def detect_gates(text: str) -> list[str]:
    """Detect which primordial gates a text grounds to."""
    text_lower = text.lower()
    gates = []
    for gate, keywords in GATE_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in text_lower)
        if hits >= 2:
            gates.append(gate)
    return gates if gates else ['relation']  # default: everything is at least a relation


def detect_layers(text: str) -> list[str]:
    """Detect which framework layers a text connects to."""
    text_lower = text.lower()
    layers = []
    for layer, keywords in LAYER_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in text_lower)
        if hits >= 2:
            layers.append(layer)
    return layers


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE) -> list[str]:
    paragraphs = text.split('\n\n')
    chunks = []
    current = ''
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 2 > chunk_size and current:
            chunks.append(current.strip())
            current = para
        else:
            current = current + '\n\n' + para if current else para
    if current.strip():
        chunks.append(current.strip())
    return chunks


# === Build Fieldmap ===

class FieldmapBuilder:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = sqlite3.connect(str(db_path))
        self.cur = self.conn.cursor()
        self.count = 0
        self._init_db()

    def _init_db(self):
        self.cur.execute('DROP TABLE IF EXISTS fractal_nodes')
        self.cur.execute('''CREATE TABLE fractal_nodes (
            id TEXT PRIMARY KEY,
            type TEXT,
            name_nodes TEXT,
            mean_nodes TEXT,
            frame_nodes TEXT,
            raw_content TEXT
        )''')

    def ins(self, nid, ntype, name_nodes, mean_nodes, frame_nodes, raw_content=''):
        self.cur.execute(
            'INSERT OR IGNORE INTO fractal_nodes VALUES (?,?,?,?,?,?)',
            (nid, ntype, json.dumps(name_nodes), json.dumps(mean_nodes),
             json.dumps(frame_nodes), raw_content)
        )
        self.count += 1

    def build(self, root_dir: Path):
        # ══════════════════════════════════
        # LAYER 0: EXISTENCE SUBSTRATE
        # ══════════════════════════════════
        existence_id = nh('EXISTENCE')
        self.ins(nh('N:existence'), 'base_name', [], [], [], 'existence')
        self.ins(existence_id, 'existence', [nh('N:existence')], [], [],
                 'Existence substrate — the ontological field in which all grounded entities are defined. '
                 'Not a node among many. The base field.')

        # ══════════════════════════════════
        # LAYER 1: PRIMORDIAL FILTER GATES
        # ══════════════════════════════════
        print('[*] Building primordial filter gates...')
        gates = {
            'binary': ('Binary', 'A ↔ B polarity. Distinguish, classify, split. '
                       'Existence/non-existence, K/U, true/false. '
                       'Most common primitive in history of thought but not sufficient alone.'),
            'gradient': ('Gradient', 'Scalar [0,1]. Measure, weight, confidence, intensity. '
                         'Covers what binary cannot: degree, middle ground, soft weighting.'),
            'sequence': ('Sequence', 'a → b → c. Temporal order, causality, cycles. '
                         'Covers directed processes that binary and gradient cannot express.'),
            'relation': ('Relation', 'Node + edge. Spatial, network, topology, structure. '
                         'N-ary connections that cannot be reduced to binary or sequence.'),
            'recursion': ('Recursion', 'f(f). Self-reference, fractal, meta-cognition. '
                          'The only primitive that can generate the others. '
                          'Creates meta-levels. Makes the system self-aware.'),
        }

        gate_ids = {}
        for gate_key, (gate_name, gate_desc) in gates.items():
            gid = nh(f'GATE:{gate_key}')
            gate_ids[gate_key] = gid
            self.ins(nh(f'N:{gate_key}'), 'base_name', [], [], [], gate_key)
            self.ins(gid, 'filter_gate',
                     [nh(f'N:{gate_key}')], [], [existence_id],
                     f'{gate_name} — {gate_desc}')

        # Update existence to point to all gates
        all_gate_ids = list(gate_ids.values())
        self.cur.execute('UPDATE fractal_nodes SET mean_nodes=? WHERE id=?',
                         (json.dumps(all_gate_ids), existence_id))

        # ══════════════════════════════════
        # LAYER 2: FRAMEWORK LAYERS
        # ══════════════════════════════════
        print('[*] Building framework layers...')
        layers = {
            'nmf': ('NMF', 'Name = f(Meaning, Frame). '
                    'Every entity has 3 dimensions: what it is called here (Name), '
                    'what it contains (Meaning), where it lives (Frame). '
                    'Same Meaning + different Frame = different Name.',
                    ['binary', 'relation']),  # grounds to these gates
            'ku': ('K/U Split', 'Invariant vs Variant. '
                   'Everything separates into K (what stays) and U (what changes). '
                   'Fix at K level, never patch U.',
                   ['binary', 'gradient']),
            'collapse': ('Collapse', 'Decision emerges when context is sufficient. '
                         'Not chosen — emerges. Insufficient context = no decision. '
                         'Contradictory context = failed collapse.',
                         ['binary', 'gradient', 'sequence']),
            'ipod': ('IPOD', 'Input/Process/Output/Data. '
                     'Universal decomposition. Everything has I(receive), P(transform), '
                     'O(emit), D(remember). Not 4 steps — 4 simultaneous aspects.',
                     ['sequence', 'relation', 'recursion']),
            'gap': ('GAP', 'Difference when comparing two things. '
                    'Gap between imagination and observation = learning signal. '
                    'Gap is not error — gap is signal.',
                    ['gradient', 'binary']),
            'superpose': ('Superpose', 'E = Superpose(K, U). '
                          'Existence = grounded known + structured unknown. '
                          'U is NOT absence — U is unresolved presence.',
                          ['binary', 'gradient', 'recursion']),
        }

        layer_ids = {}
        for layer_key, (layer_name, layer_desc, gate_anchors) in layers.items():
            lid = nh(f'LAYER:{layer_key}')
            layer_ids[layer_key] = lid
            self.ins(nh(f'N:{layer_key}'), 'base_name', [], [], [], layer_key)
            # Frame = existence + gate anchors
            frame = [existence_id] + [gate_ids[g] for g in gate_anchors]
            self.ins(lid, 'framework_layer',
                     [nh(f'N:{layer_key}')], [], frame,
                     f'{layer_name} — {layer_desc}')

        # ══════════════════════════════════
        # LAYER 2.5: DISCOVERIES (from discoveries.md)
        # ══════════════════════════════════
        discoveries_path = root_dir.parent / 'discoveries.md'
        if not discoveries_path.exists():
            discoveries_path = ROOT_DIR / 'sources' / 'discoveries.md'

        if discoveries_path.exists():
            print('[*] Loading discoveries...')
            disc_text = read_text_file(discoveries_path)
            # Split by ## headers
            sections = re.split(r'\n## (\d+\. .+)\n', disc_text)
            disc_ids = []
            for i in range(1, len(sections), 2):
                title = sections[i].strip()
                body = sections[i+1].strip() if i+1 < len(sections) else ''
                disc_id = nh(f'DISC:{title}')
                disc_name_id = nh(f'N:disc_{title[:30]}')
                self.ins(disc_name_id, 'base_name', [], [], [], title)

                # Detect which gates/layers this discovery grounds to
                full_text = title + ' ' + body
                disc_gates = detect_gates(full_text)
                disc_layers = detect_layers(full_text)
                frame = [existence_id]
                frame += [gate_ids[g] for g in disc_gates if g in gate_ids]
                frame += [layer_ids[l] for l in disc_layers if l in layer_ids]

                self.ins(disc_id, 'discovery',
                         [disc_name_id], [], frame,
                         f'{title}\n{body[:400]}')
                disc_ids.append(disc_id)
                print(f'  discovery  {title[:60]:60} gates={disc_gates} layers={disc_layers}')

        # ══════════════════════════════════
        # LAYER 2.5: GROUNDED DESIGN (from grounded_fieldmap_design_full.md)
        # ══════════════════════════════════
        grounded_path = ROOT_DIR / 'sources' / 'grounded_fieldmap_design_full.md'
        if grounded_path.exists():
            print('[*] Loading grounded fieldmap design...')
            gd_text = read_text_file(grounded_path)
            sections = re.split(r'\n## (\d+\. .+)\n', gd_text)
            for i in range(1, len(sections), 2):
                title = sections[i].strip()
                body = sections[i+1].strip() if i+1 < len(sections) else ''
                gd_id = nh(f'GROUNDED:{title}')
                gd_name_id = nh(f'N:gd_{title[:30]}')
                self.ins(gd_name_id, 'base_name', [], [], [], title)

                full_text = title + ' ' + body
                gd_gates = detect_gates(full_text)
                gd_layers = detect_layers(full_text)
                frame = [existence_id]
                frame += [gate_ids[g] for g in gd_gates if g in gate_ids]
                frame += [layer_ids[l] for l in gd_layers if l in layer_ids]

                self.ins(gd_id, 'design_spec',
                         [gd_name_id], [], frame,
                         f'{title}\n{body[:400]}')
                print(f'  design     {title[:60]:60} gates={gd_gates}')

        # ══════════════════════════════════
        # LAYER 2.5: PRINCIPLES (from PRINCIPLE.md)
        # ══════════════════════════════════
        principle_path = ROOT_DIR / 'sources' / 'PRINCIPLE.md'
        if principle_path.exists():
            print('[*] Loading principles...')
            pr_text = read_text_file(principle_path)
            sections = re.split(r'\n## (\d+\. .+)\n', pr_text)
            for i in range(1, len(sections), 2):
                title = sections[i].strip()
                body = sections[i+1].strip() if i+1 < len(sections) else ''
                pr_id = nh(f'PRINCIPLE:{title}')
                pr_name_id = nh(f'N:pr_{title[:30]}')
                self.ins(pr_name_id, 'base_name', [], [], [], title)

                full_text = title + ' ' + body
                pr_gates = detect_gates(full_text)
                pr_layers = detect_layers(full_text)
                frame = [existence_id]
                frame += [gate_ids[g] for g in pr_gates if g in gate_ids]
                frame += [layer_ids[l] for l in pr_layers if l in layer_ids]

                self.ins(pr_id, 'principle',
                         [pr_name_id], [], frame,
                         f'{title}\n{body[:400]}')
                print(f'  principle  {title[:60]:60} gates={pr_gates}')

        # ══════════════════════════════════
        # LAYER 3: CATEGORIES (from folder structure)
        # ══════════════════════════════════
        print('\n[*] Building categories...')
        category_ids = {}
        for category_dir in sorted(root_dir.iterdir()):
            if not category_dir.is_dir():
                continue
            cat_name = category_dir.name
            cat_id = nh(f'CAT:{cat_name}')
            category_ids[cat_name] = cat_id
            self.ins(nh(f'N:{cat_name}'), 'base_name', [], [], [], cat_name)
            self.ins(cat_id, 'category', [nh(f'N:{cat_name}')], [], [existence_id], cat_name)

        # ══════════════════════════════════
        # LAYER 4: CONTENT NODES (documents)
        # ══════════════════════════════════
        all_docs = []
        all_temp_dirs = []

        for category_dir in sorted(root_dir.iterdir()):
            if not category_dir.is_dir():
                continue
            cat_name = category_dir.name
            cat_id = category_ids[cat_name]
            print(f'\n[*] Processing {cat_name}...')

            # Collect files + extract zips
            files = []
            for dirpath, dirnames, filenames in os.walk(category_dir):
                for fname in filenames:
                    fpath = Path(dirpath) / fname
                    if fpath.suffix.lower() in ('.rar', '.mp4', '.png', '.jpg', '.gif', '.ico', '.wav', '.mp3'):
                        continue
                    if fpath.suffix.lower() == '.zip':
                        try:
                            tmp = Path(tempfile.mkdtemp(prefix='fieldmap_'))
                            all_temp_dirs.append(tmp)
                            with zipfile.ZipFile(str(fpath), 'r') as zf:
                                zf.extractall(str(tmp))
                            for dp2, _, fn2 in os.walk(tmp):
                                for f2 in fn2:
                                    fp2 = Path(dp2) / f2
                                    if fp2.suffix.lower() not in ('.png', '.jpg', '.gif', '.ico', '.wav', '.mp3', '.mp4', '.zip', '.rar'):
                                        files.append(fp2)
                        except Exception as e:
                            print(f'  [!] ZIP error {fpath.name}: {e}')
                        continue
                    files.append(fpath)

            # Subfolder nodes
            subfolder_ids = {}
            for fpath in files:
                try:
                    rel = fpath.relative_to(category_dir)
                except ValueError:
                    continue
                if len(rel.parts) > 1:
                    subfolder = rel.parts[0]
                    if subfolder not in subfolder_ids:
                        sf_id = nh(f'SUBFOLDER:{cat_name}:{subfolder}')
                        subfolder_ids[subfolder] = sf_id
                        self.ins(nh(f'N:{subfolder}'), 'base_name', [], [], [], subfolder)
                        self.ins(sf_id, 'subfolder', [nh(f'N:{subfolder}')], [], [cat_id], subfolder)

            # Process each file
            for fpath in files:
                text = extract_text(fpath)
                if not text or len(text.strip()) < 20:
                    continue

                try:
                    rel = fpath.relative_to(category_dir)
                except ValueError:
                    rel = Path(fpath.name)
                fname = fpath.stem
                fext = fpath.suffix.lower()

                # Type
                if fext in ('.pdf', '.tex'):
                    doc_type = 'paper'
                elif fext == '.docx':
                    doc_type = 'document'
                elif fext in ('.py', '.js'):
                    doc_type = 'code'
                elif fext == '.md':
                    doc_type = 'document'
                elif fext == '.txt':
                    doc_type = 'text'
                else:
                    doc_type = 'file'

                # Frame = folder context
                if len(rel.parts) > 1:
                    frame_id = subfolder_ids.get(rel.parts[0], cat_id)
                else:
                    frame_id = cat_id

                # Detect grounding
                doc_gates = detect_gates(text)
                doc_layers = detect_layers(text)

                # Build frame: category + gates + layers
                doc_frame = [frame_id]
                doc_frame += [gate_ids[g] for g in doc_gates if g in gate_ids]
                doc_frame += [layer_ids[l] for l in doc_layers if l in layer_ids]

                # Doc node
                doc_id = nh(f'DOC:{cat_name}:{rel}')
                name_id = nh(f'N:{fname}')
                self.ins(name_id, 'base_name', [], [], [], fname)

                # Keywords as meaning links
                keywords = extract_keywords(text)
                kw_ids = []
                for kw in keywords:
                    kw_id = nh(f'KW:{kw}')
                    self.ins(kw_id, 'keyword', [nh(f'N:{kw}')], [], [], kw)
                    self.ins(nh(f'N:{kw}'), 'base_name', [], [], [], kw)
                    kw_ids.append(kw_id)

                # Chunks
                chunks = chunk_text(text)
                chunk_ids = []
                for ci, chunk in enumerate(chunks):
                    chunk_id = nh(f'CHUNK:{cat_name}:{rel}:{ci}')
                    chunk_name_id = nh(f'N:chunk_{fname}_{ci}')
                    self.ins(chunk_name_id, 'base_chunk_name', [], [], [], f'{fname}_chunk_{ci}')
                    chunk_kws = extract_keywords(chunk, max_kw=8)
                    chunk_kw_ids = [nh(f'KW:{kw}') for kw in chunk_kws]
                    self.ins(chunk_id, 'doc_chunk',
                             [chunk_name_id], chunk_kw_ids, [doc_id],
                             chunk[:CHUNK_SIZE])
                    chunk_ids.append(chunk_id)

                # Doc node — grounded to gates + layers via frame
                preview = text[:300].replace('\n', ' ').strip()
                self.ins(doc_id, doc_type,
                         [name_id], chunk_ids + kw_ids, doc_frame,
                         f'{fname} ({fext}) | {len(text)} chars | {len(chunks)} chunks | gates={doc_gates} | layers={doc_layers}\n{preview}')

                all_docs.append((doc_id, set(keywords), cat_name))
                print(f'  {doc_type:10} {fname[:45]:45} {len(chunks):3}ch {len(doc_gates)}G {len(doc_layers)}L')

        # ══════════════════════════════════
        # TOPIC NODES (group docs by keyword)
        # ══════════════════════════════════
        print('\n[*] Building topic nodes...')
        kw_to_docs = defaultdict(list)
        for doc_id, kws, cat in all_docs:
            for kw in kws:
                kw_to_docs[kw].append(doc_id)

        topic_count = 0
        for kw, doc_ids in sorted(kw_to_docs.items()):
            if len(doc_ids) < 3:
                continue
            topic_id = nh(f'TOPIC:{kw}')
            topic_name_id = nh(f'N:topic_{kw}')
            self.ins(topic_name_id, 'base_name', [], [], [], f'topic_{kw}')
            # Topic grounds to relevant gate
            topic_frame = [existence_id]
            for gate_key, gate_kws in GATE_KEYWORDS.items():
                if kw in gate_kws:
                    topic_frame.append(gate_ids[gate_key])
            self.ins(topic_id, 'topic',
                     [topic_name_id], doc_ids, topic_frame,
                     f'{kw} ({len(doc_ids)} docs)')
            topic_count += 1
        print(f'[+] {topic_count} topic nodes')

        # Cleanup
        for tmp in all_temp_dirs:
            try:
                shutil.rmtree(str(tmp), ignore_errors=True)
            except Exception:
                pass

        # Update existence with all top-level children
        all_children = all_gate_ids + list(layer_ids.values()) + list(category_ids.values())
        self.cur.execute('UPDATE fractal_nodes SET mean_nodes=? WHERE id=?',
                         (json.dumps(all_children), existence_id))

        self.conn.commit()

    def summary(self):
        print(f'\n{"="*60}')
        print(f'Fieldmap: {self.db_path}')
        total = self.cur.execute('SELECT COUNT(*) FROM fractal_nodes').fetchone()[0]
        print(f'Total nodes: {total}')
        print()
        for r in self.cur.execute('SELECT type, COUNT(*) FROM fractal_nodes GROUP BY type ORDER BY COUNT(*) DESC'):
            print(f'  {r[0]:25} {r[1]:5}')

        # Show grounding stats
        print(f'\n--- Grounding Stats ---')
        for gate in ['binary', 'gradient', 'sequence', 'relation', 'recursion']:
            gid = nh(f'GATE:{gate}')
            count = self.cur.execute(
                "SELECT COUNT(*) FROM fractal_nodes WHERE frame_nodes LIKE ?",
                (f'%{gid}%',)
            ).fetchone()[0]
            print(f'  {gate:15} {count:5} nodes grounded')

        for layer in ['nmf', 'ku', 'collapse', 'ipod', 'gap', 'superpose']:
            lid = nh(f'LAYER:{layer}')
            count = self.cur.execute(
                "SELECT COUNT(*) FROM fractal_nodes WHERE frame_nodes LIKE ?",
                (f'%{lid}%',)
            ).fetchone()[0]
            print(f'  {layer:15} {count:5} nodes connected')

    def close(self):
        self.conn.close()


def main():
    print(f'[*] Source: {ROOT_DIR}')
    print(f'[*] Output: {DB_PATH}')

    builder = FieldmapBuilder(DB_PATH)
    builder.build(ROOT_DIR)
    builder.summary()
    builder.close()

    size_mb = DB_PATH.stat().st_size / 1024 / 1024
    print(f'\n[+] Done: {DB_PATH.name} ({size_mb:.1f} MB)')


if __name__ == '__main__':
    main()