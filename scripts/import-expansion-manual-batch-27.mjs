import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["10819", "backtracking-10819", "backtracking", "Difference Maximum", `from itertools import permutations
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = 0
for p in permutations(a):
    ans = max(ans, sum(abs(p[i] - p[i + 1]) for i in range(n - 1)))
print(ans)
`],
  ["10971", "backtracking-10971", "backtracking", "TSP 2", `import sys
input = sys.stdin.readline
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
INF = 10**15
ans = INF
for start in range(n):
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0
    for mask in range(1 << n):
        for cur in range(n):
            cost = dp[mask][cur]
            if cost == INF:
                continue
            for nxt in range(n):
                if mask & (1 << nxt) or w[cur][nxt] == 0:
                    continue
                nm = mask | (1 << nxt)
                dp[nm][nxt] = min(dp[nm][nxt], cost + w[cur][nxt])
    full = (1 << n) - 1
    for last in range(n):
        if last != start and w[last][start]:
            ans = min(ans, dp[full][last] + w[last][start])
print(ans)
`],
  ["12893", "disjoint_set-12893", "disjoint_set", "Enemies", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
color = [0] * (n + 1)
for s in range(1, n + 1):
    if color[s]:
        continue
    color[s] = 1
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if color[y] == color[x]:
                print(0)
                raise SystemExit
            if color[y] == 0:
                color[y] = -color[x]
                q.append(y)
print(1)
`],
  ["14888", "backtracking-14888", "backtracking", "Operator Insertion", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))
mn, mx = 10**18, -10**18
def div(x, y):
    return x // y if x >= 0 else -((-x) // y)
def dfs(idx, value):
    global mn, mx
    if idx == n:
        mn = min(mn, value)
        mx = max(mx, value)
        return
    for op in range(4):
        if ops[op] == 0:
            continue
        ops[op] -= 1
        if op == 0:
            dfs(idx + 1, value + a[idx])
        elif op == 1:
            dfs(idx + 1, value - a[idx])
        elif op == 2:
            dfs(idx + 1, value * a[idx])
        else:
            dfs(idx + 1, div(value, a[idx]))
        ops[op] += 1
dfs(1, a[0])
print(mx)
print(mn)
`],
  ["14925", "dynamic_programming_2-14925", "dynamic_programming_2", "Build Farm", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j, value in enumerate(row, 1):
        if value == 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            ans = max(ans, dp[i][j])
print(ans)
`],
  ["14938", "shortest_path-14938", "shortest_path", "Seogang Ground", `import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = 10**9
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = min(dist[a][b], l)
    dist[b][a] = min(dist[b][a], l)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        dik = dist[i][k]
        for j in range(1, n + 1):
            if dist[i][j] > dik + dist[k][j]:
                dist[i][j] = dik + dist[k][j]
ans = 0
for i in range(1, n + 1):
    ans = max(ans, sum(items[j] for j in range(1, n + 1) if dist[i][j] <= m))
print(ans)
`],
  ["15686", "brute_force-15686", "brute_force", "Chicken Delivery", `from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
homes, chickens = [], []
for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 1:
            homes.append((i, j))
        elif v == 2:
            chickens.append((i, j))
ans = 10**9
for picked in combinations(chickens, m):
    total = 0
    for hx, hy in homes:
        total += min(abs(hx - cx) + abs(hy - cy) for cx, cy in picked)
    ans = min(ans, total)
print(ans)
`],
  ["16168", "disjoint_set-16168", "disjoint_set", "Parade", `import sys
input = sys.stdin.readline
v, e = map(int, input().split())
parent = list(range(v + 1))
deg = [0] * (v + 1)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
for _ in range(e):
    a, b = map(int, input().split())
    deg[a] += 1
    deg[b] += 1
    union(a, b)
used = [i for i in range(1, v + 1) if deg[i] > 0]
connected = not used or len({find(i) for i in used}) == 1
odd = sum(d % 2 for d in deg)
print("YES" if connected and odd in (0, 2) else "NO")
`],
  ["17070", "dynamic_programming_2-17070", "dynamic_programming_2", "Move Pipe 1", `import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(2, n):
        if grid[i][j]:
            continue
        dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2]
        if i > 0:
            dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
        if i > 0 and grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
            dp[i][j][2] += sum(dp[i - 1][j - 1])
