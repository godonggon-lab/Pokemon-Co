import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["15732", "binary_search-15732", "binary_search", "Doyeon", `import sys
input = sys.stdin.readline
n, k, d = map(int, input().split())
rules = [tuple(map(int, input().split())) for _ in range(k)]
def count(x):
    total = 0
    for a, b, c in rules:
        if x >= a:
            total += (min(x, b) - a) // c + 1
    return total
lo, hi = 1, n
while lo < hi:
    mid = (lo + hi) // 2
    if count(mid) >= d:
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["15823", "binary_search-15823", "binary_search", "Card Pack", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
def ok(length):
    used = set()
    packs = cnt = left = 0
    for right, x in enumerate(a):
        while x in used:
            used.remove(a[left])
            left += 1
            cnt -= 1
        used.add(x)
        cnt += 1
        if cnt == length:
            packs += 1
            used.clear()
            cnt = 0
            left = right + 1
    return packs >= m
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi + 1) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
`],
  ["17175", "dynamic_programming_1-17175", "dynamic_programming_1", "Fibonacci Calls", `import sys
n = int(sys.stdin.readline())
MOD = 1000000007
dp = [0] * max(3, n + 1)
dp[0] = dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + 1) % MOD
print(dp[n])
`],
  ["17212", "dynamic_programming_1-17212", "dynamic_programming_1", "Coin", `import sys
n = int(sys.stdin.readline())
coins = [1, 2, 5, 7]
dp = [10**9] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for c in coins:
        if i >= c:
            dp[i] = min(dp[i], dp[i - c] + 1)
print(dp[n])
`],
  ["17266", "binary_search-17266", "binary_search", "Dark Road", `import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
x = list(map(int, input().split()))
ans = max(x[0], n - x[-1])
for a, b in zip(x, x[1:]):
    ans = max(ans, (b - a + 1) // 2)
print(ans)
`],
  ["17291", "dynamic_programming_1-17291", "dynamic_programming_1", "Fly", `import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1
for year in range(2, n + 1):
    born = dp[year - 1] * 2
    dead = 0
    for birth in range(1, year):
        age = year - birth
        if (birth <= 3 and age == 4) or (birth >= 4 and age == 3):
            dead += dp[birth] - (dp[birth - 1] * 2 if birth > 1 else 0)
    dp[year] = born - dead
print(dp[n])
`],
  ["17393", "binary_search-17393", "binary_search", "Shoot", `import bisect, sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
out = []
for i, power in enumerate(a):
    out.append(str(bisect.bisect_right(b, power) - i - 1))
print(" ".join(out))
`],
  ["17451", "binary_search-17451", "binary_search", "Parallel Universe", `import sys
input = sys.stdin.readline
n = int(input())
v = list(map(int, input().split()))
speed = 0
for x in reversed(v):
    if speed <= x:
        speed = x
    else:
        speed = ((speed + x - 1) // x) * x
print(speed)
`],
  ["17503", "binary_search-17503", "binary_search", "Beer Festival", `import heapq, sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
beers = sorted((tuple(map(int, input().split())) for _ in range(k)), key=lambda x: x[1])
heap = []
pref = 0
for favor, level in beers:
    heapq.heappush(heap, favor)
    pref += favor
    if len(heap) > n:
        pref -= heapq.heappop(heap)
    if len(heap) == n and pref >= m:
        print(level)
        break
else:
    print(-1)
`],
  ["17521", "brute_force-17521", "brute_force", "Byte Coin", `import sys
input = sys.stdin.readline
n, w = map(int, input().split())
prices = [int(input()) for _ in range(n)]
coin = 0
for i in range(n - 1):
    if prices[i] < prices[i + 1]:
        buy = w // prices[i]
        coin += buy
        w -= buy * prices[i]
    elif prices[i] > prices[i + 1]:
        w += coin * prices[i]
        coin = 0
w += coin * prices[-1]
print(w)
`],
  ["17610", "brute_force-17610", "brute_force", "Yangpal", `import sys
input = sys.stdin.readline
k = int(input())
w = list(map(int, input().split()))
possible = {0}
for x in w:
    nxt = set(possible)
    for s in possible:
        nxt.add(s + x)
        nxt.add(abs(s - x))
    possible = nxt
print(sum(1 for x in range(1, sum(w) + 1) if x not in possible))
`],
  ["17616", "graph_traversal-17616", "graph_traversal", "Ranking", `from collections import deque
import sys
input = sys.stdin.readline
n, m, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
rg = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    rg[b].append(a)
def count(start, graph):
    seen = [False] * (n + 1)
    seen[start] = True
    q = deque([start])
    c = 0
    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            if not seen[nx]:
                seen[nx] = True
                c += 1
                q.append(nx)
    return c
print(count(x, rg) + 1, n - count(x, g))
`],
  ["18223", "shortest_path-18223", "shortest_path", "Minjun and Masan", `import heapq, sys
input = sys.stdin.readline
v, e, p = map(int, input().split())
g = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
def dijkstra(start):
    dist = [10**15] * (v + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, x = heapq.heappop(pq)
        if d != dist[x]:
            continue
        for nx, w in g[x]:
            nd = d + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))
    return dist
d1 = dijkstra(1)
dp = dijkstra(p)
print("SAVE HIM" if d1[v] == d1[p] + dp[v] else "GOOD BYE")
`],
  ["18243", "shortest_path-18243", "shortest_path", "Small World", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
INF = 10**9
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(k):
    a, b = map(int, input().split())
    d[a - 1][b - 1] = d[b - 1][a - 1] = 1
for mid in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][mid] + d[mid][j]:
                d[i][j] = d[i][mid] + d[mid][j]
