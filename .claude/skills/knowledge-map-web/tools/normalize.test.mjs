// 数据检查、md 转换、单文件网页的回归用例：node --test tools/*.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { normalize } from "../lib/normalize.js";
import { parseMd } from "../lib/md.js";
import { formulaHtml, formulaRuns } from "../lib/formula.js";
import { load, singleHtml } from "./build-lib.mjs";
import { pinyinInitials } from "../lib/pinyin-dict.js";

// md 文本 → load() 的结果
const convert = md => { const f = join(mkdtempSync(join(tmpdir(), "kmap-")), "x.md"); writeFileSync(f, md); return load(f); };

const SAMPLE = join(dirname(fileURLToPath(import.meta.url)), "..", "examples", "sample.json");
const sample = () => JSON.parse(readFileSync(SAMPLE, "utf8"));
const ids = d => d.nodes.map(n => n.id);

test("示例数据通过检查", () => {
  assert.deepEqual(normalize(sample()).errors, []);
});

test("只有一个节点的主干，编号不存在也要报错", () => {
  const d = sample(); d.chains = [{ name: "坏主干", path: ["9.9"] }];
  assert.deepEqual(normalize(d).errors, ["主干「坏主干」：9.9 不存在"]);
});

test("多节点主干里每个不存在的编号都报出来", () => {
  const d = sample(), [a] = ids(d); d.chains = [{ name: "坏主干", paths: [["8.8", a, "9.9"]] }];
  assert.deepEqual(normalize(d).errors, ["主干「坏主干」：8.8 不存在", "主干「坏主干」：9.9 不存在"]);
});

test("只有一个有效节点的主干没有错误", () => {
  const d = sample(), [a] = ids(d); d.chains = [{ name: "单点", path: [a] }];
  assert.deepEqual(normalize(d).errors, []);
});

test("依赖指向不存在的知识要报错", () => {
  const d = sample(); d.nodes[0].deps = [{ id: "9.9" }];
  assert.ok(normalize(d).errors.some(e => e.includes("依赖的 9.9 不存在")));
});

test("md 示例转换后通过检查，md 的各种写法都读到了", async () => {
  const md = readFileSync(join(dirname(SAMPLE), "sample.md"), "utf8");
  const r = convert(md);
  assert.deepEqual(r.errors, []);
  assert.deepEqual(r.warns, []);
  const d = normalize(r.raw).data, by = Object.fromEntries(d.nodes.map(n => [n.id, n]));
  assert.deepEqual(d.nodes.map(n => n.id), ["0.1", "1.1.1", "1.1.2", "2.1", "3.1"]);
  assert.deepEqual(d.groups.map(g => [g.id, g.name]), [["1.1", "运动的描述"]]);
  assert.equal(by["1.1.1"].group, "1.1");
  assert.equal(by["1.1.1"].region, "运动学");
  assert.deepEqual(by["2.1"].conditions, ["惯性参考系", "宏观、低速"]);
  assert.equal(by["2.1"].importance, 3);
  assert.deepEqual(by["1.1.2"].counterexamples, ["速度大，加速度不一定大：匀速飞行的飞机 a＝0"]);
  assert.deepEqual(by["3.1"].deps, [{ id: "2.1", kind: "推出", how: "F＝ma 沿位移累积", method: "累积" }]);
  assert.deepEqual(by["1.1.2"].deps, [{ id: "1.1.1", kind: "推出", how: "速度再求一次变化率" }]);
  assert.equal(by["1.1.2"].from, "由 速度（1.1.1）（速度再求一次变化率）");
  assert.deepEqual(d.chains, [{ name: "从位移到能量", paths: [["0.1", "1.1.1", "1.1.2", "2.1", "3.1"]] }]);
  assert.deepEqual(d.methods[1], { name: "累积", desc: "把每一小段的效果加起来。", nodes: ["3.1"] });
  assert.deepEqual(d.regions.map(r => r.anchor), [0.2, 0.5, 0.8]);
});

test("MD 字段内的多行块公式完整进入 KaTeX 渲染", () => {
  const md = readFileSync(join(dirname(SAMPLE), "sample.md"), "utf8");
  const parsed = parseMd(md);
  assert.deepEqual(parsed.errors, []);
  assert.deepEqual(parsed.warns, []);
  const formula = parsed.raw.nodes.find(node => node.id === "3.1").one;
  assert.equal(formula, "$$\nW=\\Delta E_k\n$$");

  const previous = globalThis.katex;
  globalThis.katex = { renderToString: (source, options) => `<math data-display="${options.displayMode}">${source.trim()}</math>` };
  try {
    assert.equal(formulaHtml(formula), '<math data-display="true">W=\\Delta E_k</math>');
  } finally {
    if (previous) globalThis.katex = previous;
    else delete globalThis.katex;
  }

  const broken = parseMd(md.replace("W=\\Delta E_k\n$$", "W=\\Delta E_k"));
  assert.ok(broken.warns.some(warning => warning.includes("块公式缺少结束 $$")));
});

test("标志里的旧公式没有 LaTeX 定界符时给出提醒", () => {
  const md = readFileSync(join(dirname(SAMPLE), "sample.md"), "utf8").replace("$F=ma$", "F=ma");
  const parsed = parseMd(md);
  assert.ok(parsed.warns.some(warning => warning.includes("标志含公式但没有使用 $...$")));
});

