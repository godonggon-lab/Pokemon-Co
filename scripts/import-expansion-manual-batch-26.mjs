import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["16960", "binary_search-16960", "binary_search", "Switch and Lamps", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
switches = []
cnt = [0] * (m + 1)
for _ in range(n):
    data = list(map(int, input().split()))
    lamps = data[1:]
    switches.append(lamps)
    for lamp in lamps:
        cnt[lamp] += 1
print(1 if any(all(cnt[lamp] >= 2 for lamp in lamps) for lamps in switches) else 0)
`],
  ["17073", "tree-17073", "tree", "Tree Water", `import sys
input = sys.stdin.readline
n, w = map(int, input().split())
deg = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    deg[a] += 1
    deg[b] += 1
leaves = sum(1 for i in range(2, n + 1) if deg[i] == 1)
print(w / leaves)
`],
  ["17085", "brute_force-17085", "brute_force", "Crosses", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
crosses = []
for i in range(n):
    for j in range(m):
        if grid[i][j] != "#":
            continue
        cells = {(i, j)}
        k = 0
        while True:
            crosses.append((1 + 4 * k, set(cells)))
            k += 1
            added = [(i+k,j),(i-k,j),(i,j+k),(i,j-k)]
            if all(0 <= x < n and 0 <= y < m and grid[x][y] == "#" for x, y in added):
                cells.update(added)
            else:
                break
ans = 0
for a, ca in crosses:
    for b, cb in crosses:
        if ca.isdisjoint(cb):
            ans = max(ans, a * b)
print(ans)
`],
  ["17086", "graph_traversal-17086", "graph_traversal", "Baby Shark 2", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            dist[i][j] = 0
            q.append((i, j))
while q:
    x, y = q.popleft()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
print(max(map(max, dist)))
`],
  ["17090", "disjoint_set-17090", "disjoint_set", "Escape Room", `import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
state = [[0] * m for _ in range(n)]
dirs = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return 2
    if state[x][y]:
        return state[x][y]
    state[x][y] = 1
    dx, dy = dirs[grid[x][y]]
    res = dfs(x + dx, y + dy)
    state[x][y] = 2 if res == 2 else 3
    return state[x][y]
ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 2:
            ans += 1
print(ans)
`],
  ["17124", "binary_search-17124", "binary_search", "Two Arrays", `import bisect, sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    total = 0
    for x in a:
        idx = bisect.bisect_left(b, x)
        cand = []
        if idx < m:
            cand.append(b[idx])
        if idx:
            cand.append(b[idx - 1])
        total += min(cand, key=lambda y: (abs(y - x), y))
    out.append(str(total))
print("\\n".join(out))
`],
  ["17129", "graph_traversal-17129", "graph_traversal", "Williamson", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
q = deque()
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "2":
            q.append((i, j))
            dist[i][j] = 0
while q:
    x, y = q.popleft()
    if grid[x][y] in "345":
        print("TAK")
        print(dist[x][y])
        break
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "1" and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
else:
    print("NIE")
`],
  ["17179", "binary_search-17179", "binary_search", "Cake Cutting", `import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
cuts = [int(input()) for _ in range(m)] + [l]
queries = [int(input()) for _ in range(n)]
def can(q, length):
    prev = cnt = 0
    for cut in cuts:
        if cut - prev >= length:
            cnt += 1
            prev = cut
    return cnt >= q + 1
out = []
for q in queries:
    lo, hi = 1, l
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(q, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    out.append(str(ans))
print("\\n".join(out))
`],
  ["17208", "dynamic_programming_2-17208", "dynamic_programming_2", "Cow Burger", `import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(m + 1)]
for _ in range(n):
    b, f = map(int, input().split())
    for i in range(m, b - 1, -1):
        for j in range(k, f - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - b][j - f] + 1)
print(dp[m][k])
`],
  ["17265", "dynamic_programming_2-17265", "dynamic_programming_2", "My Life", `import sys
input = sys.stdin.readline
n = int(input())
grid = [input().split() for _ in range(n)]
mx = [[-10**18] * n for _ in range(n)]
mn = [[10**18] * n for _ in range(n)]
mx[0][0] = mn[0][0] = int(grid[0][0])
def calc(a, op, b):
    b = int(b)
    if op == "+": return a + b
    if op == "-": return a - b
    return a * b
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 1:
            continue
        for pi, pj, oi, oj in ((i-2,j,i-1,j),(i,j-2,i,j-1),(i-1,j-1,i-1,j),(i-1,j-1,i,j-1)):
            if 0 <= pi < n and 0 <= pj < n and 0 <= oi < n and 0 <= oj < n:
                op = grid[oi][oj]
                val = grid[i][j]
                for prev in (mx[pi][pj], mn[pi][pj]):
                    if -10**17 < prev < 10**17:
                        res = calc(prev, op, val)
                        mx[i][j] = max(mx[i][j], res)
                        mn[i][j] = min(mn[i][j], res)
print(mx[n-1][n-1], mn[n-1][n-1])
`],
  ["17845", "dynamic_programming_2-17845", "dynamic_programming_2", "Lecture", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(k):
    value, time = map(int, input().split())
    for t in range(n, time - 1, -1):
        dp[t] = max(dp[t], dp[t - time] + value)
print(dp[n])
`],
  ["17951", "binary_search-17951", "binary_search", "Test Groups", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
def ok(score):
    cnt = cur = 0
    for x in a:
        cur += x
        if cur >= score:
            cnt += 1
            cur = 0
    return cnt >= k
lo, hi = 0, sum(a)
while lo < hi:
    mid = (lo + hi + 1) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
`],
  ["18113", "binary_search-18113", "binary_search", "Ramen", `import sys
input = sys.stdin.readline
n, k, m = map(int, input().split())
pieces = []
for _ in range(n):
    x = int(input())
    if x >= 2 * k:
        pieces.append(x - 2 * k)
    elif x > k:
        pieces.append(x - k)
lo, hi = 1, max(pieces, default=0)
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if sum(x // mid for x in pieces) >= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
`],
  ["18114", "binary_search-18114", "binary_search", "Black Friday", `import bisect, sys
input = sys.stdin.readline
n, c = map(int, input().split())
a = sorted(map(int, input().split()))
if c in a:
    print(1)
    raise SystemExit
for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        if s == c:
            print(1)
            raise SystemExit
        if s < c:
            idx = bisect.bisect_left(a, c - s, j + 1)
            if idx < n and a[idx] == c - s:
                print(1)
                raise SystemExit
print(0)
`],
  ["18868", "brute_force-18868", "brute_force", "Multiverse 2", `import sys
input = sys.stdin.readline
m, n = map(int, input().split())
universes = []
for _ in range(m):
    arr = list(map(int, input().split()))
    order = {v:i for i, v in enumerate(sorted(set(arr)))}
    universes.append(tuple(order[x] for x in arr))
ans = 0
for i in range(m):
    for j in range(i + 1, m):
        if universes[i] == universes[j]:
            ans += 1
print(ans)
`],
  ["13019", "greedy-13019", "greedy", "A to B", `import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
if sorted(a) != sorted(b):
    print(-1)
else:
    i = j = len(a) - 1
    keep = 0
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            keep += 1
            i -= 1
            j -= 1
        else:
            i -= 1
    print(len(a) - keep)
`],
  ["19539", "greedy-19539", "greedy", "Apple Tree", `import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
s = sum(h)
print("YES" if s % 3 == 0 and sum(x // 2 for x in h) >= s // 3 else "NO")
`],
  ["19947", "brute_force-19947", "brute_force", "Investment", `import sys
h, y = map(int, sys.stdin.readline().split())
dp = [0] * (y + 1)
dp[0] = h
for i in range(1, y + 1):
    dp[i] = int(dp[i - 1] * 1.05)
    if i >= 3:
        dp[i] = max(dp[i], int(dp[i - 3] * 1.20))
    if i >= 5:
        dp[i] = max(dp[i], int(dp[i - 5] * 1.35))
print(dp[y])
`],
  ["20040", "disjoint_set-20040", "disjoint_set", "Cycle Game", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
for turn in range(1, m + 1):
    a, b = map(int, input().split())
    ra, rb = find(a), find(b)
    if ra == rb:
        print(turn)
        break
    parent[rb] = ra
else:
    print(0)
`],
  ["20116", "prefix_sum-20116", "prefix_sum", "Balance", `import sys
input = sys.stdin.readline
n, l = map(int, input().split())
x = list(map(int, input().split()))
total = x[-1]
ok = True
for i in range(n - 2, -1, -1):
    cnt = n - i - 1
    center = total / cnt
    if not (x[i] - l < center < x[i] + l):
        ok = False
        break
    total += x[i]
print("stable" if ok else "unstable")
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
  console.log(`[import-manual-batch-26] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-26] wrote ${OUT}`);
