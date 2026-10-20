// Rich formula rendering for knowledge-map Markdown fields.
// `$...$` and `$$...$$` use LaTeX/KaTeX. Legacy mixed notation keeps a lightweight fallback.

export function formulaRuns(value) {
  const source = String(value || "");
  const runs = [];
  let plain = "";

  const push = (text, script = "") => {
    if (!text) return;
    const last = runs[runs.length - 1];
    if (last && last.script === script) last.text += text;
    else runs.push({ text, script });
  };
  const flush = () => {
    push(plain);
    plain = "";
  };

  for (let i = 0; i < source.length; i++) {
    const mark = source[i];
    if ((mark !== "^" && mark !== "_") || i + 1 >= source.length) {
      plain += mark;
      continue;
    }

    let end = i + 1;
    let text = "";
    if (source[end] === "{") {
      const close = source.indexOf("}", end + 1);
      if (close < 0) {
        plain += mark;
        continue;
      }
      text = source.slice(end + 1, close);
      end = close;
    } else if (source[end] === "(") {
      const close = source.indexOf(")", end + 1);
      if (close < 0) {
        plain += mark;
        continue;
      }
      text = source.slice(end, close + 1);
      end = close;
    } else {
      const rest = source.slice(end);
      const digits = rest.match(/^\d+/u);
      if (digits) {
        text = digits[0];
        end += text.length - 1;
      } else {
        const [first = ""] = Array.from(rest);
        text = first;
        end += first.length - 1;
      }
    }

    flush();
    push(text, mark === "^" ? "sup" : "sub");
    i = end;
  }

  flush();
  return runs;
}

const escapeHtml = value => String(value || "").replace(/[&<>]/g, char => ({
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
}[char]));

const legacyHtml = value => formulaRuns(value).map(run => run.script
  ? `<${run.script} class="fm-script">${escapeHtml(run.text)}</${run.script}>`
  : escapeHtml(run.text)).join("");

function renderLatex(source, displayMode) {
  if (!globalThis.katex) return `<code class="latex-raw">${escapeHtml(source)}</code>`;
  try {
    return globalThis.katex.renderToString(source, {
      displayMode,
      throwOnError: false,
      strict: "ignore",
      output: "htmlAndMathml",
    });
  } catch {
    return `<code class="latex-raw">${escapeHtml(source)}</code>`;
  }
}

export function formulaHtml(value) {
  const source = String(value || "");
  if (!source.includes("$")) return legacyHtml(source);

  let html = "";
  let plainStart = 0;
  let cursor = 0;
  while (cursor < source.length) {
    if (source[cursor] !== "$" || (cursor > 0 && source[cursor - 1] === "\\")) {
      cursor++;
      continue;
    }
    const displayMode = source[cursor + 1] === "$";
    const delimiterLength = displayMode ? 2 : 1;
    const contentStart = cursor + delimiterLength;
    const close = source.indexOf(displayMode ? "$$" : "$", contentStart);
    if (close < 0) break;
    html += legacyHtml(source.slice(plainStart, cursor));
    html += renderLatex(source.slice(contentStart, close), displayMode);
    cursor = close + delimiterLength;
    plainStart = cursor;
  }
  html += legacyHtml(source.slice(plainStart));
  return html;
}
