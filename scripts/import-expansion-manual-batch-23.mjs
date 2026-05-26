import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["11049", "dynamic_programming_2-11049", "dynamic_programming_2", "Matrix Chain Multiplication", `import sys
input = sys.stdin.readline
n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        dp[l][r] = 10**18
        for k in range(l, r):
            cost = dp[l][k] + dp[k + 1][r] + mat[l][0] * mat[k][1] * mat[r][1]
            dp[l][r] = min(dp[l][r], cost)
print(dp[0][n - 1])
`],
  ["11066", "dynamic_programming_2-11066", "dynamic_programming_2", "File Merge", `import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    k = int(input())
    a = [0] + list(map(int, input().split()))
    prefix = [0] * (k + 1)
    for i in range(1, k + 1):
        prefix[i] = prefix[i - 1] + a[i]
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    for length in range(2, k + 1):
        for l in range(1, k - length + 2):
            r = l + length - 1
            dp[l][r] = min(dp[l][m] + dp[m + 1][r] for m in range(l, r)) + prefix[r] - prefix[l - 1]
    out.append(str(dp[1][k]))
print("\\n".join(out))
`],
  ["11265", "shortest_path-11265", "shortest_path", "Party", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
out = []
for _ in range(m):
    a, b, c = map(int, input().split())
    out.append("Enjoy other party" if d[a - 1][b - 1] <= c else "Stay here")
print("\\n".join(out))
`],
  ["11562", "shortest_path-11562", "shortest_path", "Backdoor", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 10**9
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    d[a][b] = 0
    d[b][a] = 0 if c == 1 else 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
out = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    out.append(str(d[s - 1][e - 1]))
print("\\n".join(out))
`],
  ["11657", "shortest_path-11657", "shortest_path", "Time Machine", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0
neg = False
for i in range(n):
    updated = False
    for a, b, c in edges:
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            updated = True
            if i == n - 1:
                neg = True
    if not updated:
        break
if neg:
    print(-1)
else:
    print("\\n".join(str(dist[i]) if dist[i] != INF else "-1" for i in range(2, n + 1)))
`],
  ["12865", "dynamic_programming_2-12865", "dynamic_programming_2", "Ordinary Knapsack", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (k + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for cap in range(k, w - 1, -1):
        dp[cap] = max(dp[cap], dp[cap - w] + v)
print(dp[k])
`],
  ["13302", "dynamic_programming_2-13302", "dynamic_programming_2", "Resort", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
closed = set(map(int, input().split())) if m else set()
INF = 10**9
dp = [[INF] * 45 for _ in range(n + 6)]
dp[0][0] = 0
for day in range(n):
    for coupon in range(45):
        if dp[day][coupon] == INF:
            continue
        if day + 1 in closed:
            dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon])
        else:
            dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon] + 10000)
            dp[day + 3][coupon + 1] = min(dp[day + 3][coupon + 1], dp[day][coupon] + 25000)
            dp[day + 5][coupon + 2] = min(dp[day + 5][coupon + 2], dp[day][coupon] + 37000)
            if coupon >= 3:
                dp[day + 1][coupon - 3] = min(dp[day + 1][coupon - 3], dp[day][coupon])
print(min(dp[n]))
`],
  ["13397", "binary_search-13397", "binary_search", "Divide Sequence 2", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
def ok(limit):
    groups = 1
    mn = mx = a[0]
    for x in a[1:]:
        mn = min(mn, x)
        mx = max(mx, x)
        if mx - mn > limit:
            groups += 1
            mn = mx = x
    return groups <= m
lo, hi = 0, max(a) - min(a)
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["13424", "shortest_path-13424", "shortest_path", "Secret Meeting", `import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    INF = 10**9
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        d[a - 1][b - 1] = d[b - 1][a - 1] = min(d[a - 1][b - 1], c)
    friends_n = int(input())
    friends = [x - 1 for x in map(int, input().split())]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    best = min(range(n), key=lambda room: (sum(d[f][room] for f in friends), room))
    out.append(str(best + 1))
print("\\n".join(out))
`],
  ["13565", "graph_traversal-13565", "graph_traversal", "Percolation", `from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
grid = [input().strip() for _ in range(m)]
q = deque()
seen = [[False] * n for _ in range(m)]
for j in range(n):
    if grid[0][j] == "0":
        q.append((0, j))
        seen[0][j] = True
while q:
    x, y = q.popleft()
    if x == m - 1:
        print("YES")
        break
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and not seen[nx][ny] and grid[nx][ny] == "0":
            seen[nx][ny] = True
            q.append((nx, ny))
else:
    print("NO")
