// 把一份按《md格式》写的知识清单转成知识数据（RawData）。格式说明见 .claude/skills/knowledge-map-web/SKILL.md。
//
//   ## 页面设置                      标题、编号写法、学段、推荐、保存键；区域表
//   ## 主干链                        1. **名称** 下面每行一条路径：编号用 → 或 ⇢ 连接，"/" 从前一个编号分出支路
//   ## 第 N 层　楼层名：一句说明      楼层
//   ### 编号 名称　〔学段〕            分组；没有知识点时它本身就是一张卡片
//   #### 编号 名称                    分组里的知识点（卡片，带分组名前缀）
//   ## 思想方法                      旧格式：- **名称**：说明｜出现在：编号  新格式：### 方法名 + fields
//   ## 工具箱                        - **名称**：公式  缩进 - 来自/用在/说明
//   ## 题型入口                      ### 题型名  - 分类名：编号（提示）
//
// 字段写成"- 字段：内容"；要点、注释这类列表可以一行用"；"隔开，也可以在下面缩进写"  - 一条"。
// LaTeX 块公式可以写成"- 标志：$$"，后面原样写公式，直到独立一行的"$$"。

const KINDS = ["推出", "用到", "推广", "特例", "前提", "对照"];
const LIST_FIELDS = { 要点: "points", 注释: "notes", 条件: "conditions", 反例: "counterexamples", 标签: "tags" };
const TEXT_FIELDS = { 是什么: "what", 后来发展到: "next", 用在哪: "use", 例子: "eg", 往上通向: "upto" };
const KNOWN = new Set([
  "短名", "区域", "标志", "从哪来", "依赖", "类型", "重要度",
  "说明", "方向", "依据", "信号", "出现在", "易错",
  ...Object.keys(LIST_FIELDS), ...Object.keys(TEXT_FIELDS),
]);
const WORDS = { 推出: "由 ", 用到: "用到 ", 推广: "推广自 ", 特例: "是这个的特例：", 前提: "前提是 ", 对照: "对照 " };

/** 读一段里的"- 字段：内容"、字段内的 $$ 块公式，以及下面缩进的"  - 条目" */
function fields(lines, start, where, warns) {
  const f = {}, lists = {}, blocks = {};
  let cur = null, mathField = null, mathStart = 0;
  lines.forEach((ln, i) => {
    if (mathField) {
      f[mathField] += "\n" + ln;
      if (ln.trim() === "$$") mathField = null;
      return;
    }
    const m = ln.match(/^- ([^：:\s]{1,8})[：:]\s*(.*)$/);
    if (m) {
      cur = m[1];
      if (!KNOWN.has(cur)) warns.push(`第 ${start + i + 1} 行（${where}）：不认识的字段"${cur}"，没有放进页面`);
      f[cur] = m[2].trim(); lists[cur] = []; blocks[cur] = [];
      if (f[cur] === "$$") { mathField = cur; mathStart = start + i + 1; }
      return;
    }
    const s = ln.match(/^\s{2,}[-*] (.*)$/);
    if (s && cur) { lists[cur].push(s[1].trim()); blocks[cur].push(ln); return; }
    // 所有缩进行都收集到 blocks（含非 - 开头的续行）
    if (cur && /^\s{2,}/.test(ln)) { blocks[cur].push(ln); return; }
  });
  if (mathField) warns.push(`第 ${mathStart} 行（${where}）：字段"${mathField}"的块公式缺少结束 $$`);
  const marker = f["标志"] || "";
  if (!marker.includes("$") && /[=<>≤≥⇒⇔⟺∫√Σ∑^_/₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹∈∉⊆∩∪∀∃πΔαβλΩ]/u.test(marker)) {
    warns.push(`第 ${start + 1} 行（${where}）：标志含公式但没有使用 $...$ LaTeX 定界符`);
  }
  return { f, lists, blocks };
}

