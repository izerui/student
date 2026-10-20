// 边改边看：node .claude/skills/knowledge-map-web/tools/serve.mjs <原稿.md|.json> <输出.html> [端口]
// 先生成一次；之后盯着原稿，内容一变就重新生成输出文件，浏览器里打开的页面自动刷新。
// 原稿有错误时不覆盖输出文件，在终端列出错误，页面上也显示出来。
import { createServer } from "node:http";
import { readFileSync, watch, writeFileSync } from "node:fs";
import { basename, dirname, resolve } from "node:path";
import { load, singleHtml } from "./build-lib.mjs";

const [src, out, port = "8080"] = process.argv.slice(2);
if (!src || !out) { console.log("用法：node tools/serve.mjs <原稿.md|.json> <输出.html> [端口]"); process.exit(2); }
const esc = s => s.replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
// 页面每秒问一次版本号，变了就刷新
const RELOAD = `<script>(() => { let v; setInterval(async () => { try { const n = await (await fetch("/__v")).text(); if (v && n !== v) location.reload(); v = n; } catch {} }, 1000); })();</script>\n`;
let page = "", version = 0, last = null;
const build = () => {
  const text = readFileSync(src, "utf8");
  if (text === last) return;   // 只有内容真的变了才生成（macOS 上别的程序读一下文件也会触发监听）
  last = text;
  const t = new Date().toLocaleTimeString(), r = load(src);
  r.warns.forEach(w => console.log(t, "提醒：" + w));
  if (r.errors.length) {
    r.errors.forEach(e => console.log(t, "错误：" + e));
    console.log(t, `${r.errors.length} 处错误，${out} 没有更新`);
    page = `<!DOCTYPE html><meta charset="utf-8">${RELOAD}<body style="font:15px/1.8 sans-serif;padding:40px"><h2>原稿有 ${r.errors.length} 处错误</h2><ul style="color:#B23B3B">${r.errors.map(e => `<li>${esc(e)}</li>`).join("")}</ul>`;
  } else {
    writeFileSync(out, singleHtml(r.raw));
    page = singleHtml(r.raw, RELOAD);
    console.log(t, `${r.summary} → ${out}`);
  }
  version++;
};
build();
let timer = 0;
// 盯着目录而不是文件：很多编辑器保存时先写临时文件再改名替换，盯着文件的话替换一次就失效了
watch(dirname(resolve(src)), (_, name) => { if (name === basename(src)) { clearTimeout(timer); timer = setTimeout(build, 150); } });
createServer((req, res) => {
  if (req.url === "/__v") { res.writeHead(200, { "cache-control": "no-cache" }).end(String(version)); return; }
  res.writeHead(200, { "content-type": "text/html; charset=utf-8", "cache-control": "no-cache" }).end(page);
}).listen(+port, "127.0.0.1", () => console.log(`打开 http://127.0.0.1:${port}/　保存原稿后页面自动刷新（Ctrl+C 停止）`));
