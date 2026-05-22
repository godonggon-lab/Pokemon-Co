import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1167", "tree-1167", "tree", "Tree Diameter", `from collections import deque
import sys
input = sys.stdin.readline
v = int(input())
g = [[] for _ in range(v + 1)]
for _ in range(v):
    data = list(map(int, input().split()))
    x = data[0]
    i = 1
    while data[i] != -1:
        g[x].append((data[i], data[i + 1]))
        i += 2
def far(start):
    dist = [-1] * (v + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for nx, w in g[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + w
                q.append(nx)
    node = max(range(1, v + 1), key=lambda i: dist[i])
    return node, dist[node]
a, _ = far(1)
_, ans = far(a)
print(ans)
`],
  ["1248", "backtracking-1248", "backtracking", "Guess", `import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
sign = [[""] * n for _ in range(n)]
idx = 0
for i in range(n):
    for j in range(i, n):
        sign[i][j] = s[idx]
        idx += 1
ans = []
def ok(pos):
    total = 0
    for i in range(pos, -1, -1):
        total += ans[i]
        c = sign[i][pos]
        if c == "+" and total <= 0:
            return False
        if c == "-" and total >= 0:
            return False
        if c == "0" and total != 0:
            return False
    return True
def dfs(pos):
    if pos == n:
        print(*ans)
        raise SystemExit
    candidates = [0] if sign[pos][pos] == "0" else (range(1, 11) if sign[pos][pos] == "+" else range(-10, 0))
    for x in candidates:
        ans.append(x)
        if ok(pos):
            dfs(pos + 1)
        ans.pop()
dfs(0)
`],
  ["1493", "divide_and_conquer-1493", "divide_and_conquer", "Fill Box", `import sys
input = sys.stdin.readline
l, w, h = map(int, input().split())
n = int(input())
cubes = [0] * 20
for _ in range(n):
    a, b = map(int, input().split())
    cubes[a] = b
used = 0
filled = 0
for i in range(19, -1, -1):
    filled *= 8
    fit = (l >> i) * (w >> i) * (h >> i) - filled
    take = min(fit, cubes[i])
    used += take
    filled += take
print(used if filled == l * w * h else -1)
`],
  ["1595", "tree-1595", "tree", "Northern Lights", `from collections import defaultdict, deque
import sys
g = defaultdict(list)
nodes = set()
for line in sys.stdin:
    if not line.strip():
        continue
    a, b, c = map(int, line.split())
    g[a].append((b, c))
    g[b].append((a, c))
    nodes.add(a); nodes.add(b)
if not nodes:
    print(0)
else:
    def far(start):
        dist = {start: 0}
        q = deque([start])
        while q:
            x = q.popleft()
            for nx, w in g[x]:
                if nx not in dist:
                    dist[nx] = dist[x] + w
                    q.append(nx)
        node = max(dist, key=dist.get)
        return node, dist[node]
    a, _ = far(next(iter(nodes)))
    _, ans = far(a)
    print(ans)
`],
  ["1753", "shortest_path-1753", "shortest_path", "Shortest Path", `import heapq, sys
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
g = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
dist = [10**18] * (v + 1)
dist[k] = 0
pq = [(0, k)]
while pq:
    d, x = heapq.heappop(pq)
    if d != dist[x]:
        continue
    for nx, w in g[x]:
        nd = d + w
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(pq, (nd, nx))
print("\\n".join("INF" if dist[i] == 10**18 else str(dist[i]) for i in range(1, v + 1)))
`],
  ["1865", "shortest_path-1865", "shortest_path", "Wormholes", `import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    dist = [0] * (n + 1)
    neg = False
    for i in range(n):
        updated = False
        for a, b, c in edges:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                updated = True
                if i == n - 1:
                    neg = True
                    break
        if neg or not updated:
            break
    out.append("YES" if neg else "NO")
print("\\n".join(out))
`],
  ["1937", "dynamic_programming_2-1937", "dynamic_programming_2", "Greedy Panda", `import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > a[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]
print(max(dfs(i, j) for i in range(n) for j in range(n)))
`],
  ["1939", "binary_search-1939", "binary_search", "Weight Limit", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
hi = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
    hi = max(hi, c)
s, e = map(int, input().split())
def can(limit):
    seen = [False] * (n + 1)
    seen[s] = True
    q = deque([s])
    while q:
        x = q.popleft()
        if x == e:
            return True
        for nx, w in g[x]:
            if not seen[nx] and w >= limit:
                seen[nx] = True
                q.append(nx)
    return False
lo, ans = 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
`],
  ["1948", "topological_sorting-1948", "topological_sorting", "Critical Path", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    rev[b].append((a, c))
    indeg[b] += 1
s, e = map(int, input().split())
q = deque([s])
dist = [0] * (n + 1)
while q:
    x = q.popleft()
    for nx, w in g[x]:
        if dist[nx] < dist[x] + w:
            dist[nx] = dist[x] + w
        indeg[nx] -= 1
        if indeg[nx] == 0:
            q.append(nx)
cnt = 0
seen = [False] * (n + 1)
seen[e] = True
q = deque([e])
while q:
    x = q.popleft()
    for px, w in rev[x]:
        if dist[x] == dist[px] + w:
            cnt += 1
            if not seen[px]:
                seen[px] = True
                q.append(px)
print(dist[e])
print(cnt)
`],
  ["1956", "shortest_path-1956", "shortest_path", "Exercise", `import sys
input = sys.stdin.readline
v, e = map(int, input().split())
INF = 10**12
d = [[INF] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = min(d[a - 1][b - 1], c)
for k in range(v):
    for i in range(v):
        for j in range(v):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
ans = min(d[i][i] for i in range(v))
print(ans if ans < INF else -1)
`],
  ["1987", "backtracking-1987", "backtracking", "Alphabet", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]
ans = 0
def dfs(x, y, mask, depth):
    global ans
    ans = max(ans, depth)
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            bit = 1 << (ord(board[nx][ny]) - 65)
            if not (mask & bit):
                dfs(nx, ny, mask | bit, depth + 1)
dfs(0, 0, 1 << (ord(board[0][0]) - 65), 1)
print(ans)
`],
  ["2022", "binary_search-2022", "binary_search", "Ladder", `import math, sys
x, y, c = map(float, sys.stdin.readline().split())
lo, hi = 0.0, min(x, y)
for _ in range(100):
    mid = (lo + hi) / 2
    h1 = math.sqrt(x * x - mid * mid)
    h2 = math.sqrt(y * y - mid * mid)
    cc = h1 * h2 / (h1 + h2)
    if cc > c:
        lo = mid
    else:
        hi = mid
print(f"{lo:.3f}")
`],
  ["2023", "backtracking-2023", "backtracking", "Interesting Prime", `import math, sys
n = int(sys.stdin.readline())
def prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
out = []
def dfs(x, length):
    if length == n:
        out.append(str(x))
        return
    for d in (1, 3, 7, 9):
        nx = x * 10 + d
        if prime(nx):
            dfs(nx, length + 1)
for start in (2, 3, 5, 7):
    dfs(start, 1)
print("\\n".join(out))
`],
  ["2056", "dynamic_programming_2-2056", "dynamic_programming_2", "Work", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
time = [0] * (n + 1)
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for pre in data[2:]:
        g[pre].append(i)
        indeg[i] += 1
q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
for i in q:
    dp[i] = time[i]
while q:
    x = q.popleft()
    for nx in g[x]:
        dp[nx] = max(dp[nx], dp[x] + time[nx])
        indeg[nx] -= 1
        if indeg[nx] == 0:
            q.append(nx)
print(max(dp))
`],
  ["2109", "greedy-2109", "greedy", "Lecture Tour", `import heapq, sys
input = sys.stdin.readline
n = int(input())
jobs = sorted((tuple(map(int, input().split())) for _ in range(n)), key=lambda x: x[1])
heap = []
for pay, day in jobs:
    heapq.heappush(heap, pay)
    if len(heap) > day:
        heapq.heappop(heap)
print(sum(heap))
`],
  ["2118", "two_pointer-2118", "two_pointer", "Two Towers", `import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
total = sum(a)
ans = cur = 0
r = 0
for l in range(n):
    while cur * 2 < total:
        cur += a[r % n]
        r += 1
    ans = max(ans, min(cur, total - cur))
    cur -= a[l]
print(ans)
`],
  ["2146", "graph_traversal-2146", "graph_traversal", "Bridge Making", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
label = 1
q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            label += 1
            grid[i][j] = label
            qq = deque([(i, j)])
            while qq:
                x, y = qq.popleft()
                q.append((x, y))
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = label
                        qq.append((nx, ny))
dist = [[0] * n for _ in range(n)]
ans = 10**9
while q:
    x, y = q.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            elif grid[nx][ny] != grid[x][y]:
                ans = min(ans, dist[nx][ny] + dist[x][y])
print(ans)
`],
  ["2224", "shortest_path-2224", "shortest_path", "Propositions", `import sys
input = sys.stdin.readline
n = int(input())
reach = [[False] * 52 for _ in range(52)]
def idx(ch):
    return ord(ch) - 65 if ch <= "Z" else ord(ch) - 71
def ch(i):
    return chr(i + 65) if i < 26 else chr(i + 71)
for _ in range(n):
    a, _, b = input().split()
    reach[idx(a)][idx(b)] = True
for k in range(52):
    for i in range(52):
        if reach[i][k]:
            for j in range(52):
                reach[i][j] = reach[i][j] or reach[k][j]
out = []
for i in range(52):
    for j in range(52):
        if i != j and reach[i][j]:
            out.append(f"{ch(i)} => {ch(j)}")
print(len(out))
print("\\n".join(out))
`],
  ["2252", "topological_sorting-2252", "topological_sorting", "Line Up", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
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
print(*out)
`],
  ["2458", "shortest_path-2458", "shortest_path", "Height Order", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
reach = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    reach[a - 1][b - 1] = True
for k in range(n):
    for i in range(n):
        if reach[i][k]:
            for j in range(n):
                reach[i][j] = reach[i][j] or reach[k][j]
ans = 0
for i in range(n):
    known = 0
    for j in range(n):
        if i != j and (reach[i][j] or reach[j][i]):
            known += 1
    if known == n - 1:
        ans += 1
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
  console.log(`[import-manual-batch-20] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-20] wrote ${OUT}`);
