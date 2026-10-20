// 检查并整理一份知识数据：编号唯一、引用存在、依赖不往高层指、无环、枚举值合法。
// tools/build.mjs 生成网页时和网页打开时都用这一份，保证两处的理解一致。

const KINDS = { 推出: 0, 前提: 1, 推广: 1, 特例: 1, 用到: 2, 对照: 3 };
const TYPES = ["起点", "结论", "中间步"];
const LISTS = ["tags", "conditions", "points", "counterexamples", "notes"];
const PALETTE = ["#607D8B", "#1565C0", "#2E7D32", "#EF6C00", "#C2185B", "#5E35B1", "#00838F", "#6D4C41"];

const str = v => (v === undefined || v === null ? "" : String(v));
const lists = o => {
  const out = {};
  for (const f of LISTS) if (Array.isArray(o[f]) && o[f].length) out[f] = o[f];
  return out;
};

/** 检查并整理：返回 { data, errors, warns }；data 是页面使用的形状（多了 edges、regionColor） */
export function normalize(raw) {
  const errors = [], warns = [];
  const title = raw.title || "知识大厦";
  const idp = raw.idPattern || "\\d+\\.\\d{1,2}";
  const idRe = new RegExp(`^(?:${idp})$`);

  const layers = [...(raw.layers || [])].sort((a, b) => a.L - b.L).map(l => ({ L: l.L, name: l.name, sub: l.sub || "" }));
  const layerIds = new Set(layers.map(l => l.L));
  if (!layers.length) errors.push("layers 为空：至少要有一层");

  const regions = (raw.regions || []).map((r, i) => ({
    r: r.name, color: r.color || PALETTE[i % PALETTE.length], desc: r.desc || "",
    ...(r.anchor !== undefined ? { anchor: r.anchor } : {}),
  }));
  const regionNames = new Set(regions.map(r => r.r));
  if (!regions.length) errors.push("regions 为空：至少要有一个区域");

  const nodes = [], seen = new Set();
  for (const n of raw.nodes || []) {
    const nid = str(n.id), where = `知识 ${nid || "(无编号)"}`;
    for (const f of ["id", "name", "layer", "region", "what"])
      if (n[f] === undefined || n[f] === null || n[f] === "") errors.push(`${where}：缺少 ${f}`);
    if (seen.has(nid)) errors.push(`${where}：编号重复`);
    seen.add(nid);
    if (!idRe.test(nid)) warns.push(`${where}：编号不符合 idPattern ${idp}，正文里的（${nid}）不会变成链接`);
    if (!layerIds.has(n.layer)) errors.push(`${where}：layer=${n.layer} 不在 layers 里`);
    if (!regionNames.has(n.region)) errors.push(`${where}：region=${n.region} 不在 regions 里`);
    const deps = [];
    for (const d0 of n.deps || []) {
      const d = typeof d0 === "string" ? { id: d0 } : d0;
      const kind = d.kind || "用到";
      if (!(kind in KINDS)) errors.push(`${where}：依赖 ${d.id} 的 kind=${kind}，只能是 ${Object.keys(KINDS).join("/")}`);
      const dep = { id: str(d.id), kind };
      for (const k of ["how", "method", "condition", "detail"]) if (d[k]) dep[k] = d[k];
      if (d.main) dep.main = true;
      deps.push(dep);
    }
    if (n.type && !TYPES.includes(n.type)) errors.push(`${where}：type=${n.type}，只能是 ${TYPES.join("/")}`);
    if (n.importance !== undefined && ![0, 1, 2, 3].includes(n.importance)) errors.push(`${where}：importance 只能是 0～3`);
    for (const f of LISTS) {
      const v = n[f];
      if (v !== undefined && !(Array.isArray(v) && v.every(x => typeof x === "string"))) errors.push(`${where}：${f} 要写成字符串数组`);
    }
    nodes.push({
      id: nid, name: n.name || "", full: n.full || n.name || "", one: n.one || (n.what || "").slice(0, 16),
      stage: n.stage || "", layer: n.layer, region: n.region,
      what: n.what || "", from: n.from || "", next: n.next || "", use: n.use || "", eg: n.eg || "", upto: n.upto || "",
      deps, ...lists(n),
      ...(n.type ? { type: n.type } : {}), ...(n.importance ? { importance: n.importance } : {}),
      ...(n.group ? { group: str(n.group) } : {}),
      ...(n._pyN ? { _pyN: n._pyN } : {}), ...(n._pyX ? { _pyX: n._pyX } : {}),
    });
  }

  const by = {};
  nodes.forEach(n => (by[n.id] = n));
  const edges = new Map(), main = new Set();
  for (const n of nodes) for (const d of n.deps) {
    if (!by[d.id]) { errors.push(`知识 ${n.id}：依赖的 ${d.id} 不存在`); continue; }
    if (d.id === n.id) { errors.push(`知识 ${n.id}：依赖了自己`); continue; }
    if (by[d.id].layer > n.layer)
      errors.push(`知识 ${n.id}（第 ${n.layer} 层）依赖了更高层的 ${d.id}（第 ${by[d.id].layer} 层）：依赖只能指向同层或更低层`);
    const e = d.id + ">" + n.id;
    if (d.main) main.add(e);
    const old = edges.get(e);
    if (old === undefined || KINDS[d.kind] < KINDS[old]) edges.set(e, d.kind);
  }

  // 有环就没法“从地基往上推”
  const ch = {};
  for (const e of edges.keys()) { const [a, b] = e.split(">"); (ch[a] = ch[a] || []).push(b); }
  const state = {};
  const dfs = (x, path) => {
    state[x] = 1;
    for (const y of ch[x] || []) {
      if (state[y] === 1) errors.push("依赖成环：" + [...path, x, y].join(" → "));
      else if (!state[y]) dfs(y, [...path, x]);
    }
    state[x] = 2;
  };
  for (const x of Object.keys(by)) if (!state[x]) dfs(x, []);

  const chains = [];
  for (const c of raw.chains || []) {
    const paths = (c.paths || [c.path || []]).filter(p => p.length).map(p => p.map(String));
    for (const p of paths) {
      // 先逐个查编号：只有一个节点的主干没有“相邻两步”，也要查到
      const missing = p.filter(i => !by[i]);
      missing.forEach(i => errors.push(`主干「${c.name}」：${i} 不存在`));
      if (missing.length) continue;
      for (let i = 1; i < p.length; i++)
        if (!edges.has(p[i - 1] + ">" + p[i])) warns.push(`主干「${c.name}」：${p[i - 1]}→${p[i]} 没有对应的依赖，播放时这一步没有“怎么推的”`);
    }
    if (paths.length) chains.push({ name: c.name, paths });
  }

  // 房间（groups）：把同一类的几个知识点框在一起，卡片上显示房间名前缀；房间本身有整体讲解
  const groups = [], gids = new Set();
  for (const g of raw.groups || []) {
    const gid = str(g.id);
    if (!gid || !g.name) { errors.push(`房间 ${gid || "(无编号)"}：缺少 id 或 name`); continue; }
    if (gids.has(gid) || by[gid]) errors.push(`房间 ${gid}：编号重复（和别的房间或知识重名）`);
    gids.add(gid);
    groups.push({
      id: gid, name: g.name, full: g.full || g.name, stage: g.stage || "", one: g.one || "",
      what: g.what || "", from: g.from || "", next: g.next || "", use: g.use || "", eg: g.eg || "", upto: g.upto || "",
      ...lists(g),
      ...(g._pyN ? { _pyN: g._pyN } : {}), ...(g._pyX ? { _pyX: g._pyX } : {}),
    });
  }
  const members = {};
  for (const n of nodes) if (n.group) {
    if (!gids.has(n.group)) errors.push(`知识 ${n.id}：group=${n.group} 不在 groups 里`);
    (members[n.group] = members[n.group] || []).push(n);
  }
  for (const g of groups) {
    const ms = members[g.id] || [];
    if (!ms.length) warns.push(`房间 ${g.id}「${g.name}」里没有知识点`);
    else if (new Set(ms.map(m => m.layer)).size > 1) errors.push(`房间 ${g.id}「${g.name}」的知识点不在同一层：同一个房间要放在同一楼层`);
  }

  const featured = (raw.featured || []).map(String).filter(i => by[i]);
  const methods = [];
  for (const m of raw.methods || []) {
    const ids = (m.nodes || []).map(String);
    ids.forEach(i => { if (!by[i]) errors.push(`方法「${m.name}」：${i} 不存在`); });
    methods.push({
      name: m.name, desc: m.desc || "", nodes: ids.filter(i => by[i]),
      ...(m.labels && m.labels.length ? {labels: m.labels} : {}),
      ...(m.direction ? {direction: m.direction} : {}),
      ...(m.basis ? {basis: m.basis} : {}),
      ...(m.signal ? {signal: m.signal} : {}),
      ...(m.examples && m.examples.length ? {examples: m.examples} : {}),
      ...(m.pitfalls && m.pitfalls.length ? {pitfalls: m.pitfalls} : {}),
    });
  }
  const mnames = new Set(methods.map(m => m.name));
  for (const n of nodes) for (const d of n.deps)
    if (d.method && methods.length && !mnames.has(d.method))
      warns.push(`知识 ${n.id}：依赖 ${d.id} 的方法「${d.method}」不在 methods 里（页面照常显示，只是方法列表里没有它）`);

  // 工具箱
  const toolbox = [];
  for (const t of raw.toolbox || []) {
    const usedBy = (t.usedBy || []).map(String);
    usedBy.forEach(i => { if (!by[i]) warns.push(`工具箱「${t.name}」：${i} 不存在`); });
    toolbox.push({name: t.name, ...(t.formula ? {formula: t.formula} : {}), ...(t.source ? {source: t.source} : {}), usedBy: usedBy.filter(i => by[i]), ...(t.notes ? {notes: t.notes} : {})});
  }

  // 题型入口
  const entryList = [];
  for (const e of raw.entries || []) {
    const targets = (e.targets || []).map(t => {
      const ns = (t.nodes || []).map(String);
      ns.forEach(i => { if (!by[i]) warns.push(`题型入口「${e.pattern}」的「${t.case}」：${i} 不存在`); });
      return {case: t.case || "", nodes: ns.filter(i => by[i]), ...(t.hint ? {hint: t.hint} : {})};
    });
    entryList.push({pattern: e.pattern, targets, ...(e.tags ? {tags: e.tags} : {})});
  }

  const data = {
    title, idPattern: idp, featured,
    ...(raw.storageKey ? { storageKey: raw.storageKey } : {}),
    ...(raw.stages ? { stages: raw.stages } : {}),
    layers, regions, regionColor: Object.fromEntries(regions.map(r => [r.r, r.color])),
    nodes,
    edges: [...edges].map(([e, k]) => { const [a, b] = e.split(">"); return { a, b, k, ...(main.has(e) ? { main: true } : {}) }; }),
    chains, methods, groups, toolbox, entries: entryList,
  };
  return { data, errors, warns };
}