test("md 里依赖写错时报出来", async () => {
  const md = readFileSync(join(dirname(SAMPLE), "sample.md"), "utf8").replace("⇐用到 1.1.2（力决定加速度）", "⇐用到 9.9（不存在）");
  assert.ok(convert(md).errors.some(e => e.includes("依赖的 9.9 不存在")));
});

test("混合公式记法转成统一的上下标排版", () => {
  assert.deepEqual(formulaRuns("a^(m/n)"), [
    { text: "a", script: "" },
    { text: "(m/n)", script: "sup" },
  ]);
  assert.equal(formulaHtml("log_c b"), 'log<sub class="fm-script">c</sub> b');
  assert.equal(formulaHtml("aₚ+a_q"), 'aₚ+a<sub class="fm-script">q</sub>');
  assert.equal(formulaHtml("∫ₐᵇf(x)dx"), "∫ₐᵇf(x)dx");
  assert.equal(formulaHtml("y=Ce^{kx}"), 'y=Ce<sup class="fm-script">kx</sup>');
});

test("Markdown LaTeX 交给 KaTeX 富文本渲染", () => {
  const previous = globalThis.katex;
  globalThis.katex = { renderToString: (source, options) => `<math data-display="${options.displayMode}">${source}</math>` };
  try {
    assert.equal(formulaHtml("指数 $a^{m/n}$"), '指数 <math data-display="false">a^{m/n}</math>');
    assert.equal(formulaHtml("$$\\frac{a}{b}$$"), '<math data-display="true">\\frac{a}{b}</math>');
  } finally {
    if (previous) globalThis.katex = previous;
    else delete globalThis.katex;
  }
});

test("单文件网页嵌着数据、KaTeX 和检查代码，不再引用外部文件", () => {
  const html = singleHtml(sample());
  assert.ok(html.includes("window.KMAP_DATA = {"));
  assert.ok(html.includes("function normalize("));
  assert.ok(html.includes("function formulaRuns("));
  assert.ok(html.includes("data-kmap-katex"));
  assert.ok(html.includes("data:font/woff2;base64,"));
  assert.ok(!html.includes("url(fonts/"));
  assert.ok(!/(?:^|\n)import .* from|<script\s+src=/m.test(html));
  assert.ok(html.includes("力学小楼"));
});

test("构建时拼音首字母索引嵌入 HTML 数据，搜索命中", () => {
  const md = readFileSync(join(dirname(SAMPLE), "sample.md"), "utf8");
  const r = convert(md);
  assert.deepEqual(r.errors, []);
  const html = singleHtml(r.raw);
  assert.ok(html.includes('"_pyN"'));
  const n21 = r.raw.nodes.find(n => n.id === "2.1");
  assert.ok(n21._pyN, "节点 2.1 应有 _pyN 字段");
  assert.ok(n21._pyN.includes("nddedl"), `"牛顿第二定律"的 _pyN 应含 nddedl，实际: ${n21._pyN}`);
  const n31 = r.raw.nodes.find(n => n.id === "3.1");
  assert.ok(n31._pyN.includes("dndl"), `"动能定理"的 _pyN 应含 dndl，实际: ${n31._pyN}`);
});

test("拼音字典覆盖历次报告的反例", () => {
  assert.equal(pinyinInitials("杂交"), "zj");
  assert.equal(pinyinInitials("杂合子"), "zhz");
  assert.equal(pinyinInitials("杂质"), "zz");
  assert.equal(pinyinInitials("然"), "r");
  assert.equal(pinyinInitials("热"), "r");
  assert.equal(pinyinInitials("人"), "r");
  assert.equal(pinyinInitials("燃烧"), "rs");
  assert.equal(pinyinInitials("在"), "z");
  assert.equal(pinyinInitials("考"), "k");
  assert.equal(pinyinInitials("热力学"), "rlx");
  assert.equal(pinyinInitials("哈勃定律"), "hbdl");
  assert.equal(pinyinInitials("卡尔文循环"), "kewxh");
  assert.equal(pinyinInitials("搭配"), "dp");
});

test("富方法的标签、例子、易错支持行内和缩进两种写法", () => {
  const md = `# 测试
## 页面设置
- 标题：测试
| 区域 | 颜色 |
|---|---|
| A | #607D8B |
## 第 0 层　底层：基础
### 0.1 知识一
- 区域：A
- 是什么：第一个知识
### 0.2 知识二
- 区域：A
- 是什么：第二个知识
- 从哪来：⇐用到 0.1
## 思想方法
### 方法一
- 说明：测试方法
- 出现在：0.1、0.2
- 标签：做法A；做法B
  - 做法C
- 例子：行内例子一
  - 缩进例子二
- 易错：行内陷阱一；行内陷阱二
  - 缩进陷阱三
`;
  const r = convert(md);
  assert.deepEqual(r.errors, []);
  const d = normalize(r.raw).data;
  const m = d.methods[0];
  assert.equal(m.name, "方法一");
  assert.deepEqual(m.labels, ["做法A", "做法B", "做法C"], "标签应合并行内分号分割和缩进列表");
  assert.deepEqual(m.examples, ["行内例子一", "缩进例子二"], "例子应合并行内和缩进");
  assert.deepEqual(m.pitfalls, ["行内陷阱一", "行内陷阱二", "缩进陷阱三"], "易错应合并行内分号分割和缩进");
});
