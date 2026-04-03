"""Generate 3D fieldmap visualization — pyramid + grounded architecture"""
import sys, io; sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import sqlite3, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = str(ROOT / 'kevin_fieldmap.db')
OUT = str(ROOT / 'kevin_fieldmap_3d.html')

SHOW = {'existence', 'filter_gate', 'framework_layer', 'pyramid_vertex', 'pyramid', 'pyramid_edge',
        'category', 'subfolder', 'topic', 'paper', 'text', 'document', 'code', 'file',
        'principle', 'discovery', 'design_spec'}

conn = sqlite3.connect(DB)
c = conn.cursor()
rows = c.execute('SELECT id, type, name_nodes, mean_nodes, frame_nodes, raw_content FROM fractal_nodes').fetchall()

nodes = []
edges = []
node_ids = set()

for nid, ntype, n_nodes, m_nodes, f_nodes, raw in rows:
    if ntype not in SHOW:
        continue
    nodes.append({"id": nid, "type": ntype, "raw": (raw or "")[:200]})
    node_ids.add(nid)

for nid, ntype, n_nodes, m_nodes, f_nodes, raw in rows:
    if nid not in node_ids:
        continue
    try:
        m_list = json.loads(m_nodes) if m_nodes else []
    except: m_list = []
    try:
        f_list = json.loads(f_nodes) if f_nodes else []
    except: f_list = []
    for m in m_list:
        if m in node_ids:
            edges.append({"src": nid, "dst": m})
    for f in f_list:
        if f in node_ids:
            edges.append({"src": f, "dst": nid})

conn.close()
print(f'Nodes: {len(nodes)}, Edges: {len(edges)}')