print(sum(dp[n - 1][n - 1]))
`],
  ["17484", "brute_force-17484", "brute_force", "Jinwoo's Moon Travel", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]
INF = 10**9
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
for j in range(m):
    for d in range(3):
        dp[0][j][d] = fuel[0][j]
for i in range(1, n):
    for j in range(m):
        for nd, pj in enumerate((j + 1, j, j - 1)):
            if 0 <= pj < m:
                for pd in range(3):
                    if pd != nd:
                        dp[i][j][nd] = min(dp[i][j][nd], dp[i - 1][pj][pd] + fuel[i][j])
print(min(min(row) for row in dp[-1]))
`],
  ["18290", "backtracking-18290", "backtracking", "NM and K", `import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
used = [[False] * m for _ in range(n)]
cells = [(i, j) for i in range(n) for j in range(m)]
ans = -10**18
def ok(x, y):
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and used[nx][ny]:
            return False
    return True
def dfs(idx, cnt, total):
    global ans
    if cnt == k:
        ans = max(ans, total)
        return
    if idx == len(cells):
        return
    if len(cells) - idx < k - cnt:
        return
    x, y = cells[idx]
    if ok(x, y):
        used[x][y] = True
        dfs(idx + 1, cnt + 1, total + grid[x][y])
        used[x][y] = False
    dfs(idx + 1, cnt, total)
dfs(0, 0, 0)
print(ans)
`],
  ["19699", "backtracking-19699", "backtracking", "Barn Cow", `from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
w = list(map(int, input().split()))
limit = sum(sorted(w, reverse=True)[:m])
prime = [True] * (limit + 1)
if limit >= 0:
    prime[0] = False
if limit >= 1:
    prime[1] = False
for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False
ans = sorted({sum(c) for c in combinations(w, m) if prime[sum(c)]})
print(*ans if ans else [-1])
`],
  ["19949", "backtracking-19949", "backtracking", "Yeongjae's Exam", `import sys
from functools import lru_cache
answers = list(map(int, sys.stdin.readline().split()))
@lru_cache(None)
def dfs(idx, prev1, prev2, score):
    if idx == 10:
        return 1 if score >= 5 else 0
    total = 0
    for x in range(1, 6):
        if x == prev1 == prev2:
            continue
        total += dfs(idx + 1, x, prev1, score + (x == answers[idx]))
    return total
print(dfs(0, 0, 0, 0))
`],
  ["20117", "greedy-20117", "greedy", "Strange Quality", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
print(sum(a[n // 2:]))
`],
  ["20364", "tree-20364", "tree", "Real Estate Fight", `import sys
input = sys.stdin.readline
n, q = map(int, input().split())
occupied = [False] * (n + 1)
out = []
for _ in range(q):
    x = int(input())
    cur = x
    blocked = 0
    while cur:
        if occupied[cur]:
            blocked = cur
        cur //= 2
    out.append(str(blocked))
    if blocked == 0:
        occupied[x] = True
print("\\n".join(out))
`],
  ["20551", "binary_search-20551", "binary_search", "Sort My Cards", `import bisect, sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
out = []
for _ in range(m):
    q = int(input())
    idx = bisect.bisect_left(a, q)
    out.append(str(idx if idx < n and a[idx] == q else -1))
print("\\n".join(out))
`],
  ["21313", "greedy-21313", "greedy", "Octopus", `import sys
n = int(sys.stdin.readline())
ans = [1 if i % 2 == 0 else 2 for i in range(n)]
if n % 2 == 1 and n > 1:
    ans[-1] = 3
print(*ans)
`],
  ["21314", "greedy-21314", "greedy", "Minkyum Number", `import sys
s = sys.stdin.readline().strip()
mx = []
cnt = 0
for ch in s:
    if ch == "M":
        cnt += 1
    else:
        mx.append("5" + "0" * cnt)
        cnt = 0
if cnt:
    mx.append("1" * cnt)
mn = []
cnt = 0
for ch in s:
    if ch == "M":
        cnt += 1
    else:
        if cnt:
            mn.append("1" + "0" * (cnt - 1))
        mn.append("5")
        cnt = 0
if cnt:
    mn.append("1" + "0" * (cnt - 1))
print("".join(mx))
print("".join(mn))
`],
  ["21921", "two_pointer-21921", "two_pointer", "Blog", `import sys
input = sys.stdin.readline
n, x = map(int, input().split())
a = list(map(int, input().split()))
cur = sum(a[:x])
best = cur
cnt = 1
for i in range(x, n):
    cur += a[i] - a[i - x]
    if cur > best:
        best = cur
        cnt = 1
    elif cur == best:
        cnt += 1
if best == 0:
    print("SAD")
else:
    print(best)
    print(cnt)
`],
  ["22862", "two_pointer-22862", "two_pointer", "Longest Even Subsequence", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
left = odd = even = ans = 0
for right, value in enumerate(a):
    if value % 2:
        odd += 1
    else:
        even += 1
    while odd > k:
        if a[left] % 2:
            odd -= 1
        else:
            even -= 1
        left += 1
    ans = max(ans, even)
print(ans)
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
  console.log(`[import-manual-batch-27] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-27] wrote ${OUT}`);
