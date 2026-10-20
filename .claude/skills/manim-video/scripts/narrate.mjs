#!/usr/bin/env node
/**
 * 旁白生成 CLI —— OpenAI 兼容的 /v1/audio/speech（默认 tts.style520.com）。
 *
 * 用法：
 *   node scripts/narrate.mjs <workspace> [segments.json]
 *
 * 输入 segments.json（默认取 <workspace>/segments.json）：
 *   [
 *     { "id": "s1", "text": "完整旁白……",
 *       "cues": [{ "id": "c1", "marker": "必须逐字出现在 text 里的短语" }] }
 *   ]
 *
 * 输出：
 *   <workspace>/durations.json      每段的时长、语音起止、cue 时间点
 *   <workspace>/public/audio/*.wav  正式音频
 *
 * 环境变量（在 Claude Code 里由项目 .claude/settings.local.json 的 env 注入）：
 *   TTS_API_KEY        必需
 *   TTS_BASE_URL       接口地址，默认 https://tts.style520.com/v1
 *   TTS_MODEL          默认 tts-1
 *   TTS_VOICE          默认 zh-CN-YunjianNeural（云健）；
 *                      可选值见 GET <TTS_BASE_URL>/audio/voices
 *   VIDEO_TTS_RATE     默认 1.0（取值 0.5–2）
 *   HTTPS_PROXY / HTTP_PROXY  可选，检测到就自动生效（见下方代理自举）
 *
 * 设计要点（从生产流水线原样保留）：
 *   - 段级 hash 缓存：只有改过的段重新合成，其余直接复用，省钱省时间
 *   - 首尾静音补齐：头 0.2s / 尾 0.5s，固定值不开放调节（见下方常量注释）
 *   - 单段 3 次退避重试：外部抖动不该让整批作废
 *   - 原子提交：先写暂存区再整体换入，中途失败回滚，不留半套产物
 */

import { execFile, spawnSync } from "node:child_process";
import { createHash, randomUUID } from "node:crypto";
import { existsSync } from "node:fs";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);

// ---------------------------------------------------------------------------
// 代理自举
// ---------------------------------------------------------------------------

/**
 * Node 的原生 fetch 不认 HTTP_PROXY/HTTPS_PROXY。
 *
 * 在沙箱或公司网络里这会表现成一个很误导人的症状：curl 请求同一个地址是通的
 * （curl 自己读环境变量），本脚本却报 EAI_AGAIN，看起来像 DNS 坏了，实际是流量
 * 没走代理。Node 的 `--use-env-proxy` 会让内置 undici 认这些变量，但它只能在
 * 进程启动时给，运行期设不了——所以检测到代理就带着 flag 把自己重启一次。
 */
function envProxy() {
  return (
    process.env.HTTPS_PROXY ||
    process.env.https_proxy ||
    process.env.HTTP_PROXY ||
    process.env.http_proxy ||
    ""
  );
}

function bootstrapProxy() {
  const proxy = envProxy();
  if (!proxy) return;
  if (process.env.NODE_USE_ENV_PROXY === "1") {
    // 已经是重启后的自己。说一声，免得后面出网络问题时还要猜代理有没有生效。
    console.log(`代理：已启用 ${proxy}`);
    return;
  }

  if (!process.allowedNodeEnvironmentFlags.has("--use-env-proxy")) {
    console.warn(
      "⚠️  检测到代理环境变量，但当前 Node 不支持 --use-env-proxy（需 v22.15+ 或 v24+）。\n" +
        "    若合成阶段报 fetch failed / EAI_AGAIN，请升级 Node。",
    );
    return;
  }

  const result = spawnSync(process.execPath, [fileURLToPath(import.meta.url), ...process.argv.slice(2)], {
    stdio: "inherit",
    // 关掉 Node 对 EnvHttpProxyAgent 的实验性告警：它每次都刷两行，在本就冗长的
    // 制作日志里纯属噪声，还会让人误以为出了问题。代理是否生效由上面那行自己报。
    env: { ...process.env, NODE_USE_ENV_PROXY: "1", NODE_NO_WARNINGS: "1" },
  });
  process.exit(result.status ?? 1);
}

