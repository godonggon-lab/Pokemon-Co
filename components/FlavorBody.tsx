// 합성된 포켓몬 시나리오 본문 렌더러.
// 가벼운 마크다운 변환 (** , ` , > , 줄바꿈) — 외부 의존성 없이.

import type { FlavorProblem, ProblemMeta } from "@/lib/flavor";

function escapeHtml(s: string) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// ---- 수식 전처리 (escapeHtml 전에 실행) ----
function decodeHtmlMath(s: string): string {
  return s
    .replace(/&le;/g, "≤").replace(/&ge;/g, "≥")
    .replace(/&ne;/g, "≠").replace(/&times;/g, "×")
    .replace(/&divide;/g, "÷").replace(/&middot;/g, "·")
    .replace(/&minus;/g, "−").replace(/&plusmn;/g, "±")
    .replace(/&lfloor;/g, "⌊").replace(/&rfloor;/g, "⌋")
    .replace(/&lceil;/g, "⌈").replace(/&rceil;/g, "⌉")
    .replace(/&infin;/g, "∞").replace(/&in;/g, "∈")
    .replace(/&cup;/g, "∪").replace(/&cap;/g, "∩")
    .replace(/&sub;/g, "⊂").replace(/&sube;/g, "⊆")
    // 화살표
    .replace(/&larr;/g, "←").replace(/&rarr;/g, "→")
    .replace(/&uarr;/g, "↑").replace(/&darr;/g, "↓")
    .replace(/&harr;/g, "↔").replace(/&lArr;/g, "⇐")
    .replace(/&rArr;/g, "⇒").replace(/&hArr;/g, "⇔")
    .replace(/&uArr;/g, "⇑").replace(/&dArr;/g, "⇓")
    // 기타
    .replace(/&alpha;/g, "α").replace(/&beta;/g, "β")
    .replace(/&gamma;/g, "γ").replace(/&delta;/g, "δ")
    .replace(/&epsilon;/g, "ε").replace(/&lambda;/g, "λ")
    .replace(/&mu;/g, "μ").replace(/&pi;/g, "π")
    .replace(/&sigma;/g, "σ").replace(/&theta;/g, "θ")
    .replace(/&hellip;/g, "…").replace(/&mdash;/g, "—")
    .replace(/&ndash;/g, "–").replace(/&laquo;/g, "«")
    .replace(/&raquo;/g, "»")
    // 인용 부호
    .replace(/&lsquo;/g, "‘").replace(/&rsquo;/g, "’")
    .replace(/&ldquo;/g, "“").replace(/&rdquo;/g, "”")
    .replace(/&apos;/g, "'").replace(/&quot;/g, '"')
    .replace(/&lsaquo;/g, "‹").replace(/&rsaquo;/g, "›")
    // 기타 자주 쓰이는 것
    .replace(/&deg;/g, "°").replace(/&micro;/g, "μ")
    .replace(/&para;/g, "¶").replace(/&copy;/g, "©")
    .replace(/&reg;/g, "®").replace(/&trade;/g, "™")
    .replace(/&nbsp;/g, " ")
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-fA-F]+);/g, (_, h) => String.fromCharCode(parseInt(h, 16)));
}

function latexToUnicode(s: string): string {
  let o = s;
  o = o.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, "($1)/($2)");
  o = o.replace(/\\sqrt\{([^{}]+)\}/g, "√($1)");
  o = o.replace(/\\left[([{]/g, m => m.slice(-1)).replace(/\\right[)\]}]/g, m => m.slice(-1));
  o = o.replace(/\\leq?(?![a-z])/g, "≤");
  o = o.replace(/\\geq?(?![a-z])/g, "≥");
  o = o.replace(/\\neq?(?![a-z])/g, "≠");
  o = o.replace(/\\times(?![a-z])/g, "×");
  o = o.replace(/\\div(?![a-z])/g, "÷");
  o = o.replace(/\\cdot(?![a-z])/g, "·");
  o = o.replace(/\\ldots|\\dots(?![a-z])/g, "…");
  o = o.replace(/\\infty/g, "∞");
  o = o.replace(/\\pm(?![a-z])/g, "±");
  o = o.replace(/\\in(?![a-z])/g, "∈");
  o = o.replace(/\\notin/g, "∉");
  o = o.replace(/\\cup(?![a-z])/g, "∪");
  o = o.replace(/\\cap(?![a-z])/g, "∩");
  // 화살표
  o = o.replace(/\\rightarrow|\\to(?![a-z])/g, "→");
  o = o.replace(/\\leftarrow|\\gets(?![a-z])/g, "←");
  o = o.replace(/\\uparrow/g, "↑");
  o = o.replace(/\\downarrow/g, "↓");
  o = o.replace(/\\Rightarrow/g, "⇒");
  o = o.replace(/\\Leftarrow/g, "⇐");
  o = o.replace(/\\leftrightarrow/g, "↔");
  o = o.replace(/\\Leftrightarrow/g, "⇔");
  // 그리스 문자
  o = o.replace(/\\alpha/g, "α").replace(/\\beta/g, "β");
  o = o.replace(/\\gamma/g, "γ").replace(/\\delta/g, "δ");
  o = o.replace(/\\epsilon/g, "ε").replace(/\\lambda/g, "λ");
  o = o.replace(/\\mu/g, "μ").replace(/\\pi/g, "π");
  o = o.replace(/\\sigma/g, "σ").replace(/\\theta/g, "θ");
  // 아래첨자 _숫자 → 유니코드 아래첨자
  o = o.replace(/_(\d)/g, (_, d) => "₀₁₂₃₄₅₆₇₈₉"[Number(d)] ?? `_${d}`);
  o = o.replace(/\\,/g, "");
  o = o.replace(/[{}]/g, "");
  o = o.replace(/\^(\d)/g, (_, d) => "⁰¹²³⁴⁵⁶⁷⁸⁹"[Number(d)] ?? `^${d}`);
  return o.trim();
}