html = '''<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>Kevin T.N. Knowledge Fieldmap — Pyramid</title>
<style>
  body { margin: 0; overflow: hidden; background: #000; }
  #info { position: absolute; top: 10px; left: 10px; color: #555; font: 11px monospace; pointer-events: none; z-index: 10; line-height: 1.6; }
  #tooltip { position: absolute; display: none; background: rgba(0,0,0,0.95); color: #ccc; font: 11px monospace; padding: 8px 12px; border-radius: 4px; max-width: 500px; pointer-events: none; z-index: 10; border: 1px solid #333; white-space: pre-wrap; }
  #legend { position: absolute; bottom: 10px; left: 10px; color: #555; font: 10px monospace; z-index: 10; }
</style>
</head><body>
<div id="info">
  <span id="nc">0</span> bodies · <span id="ec">0</span> bonds<br>
  Kevin T.N. Knowledge Fieldmap<br>
  Pyramid (4 vertices) → Gates → Layers → Content<br>
  drag · scroll · hover
</div>
<div id="tooltip"></div>
<div id="legend"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script>
const NODES = ''' + json.dumps(nodes) + ''';
const EDGES = ''' + json.dumps(edges) + ''';

document.getElementById('nc').textContent = NODES.length;
document.getElementById('ec').textContent = EDGES.length;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.1, 8000);
camera.position.set(150, 350, 700);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setClearColor(0x020208);
document.body.appendChild(renderer.domElement);
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.04;

// === REALITY SPHERES ===
// === REALITY SPHERES ===
// Subjective: r=220, bright warm tone, centered
const SUBJ_R = 220;
const subjSphere = new THREE.Mesh(
  new THREE.SphereGeometry(SUBJ_R, 48, 48),
  new THREE.MeshBasicMaterial({
    color: 0x88aaff, transparent: true, opacity: 0.05,
    side: THREE.DoubleSide, depthWrite: false
  })
);
scene.add(subjSphere);
const subjWire = new THREE.LineSegments(
  new THREE.EdgesGeometry(new THREE.SphereGeometry(SUBJ_R, 14, 14)),
  new THREE.LineBasicMaterial({color: 0xaaccff, transparent: true, opacity: 0.08})
);
scene.add(subjWire);

// Intersubjective: r=1100 (5x subj), far offset, only small overlap
// Overlap < half of subjective sphere = attention window
const INTER_R = 1100;
const INTER_OFFSET = {x: 900, y: -200, z: 600};
const interSphere = new THREE.Mesh(
  new THREE.SphereGeometry(INTER_R, 64, 64),
  new THREE.MeshBasicMaterial({
    color: 0xaaffcc, transparent: true, opacity: 0.02,
    side: THREE.DoubleSide, depthWrite: false
  })
);
interSphere.position.set(INTER_OFFSET.x, INTER_OFFSET.y, INTER_OFFSET.z);
scene.add(interSphere);
const interWire = new THREE.LineSegments(
  new THREE.EdgesGeometry(new THREE.SphereGeometry(INTER_R, 24, 24)),
  new THREE.LineBasicMaterial({color: 0x88ffbb, transparent: true, opacity: 0.04})
);
interWire.position.set(INTER_OFFSET.x, INTER_OFFSET.y, INTER_OFFSET.z);
scene.add(interWire);

// Labels
function makeSphereLabel(text, color, pos) {
  const cv = document.createElement('canvas'); cv.width=800; cv.height=48;
  const cx = cv.getContext('2d'); cx.font='15px monospace';
  cx.fillStyle = color; cx.globalAlpha = 0.6;
  cx.fillText(text, 4, 32);
  const sp = new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(cv),transparent:true}));
  sp.scale.set(55, 4, 1);
  sp.position.set(pos.x, pos.y, pos.z);
  scene.add(sp);
}
makeSphereLabel('CHU QUAN — subjective / memory / unconscious', '#aaccff', {x:0, y:SUBJ_R+8, z:0});
makeSphereLabel('LIEN CHU THE — intersubjective / attention overlap', '#88ffbb', {x:INTER_OFFSET.x, y:INTER_OFFSET.y+INTER_R+15, z:INTER_OFFSET.z});
makeSphereLabel('TUYET DOI — absolute / pyramid boundary', '#ff88ff', {x:0, y:460, z:0});

// Starfield
{
  const g = new THREE.BufferGeometry();
  const p = new Float32Array(4000*3);
  for (let i=0;i<p.length;i++) p[i]=(Math.random()-0.5)*3500;
  g.setAttribute('position', new THREE.BufferAttribute(p,3));
  scene.add(new THREE.Points(g, new THREE.PointsMaterial({color:0x111122,size:0.5})));
}

const COL = {
  existence: 0xffffff,
  pyramid_vertex: 0xff00ff,
  pyramid: 0xff00ff,
  pyramid_edge: 0xff00ff,
  filter_gate: 0xffcc00,
  framework_layer: 0x00ccff,
  category: 0xff8800,
  subfolder: 0xcc6600,
  topic: 0x22cc88,
  paper: 0x4499ff,
  text: 0x44bbff,
  document: 0x6699ff,
  code: 0x44ff44,
  file: 0x888888,
  principle: 0xff44dd,
  discovery: 0xff6644,
  design_spec: 0xaaaa44,
};

const legend = document.getElementById('legend');
legend.innerHTML = [
  ['pyramid','#ff00ff'],['existence','#ffffff'],['gate','#ffcc00'],['layer','#00ccff'],
  ['principle','#ff44dd'],['discovery','#ff6644'],['topic','#22cc88'],
  ['paper','#4499ff'],['code','#44ff44']
].map(([t,c]) => '<span style="color:'+c+'">● '+t+'</span>').join('  ');

const edgeCnt = {};
NODES.forEach(n => edgeCnt[n.id]=0);
EDGES.forEach(e => { if(edgeCnt[e.src]!==undefined) edgeCnt[e.src]++; if(edgeCnt[e.dst]!==undefined) edgeCnt[e.dst]++; });

const G_CONST = 600, DT = 0.015, SOFT = 5;

// === PYRAMID GEOMETRY — tetrahedron around origin ===
// 4 vertices of a regular tetrahedron, radius 350
const PYRAMID_R = 350;
const PYRAMID_POS = [
  {x: 0, y: PYRAMID_R * 1.2, z: 0},                          // top: NMF
  {x: PYRAMID_R * 0.94, y: -PYRAMID_R * 0.4, z: 0},          // front-right: SDCHV
  {x: -PYRAMID_R * 0.47, y: -PYRAMID_R * 0.4, z: PYRAMID_R * 0.82},  // back-left: Phap Luan
  {x: -PYRAMID_R * 0.47, y: -PYRAMID_R * 0.4, z: -PYRAMID_R * 0.82}, // back-right: 3 Tang
];

class Body {
  constructor(node, parent, a, e, inc, phase, mass, fixedPos, surfaceR) {
    this.node = node; this.parent = parent; this.mass = mass;
    this.a = a; this.e = Math.min(e, 0.92);
    this.inc = inc; this.angle = phase;
    this.pos = new THREE.Vector3();
    this.fixedPos = fixedPos || null;
    this.surfaceR = surfaceR || 0;  // if >0, orbit on sphere surface of this radius
    this.phi = (Math.random()-0.5) * Math.PI;  // latitude for surface orbit

    const color = COL[node.type] || 0x888888;
    let sz;
    if (node.type === 'existence') sz = 7;
    else if (node.type === 'pyramid_vertex') sz = 5;
    else if (node.type === 'filter_gate') sz = 3.5;
    else if (node.type === 'framework_layer') sz = 3;
    else if (node.type === 'category') sz = 2.5;
    else if (node.type === 'principle') sz = 2;
    else if (node.type === 'discovery') sz = 1.8;
    else if (node.type === 'topic') sz = 1.0 + Math.min((edgeCnt[node.id]||0)*0.05, 2);
    else sz = 0.8;

    const opacity = ['paper','text','document','code','file'].includes(node.type) ? 0.5 : 0.85;
    this.mesh = new THREE.Mesh(
      new THREE.SphereGeometry(sz, 10, 10),
      new THREE.MeshBasicMaterial({color, transparent: true, opacity})
    );
    this.mesh.userData = node;
    scene.add(this.mesh);

    // Glow
    if (['existence','pyramid_vertex','filter_gate'].includes(node.type)) {
      const glow = new THREE.Mesh(
        new THREE.SphereGeometry(sz * 3.5, 16, 16),
        new THREE.MeshBasicMaterial({color, transparent: true, opacity: 0.04})
      );
      this.glowMesh = glow;
      scene.add(glow);
    }

    // Label
    if (['existence','pyramid_vertex','filter_gate','framework_layer','category'].includes(node.type)) {
      const cv = document.createElement('canvas'); cv.width=512; cv.height=64;
      const cx = cv.getContext('2d'); cx.font='bold 20px monospace';
      cx.fillStyle='#'+color.toString(16).padStart(6,'0'); cx.globalAlpha=0.7;
      const label = (node.raw||'').split(' — ')[0].substring(0,25);
      cx.fillText(label, 4, 38);
      this.label = new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(cv),transparent:true}));
      this.label.scale.set(25, 3.5, 1);
      scene.add(this.label);
    }

    // Orbit trail
    if (parent && a > 5 && !fixedPos) {
      const b = a * Math.sqrt(1 - this.e*this.e);
      const curve = new THREE.EllipseCurve(0, 0, a, b, 0, Math.PI*2, false, 0);
      const pts = curve.getPoints(50).map(p => new THREE.Vector3(p.x, 0, p.y));
      this.trail = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints(pts),
        new THREE.LineBasicMaterial({color, transparent: true, opacity: 0.04})
      );
      this.trail.rotation.x = inc;
      scene.add(this.trail);
    }
  }

  update(dt) {
    // Surface orbit: node moves on sphere surface, synced with sphere rotation
    if (this.surfaceR > 0) {
      const st = Date.now() * 0.00003;  // same base speed as subjSphere rotation
      const speed = 0.3 + this.mass * 0.05;
      this.angle += dt * speed * 0.15;
      this.phi += Math.sin(this.angle * 0.7) * dt * 0.02;  // gentle latitude wobble
      // Spherical coords on surface
      const theta = this.angle + st * 1.0;  // synced with subjSphere.rotation.y
      const R = this.surfaceR;
      const x = R * Math.cos(theta) * Math.cos(this.phi);
      const y = R * Math.sin(this.phi);
      const z = R * Math.sin(theta) * Math.cos(this.phi);
      this.pos.set(x, y, z);
      this.mesh.position.copy(this.pos);
      if (this.label) this.label.position.set(x, y + 6, z);
      return;
    }

    if (this.fixedPos) {
      // Slow rotation for pyramid vertices
      const t = Date.now() * 0.0001;
      const fp = this.fixedPos;
      const cosT = Math.cos(t * 0.2);
      const sinT = Math.sin(t * 0.2);
      this.pos.set(
        fp.x * cosT - fp.z * sinT,
        fp.y,
        fp.x * sinT + fp.z * cosT
      );
      this.mesh.position.copy(this.pos);
      if (this.label) this.label.position.set(this.pos.x, this.pos.y + 12, this.pos.z);
      if (this.glowMesh) this.glowMesh.position.copy(this.pos);
      return;
    }

    if (!this.parent && this.a === 0) {
      this.mesh.position.set(0, 0, 0);
      this.pos.set(0, 0, 0);
      if (this.label) this.label.position.set(0, 14, 0);
      if (this.glowMesh) this.glowMesh.position.set(0, 0, 0);
      return;
    }

    const p = this.a * (1 - this.e * this.e);
    const denom = 1 + this.e * Math.cos(this.angle);
    const r = Math.max(p / Math.max(denom, 0.05), 1);
    const pMass = this.parent ? this.parent.mass : 100;
    const L = Math.sqrt(G_CONST * pMass * Math.abs(p));
    const inertia = 1 + this.mass * 0.06;
    this.angle += L / (r * r + SOFT) / inertia * dt;

    const x = r * Math.cos(this.angle);
    const z = r * Math.sin(this.angle);
    const y = z * Math.sin(this.inc);
    const z2 = z * Math.cos(this.inc);
    const px = this.parent ? this.parent.pos.x : 0;
    const py = this.parent ? this.parent.pos.y : 0;
    const pz = this.parent ? this.parent.pos.z : 0;

    this.pos.set(px + x, py + y, pz + z2);
    this.mesh.position.copy(this.pos);
    if (this.label) this.label.position.set(this.pos.x, this.pos.y + 8, this.pos.z);
    if (this.glowMesh) this.glowMesh.position.copy(this.pos);
    if (this.trail) this.trail.position.set(px, py, pz);
  }
}

// === CREATE BODIES ===
const bodies = [], bodyById = {};
const byType = {};
NODES.forEach(n => { if (!byType[n.type]) byType[n.type]=[]; byType[n.type].push(n); });

// Existence at center
const exNode = NODES.find(n => n.type === 'existence');
if (exNode) {
  const b = new Body(exNode, null, 0, 0, 0, 0, 100, null);
  bodies.push(b); bodyById[exNode.id] = b;
}

// Pyramid vertices — fixed positions, slow rotation
const pyVerts = byType['pyramid_vertex'] || [];
pyVerts.forEach((n, i) => {
  const fp = PYRAMID_POS[i % PYRAMID_POS.length];
  const b = new Body(n, null, 0, 0, 0, 0, 30, fp);
  bodies.push(b); bodyById[n.id] = b;
});

// Draw pyramid wireframe edges
const pyramidLineMat = new THREE.LineBasicMaterial({color: 0xff00ff, transparent: true, opacity: 0.15});
let pyramidLines = [];

// === LAYERED SPHERE STRUCTURE ===
// Layer 1 (r~30): Filter Gates — most fundamental, closest to existence
const gateNodes = byType['filter_gate'] || [];
gateNodes.forEach((n, i) => {
  const a = 25 + i * 8;
  const e = 0.1 + Math.random()*0.1;
  const inc = (Math.random()-0.5)*0.8;
  const phase = (i/gateNodes.length)*Math.PI*2;
  const b = new Body(n, bodyById[exNode.id], a, e, inc, phase, 25);
  bodies.push(b); bodyById[n.id] = b;
});

// Layer 2 (r~60): Framework Layers — built on gates
const layerNodes = byType['framework_layer'] || [];
layerNodes.forEach((n, i) => {
  const a = 55 + i * 8;
  const e = 0.12 + Math.random()*0.12;
  const inc = (Math.random()-0.5)*0.9;
  const phase = (i/layerNodes.length)*Math.PI*2 + 0.3;
  const b = new Body(n, bodyById[exNode.id], a, e, inc, phase, 18);
  bodies.push(b); bodyById[n.id] = b;
});

// Layer 3 (r~100): Principles — general rules, orbit layers
(byType['principle']||[]).forEach((n, i) => {
  const parent = bodyById[layerNodes[i % Math.max(layerNodes.length,1)]?.id] || bodyById[exNode.id];
  const a = 30 + (i%12)*4;
  const b = new Body(n, parent, a, 0.15+Math.random()*0.2, (Math.random()-0.5)*1.2, (i/35)*Math.PI*2, 6);
  bodies.push(b); bodyById[n.id] = b;
});

// Layer 4 (r~140): Discoveries + Design specs — more specific
(byType['discovery']||[]).forEach((n, i) => {
  const parent = bodyById[layerNodes[i % Math.max(layerNodes.length,1)]?.id] || bodyById[exNode.id];
  const b = new Body(n, parent, 50 + i*3, 0.2+Math.random()*0.2, (Math.random()-0.5)*1.0, Math.random()*Math.PI*2, 4);
  bodies.push(b); bodyById[n.id] = b;
});
(byType['design_spec']||[]).forEach((n, i) => {
  const parent = bodyById[layerNodes[i % Math.max(layerNodes.length,1)]?.id] || bodyById[exNode.id];
  const b = new Body(n, parent, 55 + i*3, 0.2+Math.random()*0.2, (Math.random()-0.5)*0.8, Math.random()*Math.PI*2, 3);
  bodies.push(b); bodyById[n.id] = b;
});

// Layer 5 (r~180): Topics — branching out, many nodes
const catNodes = byType['category'] || [];
(byType['topic']||[]).forEach((n, i) => {
  const mass = 2 + (edgeCnt[n.id]||0) * 0.3;
  const phase = (i / Math.max((byType['topic']||[]).length, 1)) * Math.PI * 2 + Math.random() * 0.5;
  const b = new Body(n, null, 0, 0, (Math.random()-0.5)*Math.PI, phase, mass, null, 180);
  bodies.push(b); bodyById[n.id] = b;
});

// Surface (r~220): Papers/docs — most specific, most numerous, on the skin
['paper','text','document','code','file'].forEach(dt => {
  (byType[dt]||[]).forEach((n, i) => {
    const mass = 1 + (edgeCnt[n.id]||0) * 0.2;
    const phase = Math.random() * Math.PI * 2;
    const b = new Body(n, null, 0, 0, (Math.random()-0.5)*Math.PI, phase, mass, null, SUBJ_R);
    bodies.push(b); bodyById[n.id] = b;
  });
});

// Categories — structural, orbit mid-range
catNodes.forEach((n, i) => {
  const a = 140 + i * 20;
  const e = 0.1 + Math.random()*0.1;
  const inc = (Math.random()-0.5)*0.5;
  const phase = (i/catNodes.length)*Math.PI*2;
  const b = new Body(n, bodyById[exNode.id], a, e, inc, phase, 12);
  bodies.push(b); bodyById[n.id] = b;
});

// Tooltip
const tooltip = document.getElementById('tooltip');
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
const allMeshes = bodies.map(b => b.mesh);

renderer.domElement.addEventListener('mousemove', e => {
  mouse.x = (e.clientX / innerWidth) * 2 - 1;
  mouse.y = -(e.clientY / innerHeight) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);
  const hits = raycaster.intersectObjects(allMeshes);
  if (hits.length > 0) {
    const d = hits[0].object.userData;
    tooltip.style.display = 'block';
    tooltip.style.left = (e.clientX + 14) + 'px';
    tooltip.style.top = (e.clientY + 14) + 'px';
    tooltip.textContent = '[' + d.type + '] ' + d.raw;
  } else {
    tooltip.style.display = 'none';
  }
});

// Animate
function animate() {
  requestAnimationFrame(animate);
  bodies.forEach(b => b.update(DT));

  // Slowly rotate reality spheres — different speeds, different axes
  const rt = Date.now() * 0.00003;
  subjSphere.rotation.y = rt * 1.0;
  subjSphere.rotation.x = Math.sin(rt * 0.3) * 0.1;
  subjWire.rotation.copy(subjSphere.rotation);
  interSphere.rotation.y = rt * 0.6;
  interSphere.rotation.z = Math.sin(rt * 0.5) * 0.15;
  interWire.rotation.copy(interSphere.rotation);

  // Draw pyramid wireframe (update positions each frame)
  pyramidLines.forEach(l => scene.remove(l));
  pyramidLines = [];
  if (pyVerts.length >= 4) {
    const vp = pyVerts.map(n => bodyById[n.id]?.pos).filter(Boolean);
    if (vp.length >= 4) {
      const pairs = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
      pairs.forEach(([a,b]) => {
        const geom = new THREE.BufferGeometry().setFromPoints([vp[a].clone(), vp[b].clone()]);
        const line = new THREE.Line(geom, pyramidLineMat);
        scene.add(line);
        pyramidLines.push(line);
      });
    }
  }

  controls.update();
  renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
</script>
</body></html>'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Output: {OUT}')