bootstrapProxy();

const TTS_BASE = "https://tts.style520.com/v1";
const SAMPLE_RATE = 48_000;
const TOTAL_TIMEOUT_MS = 10 * 60 * 1000;

/**
 * 段间静音属于固定渲染管道，不开放给调用方。
 *
 * 0.5 秒尾静音正好被转场吃掉，不留多余空气。这个值曾经开放成参数（默认 0.9s），
 * 实测会被无依据地调大：10 段 × 多出的 0.4s = 4 秒纯静音，占一条两分钟成片的 3%，
 * 观感直接就是「拖」。全片一致的渲染常量该由管道定死。
 */
const HEAD_PAD_SEC = 0.2;
const TAIL_PAD_SEC = 0.5;

/** 单段合成：首次 + 2 次重试。失败几乎全是外部抖动（接口超时、空音频、偶发 5xx）。 */
const MAX_ATTEMPTS = 3;
const RETRY_BASE_MS = 1000;

// ---------------------------------------------------------------------------
// 小工具
// ---------------------------------------------------------------------------

const die = (message) => {
  console.error(`旁白生成失败：${message}`);
  process.exit(1);
};

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function hashOf(value) {
  return createHash("sha256").update(JSON.stringify(value)).digest("hex");
}

function segmentHash(segment, config) {
  return hashOf({ segment, ...config, head: HEAD_PAD_SEC, tail: TAIL_PAD_SEC });
}

function resolveConfig() {
  const apiKey = process.env.TTS_API_KEY;
  if (!apiKey) {
    die(
      "缺少 TTS_API_KEY。写进项目 .claude/settings.local.json 的 env：\n" +
        '  "env": { "TTS_API_KEY": "sk-xxxx" }\n' +
        "不会用静音占位——没有旁白的讲解视频是废品，必须显式失败。",
    );
  }
  const rate = Number.parseFloat(process.env.VIDEO_TTS_RATE ?? "1.0");
  if (!Number.isFinite(rate) || rate < 0.5 || rate > 2) die("VIDEO_TTS_RATE 必须是 0.5–2 之间的数字");
  return {
    apiKey,
    baseUrl: (process.env.TTS_BASE_URL ?? TTS_BASE).replace(/\/+$/, ""),
    model: process.env.TTS_MODEL ?? "tts-1",
    voice: process.env.TTS_VOICE ?? "zh-CN-YunjianNeural",
    rate,
  };
}

// ---------------------------------------------------------------------------
// 校验
// ---------------------------------------------------------------------------

function validateSegments(segments) {
  if (!Array.isArray(segments) || segments.length === 0) {
    die("segments 必须是非空数组");
  }
  const ids = new Set();
  for (const segment of segments) {
    if (!segment?.id || !/^[A-Za-z0-9_-]+$/.test(segment.id)) {
      die(`场景 id 非法（只允许字母数字下划线连字符）: ${JSON.stringify(segment?.id)}`);
    }
    if (ids.has(segment.id)) die(`场景 id 重复: ${segment.id}`);
    ids.add(segment.id);

    const text = typeof segment.text === "string" ? segment.text.trim() : "";
    if (!text) die(`场景 ${segment.id} 的 text 为空`);
    if (text.length > 1000) die(`场景 ${segment.id} 的 text 超过 1000 字`);

    const cueIds = new Set();
    for (const cue of segment.cues ?? []) {
      if (!cue?.id || !/^[A-Za-z0-9_-]+$/.test(cue.id)) {
        die(`场景 ${segment.id} 的 cue id 非法: ${JSON.stringify(cue?.id)}`);
      }
      if (cueIds.has(cue.id)) die(`场景 ${segment.id} 的 cue id 重复: ${cue.id}`);
      cueIds.add(cue.id);
      // marker 必须逐字出现在旁白里——这是 cue 定位的唯一依据，写错了画面就会对错时刻。
      if (!cue.marker || !text.includes(cue.marker)) {
        die(
          `场景 ${segment.id} 的 cue ${cue.id} 的 marker 未逐字出现在旁白中：\n` +
            `  marker: ${JSON.stringify(cue.marker)}\n` +
            `  旁白:   ${JSON.stringify(text.slice(0, 120))}…`,
        );
      }
    }
  }
}

