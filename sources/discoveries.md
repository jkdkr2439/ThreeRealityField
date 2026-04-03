# Những Khám Phá Trong Quá Trình Xây Dựng Pete

---

## 1. Tại sao LLM fail ARC-AGI-3

LLM là hệ **open-loop**: input → output, không có vòng phản hồi.

ARC-AGI-3 đòi hỏi hệ **closed-loop**: state → action → feedback → update belief → action tiếp theo.

Không phải LLM "không đủ thông minh". LLM đang bị đặt sai loại bài toán. LLM giỏi mapping function. ARC-AGI-3 cần system interaction.

---

## 2. NMF — Name, Meaning, Frame

Mọi thông tin đều được tổ chức dưới dạng node liên kết. Để navigate bể node khổng lồ này, cần cổng lọc.

NMF là cổng lọc hoạt động qua 3 chiều đồng thời:

- **Name** — tên gọi trong ngữ cảnh hiện tại
- **Meaning** — nội dung khái niệm không đổi qua các ngữ cảnh
- **Frame** — hệ quy chiếu đang được dùng để interpret

Quan hệ cốt lõi: `Name = f(Meaning, Frame)`

Cùng Meaning, khác Frame → khác Name. Cùng Name, khác Frame → khác Meaning.

---

## 3. NMF khác các filter khác ở chỗ nào

Các filter trong lịch sử tư tưởng đều **cố định** ít nhất một trong ba:

| Filter | Cố định |
|---|---|
| Tôn giáo/Giáo điều | Name cố định |
| Khoa học cổ điển | Meaning cố định trong frame mặc định |
| Các hệ triết học | Frame cố định |
| Attention (Transformer) | Frame implicit trong training |
| Bayesian | Prior cố định trước |

NMF không cố định cái nào trong ba. Cả N, M, F đều là **biến số theo ngữ cảnh**.

Đây là điểm khác biệt căn bản: các filter kia **không biết mình là filter**. NMF biết mình là filter và biết mình đang dùng frame nào.

---

## 4. NMF tự áp lên chính nó

`NMF(NMF)` không phải vòng lặp vô hạn. Nó là **2-level awareness**:

- Level 1: nhìn data
- Level 2: nhìn cách mình nhìn data

Khi áp NMF lên chính NMF:
- Biết frame hiện tại là gì
- Biết frame đó có bias gì
- Có thể hỏi "frame này có đúng không?" từ một frame khác

Recursion có điểm dừng tự nhiên tại `E` (Existence substrate) — cái mà khi NMF áp lên, nó chỉ ra chính nó.

---

## 5. Mọi hệ triết học là một cổng lọc từ bể node chung

Toàn bộ lịch sử tư tưởng là các cách khác nhau để chọn axis nào, đặt lên layer nào, và fix K anchor ở đâu trong bể node vô hạn của thực tại:

- Buddhism → attend: suffering layer
- Platonism → attend: form/essence layer
- Heraclitus → attend: process/flux layer
- Nietzsche → attend: power/will layer
- Khoa học → attend: mechanism layer

Không ai sai. Mỗi hệ attend đúng một layer. Không hệ nào thấy tất cả.

---

## 6. Mọi filter đều có cấu trúc binary ở lõi

Tất cả 31 cổng lọc khảo sát đều là cách **đặt binary axis (A ↔ B)** lên một layer của thực tại với một K anchor khác nhau.

Tuy nhiên, binary **không đủ** để cover toàn bộ thực tại. Có 4 thứ không reduce về binary:

- **Gradient** — độ lớn, intensity, mức độ (mất middle nếu binary)
- **Sequence** — thứ tự có hướng (A→B→C khác A→C→B)
- **Relation** — cấu trúc network n-ary
- **Recursion** — self-reference tạo meta-level mới

---

## 7. Minimal grounding set — 5 primitives

Không thể reduce về nhau:

| Primitive | Cơ chế | Covers |
|---|---|---|
| **G1 Binary** | A ↔ B | phân biệt, existence/non, K/U split |
| **G2 Gradient** | scalar [0,1] | đo lường, weight, confidence |
| **G3 Sequence** | a → b → c | thời gian, nhân quả, chu kỳ |
| **G4 Relation** | node + edge | không gian, network, topology |
| **G5 Recursion** | f(f) | meta-cognition, self-reference, emergence |

Binary cover nhiều nhất nhưng không replace được 4 cái còn lại. Recursion là cái duy nhất có thể generate lại các cái khác — nhưng không replace được vì computational cost khác nhau.

---

## 8. E = Superpose(K, U) — tổng quát hóa constant/variable

