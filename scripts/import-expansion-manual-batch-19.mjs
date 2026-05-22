import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1025", "brute_force-1025", "brute_force", "Find Square", `import math, sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
ans = -1
for sx in range(n):
    for sy in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == 0 and dy == 0:
                    continue
                x, y = sx, sy
                s = ""
                while 0 <= x < n and 0 <= y < m:
                    s += grid[x][y]
                    v = int(s)
                    r = math.isqrt(v)
                    if r * r == v:
                        ans = max(ans, v)
                    x += dx
                    y += dy
print(ans)
`],
  ["1062", "backtracking-1062", "backtracking", "Teaching", `import itertools, sys
input = sys.stdin.readline
n, k = map(int, input().split())
base = set("antic")
words = []
for _ in range(n):
    mask = 0
    for ch in set(input().strip()) - base:
        mask |= 1 << (ord(ch) - 97)
    words.append(mask)
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    candidates = [i for i in range(26) if chr(i + 97) not in base]
    ans = 0
    for comb in itertools.combinations(candidates, k - 5):
        teach = 0
        for i in comb:
            teach |= 1 << i
        ans = max(ans, sum((w & ~teach) == 0 for w in words))
    print(ans)
`],
  ["1166", "binary_search-1166", "binary_search", "Gift", `import sys
