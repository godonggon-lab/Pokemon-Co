import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1727", "dynamic_programming_2-1727", "dynamic_programming_2", "Couples", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
if n > m:
    a, b = b, a
    n, m = m, n
INF = 10**18
dp = [[INF] * (m + 1) for _ in range(n + 1)]
for j in range(m + 1):
    dp[0][j] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + abs(a[i - 1] - b[j - 1]))
print(dp[n][m])
`],
  ["1757", "dynamic_programming_2-1757", "dynamic_programming_2", "Running", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [int(input()) for _ in range(n)]
NEG = -10**15
dp = [[NEG] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for tired in range(m + 1):
        if dp[i][tired] == NEG:
            continue
        if tired == 0:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
        else:
            dp[i + 1][tired - 1] = max(dp[i + 1][tired - 1], dp[i][tired])
        if tired < m:
            dp[i + 1][tired + 1] = max(dp[i + 1][tired + 1], dp[i][tired] + d[i])
print(dp[n][0])
`],
  ["1823", "dynamic_programming_2-1823", "dynamic_programming_2", "Harvest", `import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for length in range(1, n + 1):
    day = n - length + 1
    for l in range(n - length + 1):
        r = l + length - 1
        if l == r:
            dp[l][r] = day * a[l]
        else:
            dp[l][r] = max(dp[l + 1][r] + day * a[l], dp[l][r - 1] + day * a[r])
print(dp[0][n - 1])
`],
  ["1958", "dynamic_programming_2-1958", "dynamic_programming_2", "LCS 3", `import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()
dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(c) + 1):
            if a[i - 1] == b[j - 1] == c[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
print(dp[-1][-1][-1])
`],
  ["2073", "dynamic_programming_2-2073", "dynamic_programming_2", "Pipe", `import sys
input = sys.stdin.readline
d, p = map(int, input().split())
dp = [0] * (d + 1)
dp[0] = 10**9
for _ in range(p):
    length, cap = map(int, input().split())
    for x in range(d, length - 1, -1):
        dp[x] = max(dp[x], min(dp[x - length], cap))
print(dp[d])
`],
  ["2157", "dynamic_programming_2-2157", "dynamic_programming_2", "Travel", `import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        edges[a].append((b, c))
NEG = -10**15
dp = [[NEG] * (n + 1) for _ in range(m + 1)]
dp[1][1] = 0
for cnt in range(1, m):
    for city in range(1, n + 1):
        if dp[cnt][city] == NEG:
            continue
        for nxt, score in edges[city]:
            dp[cnt + 1][nxt] = max(dp[cnt + 1][nxt], dp[cnt][city] + score)
print(max(dp[cnt][n] for cnt in range(1, m + 1)))
`],
  ["2160", "brute_force-2160", "brute_force", "Pictures", `import sys
input = sys.stdin.readline
n = int(input())
pics = [["".join(input().strip() for _ in range(5))] for __ in range(n)]
best = (10**9, 1, 2)
for i in range(n):
    for j in range(i + 1, n):
        diff = sum(x != y for x, y in zip(pics[i][0], pics[j][0]))
        if diff < best[0]:
            best = (diff, i + 1, j + 1)
print(best[1], best[2])
`],
  ["2228", "dynamic_programming_2-2228", "dynamic_programming_2", "Divide Sections", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] + [int(input()) for _ in range(n)]
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i]
NEG = -10**15
dp = [[NEG] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, i + 1):
            prev = 0 if k <= 2 and j == 1 else (dp[k - 2][j - 1] if k >= 2 else NEG)
            if prev != NEG:
                dp[i][j] = max(dp[i][j], prev + prefix[i] - prefix[k - 1])
print(dp[n][m])
`],
  ["2229", "dynamic_programming_2-2229", "dynamic_programming_2", "Group Division", `import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    mn = mx = a[i]
    for j in range(i, 0, -1):
        mn = min(mn, a[j])
        mx = max(mx, a[j])
        dp[i] = max(dp[i], dp[j - 1] + mx - mn)