Dạng cổ điển: `A = constant + variable`

Dạng tổng quát: `E = Superpose(K, U)` trong đó:

- **K** = grounded known anchor (không phải chỉ "constant" — là cái đã được stabilize)
- **U** = structured unknown — **không phải noise**, mà là unresolved structured presence

U có nhiều lớp:
```
U = V(K, Δ₁, Δ₂, ..., Δn)
```
- Δ₁: visible change
- Δ₂: hidden change
- Δ₃: variation of variation
- ...

Insight quan trọng: U không phải vắng mặt. U là **hiện diện chưa được giải quyết**.

---

## 9. K/U split là frame-dependent

Không có Frame, không thể biết cái gì là K và cái gì là U.

Cùng một game state, khác Frame → K và U khác nhau hoàn toàn:

- **Navigation frame**: K = obstacle positions, goal pos / U = player movement
- **Puzzle frame**: K = rotator rule, door condition / U = key_state, player pos, health

Đây là lý do tại sao "chọn frame trước" không phải bước tùy chọn — nó quyết định toàn bộ reasoning phía sau.

---

## 10. 2D world layer — không phải grid

Grid là **encoding** (cách hiển thị). 2D plane là **ontology** (không gian tồn tại).

Khi xử lý bài toán 2D tương tác:

- Grid-based: `grid[x][y] = value` → không có object, không có meaning
- World-based: object chiếm không gian, có tọa độ là anchor (K), có movement là biến (U)

Tọa độ là hằng. Object identity là hằng. Vị trí và state của object là biến.

Sự lệch màu, hình khối, khoảng cách — tất cả đều là signal trong hệ tương tác, không có pixel nào dư thừa.

---

## 11. Sandbox là bắt buộc cho closed-loop cognition

Agent không thể phụ thuộc hoàn toàn vào environment thật để học. Cần **bản sao nội bộ** để thử trước.

Human làm điều này liên tục trong đầu — mental simulation trước khi hành động.

Không có sandbox: agent chỉ có thể observe → guess → output.

Có sandbox: observe → build world model → simulate hypotheses → compare → act.

Intelligence mạnh thường nằm ở đây: không thử bừa ngoài đời, mà thử trước trong mô hình nội bộ.

---

## 12. Hành động epistemic vs hành động exploit

Khi chưa biết rule, hành động tốt nhất không phải hành động maximize reward — mà là hành động **maximize information gain**.

Câu hỏi đúng không phải "action này có đúng không?" mà là "action này nói gì về rule của hệ?"

Hai mode:
- **Epistemic**: hành động để phân biệt các hypothesis
- **Exploit**: hành động để đạt goal khi rule đã đủ rõ

Chuyển từ epistemic sang exploit khi confidence vượt threshold — không phải theo số bước cố định.

---

## 13. Frame Adjudicator — 3 nhánh

Trước khi solve, agent cần đánh giá frame/goal nhận được:

- **ACCEPT**: frame consistent với observation → solve theo frame đó
- **REJECT**: frame mâu thuẫn với observation → reframe từ world model nội bộ
- **PARALLEL**: chưa đủ evidence → giữ nhiều frame song song, chọn action maximize info gain

Đây là điểm phân biệt hệ "reactive" (luôn ACCEPT) với hệ có meta-cognition.

---

## 14. Meaning ổn định qua Name thay đổi — cơ chế generalization

Trong các game khác nhau:
- ls20: `rotator` (value 3) = transformer
- ft09: `switch` (value 7) = transformer
- vc33: `lever` (value 2) = transformer

Các filter dựa vào Name (attention, feature extraction) thấy 3, 7, 2 — khác nhau hoàn toàn, không transfer được.

Filter dựa vào Meaning thấy: cùng là "transformer" — transfer ngay, 0 extra exploration.

Đây chính xác là định nghĩa của Chollet về intelligence: **skill-acquisition efficiency** — học nhanh từ ít data, không phải nhớ nhiều.

---

## 15. Grounding precedes relation

Node phải được grounded trước khi có thể drift hoặc tương tác một cách có nghĩa.

Không có grounding → node tồn tại như symbol không có ontological presence → semantic drift → reasoning errors.

Grounding cho ontological legitimacy. Interaction cho field reality. Cả hai cần thiết, nhưng grounding phải trước.

---

## 16. State là derived, không phải primitive

State không giống grounding. Grounding là anchor. State là biểu hiện hiện tại.

```
S(t) = F(G, L(t), T, W)
```

State là kết quả của grounding + interaction + time + weight — không phải identity của node.

