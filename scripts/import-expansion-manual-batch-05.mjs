import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1942", "string-1942", "string", "Digital Clock", `import sys

def to_sec(value):
    h, m, s = map(int, value.split(':'))
    return h * 3600 + m * 60 + s

def good(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return (h * 10000 + m * 100 + s) % 3 == 0

answers = []
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    start_s, end_s = line.split()
    start = to_sec(start_s)
    end = to_sec(end_s)
    if start <= end:
        values = range(start, end + 1)
    else:
        values = list(range(start, 24 * 3600)) + list(range(0, end + 1))
    answers.append(str(sum(1 for sec in values if good(sec))))
print('\\n'.join(answers))
`],
  ["3005", "string-3005", "string", "Crossword", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]
words = []
for row in grid:
    words.extend(part for part in row.split('#') if len(part) >= 2)
for col in range(c):
    current = []
    for row in range(r):
        if grid[row][col] == '#':
            if len(current) >= 2:
                words.append(''.join(current))
            current = []
        else:
            current.append(grid[row][col])
    if len(current) >= 2:
        words.append(''.join(current))
print(min(words))
`],
  ["3107", "string-3107", "string", "IPv6", `import sys
s = sys.stdin.readline().strip()
if '::' in s:
    left, right = s.split('::')
    left_parts = left.split(':') if left else []
    right_parts = right.split(':') if right else []
    missing = 8 - len(left_parts) - len(right_parts)
    parts = left_parts + ['0'] * missing + right_parts
else:
    parts = s.split(':')
print(':'.join(part.zfill(4) for part in parts))
`],
  ["20114", "string-20114", "string", "Missing Note", `import sys
input = sys.stdin.readline
n, h, w = map(int, input().split())
rows = [input().strip() for _ in range(h)]
answer = []
for idx in range(n):
    ch = '?'
    for row in rows:
        for value in row[idx * w:(idx + 1) * w]:
            if value != '?':
                ch = value
                break
        if ch != '?':
            break
    answer.append(ch)
print(''.join(answer))
`],
  ["3343", "math-3343", "math", "Roses", `import sys
n, a, b, c, d = map(int, sys.stdin.readline().split())
answer = 10 ** 30
limit_c = min(c, n // a + 2)
for x in range(limit_c + 1):
    remain = max(0, n - a * x)
    y = (remain + c - 1) // c
    answer = min(answer, b * x + d * y)
limit_a = min(a, n // c + 2)
for y in range(limit_a + 1):
    remain = max(0, n - c * y)
    x = (remain + a - 1) // a
    answer = min(answer, b * x + d * y)
print(answer)
`],
  ["9421", "math-9421", "math", "Prime Happy Numbers", `import sys
n = int(sys.stdin.readline())
prime = [True] * (n + 1)
if n >= 0:
    prime[0] = False
if n >= 1:
    prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

def happy(value):
    seen = set()
    while value != 1 and value not in seen:
        seen.add(value)
        value = sum(int(ch) ** 2 for ch in str(value))
    return value == 1

print('\\n'.join(str(i) for i in range(2, n + 1) if prime[i] and happy(i)))
`],
  ["1022", "implementation-1022", "implementation", "Spiral", `import sys
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

def value(r, c):
    layer = max(abs(r), abs(c))
    end = (2 * layer + 1) ** 2
    if r == layer:
        return end - (layer - c)
    end -= 2 * layer
    if c == -layer:
        return end - (layer - r)
    end -= 2 * layer
    if r == -layer:
        return end - (c + layer)
    end -= 2 * layer
    return end - (r + layer)

grid = [[value(r, c) for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]
width = max(len(str(item)) for row in grid for item in row)
print('\\n'.join(' '.join(str(item).rjust(width) for item in row) for row in grid))
`],
  ["1283", "implementation-1283", "implementation", "Shortcut Keys", `import sys
input = sys.stdin.readline
n = int(input())
used = set()
out = []
for _ in range(n):
    line = input().rstrip('\\n')
    words = line.split(' ')
    picked = None
    offset = 0
    for word in words:
        if word:
            ch = word[0].lower()
            if ch not in used:
                picked = offset
                used.add(ch)
                break
        offset += len(word) + 1
    if picked is None:
        for idx, ch in enumerate(line):
            if ch != ' ' and ch.lower() not in used:
                picked = idx
                used.add(ch.lower())
                break
    if picked is None:
        out.append(line)
    else:
        out.append(line[:picked] + '[' + line[picked] + ']' + line[picked + 1:])
print('\\n'.join(out))
`],
  ["1034", "brute_force-1034", "brute_force", "Lamps", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rows = [input().strip() for _ in range(n)]
k = int(input())
answer = 0
for row in rows:
    zeros = row.count('0')
    if zeros <= k and (k - zeros) % 2 == 0:
        answer = max(answer, rows.count(row))
print(answer)
`],
  ["18232", "graph_traversal-18232", "graph_traversal", "Teleport Jeong Jin", `import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)
dist = [-1] * (n + 1)
dist[s] = 0
queue = deque([s])
while queue:
    cur = queue.popleft()
    if cur == e:
        break
    for nxt in (cur - 1, cur + 1):
        if 1 <= nxt <= n and dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)
    for nxt in links[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)
print(dist[e])
`]
];

async function readJson(file, fallback) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return fallback;
  }
}

function stableHash(value) {
  return createHash("sha1").update(value).digest("hex").slice(0, 12);
}

const existing = await readJson(OUT, []);
const bySlug = new Map(existing.map((problem) => [problem.slug, problem]));

for (const [id, slug, categorySlug, title, code] of PROBLEMS) {
  bySlug.set(slug, {
    id,
    slug,
    categorySlug,
    sources: [{ lang: "python", file: `local/oracle/${slug}.py`, code }],
    link: `https://www.acmicpc.net/problem/${id}`,
    authors: ["dongjun"],
    hash: stableHash(`extra:${slug}`),
    createdAt: Date.now()
  });
  console.log(`[import-manual-batch-05] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-05] wrote ${OUT}`);