print(dp[n])
`],
  ["2253", "dynamic_programming_2-2253", "dynamic_programming_2", "Frog Jump", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bad = {int(input()) for _ in range(m)}
INF = 10**9
limit = int((2 * n) ** 0.5) + 3
dp = [[INF] * (limit + 1) for _ in range(n + 1)]
dp[1][0] = 0
for pos in range(1, n + 1):
    if pos in bad:
        continue
    for jump in range(limit + 1):
        if dp[pos][jump] == INF:
            continue
        for nj in (jump - 1, jump, jump + 1):
            if nj > 0 and nj <= limit and pos + nj <= n and pos + nj not in bad:
                dp[pos + nj][nj] = min(dp[pos + nj][nj], dp[pos][jump] + 1)
ans = min(dp[n])
print(ans if ans < INF else -1)
`],
  ["2285", "greedy-2285", "greedy", "Post Office", `import sys
input = sys.stdin.readline
n = int(input())
villages = sorted(tuple(map(int, input().split())) for _ in range(n))
total = sum(p for _, p in villages)
acc = 0
for x, p in villages:
    acc += p
    if acc * 2 >= total:
        print(x)
        break
`],
  ["2412", "binary_search-2412", "binary_search", "Climbing", `from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n, t = map(int, input().split())
by_y = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    by_y[y].append(x)
seen = {(0, 0)}
q = deque([(0, 0, 0)])
while q:
    x, y, d = q.popleft()
    if y == t:
        print(d)
        break
    for ny in range(y - 2, y + 3):
        for nx in by_y.get(ny, []):
            if abs(nx - x) <= 2 and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny, d + 1))
else:
    print(-1)
`],
  ["2428", "two_pointer-2428", "two_pointer", "Plagiarism", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
ans = 0
r = 0
for l in range(n):
    while r < n and a[l] * 10 >= a[r] * 9:
        r += 1
    ans += r - l - 1
print(ans)
`],
  ["2457", "greedy-2457", "greedy", "Princess Garden", `import sys
input = sys.stdin.readline
n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm * 100 + sd, em * 100 + ed))
flowers.sort()
target = 1201
cur = 301
i = ans = 0
while cur < target:
    best = cur
    while i < n and flowers[i][0] <= cur:
        best = max(best, flowers[i][1])
        i += 1
    if best == cur:
        print(0)
        break
    ans += 1
    cur = best
else:
    print(ans)
`],
  ["2467", "binary_search-2467", "binary_search", "Solutions", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
best = 10**18
ans = (a[l], a[r])
while l < r:
    s = a[l] + a[r]
    if abs(s) < best:
        best = abs(s)
        ans = (a[l], a[r])
    if s < 0:
        l += 1
    else:
        r -= 1
print(*ans)
`],
  ["2529", "backtracking-2529", "backtracking", "Inequality", `import sys
k = int(sys.stdin.readline())
ops = sys.stdin.readline().split()
answers = []
used = [False] * 10
def good(a, op, b):
    return a < b if op == "<" else a > b
def dfs(path):
    if len(path) == k + 1:
        answers.append("".join(map(str, path)))
        return
    for d in range(10):
        if not used[d] and (not path or good(path[-1], ops[len(path) - 1], d)):
            used[d] = True
            path.append(d)
            dfs(path)
            path.pop()
            used[d] = False
dfs([])
print(max(answers))
print(min(answers))
`],
  ["2565", "dynamic_programming_1-2565", "dynamic_programming_1", "Electric Wire", `import sys
input = sys.stdin.readline
n = int(input())
wires = sorted(tuple(map(int, input().split())) for _ in range(n))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if wires[j][1] < wires[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
`],
  ["2616", "dynamic_programming_2-2616", "dynamic_programming_2", "Small Train", `import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i]
dp = [[0] * (n + 1) for _ in range(4)]
for train in range(1, 4):
    for i in range(train * m, n + 1):
        block = prefix[i] - prefix[i - m]
        dp[train][i] = max(dp[train][i - 1], dp[train - 1][i - m] + block)
print(dp[3][n])
`],
  ["2623", "topological_sorting-2623", "topological_sorting", "Music Program", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    data = list(map(int, input().split()))
    for a, b in zip(data[1:], data[2:]):
        g[a].append(b)
        indeg[b] += 1
q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
out = []
while q:
    x = q.popleft()
    out.append(x)
    for nx in g[x]:
        indeg[nx] -= 1
        if indeg[nx] == 0:
            q.append(nx)
print("\\n".join(map(str, out)) if len(out) == n else "0")
`],
  ["2624", "dynamic_programming_2-2624", "dynamic_programming_2", "Coin Change", `import sys
input = sys.stdin.readline
t = int(input())
k = int(input())
dp = [0] * (t + 1)
dp[0] = 1
for _ in range(k):
    coin, count = map(int, input().split())
    nxt = dp[:]
    for amount in range(t + 1):
        if dp[amount]:
            for c in range(1, count + 1):
                if amount + coin * c <= t:
                    nxt[amount + coin * c] += dp[amount]
    dp = nxt
print(dp[t])
`]
];

async function readJson(file, fallback) {
  try { return JSON.parse(await fs.readFile(file, "utf8")); } catch { return fallback; }
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
  console.log(`[import-manual-batch-21] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-21] wrote ${OUT}`);