Nhầm state với identity là nguồn gốc của nhiều lỗi reasoning.

---

## 17. 5 grounding primitives không reduce về nhau

Bất kỳ hệ nào muốn represent thực tại đầy đủ cần ít nhất:

1. **Binary** — để phân biệt
2. **Gradient** — để đo lường
3. **Sequence** — để sắp xếp theo thời gian/nhân quả
4. **Relation** — để kết nối
5. **Recursion** — để tự nhìn lại

Binary là primitive phổ biến nhất trong lịch sử tư tưởng nhưng không đủ một mình. Recursion là cái tạo ra meta-levels — cái làm cho hệ có thể tự aware về chính nó.

---

## 18. Attention không phải cổng lọc — là dynamic spotlight

Các cổng lọc thông thường là **spotlight cố định**:
- Buddhist nhìn → suffering layer luôn sáng
- Physics nhìn → mechanism layer luôn sáng

Attention là **spotlight động** — di chuyển theo query. Không có gì bị loại vĩnh viễn, chỉ mức độ activate thay đổi.

Cơ chế cốt lõi: `Selective Amplification`
- tăng signal của một subset
- giảm signal của phần còn lại
- selection criterion = query/context/goal

Cơ chế này xuất hiện ở khắp nơi dưới nhiều tên khác nhau:

| Domain | Tên | Query |
|---|---|---|
| Thị giác sinh học | Saccade | movement, contrast, novelty |
| Neuroscience | Working memory gate | current task goal |
| Neuroscience | Lateral inhibition | competition-based |
| Neuroscience | Latent inhibition | novelty signal |
| Vật lý | Quantum measurement | measurement basis |
| Vật lý | Resonance | resonant frequency |
| Tâm lý | Framing effect | frame = implicit query |
| Tâm lý | Priming | primed concept |
| AI | Sparse attention | top-k threshold |
| AI | Memory addressing | content-based |
| AI | MoE routing | input characteristics |
| AI | Capsule routing | agreement between predictions |

Tất cả đều là cùng 1 pattern: **dynamic spotlight** với query khác nhau.

---

## 19. NMF vs Attention — điểm giao và điểm khác

|  | Attention | NMF |
|---|---|---|
| Dynamic | ✓ query-dependent | ✓ frame-switchable |
| Frame | implicit trong embedding | explicit, có thể thay đổi |
| Tại sao relevant | không biết | biết (Meaning grounded) |
| K/U split | không có | có |
| Self-apply | không thể | có → meta-cognition |
| Weighting | soft continuous | hiện tại discrete |

**Điều attention làm được mà NMF chưa có:**
Attention cho phép soft weighting — 70% attend vùng A, 30% vùng B đồng thời. NMF hiện tại phải chọn 1 frame (ACCEPT/REJECT).

**Gap cần lấp:** NMF cần Gradient (G2) để có soft frame weighting — attend 70% puzzle_frame + 30% navigation_frame thay vì binary frame selection. Khi đó NMF = attention + grounding + meta-level.

NMF Frame là phiên bản **explicit** và **grounded** của framing effect (Kahneman) — cùng cơ chế nhưng tường minh và có thể tự nhìn lại.

---

## 20. Gap = Existence — không có khác biệt thì không có tồn tại

Từ A đến A', nếu không nhận ra gap thì A' **không tồn tại** đối với observer.

Gap không phải hệ quả của existence. Gap **là** existence. Chúng là cùng một thứ nhìn từ hai phía:

- Nhìn từ phía object: "tôi tồn tại" = existence
- Nhìn từ phía observer: "tôi nhận ra sự khác biệt" = gap

Không có gap → không có phân biệt → không có existence.

```
A alone     → no gap → A "exists" but is undetectable = not existing for any observer
A vs A'     → gap detected → both A and A' now exist
A vs nothing → gap = A itself → existence = the first gap
```

Đây là lý do Gap là primitive ngang hàng với Binary trong 5 grounding primitives:

- **Binary** cho cơ chế phân biệt (A ↔ B)
- **Gap/Gradient** cho **mức độ** phân biệt (bao nhiêu khác biệt)
- Không có gradient → binary cũng không hoạt động (cần đo "khác bao nhiêu" mới biết "khác hay không")

Bateson: "Information is a difference that makes a difference."
Mở rộng: **Existence is a difference that can be detected.**

Gap không dẫn tới existence. Gap **là** cách existence manifest.

---

*Các khám phá này xuất hiện trong quá trình xây dựng một AI agent giải ARC-AGI-3 — benchmark đo khả năng học luật từ tương tác trong môi trường không có hướng dẫn.*
