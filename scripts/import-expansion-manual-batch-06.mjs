import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1497", "backtracking-1497", "backtracking", "Guitar Concert", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
masks = []
for _ in range(n):
    _name, songs = input().split()
    mask = 0
    for i, ch in enumerate(songs):
        if ch == 'Y':
            mask |= 1 << i
    masks.append(mask)
best_songs = 0
best_count = 10 ** 9
for bits in range(1, 1 << n):
    mask = 0
    count = 0
    for i in range(n):
        if bits & (1 << i):
            mask |= masks[i]
            count += 1
    songs = mask.bit_count()
    if songs > best_songs or (songs == best_songs and count < best_count):
        best_songs = songs
        best_count = count
print(-1 if best_songs == 0 else best_count)
`],
  ["17396", "shortest_path-17396", "shortest_path", "Backdoor", `import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
visible = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
dist = [10 ** 30] * n
dist[0] = 0
heap = [(0, 0)]
while heap:
    cost, cur = heapq.heappop(heap)
    if cost != dist[cur]:
        continue
    for nxt, weight in graph[cur]:
        if nxt != n - 1 and visible[nxt]:
            continue
        nc = cost + weight
        if nc < dist[nxt]:
            dist[nxt] = nc
            heapq.heappush(heap, (nc, nxt))
print(-1 if dist[n - 1] == 10 ** 30 else dist[n - 1])
`],
  ["20007", "shortest_path-20007", "shortest_path", "Rice Cake Delivery", `import heapq, sys
input = sys.stdin.readline
n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dist = [10 ** 18] * n
dist[y] = 0
heap = [(0, y)]
while heap:
    cost, cur = heapq.heappop(heap)
    if cost != dist[cur]:
        continue
    for nxt, weight in graph[cur]:
        nc = cost + weight
        if nc < dist[nxt]:
            dist[nxt] = nc
            heapq.heappush(heap, (nc, nxt))
if any(value == 10 ** 18 or value * 2 > x for value in dist):
    print(-1)
else:
    days = 1
    today = 0
    for value in sorted(dist):
        trip = value * 2
        if today + trip > x:
            days += 1
            today = 0
        today += trip
    print(days)
`],
  ["19583", "data_structure2-19583", "data_structure2", "Cyber Opening Meeting", `import sys
s, e, q = sys.stdin.readline().split()
before = set()
after = set()
for line in sys.stdin:
    if not line.strip():
        continue
    time, name = line.split()
    if time <= s:
        before.add(name)
    elif e <= time <= q:
        after.add(name)
print(len(before & after))
`],
  ["16719", "implementation-16719", "implementation", "ZOAC", `import sys
s = sys.stdin.readline().strip()
used = [False] * len(s)
out = []

def build(left, right):
    if left > right:
        return
    idx = min(range(left, right + 1), key=lambda i: s[i])
    used[idx] = True
    out.append(''.join(s[i] for i in range(len(s)) if used[i]))
    build(idx + 1, right)
    build(left, idx - 1)

build(0, len(s) - 1)
print('\\n'.join(out))
`],
  ["16927", "implementation-16927", "implementation", "Array Rotation 2", `import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
layers = min(n, m) // 2
for layer in range(layers):
    positions = []
    for c in range(layer, m - layer):
        positions.append((layer, c))
    for row in range(layer + 1, n - layer):
        positions.append((row, m - layer - 1))
    for c in range(m - layer - 2, layer - 1, -1):
        positions.append((n - layer - 1, c))
    for row in range(n - layer - 2, layer, -1):
        positions.append((row, layer))
    values = [arr[row][col] for row, col in positions]
    shift = r % len(values)
    for idx, (row, col) in enumerate(positions):
        arr[row][col] = values[(idx + shift) % len(values)]
print('\\n'.join(' '.join(map(str, row)) for row in arr))
`],
  ["17276", "implementation-17276", "implementation", "Array Rotation", `import sys
input = sys.stdin.readline
t = int(input())
answers = []
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    steps = (d % 360) // 45
    mid = n // 2
    for _step in range(steps):
        old = [row[:] for row in arr]
        for i in range(n):
            arr[i][mid] = old[i][i]
            arr[i][n - 1 - i] = old[i][mid]
            arr[mid][n - 1 - i] = old[i][n - 1 - i]
            arr[i][i] = old[mid][i]
    answers.extend(' '.join(map(str, row)) for row in arr)
print('\\n'.join(answers))
`],
  ["18311", "implementation-18311", "implementation", "Round Trip", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
courses = list(map(int, input().split()))
for idx, length in enumerate(courses, 1):
    if k < length:
        print(idx)
        sys.exit()
    k -= length
for idx in range(n, 0, -1):
    length = courses[idx - 1]
    if k < length:
        print(idx)
        sys.exit()
    k -= length
`],
  ["20164", "implementation-20164", "implementation", "Odd Holic", `import sys
s = sys.stdin.readline().strip()
mn = 10 ** 9
mx = 0

def odd_count(value):
    return sum((ord(ch) - 48) % 2 for ch in value)

def dfs(value, total):
    global mn, mx
    total += odd_count(value)
    if len(value) == 1:
        mn = min(mn, total)
        mx = max(mx, total)
    elif len(value) == 2:
        dfs(str(int(value[0]) + int(value[1])), total)
    else:
        for i in range(1, len(value) - 1):
            for j in range(i + 1, len(value)):
                dfs(str(int(value[:i]) + int(value[i:j]) + int(value[j:])), total)

dfs(s, 0)
print(mn, mx)
`],
  ["2469", "implementation-2469", "implementation", "Ladder", `import sys
input = sys.stdin.readline
k = int(input())
n = int(input())
target = list(input().strip())
lines = [input().strip() for _ in range(n)]
top = [chr(ord('A') + i) for i in range(k)]
unknown = lines.index('?' * (k - 1))
for line in lines[:unknown]:
    for i, ch in enumerate(line):
        if ch == '-':
            top[i], top[i + 1] = top[i + 1], top[i]
bottom = target[:]
for line in reversed(lines[unknown + 1:]):
    for i, ch in enumerate(line):
        if ch == '-':
            bottom[i], bottom[i + 1] = bottom[i + 1], bottom[i]
answer = ['*'] * (k - 1)
i = 0
possible = True
while i < k - 1:
    if top[i] == bottom[i]:
        i += 1
    elif top[i] == bottom[i + 1] and top[i + 1] == bottom[i]:
        answer[i] = '-'
        top[i], top[i + 1] = top[i + 1], top[i]
        i += 2
    else:
        possible = False
        break
if top[-1] != bottom[-1]:
    possible = False
print(''.join(answer) if possible else 'x' * (k - 1))
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
  console.log(`[import-manual-batch-06] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-06] wrote ${OUT}`);
