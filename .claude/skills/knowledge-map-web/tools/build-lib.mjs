// 生成单文件网页用的公共部分：读原稿（md 或 JSON）、检查、把数据和检查代码嵌进网页模板。build.mjs 和 serve.mjs 共用。
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { parseMd } from "../lib/md.js";
import { normalize } from "../lib/normalize.js";
import { pinyinInitials } from "../lib/pinyin-dict.js";

export const SKILL = join(dirname(fileURLToPath(import.meta.url)), "..");

function katexHead() {
  const root = join(SKILL, "vendor", "katex");
  let css = readFileSync(join(root, "katex.min.css"), "utf8");
  css = css.replace(/url\(fonts\/([^)]+\.woff2)\)/g, (_, name) => {
    const encoded = readFileSync(join(root, "fonts", name)).toString("base64");
    return `url(data:font/woff2;base64,${encoded})`;
  });
  css = css.replace(/,url\(fonts\/[^)]+\.(?:woff|ttf)\) format\("[^"]+"\)/g, "");
  const js = readFileSync(join(root, "katex.min.js"), "utf8").replace(/<\/script/gi, "<\\/script");
  return `<style data-kmap-katex>${css}</style>\n<script data-kmap-katex>${js}</script>\n`;
}

/** 读一份原稿：.md 按 md 格式解析，.json 直接读；再用页面同一套规则检查。返回 { raw, errors, warns, summary } */
export function load(path) {
  let raw, errors = [], warns = [];
  if (/\.json$/i.test(path)) {
    try { raw = JSON.parse(readFileSync(path, "utf8")); } catch (e) { return { raw: null, errors: [`读不了 ${path}：${e.message}`], warns, summary: "" }; }
  } else {
    const p = parseMd(readFileSync(path, "utf8"));
    raw = p.raw; errors = p.errors; warns = p.warns;
  }
  const n = normalize(raw), d = n.data;
  // 构建时为每个节点和分组注入拼音首字母索引，供搜索用
  // _pyN: 名称的拼音（高优先搜索）；_pyX: 标志和标签的拼音（低优先补充）
  for (const node of raw.nodes || []) {
    node._pyN = pinyinInitials(node.name + (node.full && node.full !== node.name ? node.full : ''));
    node._pyX = pinyinInitials((node.one || '') + (node.tags || []).join(''));
  }
  for (const group of raw.groups || []) {
    group._pyN = pinyinInitials(group.name + (group.full && group.full !== group.name ? group.full : ''));
    group._pyX = pinyinInitials(group.one || '');
  }
  return {
    raw, errors: [...errors, ...n.errors], warns: [...warns, ...n.warns],
    summary: `知识 ${d.nodes.length}，分组 ${d.groups.length}，关系 ${d.edges.length}，楼层 ${d.layers.length}，主干 ${d.chains.length}，方法 ${d.methods.length}`,
  };
}

/** 单文件网页：模板里的 import 换成嵌入的数据和 lib/normalize.js 的代码，双击就能打开，不依赖别的文件 */
export function singleHtml(raw, extraHead = "") {
  const page = readFileSync(join(SKILL, "template.html"), "utf8");
  const normalizeLib = readFileSync(join(SKILL, "lib", "normalize.js"), "utf8").replace(/^export /gm, "");
  const formulaLib = readFileSync(join(SKILL, "lib", "formula.js"), "utf8").replace(/^export /gm, "");
  const normalizeImport = 'import { normalize } from "./lib/normalize.js";\n';
  const formulaImport = 'import { formulaRuns, formulaHtml } from "./lib/formula.js";\n';
  if (!page.includes(normalizeImport) || !page.includes(formulaImport)) throw new Error("template.html 里找不到 lib 的 import");
  const blob = JSON.stringify(raw).replace(/</g, "\\u003c");
  return page
    .replace(normalizeImport, () => `// ── 嵌入的数据：由 .claude/skills/knowledge-map-web/tools/build.mjs 生成，不要手改，改原稿后重新生成 ──\nwindow.KMAP_DATA = ${blob};\n// ── 数据检查（lib/normalize.js）──\n${normalizeLib}\n`)
    .replace(formulaImport, () => `// ── 教材级公式排版（lib/formula.js + 内嵌 KaTeX）──\n${formulaLib}\n`)
    .replace("</head>", () => katexHead() + extraHead + "</head>");
}