function preprocessMath(s: string): string {
  let o = decodeHtmlMath(s);
  // display math $$...$$  (먼저 처리)
  o = o.replace(/\$\$([^$]+)\$\$/g, (_, m) => latexToUnicode(m));
  // inline math $...$  (개행 없는 임의 길이)
  o = o.replace(/\$([^$\n]+)\$/g, (_, m) => latexToUnicode(m));
  return o;
}

function renderInline(s: string) {
  // ` code `
  s = s.replace(/`([^`]+)`/g, (_, c) =>
    `<code class="rounded bg-zinc-800 px-1 py-0.5 font-mono text-xs text-amber-200">${c}</code>`);
  // **bold**
  s = s.replace(/\*\*([^*]+)\*\*/g, '<b class="text-white">$1</b>');
  return s;
}

function renderMarkdown(md: string) {
  // 1) 수식·엔티티 전처리 → HTML 이스케이프 → 단락 분리
  const escaped = escapeHtml(preprocessMath(md));
  const blocks = escaped.split(/\n\s*\n+/);
  const out: string[] = [];
  for (const block of blocks) {
    const lines = block.split("\n").map(l => l.replace(/\s+$/, "")).filter(l => l.length > 0);
    if (lines.length === 0) continue;

    // 2) 한 단락 내부: 줄별로 처리하되 이미지·인용은 별도 블록으로 분리
    let buffer: string[] = [];
    const flushPara = () => {
      if (buffer.length === 0) return;
      out.push(`<p class="my-2 leading-relaxed">${buffer.join("<br/>")}</p>`);
      buffer = [];
    };
    for (const line of lines) {
      // 이미지: ![alt](src)
      const imgM = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
      if (imgM) {
        flushPara();
        const src = imgM[2].replace(/&amp;/g, "&");
        out.push(`<img src="${src}" alt="${imgM[1]}" loading="lazy" class="my-3 max-w-full rounded border border-white/10" />`);
        continue;
      }
      if (line.startsWith("&gt; ")) {
        flushPara();
        out.push(`<blockquote class="my-2 border-l-2 border-amber-400/60 bg-amber-400/5 px-3 py-1 text-zinc-300">${renderInline(line.slice(5))}</blockquote>`);
        continue;
      }
      buffer.push(renderInline(line));
    }
    flushPara();
  }
  return out.join("");
}

export default function FlavorBody({
  flavor,
  meta
}: {
  flavor: FlavorProblem;
  meta?: ProblemMeta;
}) {
  return (
    <section className="space-y-4 rounded-2xl border border-white/10 bg-zinc-900/40 p-6">
      <div>
        <div className="text-xs text-zinc-500">
          {flavor.source === "boj" ? "📚 BOJ 원문" : "📖 합성 시나리오"}
        </div>
        <h2 className="text-xl font-bold text-amber-200">{flavor.subject}</h2>
        {flavor.bojTitle && (
          <div className="mt-1 text-xs text-zinc-400">
            원작: <a href={flavor.bojLink} target="_blank" rel="noreferrer" className="hover:underline">{flavor.bojTitle}</a>
            {meta && <span className="ml-2">· {meta.levelName}</span>}
            {flavor.snapshotTs && (
              <span className="ml-2 text-zinc-500">
                (Wayback {flavor.snapshotTs.slice(0, 4)}-{flavor.snapshotTs.slice(4, 6)}-{flavor.snapshotTs.slice(6, 8)})
              </span>
            )}
          </div>
        )}
      </div>

      <div className="grid grid-cols-2 gap-3 text-xs">
        <div className="rounded-lg bg-black/30 px-3 py-2">
          <div className="text-zinc-500">시간 제한</div>
          <div className="font-mono text-amber-200">{(flavor.limits.timeLimitMs / 1000).toFixed(1)} 초</div>
        </div>
        <div className="rounded-lg bg-black/30 px-3 py-2">
          <div className="text-zinc-500">메모리 제한</div>
          <div className="font-mono text-amber-200">{flavor.limits.memoryLimitMb} MB</div>
        </div>
      </div>

      <Block title="📜 상황">
        <div className="text-sm leading-relaxed text-zinc-200"
             dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.situation) }} />
      </Block>

      <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
        <Block title="📥 입력">
          <div className="text-sm text-zinc-200"
               dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.inputSpec) }} />
        </Block>
        <Block title="📤 출력">
          <div className="text-sm text-zinc-200"
               dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.outputSpec) }} />
        </Block>
      </div>

      {flavor.samples.length > 0 && (
        <Block title="🧪 예제">
          <div className="space-y-3">
            {flavor.samples.map((s, i) => (
              <div key={i} className="grid grid-cols-1 gap-2 md:grid-cols-2">
                <div>
                  <div className="text-[10px] text-zinc-500">입력 #{i + 1}</div>
                  <pre className="rounded bg-black/40 p-2 font-mono text-xs text-zinc-100">{s.in}</pre>
                </div>
                <div>
                  <div className="text-[10px] text-zinc-500">출력 #{i + 1}</div>
                  <pre className="rounded bg-black/40 p-2 font-mono text-xs text-zinc-100">{s.out}</pre>
                </div>
                {s.explain && (
                  <div className="md:col-span-2 text-[11px] text-zinc-400">💡 {s.explain}</div>
                )}
              </div>
            ))}
          </div>
        </Block>
      )}

      {flavor.limitText && (
        <Block title="📏 제한">
          <div className="text-sm text-zinc-200"
               dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.limitText) }} />
        </Block>
      )}

      {flavor.hint && (
        <Block title="💡 힌트">
          <div className="text-sm text-zinc-200"
               dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.hint) }} />
        </Block>
      )}

      {meta?.tags && meta.tags.length > 0 && (
        <div className="flex flex-wrap gap-1">
          {meta.tags.map(t => (
            <span key={t.key} className="rounded bg-white/5 px-2 py-0.5 text-[10px] text-zinc-400">
              #{t.name_ko}
            </span>
          ))}
        </div>
      )}

      {flavor.source === "synthesized" ? (
        <details className="rounded-lg border border-amber-500/20 bg-amber-500/5 p-3">
          <summary className="cursor-pointer text-xs text-amber-200">⚠️ 본 시나리오는 학습용 합성 텍스트</summary>
          <p className="mt-2 text-[11px] leading-relaxed text-zinc-300">
            이 문제 본문은 BOJ 원문 대신 카테고리·태그·정답 코드를 기반으로 자동 합성된
            포켓몬 테마 텍스트입니다. 실제 채점은 원문 정답(Oracle)과 비교하므로,
            정밀한 입력 형식·제약은 위 <a href={flavor.bojLink} target="_blank" rel="noreferrer" className="text-amber-400 underline">BOJ 원문</a>을 참고하세요.
          </p>
        </details>
      ) : (
        <>
          {flavor.raw && (
            <details className="rounded-lg border border-white/10 bg-black/30 p-3">
              <summary className="cursor-pointer text-xs text-zinc-300">📜 원문 보기 (각색 전)</summary>
              <div className="mt-3 space-y-3 text-sm text-zinc-300">
                <div>
                  <div className="mb-1 text-[10px] text-zinc-500">설명</div>
                  <div dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.raw.description) }} />
                </div>
                {flavor.raw.input && (
                  <div>
                    <div className="mb-1 text-[10px] text-zinc-500">입력</div>
                    <div dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.raw.input) }} />
                  </div>
                )}
                {flavor.raw.output && (
                  <div>
                    <div className="mb-1 text-[10px] text-zinc-500">출력</div>
                    <div dangerouslySetInnerHTML={{ __html: renderMarkdown(flavor.raw.output) }} />
                  </div>
                )}
              </div>
            </details>
          )}
          <p className="text-[11px] text-zinc-500">
            🎨 본문은 Internet Archive (Wayback Machine) 의 BOJ 스냅샷을 포켓몬 세계관으로 각색한 것입니다.
            숫자·제약·입출력 형식은 원문 그대로이며, 정답 판정에는 영향이 없습니다. 원본 저작권: BOJ.
          </p>
        </>
      )}
    </section>
  );
}

function Block({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div>
      <div className="mb-1 text-xs text-zinc-500">{title}</div>
      <div className="rounded-xl bg-black/20 p-3">{children}</div>
    </div>
  );
}