/**
 * 按 marker 在文本中的字符位置，线性估算它对应的语音时刻。
 *
 * 这是估算不是对齐：中文语速在一段内基本均匀，误差通常在半秒内，
 * 足够让画面动作卡在旁白讲到那句话的时候。要精确到词需要 ASR 强制对齐，
 * 对讲解视频的收益不抵成本。
 */
function buildCuePoints(segment, speechStartSec, speechEndSec) {
  if (!segment.cues?.length) return undefined;
  const text = segment.text.trim();
  const textLength = Math.max(1, text.length);
  const speechDuration = Math.max(0, speechEndSec - speechStartSec);
  return segment.cues.map((cue) => {
    const index = text.indexOf(cue.marker);
    return {
      id: cue.id,
      marker: cue.marker,
      timeSec: Number((speechStartSec + (index / textLength) * speechDuration).toFixed(3)),
    };
  });
}

// ---------------------------------------------------------------------------
// 合成
// ---------------------------------------------------------------------------

/** OpenAI 兼容接口：直接返回音频字节（mp3）。 */
async function requestSpeech(text, config, signal) {
  const response = await fetch(`${config.baseUrl}/audio/speech`, {
    method: "POST",
    // 单次请求限时 120 秒：卡住的请求要尽快失败，把机会留给重试，而不是耗光整批的总预算。
    signal: AbortSignal.any([signal, AbortSignal.timeout(120_000)]),
    headers: {
      Authorization: `Bearer ${config.apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ model: config.model, input: text, voice: config.voice, speed: config.rate }),
  });
  if (!response.ok) {
    const payload = await response.json().catch(() => null);
    throw new Error(`TTS 接口报错: ${payload?.error?.message ?? `HTTP ${response.status}`}`);
  }
  const type = response.headers.get("content-type") ?? "";
  if (!type.startsWith("audio/")) throw new Error(`TTS 接口没有返回音频（content-type=${type || "?"}）`);
  const buffer = Buffer.from(await response.arrayBuffer());
  if (buffer.length === 0) throw new Error("TTS 接口返回了空音频");
  return buffer;
}

/**
 * 首尾补静音、统一采样率/声道、响度归一化。
 *
 * 两遍 loudnorm：第一遍测量实际 LUFS/TP/LRA，第二遍用测量值精确归一化到
 * I=-16 LUFS / TP=-1.5 dBFS / LRA=11。这样每段旁白从源头就音量一致，
 * 不需要等到最终成片再补救。
 */
async function normalizeAudio(rawPath, outputPath) {
  const padded = `${rawPath}.padded.wav`;
  await execFileAsync(
    "ffmpeg",
    [
      "-y", "-v", "error",
      "-i", rawPath,
      "-af", `adelay=${Math.round(HEAD_PAD_SEC * 1000)}:all=1,apad=pad_dur=${TAIL_PAD_SEC}`,
      "-ar", String(SAMPLE_RATE),
      "-ac", "1",
      padded,
    ],
    { timeout: 120_000 },
  );

  // 第一遍：测量
  let measured;
  try {
    const { stderr } = await execFileAsync(
      "ffmpeg",
      [
        "-y", "-v", "error",
        "-i", padded,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-",
      ],
      { timeout: 120_000 },
    );
    const jsonMatch = stderr.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      measured = JSON.parse(jsonMatch[0]);
    }
  } catch {
    // 测量失败时跳过归一化，保留补静音后的版本
  }

  if (measured?.input_i != null) {
    // 第二遍：用测量值精确归一化
    await execFileAsync(
      "ffmpeg",
      [
        "-y", "-v", "error",
        "-i", padded,
        "-af", [
          "loudnorm=I=-16:TP=-1.5:LRA=11",
          `measured_I=${measured.input_i}`,
          `measured_TP=${measured.input_tp}`,
          `measured_LRA=${measured.input_lra}`,
          `measured_thresh=${measured.input_thresh}`,
          `offset=${measured.target_offset}`,
          "linear=true",
        ].join(":"),
        "-ar", String(SAMPLE_RATE),
        "-ac", "1",
        outputPath,
      ],
      { timeout: 120_000 },
    );
  } else {
    await fs.rename(padded, outputPath);
  }

  // 清理中间文件
  await fs.rm(padded, { force: true }).catch(() => {});
}

async function probeDuration(filePath) {
  const { stdout } = await execFileAsync(
    "ffprobe",
    ["-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", filePath],
    { timeout: 30_000 },
  );
  const duration = Number.parseFloat(stdout.trim());
  if (!Number.isFinite(duration) || duration <= 0) throw new Error(`音频时长无效: ${filePath}`);
  return duration;
}

async function synthesizeOnce(segment, config, dirs, signal) {
  const audio = await requestSpeech(segment.text.trim(), config, signal);
  const rawPath = path.join(dirs.raw, `${segment.id}.mp3`);
  const outPath = path.join(dirs.audio, `${segment.id}.wav`);
  await fs.writeFile(rawPath, audio);
  await normalizeAudio(rawPath, outPath);

  const duration = await probeDuration(outPath);
  const speechStartSec = Number(Math.min(HEAD_PAD_SEC, duration).toFixed(3));
  const speechEndSec = Number(Math.max(HEAD_PAD_SEC, duration - TAIL_PAD_SEC).toFixed(3));
  return {
    file: `audio/${segment.id}.wav`,
    durationSec: Number(duration.toFixed(3)),
    speechStartSec,
    speechEndSec,
    cuePoints: buildCuePoints(segment, speechStartSec, speechEndSec),
  };
}

async function synthesizeWithRetry(segment, config, dirs, deadline, signal) {
  for (let attempt = 1; ; attempt += 1) {
    try {
      return await synthesizeOnce(segment, config, dirs, signal);
    } catch (error) {
      const budgetLeft = deadline - Date.now();
      // 预算耗尽再试也只会立刻超时；次数用尽就如实失败。
      if (budgetLeft <= 0 || attempt >= MAX_ATTEMPTS) throw error;
      const backoff = Math.min(RETRY_BASE_MS * attempt, budgetLeft);
      console.warn(
        `  段 ${segment.id} 第 ${attempt}/${MAX_ATTEMPTS} 次失败，${backoff}ms 后重试：${error.message}`,
      );
      await sleep(backoff);
    }
  }
}

// ---------------------------------------------------------------------------
// 缓存与提交
// ---------------------------------------------------------------------------

async function readReusable(workspace, hashes) {
  try {
    const manifest = JSON.parse(await fs.readFile(path.join(workspace, ".narration-manifest.json"), "utf8"));
    const durations = JSON.parse(await fs.readFile(path.join(workspace, "durations.json"), "utf8"));
    const reusable = {};
    for (const [id, hash] of Object.entries(hashes)) {
      const entry = durations[id];
      if (!entry || manifest.segmentHashes?.[id] !== hash) continue;
      if (!existsSync(path.join(workspace, "public", entry.file))) continue;
      reusable[id] = entry;
    }
    return reusable;
  } catch {
    return {};
  }
}

/**
 * 原子提交：先把新产物备份旧的、再整体换入；任一步失败就回滚。
 *
 * 半套产物比没有产物更坏——durations.json 是新的、音频还是旧的，渲染出来音画全错位，
 * 而且从退出码看不出任何异常。
 */
async function commit(workspace, stagingAudio, durations, segmentHashes) {
  const publicDir = path.join(workspace, "public");
  const metadataDir = path.join(path.dirname(stagingAudio), "metadata");
  const backupRoot = path.join(workspace, `.narration-backup-${randomUUID()}`);
  await Promise.all([
    fs.mkdir(publicDir, { recursive: true }),
    fs.mkdir(metadataDir, { recursive: true }),
    fs.mkdir(backupRoot, { recursive: true }),
  ]);

  const json = `${JSON.stringify(durations, null, 2)}\n`;
  const stagedDurations = path.join(metadataDir, "durations.json");
  const stagedManifest = path.join(metadataDir, "manifest.json");
  await Promise.all([
    fs.writeFile(stagedDurations, json),
    fs.writeFile(
      stagedManifest,
      `${JSON.stringify({ segmentHashes, createdAt: new Date().toISOString() }, null, 2)}\n`,
    ),
  ]);

  const entries = [
    { source: stagingAudio, target: path.join(publicDir, "audio"), backup: path.join(backupRoot, "audio") },
    { source: stagedDurations, target: path.join(workspace, "durations.json"), backup: path.join(backupRoot, "durations.json") },
    { source: stagedManifest, target: path.join(workspace, ".narration-manifest.json"), backup: path.join(backupRoot, "manifest.json") },
  ];

  const backedUp = [];
  const committed = [];
  try {
    for (const entry of entries) {
      try {
        await fs.rename(entry.target, entry.backup);
        backedUp.push(entry);
      } catch (error) {
        if (error.code !== "ENOENT") throw error;
      }
    }
    for (const entry of entries) {
      await fs.rename(entry.source, entry.target);
      committed.push(entry);
    }
  } catch (error) {
    for (const entry of committed.reverse()) {
      await fs.rm(entry.target, { recursive: true, force: true }).catch(() => {});
    }
    for (const entry of backedUp.reverse()) {
      await fs.rename(entry.backup, entry.target).catch(() => {});
    }
    await fs.rm(backupRoot, { recursive: true, force: true }).catch(() => {});
    throw error;
  }
  await fs.rm(backupRoot, { recursive: true, force: true });
}

// ---------------------------------------------------------------------------
// 主流程
// ---------------------------------------------------------------------------

/** 和 manim_cli.py 一样支持 slug：自动在项目根的 videos/ 下找。 */
function resolveWorkspace(raw) {
  const candidate = path.resolve(raw);
  if (existsSync(candidate)) return candidate;
  // 向上找项目根（有 .git 的目录）
  const scriptDir = path.dirname(new URL(import.meta.url).pathname);
  let dir = path.resolve(scriptDir, "..");
  for (let i = 0; i < 10; i++) {
    const parent = path.dirname(dir);
    if (existsSync(path.join(parent, ".git"))) {
      const nested = path.join(parent, "videos", raw);
      if (existsSync(nested)) return nested;
      break;
    }
    if (parent === dir) break;
    dir = parent;
  }
  die(`项目不存在: ${raw}\n  试过: ${candidate}`);
}

async function main() {
  const [rawWorkspace, rawSegments] = process.argv.slice(2);
  if (!rawWorkspace) {
    die("用法: node scripts/narrate.mjs <workspace|slug> [segments.json]");
  }
  const workspace = resolveWorkspace(rawWorkspace);

  const segmentsPath = rawSegments ? path.resolve(rawSegments) : path.join(workspace, "segments.json");
  if (!existsSync(segmentsPath)) {
    die(`找不到 ${segmentsPath}。请先写好分段旁白（含 cues），再运行本脚本。`);
  }

  let segments;
  try {
    segments = JSON.parse(await fs.readFile(segmentsPath, "utf8"));
  } catch (error) {
    die(`segments.json 不是合法 JSON: ${error.message}`);
  }
  // 允许 {"segments": [...]} 和裸数组两种写法。
  if (!Array.isArray(segments) && Array.isArray(segments?.segments)) segments = segments.segments;
  validateSegments(segments);

  const config = resolveConfig();
  const publicConfig = { baseUrl: config.baseUrl, model: config.model, voice: config.voice, rate: config.rate };
  const hashes = Object.fromEntries(segments.map((s) => [s.id, segmentHash(s, publicConfig)]));
  const reusable = await readReusable(workspace, hashes);

  console.log(
    `旁白：${segments.length} 段 | ${config.baseUrl} | 模型 ${config.model} | 音色 ${config.voice} | 语速 ${config.rate}`,
  );

  const stagingRoot = path.join(workspace, `.narration-staging-${randomUUID()}`);
  const dirs = { raw: path.join(stagingRoot, "raw"), audio: path.join(stagingRoot, "audio") };
  await Promise.all([fs.mkdir(dirs.raw, { recursive: true }), fs.mkdir(dirs.audio, { recursive: true })]);

  const controller = new AbortController();
  const deadline = Date.now() + TOTAL_TIMEOUT_MS;
  const durations = {};
  let reusedCount = 0;

  try {
    for (const [index, segment] of segments.entries()) {
      const position = `${index + 1}/${segments.length}`;
      const cached = reusable[segment.id];
      if (cached) {
        await fs.copyFile(
          path.join(workspace, "public", cached.file),
          path.join(dirs.audio, `${segment.id}.wav`),
        );
        durations[segment.id] = cached;
        reusedCount += 1;
        console.log(`  [${position}] ${segment.id} 复用缓存 (${cached.durationSec}s)`);
        continue;
      }
      console.log(`  [${position}] ${segment.id} 合成中…（${segment.text.trim().length} 字）`);
      const entry = await synthesizeWithRetry(segment, config, dirs, deadline, controller.signal);
      durations[segment.id] = entry;
      console.log(`  [${position}] ${segment.id} 完成 ${entry.durationSec}s，${entry.cuePoints?.length ?? 0} 个 cue`);
    }

    await commit(workspace, dirs.audio, durations, hashes);
  } catch (error) {
    die(error.message);
  } finally {
    await fs.rm(stagingRoot, { recursive: true, force: true }).catch(() => {});
  }

  const total = Object.values(durations).reduce((sum, entry) => sum + entry.durationSec, 0);
  console.log(
    `\n完成：${segments.length} 段（复用 ${reusedCount}），合计 ${total.toFixed(1)}s\n` +
      `  durations.json -> ${path.join(workspace, "durations.json")}\n` +
      `  音频           -> ${path.join(workspace, "public/audio")}`,
  );
}

main().catch((error) => {
  const detail = error.stack ?? error.message ?? String(error);
  // 网络层失败最常见的根因是代理没生效，直接把排查方向给出来，别让人去猜 DNS。
  if (/fetch failed|EAI_AGAIN|ECONNREFUSED|ENOTFOUND/.test(detail)) {
    const proxy = envProxy();
    die(
      `${detail}\n\n` +
        `网络请求失败。排查顺序：\n` +
        `  1. 代理：当前 ${proxy ? `检测到 ${proxy}` : "未设置 HTTPS_PROXY/HTTP_PROXY"}。` +
        `若该网络必须走代理，设好变量后重跑，脚本会自动启用。\n` +
        `  2. 连通性：curl -s -o /dev/null -w '%{http_code}' ${TTS_BASE.replace(/\/v1$/, "")}/healthz\n` +
        `     curl 通而本脚本不通，基本就是代理没生效（Node 需 v22.15+ 或 v24+）。`,
    );
  }
  die(detail);
});
