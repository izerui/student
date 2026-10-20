// md（或 JSON）→ 单文件网页。
// 用法：node .claude/skills/knowledge-map-web/tools/build.mjs <原稿.md|.json> <输出.html> [--json 输出.json] [--check]
//   --json  另外写出整理前的 JSON（schema 规定的格式）
//   --check 只检查，不写文件
// 有错误时列出来、不写文件，退出码为 1；提醒（不影响生成）也逐条列出。
import { writeFileSync } from "node:fs";
import { load, singleHtml } from "./build-lib.mjs";

const args = process.argv.slice(2), flag = k => { const i = args.indexOf(k); return i < 0 ? null : args.splice(i, 2)[1] ?? ""; };
const check = args.includes("--check"); if (check) args.splice(args.indexOf("--check"), 1);
const jsonOut = flag("--json");
const [src, out] = args;
if (!src || (!out && !check)) {
  console.log("用法：node tools/build.mjs <原稿.md|.json> <输出.html> [--json 输出.json] [--check]");
  process.exit(2);
}
const r = load(src);
r.warns.forEach(w => console.log("提醒：" + w));
r.errors.forEach(e => console.log("错误：" + e));
if (r.errors.length) { console.log(`${src}：${r.errors.length} 处错误，没有生成`); process.exit(1); }
console.log(`${src}：${r.summary}：检查通过`);
if (check) process.exit(0);
writeFileSync(out, singleHtml(r.raw));
console.log("写出 " + out);
if (jsonOut) { writeFileSync(jsonOut, JSON.stringify(r.raw, null, 1) + "\n"); console.log("写出 " + jsonOut); }