print("Small World!" if max(max(row) for row in d) <= 6 else "Big World!")
`],
  ["18352", "graph_traversal-18352", "graph_traversal", "Specific Distance City", `from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
dist = [-1] * (n + 1)
dist[x] = 0
q = deque([x])
while q:
    cur = q.popleft()
    for nx in g[cur]:
        if dist[nx] == -1:
            dist[nx] = dist[cur] + 1
            q.append(nx)
ans = [str(i) for i in range(1, n + 1) if dist[i] == k]
print("\\n".join(ans) if ans else -1)
`],
  ["18353", "dynamic_programming_1-18353", "dynamic_programming_1", "Soldiers", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
`],
  ["18404", "graph_traversal-18404", "graph_traversal", "Knight Move", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x, y = map(int, input().split())
targets = [tuple(map(int, input().split())) for _ in range(m)]
dist = [[-1] * (n + 1) for _ in range(n + 1)]
dist[x][y] = 0
q = deque([(x, y)])
moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
while q:
    a, b = q.popleft()
    for da, db in moves:
        na, nb = a + da, b + db
        if 1 <= na <= n and 1 <= nb <= n and dist[na][nb] == -1:
            dist[na][nb] = dist[a][b] + 1
            q.append((na, nb))
print(" ".join(str(dist[a][b]) for a, b in targets))
`],
  ["18405", "graph_traversal-18405", "graph_traversal", "Competitive Infection", `from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s, tx, ty = map(int, input().split())
q = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            q.append((grid[i][j], 0, i, j))
q = deque(sorted(q))
while q:
    virus, time, x, y = q.popleft()
    if time == s:
        continue
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            grid[nx][ny] = virus
            q.append((virus, time + 1, nx, ny))
print(grid[tx - 1][ty - 1])
`],
  ["18429", "backtracking-18429", "backtracking", "Muscle Loss", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
used = [False] * n
ans = 0
def dfs(day, weight):
    global ans
    if day == n:
        ans += 1
        return
    for i in range(n):
        if not used[i] and weight + a[i] - k >= 500:
            used[i] = True
            dfs(day + 1, weight + a[i] - k)
            used[i] = False
dfs(0, 500)
print(ans)
`],
  ["18512", "brute_force-18512", "brute_force", "Jumping", `import sys
x, y, p1, p2 = map(int, sys.stdin.readline().split())
seen = set()
for i in range(10000):
    seen.add(p1 + x * i)
ans = -1
for j in range(10000):
    v = p2 + y * j
    if v in seen:
        ans = v
        break
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
  console.log(`[import-manual-batch-25] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-25] wrote ${OUT}`);