`],
  ["14226", "dynamic_programming_2-14226", "dynamic_programming_2", "Emoticon", `from collections import deque
import sys
s = int(sys.stdin.readline())
limit = 1001
dist = [[-1] * limit for _ in range(limit)]
dist[1][0] = 0
q = deque([(1, 0)])
while q:
    screen, clip = q.popleft()
    if screen == s:
        print(dist[screen][clip])
        break
    moves = [(screen, screen), (screen + clip, clip), (screen - 1, clip)]
    for ns, nc in moves:
        if 0 <= ns < limit and 0 <= nc < limit and dist[ns][nc] == -1:
            dist[ns][nc] = dist[screen][clip] + 1
            q.append((ns, nc))
`],
  ["14267", "tree-14267", "tree", "Company Culture 1", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parents = list(map(int, input().split()))
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    children[parents[i - 1]].append(i)
score = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    score[i] += w
stack = [1]
order = []
while stack:
    x = stack.pop()
    order.append(x)
    stack.extend(children[x])
for x in order:
    for nx in children[x]:
        score[nx] += score[x]
print(*score[1:])
`],
  ["14430", "dynamic_programming_1-14430", "dynamic_programming_1", "Resource Collection", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = grid[i][j] + max(dp[i - 1][j] if i else 0, dp[i][j - 1] if j else 0)
print(dp[n - 1][m - 1])
`],
  ["14442", "graph_traversal-14442", "graph_traversal", "Break Wall 2", `from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]
dist = [[[-1] * (k + 1) for _ in range(m)] for __ in range(n)]
dist[0][0][0] = 1
q = deque([(0, 0, 0)])
while q:
    x, y, b = q.popleft()
    if x == n - 1 and y == m - 1:
        print(dist[x][y][b])
        break
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            nb = b + (grid[nx][ny] == "1")
            if nb <= k and dist[nx][ny][nb] == -1:
                dist[nx][ny][nb] = dist[x][y][b] + 1
                q.append((nx, ny, nb))
else:
    print(-1)
`],
  ["14496", "graph_traversal-14496", "graph_traversal", "Transformation", `from collections import deque
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
dist = [-1] * (n + 1)
dist[a] = 0
q = deque([a])
while q:
    x = q.popleft()
    for nx in g[x]:
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
print(dist[b])
`],
  ["14595", "disjoint_set-14595", "disjoint_set", "Dongbang Project Large", `import sys
input = sys.stdin.readline
n = int(input())
parent = list(range(n + 2))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
for _ in range(int(input())):
    x, y = map(int, input().split())
    cur = find(x)
    while cur < y:
        parent[cur] = find(cur + 1)
        cur = find(cur)
walls = sum(1 for i in range(1, n) if find(i) == i)
print(walls + 1)
`],
  ["14675", "tree-14675", "tree", "Cut Vertex and Bridge", `import sys
input = sys.stdin.readline
n = int(input())
deg = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    deg[a] += 1
    deg[b] += 1
out = []
for _ in range(int(input())):
    t, k = map(int, input().split())
    out.append("yes" if (t == 2 or deg[k] > 1) else "no")
print("\\n".join(out))
`],
  ["14699", "dynamic_programming_2-14699", "dynamic_programming_2", "Ascend", `import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if h[a] < h[b]:
        g[a].append(b)
    elif h[b] < h[a]:
        g[b].append(a)
dp = [0] * (n + 1)
def dfs(x):
    if dp[x]:
        return dp[x]
    dp[x] = 1
    for nx in g[x]:
        dp[x] = max(dp[x], dfs(nx) + 1)
    return dp[x]
print("\\n".join(str(dfs(i)) for i in range(1, n + 1)))
`],
  ["14725", "trie-14725", "trie", "Ant Tunnel", `import sys
input = sys.stdin.readline
root = {}
for _ in range(int(input())):
    data = input().split()[1:]
    node = root
    for word in data:
        node = node.setdefault(word, {})
out = []
def dfs(node, depth):
    for key in sorted(node):
        out.append("--" * depth + key)
        dfs(node[key], depth + 1)
dfs(root, 0)
print("\\n".join(out))
`],
  ["14728", "dynamic_programming_2-14728", "dynamic_programming_2", "Study Plan", `import sys
input = sys.stdin.readline
n, t = map(int, input().split())
dp = [0] * (t + 1)
for _ in range(n):
    k, s = map(int, input().split())
    for time in range(t, k - 1, -1):
        dp[time] = max(dp[time], dp[time - k] + s)
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
  console.log(`[import-manual-batch-23] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-23] wrote ${OUT}`);