/** md 原稿 → { raw, errors, warns }；raw 是 JSON 文件的形状 */
export function parseMd(text) {
  const errors = [], warns = [];
  const lines = text.replace(/\r\n?/g, "\n").split("\n");

  // ── 分节：## 二级标题 ──
  const secs = [];
  lines.forEach((ln, i) => { if (/^## /.test(ln)) secs.push({ title: ln.slice(3).trim(), start: i, end: lines.length }); });
  secs.forEach((s, i) => { if (secs[i + 1]) s.end = secs[i + 1].start; });
  const sec = re => secs.find(s => re.test(s.title));
  const body = s => (s ? lines.slice(s.start + 1, s.end) : []);

  // ── 页面设置 ──
  const set = sec(/^页面设置/), S = fields(body(set), set ? set.start + 1 : 0, "页面设置", []).f;
  const h1 = lines.find(l => /^# /.test(l));
  const IDP = S["编号写法"] || "\\d+\\.\\d{1,2}(?:\\.\\d{1,2})?";
  const ID = `(?:${IDP})`;
  const regions = body(set).filter(l => /^\|/.test(l) && !/^\|\s*-/.test(l)).map(l => l.split("|").slice(1, -1).map(c => c.trim()))
    .filter(c => c[0] && c[0] !== "区域")
    .map(c => ({ name: c[0], ...(c[1] ? { color: c[1] } : {}), ...(c[2] && !isNaN(+c[2]) ? { anchor: +c[2] } : {}), ...(c[3] ? { desc: c[3] } : {}) }));
  if (!set) errors.push(`没有“## 页面设置”一节：至少要写标题和区域表`);

  // ── 楼层、分组、知识点 ──
  const layers = [];
  const rooms = [];
  for (const s of secs) {
    const lm = s.title.match(/^第\s*(\d+)\s*层[　\s]+([^：:]+)(?:[：:](.*))?$/);
    if (!lm) continue;
    const L = +lm[1];
    layers.push({ L, name: lm[2].trim(), sub: (lm[3] || "").trim() });
    let room = null, cur = null, buf = [], bufStart = 0;
    const flush = () => {
      if (!cur) return;
      const { f, lists, blocks } = fields(buf, bufStart, cur.id, warns);
      cur.f = f; cur.lists = lists; cur.blocks = blocks;
    };
    for (let i = s.start + 1; i < s.end; i++) {
      const ln = lines[i];
      const rm = ln.match(new RegExp(`^### (${ID}) (.+?)(?:[　\\s]+〔(.*?)〕)?\\s*$`));
      const pm = ln.match(new RegExp(`^#### (${ID}) (.+?)\\s*$`));
      if (rm || pm) { flush(); buf = []; bufStart = i + 1; }
      if (rm) { room = { id: rm[1], name: rm[2].trim(), stage: rm[3] || "", f: {}, lists: {}, line: i + 1, layer: L, points: [] }; rooms.push(room); cur = room; continue; }
      if (pm) {
        if (!room) { errors.push(`第 ${i + 1} 行：知识点 ${pm[1]} 前面没有分组（### 编号 名称）`); cur = null; continue; }
        cur = { id: pm[1], name: pm[2].trim(), stage: room.stage, f: {}, lists: {}, line: i + 1 }; room.points.push(cur); continue;
      }
      if (/^#{1,4} /.test(ln) && cur) { flush(); cur = null; continue; }
      if (/^---\s*$/.test(ln)) { flush(); cur = null; continue; }
      if (cur) buf.push(ln);
    }
    flush();
  }

  // ── 名称表：用来把正文里的编号写成"名称（编号）" ──
  const NAME = {}, FULL = {};
  for (const r of rooms) { NAME[r.id] = r.f["短名"] || r.name; FULL[r.id] = r.name; r.points.forEach(p => { NAME[p.id] = p.name; FULL[p.id] = p.name; }); }
  const idRe = flags => new RegExp(`(?<![\\d.])(${ID})(?![\\d])(?!\\.\\d)`, flags);

  /** "⇐推出 3.1"改成"由 函数（3.1）" */
  const plain = t => t.split(/(；)/).map(seg => {
    const k = seg.indexOf("⇐");
    seg = seg.replace(new RegExp(`(?<![\\d.（、])(${ID})(?![\\d）])(?!\\.\\d)(\\s*[^\\s、，；。（）]*)`, "g"), (all, nid, after, off) => {
      if (!(nid in NAME)) return all;
      const a = after.trimStart();
      for (const w of [FULL[nid], NAME[nid]]) if (a.startsWith(w)) return `${w}（${nid}）${a.slice(w.length)}`;
      if (k >= 0 && k < off) return `${NAME[nid]}（${nid}）${after}`;
      return all;
    });
    return seg.replace(/⇐(推出|用到|推广|特例|前提|对照)\s*/g, (_, w) => WORDS[w]);
  }).join("");

  /** 扫描文本里括号外层的编号，作为"对照"加入 out（跳过全角括号内的引用） */
  const scanOuterIds = (text, self, out) => {
    for (const sub of text.split(/[；;]/)) {
      let cleaned = "", depth = 0;
      for (let i = 0; i < sub.length; i++) {
        if (sub[i] === "\u{FF08}") { depth++; cleaned += " "; }
        else if (sub[i] === "\u{FF09}") { depth--; cleaned += " "; }
        else cleaned += depth === 0 ? sub[i] : " ";
      }
      for (const m of cleaned.matchAll(idRe("g"))) {
        const id = m[1];
        if (id === self || out.some(d => d.id === id)) continue;
        out.push({ id, kind: "对照" });
      }
    }
  };

  /** 多行格式依赖解析：从 blocks["依赖"] 中解析结构化的依赖列表 */
  const depsMultiLine = (blockLines) => {
    const out = [];
    let current = null;
    for (const ln of blockLines) {
      const stripped = ln.trim();
      // 新的来源块：  - 来源：ID
      const srcMatch = stripped.replace(/^[-*]\s*/, '').match(/^来源[：:]\s*(.+)$/);
      if (srcMatch) {
        if (current) out.push(current);
        const rawId = srcMatch[1].trim();
        const idMatch = rawId.match(idRe(""));
        current = { id: idMatch ? idMatch[1] : rawId, kind: "用到" };
        continue;
      }
      if (!current) continue;
      // 种类
      const kindMatch = stripped.match(/^种类[：:]\s*(.+)$/);
      if (kindMatch) { const k = kindMatch[1].trim(); if (KINDS.includes(k)) current.kind = k; continue; }
      // 方法
      const methodMatch = stripped.match(/^方法[：:]\s*(.+)$/);
      if (methodMatch) { current.method = methodMatch[1].trim(); continue; }
      // 条件
      const condMatch = stripped.match(/^条件[：:]\s*(.+)$/);
      if (condMatch) { current.condition = condMatch[1].trim(); continue; }
      // 步骤标题行（忽略）
      if (/^步骤[：:]/.test(stripped)) continue;
      // 编号步骤行：1. xxx 或 ① xxx
      const stepMatch = stripped.match(/^(?:\d+[.、]|[①-⑳])\s*(.+)$/);
      if (stepMatch) {
        current.how = current.how ? current.how + "；" + stepMatch[1].trim() : stepMatch[1].trim();
        continue;
      }
    }
    if (current) out.push(current);
    return out;
  };

  /** "依赖"→ 依赖列表：⇐kind 段取第一个编号及其 how/method；段内和无 ⇐ 段里的外层编号作为对照 */
  const deps = (src, self) => {
    const out = [];
    const segs = src.split(/(?=⇐)/);
    for (const seg of segs) {
      const kind = KINDS.find(k => seg.includes("⇐" + k)) || (seg.includes("⇐") ? "对照" : null);
      if (kind) {
        const kindTag = "⇐" + kind;
        const kindIdx = seg.indexOf(kindTag);
        const afterKind = seg.slice(kindIdx + kindTag.length);
        const m = afterKind.match(idRe(""));
        if (!m) continue;
        const id = m[1];
        if (id === self || out.some(d => d.id === id)) continue;
        const afterId = afterKind.slice(m.index + id.length);
        let how = "", method = "", condition = "";
        let pos = 0;
        while (pos < afterId.length && /\s/.test(afterId[pos])) pos++;
        if (afterId[pos] === "\u{FF08}") {
          let depth = 1, start = pos + 1;
          pos++;
          while (pos < afterId.length && depth > 0) {
            if (afterId[pos] === "\u{FF08}") depth++;
            else if (afterId[pos] === "\u{FF09}") { depth--; if (depth === 0) break; }
            pos++;
          }
          how = afterId.slice(start, pos).trim();
          pos++;
        }
        while (pos < afterId.length && /\s/.test(afterId[pos])) pos++;
        const mMatch = afterId.slice(pos).match(/^【([^】]*)】/);
        if (mMatch) { method = mMatch[1]; pos += mMatch[0].length; }
        while (pos < afterId.length && /\s/.test(afterId[pos])) pos++;
        const cMatch = afterId.slice(pos).match(/^〔([^〕]*)〕/);
        if (cMatch) { condition = cMatch[1]; }
        out.push({ id, kind, ...(how ? { how } : {}), ...(method ? { method } : {}), ...(condition ? { condition } : {}) });
        scanOuterIds(afterId.slice(pos), self, out);
      } else {
        scanOuterIds(seg, self, out);
      }
    }
    return out;
  };
  const list = (b, name) => {
    const inline = (b.f[name] || "").split("；").map(x => x.trim()).filter(Boolean);
    return [...inline, ...(b.lists[name] || [])];
  };
  const common = b => {
    const o = {};
    for (const [k, v] of Object.entries(TEXT_FIELDS)) if (b.f[k]) o[v] = b.f[k];
    if (b.f["从哪来"]) o.from = plain(b.f["从哪来"]);
    for (const [k, v] of Object.entries(LIST_FIELDS)) { const l = list(b, k); if (l.length) o[v] = k === "要点" || k === "注释" ? l.map(plain) : l; }
    if (b.f["类型"]) o.type = b.f["类型"];
    if (b.f["重要度"]) o.importance = +b.f["重要度"];
    return o;
  };

  const parseDeps = (entity) => {
    const blk = (entity.blocks && entity.blocks["依赖"]) || [];
    const fromBlk = (entity.blocks && entity.blocks["从哪来"]) || [];
    // 检查旧格式
    const inlineDep = (entity.f["依赖"] || "").trim();
    const inlineFrom = (entity.f["从哪来"] || "").trim();
    if (inlineDep && inlineDep.includes("⇐")) {
      errors.push(`${entity.id}：依赖使用了旧的单行格式，请转为多行格式（来源/种类/方法/步骤）`);
    }
    if (inlineFrom && inlineFrom.includes("⇐")) {
      errors.push(`${entity.id}：从哪来使用了旧的单行格式，请转为多行依赖格式（来源/种类/方法/步骤）`);
    }
    // 合并依赖和从哪来的多行块
    const allBlk = [...blk, ...fromBlk];
    return depsMultiLine(allBlk);
  };

  const nodes = [], groups = [];
  for (const r of rooms) {
    const region = r.f["区域"], one = r.f["标志"] || "";
    if (!region) errors.push(`第 ${r.line} 行：分组 ${r.id} 没写"区域"`);
    if (!r.points.length) {
      nodes.push({ id: r.id, name: NAME[r.id], full: r.name, one, stage: r.stage, layer: r.layer, region,
        what: r.f["是什么"] || "", ...common(r), deps: parseDeps(r) });
      continue;
    }
    groups.push({ id: r.id, name: NAME[r.id], full: r.name, stage: r.stage, one, ...common(r) });
    for (const p of r.points) {
      if (p.f["区域"] && p.f["区域"] !== region) warns.push(`第 ${p.line} 行：知识点 ${p.id} 的区域和分组不同，按分组的"${region}"算`);
      nodes.push({ id: p.id, name: p.name, full: p.name, one: p.f["标志"] || "", stage: r.stage, layer: r.layer, region, group: r.id,
        what: p.f["是什么"] || "", ...common(p), deps: parseDeps(p) });
    }
  }

  // ── 主干链 ──
  const chains = [];
  let ch = null;
  for (const ln of body(sec(/^主干/))) {
    const t = ln.match(/^\d+\.\s+\*\*(.+?)\*\*/);
    if (t) { ch = { name: t[1].replace(/这条链$/, ""), paths: [] }; chains.push(ch); continue; }
    if (!ch || !/^\s+\S/.test(ln)) continue;
    const toks = [...ln.matchAll(new RegExp(`(→|⇢|/)|(?<![\\d.])(${ID})(?![\\d])(?!\\.\\d)`, "g"))];
    let path = [], base = null, prev = null;
    for (const m of toks) {
      if (m[1] === "/") { ch.paths.push(path); path = base ? [base] : []; continue; }
      if (m[1]) { base = prev; continue; }
      path.push(m[2]); prev = m[2];
    }
    if (path.length) ch.paths.push(path);
  }

  // ── 思想方法（新旧格式混合）──
  const methodSec = sec(/^思想方法/);
  const methods = [];
  if (methodSec) {
    const mBody = body(methodSec);
    let mCur = null, mBuf = [], mBufStart = 0;
    const flushMethod = () => {
      if (!mCur) return;
      const { f, lists: mLists } = fields(mBuf, mBufStart, mCur.name, warns);
      mCur.desc = f["说明"] || "";
      mCur.direction = f["方向"] || "";
      mCur.basis = f["依据"] || "";
      mCur.signal = f["信号"] || "";
      const nodesStr = f["出现在"] || "";
      mCur.nodes = [...nodesStr.matchAll(idRe("g"))].map(x => x[1]);
      const merge = name => { const inline = (f[name] || "").split("；").map(x => x.trim()).filter(Boolean); return [...inline, ...(mLists[name] || [])]; };
      const labelList = merge("标签");
      if (labelList.length) mCur.labels = labelList;
      const exList = merge("例子");
      if (exList.length) mCur.examples = exList;
      const pitList = merge("易错");
      if (pitList.length) mCur.pitfalls = pitList;
      methods.push(mCur);
    };
    for (let i = 0; i < mBody.length; i++) {
      const ln = mBody[i];
      const rm = ln.match(/^### (.+)$/);
      if (rm) { flushMethod(); mCur = { name: rm[1].trim() }; mBuf = []; mBufStart = (methodSec.start + 1) + i + 1; continue; }
      const om = ln.match(/^- \*\*(.+?)\*\*：(.+?)｜出现在：(.+)$/);
      if (om) { flushMethod(); mCur = null; methods.push({ name: om[1], desc: om[2], nodes: [...om[3].matchAll(idRe("g"))].map(x => x[1]) }); continue; }
      if (mCur) { mBuf.push(ln); continue; }
    }
    flushMethod();
  }

  // ── 工具箱 ──
  const toolbox = [];
  const toolSec = sec(/^工具箱/);
  if (toolSec) {
    let tool = null;
    for (const ln of body(toolSec)) {
      const tm = ln.match(/^- \*\*(.+?)\*\*[：:]\s*(.*)$/);
      if (tm) { tool = { name: tm[1], formula: tm[2].trim() }; toolbox.push(tool); continue; }
      if (!tool) continue;
      const sub = ln.match(/^\s{2,}[-*] ([^：:]+)[：:]\s*(.*)$/);
      if (sub) {
        const key = sub[1].trim(), val = sub[2].trim();
        if (key === "来自") tool.source = val;
        else if (key === "用在") tool.usedBy = [...val.matchAll(idRe("g"))].map(x => x[1]);
        else if (key === "说明") tool.notes = val;
      }
    }
  }

  // ── 题型入口 ──
  const entries = [];
  const entrySec = sec(/^题型入口/);
  if (entrySec) {
    let entry = null;
    for (const ln of body(entrySec)) {
      const em = ln.match(/^### (.+)$/);
      if (em) { entry = { pattern: em[1].trim(), targets: [] }; entries.push(entry); continue; }
      if (!entry) continue;
      const tm = ln.match(/^- ([^：:]+)[：:]\s*(.*)$/);
      if (tm) {
        const caseName = tm[1].trim(), rest = tm[2].trim();
        const nodeIds = [...rest.matchAll(idRe("g"))].map(x => x[1]);
        // 匹配成对的全角括号提取 hint（支持嵌套）
        let hint = "";
        const pStart = rest.indexOf("\u{FF08}");
        if (pStart >= 0) {
          let depth = 1, j = pStart + 1;
          while (j < rest.length && depth > 0) {
            if (rest[j] === "\u{FF08}") depth++;
            else if (rest[j] === "\u{FF09}") { depth--; if (depth === 0) break; }
            j++;
          }
          hint = rest.slice(pStart + 1, j).trim();
        }
        entry.targets.push({ case: caseName, nodes: nodeIds, ...(hint ? { hint } : {}) });
      }
    }
  }

  const raw = {
    title: S["标题"] || (h1 ? h1.slice(2).trim() : "知识大厦"), idPattern: IDP,
    ...(S["学段"] ? { stages: S["学段"].split(/[、，,]/).map(x => x.trim()).filter(Boolean) } : {}),
    ...(S["推荐"] ? { featured: [...S["推荐"].matchAll(idRe("g"))].map(x => x[1]) } : {}),
    ...(S["保存键"] ? { storageKey: S["保存键"] } : {}),
    layers, regions, nodes, groups, chains: chains.filter(c => c.paths.length), methods,
    ...(toolbox.length ? { toolbox } : {}),
    ...(entries.length ? { entries } : {}),
  };
  if (!layers.length) errors.push(`没有楼层：要用"## 第 0 层　楼层名"这样的标题分层`);
  return { raw, errors, warns };
}