n, l, w, h = map(float, sys.stdin.readline().split())
lo, hi = 0.0, min(l, w, h)
for _ in range(100):
    mid = (lo + hi) / 2
    if int(l // mid) * int(w // mid) * int(h // mid) >= n:
        lo = mid
    else:
        hi = mid
print(lo)
`],
  ["1174", "backtracking-1174", "backtracking", "Decreasing Number", `import itertools, sys
n = int(sys.stdin.readline())
nums = []
for r in range(1, 11):
    for comb in itertools.combinations("9876543210", r):
        nums.append(int("".join(comb)))
nums.sort()
print(nums[n - 1] if n <= len(nums) else -1)
`],
  ["1240", "graph_traversal-1240", "graph_traversal", "Distance Between Nodes", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
out = []
for _ in range(m):
    s, e = map(int, input().split())
    q = deque([(s, 0)])
    seen = [False] * (n + 1)
    seen[s] = True
    while q:
        x, d = q.popleft()
        if x == e:
            out.append(str(d))
            break
        for nx, w in g[x]:
            if not seen[nx]:
                seen[nx] = True
                q.append((nx, d + w))
print("\\n".join(out))
`],
  ["1261", "shortest_path-1261", "shortest_path", "Algospot", `from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
grid = [input().strip() for _ in range(n)]
dist = [[10**9] * m for _ in range(n)]
dist[0][0] = 0
dq = deque([(0, 0)])
while dq:
    x, y = dq.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            nd = dist[x][y] + (grid[nx][ny] == "1")
            if nd < dist[nx][ny]:
                dist[nx][ny] = nd
                (dq.append if grid[nx][ny] == "1" else dq.appendleft)((nx, ny))
print(dist[n - 1][m - 1])
`],
  ["1300", "binary_search-1300", "binary_search", "K-th Number", `import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
lo, hi = 1, k
ans = k
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = sum(min(n, mid // i) for i in range(1, n + 1))
    if cnt >= k:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)
`],
  ["1342", "backtracking-1342", "backtracking", "Lucky String", `from collections import Counter
import sys
s = sys.stdin.readline().strip()
cnt = Counter(s)
ans = 0
def dfs(prev, left):
    global ans
    if left == 0:
        ans += 1
        return
    for ch in list(cnt):
        if cnt[ch] and ch != prev:
            cnt[ch] -= 1
            dfs(ch, left - 1)
            cnt[ch] += 1
dfs("", len(s))
print(ans)
`],
  ["1359", "math-1359", "math", "Lottery", `import math, sys
n, m, k = map(int, sys.stdin.readline().split())
total = math.comb(n, m)
good = 0
for i in range(k, m + 1):
    if n - m >= m - i:
        good += math.comb(m, i) * math.comb(n - m, m - i)
print(good / total)
`],
  ["1389", "shortest_path-1389", "shortest_path", "Kevin Bacon", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 10**9
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    d[a - 1][b - 1] = d[b - 1][a - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
print(min(range(n), key=lambda i: (sum(d[i]), i)) + 1)
`],
  ["1414", "minimum_spanning_tree-1414", "minimum_spanning_tree", "Bulbs", `import sys
input = sys.stdin.readline
n = int(input())
parent = list(range(n))
def val(ch):
    if ch == "0":
        return 0
    if "a" <= ch <= "z":
        return ord(ch) - 96
    return ord(ch) - 38
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True
edges = []
total = 0
for i in range(n):
    row = input().strip()
    for j, ch in enumerate(row):
        w = val(ch)
        total += w
        if i != j and w:
            edges.append((w, i, j))
used = cnt = 0
for w, a, b in sorted(edges):
    if union(a, b):
        used += w
        cnt += 1
print(total - used if cnt == n - 1 else -1)
`],
  ["1446", "dynamic_programming_1-1446", "dynamic_programming_1", "Shortcut", `import sys
input = sys.stdin.readline
n, d = map(int, input().split())
shortcuts = [[] for _ in range(d + 1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d and b - a > c:
        shortcuts[b].append((a, c))
dp = list(range(d + 1))
for i in range(1, d + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for a, c in shortcuts[i]:
        dp[i] = min(dp[i], dp[a] + c)
print(dp[d])
`],
  ["1495", "dynamic_programming_1-1495", "dynamic_programming_1", "Guitarist", `import sys
input = sys.stdin.readline
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
cur = {s}
for x in v:
    nxt = set()
    for vol in cur:
        if vol + x <= m:
            nxt.add(vol + x)
        if vol - x >= 0:
            nxt.add(vol - x)
    cur = nxt
    if not cur:
        break
print(max(cur) if cur else -1)
`],
  ["1504", "shortest_path-1504", "shortest_path", "Specific Shortest Path", `import heapq, sys
input = sys.stdin.readline
n, e = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
v1, v2 = map(int, input().split())
def dijkstra(start):
    dist = [10**15] * (n + 1)
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
d1, dv1, dv2 = dijkstra(1), dijkstra(v1), dijkstra(v2)
ans = min(d1[v1] + dv1[v2] + dv2[n], d1[v2] + dv2[v1] + dv1[n])
print(ans if ans < 10**15 else -1)
`],
  ["1535", "dynamic_programming_1-1535", "dynamic_programming_1", "Hello", `import sys
input = sys.stdin.readline
n = int(input())
loss = list(map(int, input().split()))
joy = list(map(int, input().split()))
dp = [0] * 100
for l, j in zip(loss, joy):
    for hp in range(99, l - 1, -1):
        dp[hp] = max(dp[hp], dp[hp - l] + j)
print(max(dp))
`],
  ["1561", "binary_search-1561", "binary_search", "Amusement Park", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rides = list(map(int, input().split()))
if n <= m:
    print(n)
else:
    lo, hi = 0, min(rides) * n
    while lo < hi:
        mid = (lo + hi) // 2
        served = m + sum(mid // r for r in rides)
        if served >= n:
            hi = mid
        else:
            lo = mid + 1
    t = lo
    served = m + sum((t - 1) // r for r in rides)
    for i, r in enumerate(rides, 1):
        if t % r == 0:
            served += 1
            if served == n:
                print(i)
                break
`],
  ["1577", "dynamic_programming_1-1577", "dynamic_programming_1", "Roads", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
blocked = set()
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    blocked.add(tuple(sorted(((a, b), (c, d)))))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for x in range(n + 1):
    for y in range(m + 1):
        if x < n and tuple(sorted(((x, y), (x + 1, y)))) not in blocked:
            dp[x + 1][y] += dp[x][y]
        if y < m and tuple(sorted(((x, y), (x, y + 1)))) not in blocked:
            dp[x][y + 1] += dp[x][y]
print(dp[n][m])
`],
  ["1600", "graph_traversal-1600", "graph_traversal", "Monkey Horse", `from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
dist = [[[-1] * (k + 1) for _ in range(w)] for __ in range(h)]
dist[0][0][0] = 0
q = deque([(0, 0, 0)])
normal = [(1,0),(-1,0),(0,1),(0,-1)]
horse = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
while q:
    x, y, used = q.popleft()
    if x == h - 1 and y == w - 1:
        print(dist[x][y][used])
        break
    for dx, dy in normal:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0 and dist[nx][ny][used] == -1:
            dist[nx][ny][used] = dist[x][y][used] + 1
            q.append((nx, ny, used))
    if used < k:
        for dx, dy in horse:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0 and dist[nx][ny][used + 1] == -1:
                dist[nx][ny][used + 1] = dist[x][y][used] + 1
                q.append((nx, ny, used + 1))
else:
    print(-1)
`],
  ["1613", "shortest_path-1613", "shortest_path", "History", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
reach = [[False] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    reach[a - 1][b - 1] = True
for mid in range(n):
    for i in range(n):
        if reach[i][mid]:
            for j in range(n):
                reach[i][j] = reach[i][j] or reach[mid][j]
out = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if reach[a][b]:
        out.append("-1")
    elif reach[b][a]:
        out.append("1")
    else:
        out.append("0")
print("\\n".join(out))
`],
  ["1695", "dynamic_programming_2-1695", "dynamic_programming_2", "Palindrome Making", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        if a[l] == a[r]:
            dp[l][r] = dp[l + 1][r - 1] if l + 1 <= r - 1 else 0
        else:
            dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + 1
print(dp[0][n - 1])
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
  console.log(`[import-manual-batch-19] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-19] wrote ${OUT}`);
