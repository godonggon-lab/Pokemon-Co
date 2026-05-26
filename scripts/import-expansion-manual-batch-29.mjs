import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1082", "dynamic_programming_2-1082", "dynamic_programming_2", "Room Number", `import sys
input = sys.stdin.readline
n = int(input())
price = list(map(int, input().split()))
m = int(input())
def better(a, b):
    if len(a) != len(b):
        return a if len(a) > len(b) else b
    return a if a > b else b
dp = [""] * (m + 1)
if n > 0 and price[0] <= m:
    dp[price[0]] = "0"
for cost in range(m + 1):
    if not dp[cost]:
        continue
    for d in range(n):
        if dp[cost] == "0":
            continue
        nc = cost + price[d]
        if nc <= m:
            dp[nc] = better(dp[nc], dp[cost] + str(d))
for d in range(1, n):
    if price[d] <= m:
        dp[price[d]] = better(dp[price[d]], str(d))
        for cost in range(price[d], m + 1):
            if not dp[cost]:
                continue
            for nd in range(n):
                nc = cost + price[nd]
                if nc <= m:
                    dp[nc] = better(dp[nc], dp[cost] + str(nd))
ans = "0"
for value in dp:
    if value:
        ans = better(ans, value)
print(ans)
`],
  ["2629", "dynamic_programming_2-2629", "dynamic_programming_2", "Balance Scale", `import sys
input = sys.stdin.readline
n = int(input())
w = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))
possible = {0}
for weight in w:
    nxt = set(possible)
    for x in possible:
        nxt.add(abs(x - weight))
        nxt.add(x + weight)
    possible = nxt
print(" ".join("Y" if b in possible else "N" for b in balls))
`],
  ["9470", "topological_sorting-9470", "topological_sorting", "Strahler Order", `from collections import deque
import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    k, m, p = map(int, input().split())
    g = [[] for _ in range(m + 1)]
    indeg = [0] * (m + 1)
    order = [0] * (m + 1)
    count = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, input().split())
        g[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(1, m + 1) if indeg[i] == 0)
    for i in q:
        order[i] = 1
        count[i] = 1
    while q:
        x = q.popleft()
        value = order[x] + (1 if count[x] >= 2 else 0)
        for y in g[x]:
            if order[y] < value:
                order[y] = value
                count[y] = 1
            elif order[y] == value:
                count[y] += 1
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    out.append(f"{k} {order[m] + (1 if count[m] >= 2 else 0)}")
print("\\n".join(out))
`],
  ["10711", "graph_traversal-10711", "graph_traversal", "Sandcastle", `from collections import deque
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
q = deque()
dist = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            q.append((i, j))
ans = 0
while q:
    x, y = q.popleft()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny].isdigit():
                grid[nx][ny] = str(int(grid[nx][ny]) - 1)
                if grid[nx][ny] == "0":
                    grid[nx][ny] = "."
                    dist[nx][ny] = dist[x][y] + 1
                    ans = max(ans, dist[nx][ny])
                    q.append((nx, ny))
print(ans)
`],
  ["11085", "disjoint_set-11085", "disjoint_set", "Military Movement", `import sys
input = sys.stdin.readline
p, w = map(int, input().split())
c, v = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(w)]
parent = list(range(p))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
for a, b, width in sorted(edges, key=lambda x: -x[2]):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
    if find(c) == find(v):
        print(width)
        break
`],
  ["12757", "binary_search-12757", "binary_search", "Legendary JBNU", `import bisect, sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
keys = []
values = {}
for _ in range(n):
    key, value = map(int, input().split())
    keys.append(key)
    values[key] = value
keys.sort()
out = []
def nearest(key):
    idx = bisect.bisect_left(keys, key)
    cand = []
    if idx < len(keys):
        cand.append(keys[idx])
    if idx:
        cand.append(keys[idx - 1])
    cand = [x for x in cand if abs(x - key) <= k]
    if not cand:
        return None
    cand.sort(key=lambda x: (abs(x - key), x))
    if len(cand) >= 2 and abs(cand[0] - key) == abs(cand[1] - key):
        return "?"
    return cand[0]
for _ in range(m):
    data = list(map(int, input().split()))
    if data[0] == 1:
        _, key, value = data
        if key not in values:
            bisect.insort(keys, key)
        values[key] = value
    elif data[0] == 2:
        _, key, value = data
        target = nearest(key)
        if isinstance(target, int):
            values[target] = value
    else:
        _, key = data
        target = nearest(key)
        if target is None:
            out.append("-1")
        elif target == "?":
            out.append("?")
        else:
            out.append(str(values[target]))
print("\\n".join(out))
`],
  ["14570", "tree-14570", "tree", "Marble Tree", `import sys
input = sys.stdin.readline
n = int(input())
child = [None] + [tuple(map(int, input().split())) for _ in range(n)]
k = int(input())
node = 1
while True:
    left, right = child[node]
    if left == -1 and right == -1:
        print(node)
        break
    if left == -1:
        node = right
    elif right == -1:
        node = left
    elif k % 2 == 1:
        node = left
        k = (k + 1) // 2
    else:
        node = right
        k //= 2
`],
  ["14676", "topological_sorting-14676", "topological_sorting", "Game Development", `import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
need = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    need[b] += 1
built = [0] * (n + 1)
ok = True
for _ in range(k):
    action, x = map(int, input().split())
    if action == 1:
        if built[x] == 0 and need[x] > 0:
            ok = False
            break
        built[x] += 1
        if built[x] == 1:
            for y in g[x]:
                need[y] -= 1
    else:
        if built[x] == 0:
            ok = False
            break
        built[x] -= 1
        if built[x] == 0:
            for y in g[x]:
                need[y] += 1
print("King-God-Emperor" if ok else "Lier!")
`],
  ["14863", "dynamic_programming_2-14863", "dynamic_programming_2", "Seoul to Gyeongsan", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
INF = -10**18
dp = [INF] * (k + 1)
dp[0] = 0
for _ in range(n):
    walk_t, walk_v, bike_t, bike_v = map(int, input().split())
    ndp = [INF] * (k + 1)
    for t, value in enumerate(dp):
        if value == INF:
            continue
        if t + walk_t <= k:
            ndp[t + walk_t] = max(ndp[t + walk_t], value + walk_v)
        if t + bike_t <= k:
            ndp[t + bike_t] = max(ndp[t + bike_t], value + bike_v)
    dp = ndp
print(max(dp))
`],
  ["14950", "minimum_spanning_tree-14950", "minimum_spanning_tree", "Conqueror", `import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
parent = list(range(n + 1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
ans = used = 0
for a, b, c in sorted(edges, key=lambda x: x[2]):
    ra, rb = find(a), find(b)
    if ra == rb:
        continue
    parent[rb] = ra
    ans += c + used * t
    used += 1
    if used == n - 1:
        break
print(ans)
`],
  ["15558", "graph_traversal-15558", "graph_traversal", "Jump Game", `from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
line = [input().strip(), input().strip()]
seen = [[False] * n for _ in range(2)]
q = deque([(0, 0, 0)])
seen[0][0] = True
while q:
    side, pos, time = q.popleft()
    for ns, np in ((side, pos + 1), (side, pos - 1), (1 - side, pos + k)):
        if np >= n:
            print(1)
            raise SystemExit
        if np <= time or line[ns][np] == "0" or seen[ns][np]:
            continue
        seen[ns][np] = True
        q.append((ns, np, time + 1))
print(0)
`],
  ["15659", "backtracking-15659", "backtracking", "Operator Insertion 3", `import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
counts = list(map(int, input().split()))
ops = ["+", "-", "*", "/"]
def div(a, b):
    return a // b if a >= 0 else -((-a) // b)
def eval_expr(seq):
    values = [nums[0]]
    low_ops = []
    for op, num in zip(seq, nums[1:]):
        if op == "*":
            values[-1] *= num
        elif op == "/":
            values[-1] = div(values[-1], num)
        else:
            low_ops.append(op)
            values.append(num)
    result = values[0]
    for op, value in zip(low_ops, values[1:]):
        result = result + value if op == "+" else result - value
    return result
mn, mx = 10**18, -10**18
def dfs(seq):
    global mn, mx
    if len(seq) == n - 1:
        value = eval_expr(seq)
        mn = min(mn, value)
        mx = max(mx, value)
        return
    for i, op in enumerate(ops):
        if counts[i]:
            counts[i] -= 1
            seq.append(op)
            dfs(seq)
            seq.pop()
            counts[i] += 1
dfs([])
print(mx)
print(mn)
`],
  ["16973", "graph_traversal-16973", "graph_traversal", "Rectangle Escape", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1; sc -= 1; fr -= 1; fc -= 1
ps = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        ps[i + 1][j + 1] = grid[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]
def empty(x, y):
    if x < 0 or y < 0 or x + h > n or y + w > m:
        return False
    return ps[x + h][y + w] - ps[x][y + w] - ps[x + h][y] + ps[x][y] == 0
dist = [[-1] * m for _ in range(n)]
q = deque([(sr, sc)])
dist[sr][sc] = 0
while q:
    x, y = q.popleft()
    if (x, y) == (fr, fc):
        print(dist[x][y])
        break
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and empty(nx, ny):
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
else:
    print(-1)
`],
  ["16987", "backtracking-16987", "backtracking", "Eggs", `import sys
input = sys.stdin.readline
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0
def dfs(idx):
    global ans
    if idx == n:
        ans = max(ans, sum(s <= 0 for s, _ in eggs))
        return
    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return
    hit = False
    for j in range(n):
        if j == idx or eggs[j][0] <= 0:
            continue
        hit = True
        eggs[idx][0] -= eggs[j][1]
        eggs[j][0] -= eggs[idx][1]
        dfs(idx + 1)
        eggs[j][0] += eggs[idx][1]
        eggs[idx][0] += eggs[j][1]
    if not hit:
        dfs(idx + 1)
dfs(0)
print(ans)
`],
  ["17398", "disjoint_set-17398", "disjoint_set", "Communication Network Split", `import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
edges = [None] + [tuple(map(int, input().split())) for _ in range(m)]
removed = [int(input()) for _ in range(q)]
removed_set = set(removed)
parent = list(range(n + 1))
size = [1] * (n + 1)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return 0
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    cost = size[ra] * size[rb]
    parent[rb] = ra
    size[ra] += size[rb]
    return cost
for i in range(1, m + 1):
    if i not in removed_set:
        union(*edges[i])
ans = 0
for idx in reversed(removed):
    ans += union(*edges[idx])
print(ans)
`],
  ["17404", "dynamic_programming_2-17404", "dynamic_programming_2", "RGB Street 2", `import sys
input = sys.stdin.readline
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
INF = 10**15
ans = INF
for first in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][first] = cost[0][first]
    for i in range(1, n):
        for c in range(3):
            dp[i][c] = cost[i][c] + min(dp[i - 1][p] for p in range(3) if p != c)
    for last in range(3):
        if last != first:
            ans = min(ans, dp[-1][last])
print(ans)
`],
  ["19535", "tree-19535", "tree", "D and G Tree", `import sys
input = sys.stdin.readline
n = int(input())
deg = [0] * (n + 1)
edges = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    deg[a] += 1
    deg[b] += 1
    edges.append((a, b))
d = sum((deg[a] - 1) * (deg[b] - 1) for a, b in edges)
g = sum(x * (x - 1) * (x - 2) // 6 for x in deg)
if d > 3 * g:
    print("D")
elif d < 3 * g:
    print("G")
else:
    print("DUDUDUNGA")
`],
  ["20119", "topological_sorting-20119", "topological_sorting", "Claire and Potions", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
recipes_by_ingredient = [[] for _ in range(n + 1)]
need = []
result = []
for idx in range(m):
    data = list(map(int, input().split()))
    k = data[0]
    ingredients = data[1:1 + k]
    r = data[-1]
    need.append(k)
    result.append(r)
    for ingredient in ingredients:
        recipes_by_ingredient[ingredient].append(idx)
l = int(input())
initial = list(map(int, input().split()))
known = [False] * (n + 1)
q = deque()
for x in initial:
    if not known[x]:
        known[x] = True
        q.append(x)
while q:
    x = q.popleft()
    for recipe in recipes_by_ingredient[x]:
        need[recipe] -= 1
        if need[recipe] == 0 and not known[result[recipe]]:
            known[result[recipe]] = True
            q.append(result[recipe])
ans = [i for i in range(1, n + 1) if known[i]]
print(len(ans))
print(*ans)
`],
  ["20159", "prefix_sum-20159", "prefix_sum", "Card Game", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
odd = [0]
even = [0]
for i, x in enumerate(a):
    odd.append(odd[-1] + (x if i % 2 == 0 else 0))
    even.append(even[-1] + (x if i % 2 == 1 else 0))
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans = max(ans, odd[i] + even[n] - even[i + 1])
    else:
        ans = max(ans, odd[i + 1] + even[n] - even[i + 1])
print(ans)
`],
  ["22871", "binary_search-22871", "binary_search", "Stepping Stones Large", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
def can(limit):
    ok = [False] * n
    ok[0] = True
    for i in range(n):
        if not ok[i]:
            continue
        for j in range(i + 1, n):
            power = (j - i) * (1 + abs(a[i] - a[j]))
            if power <= limit:
                ok[j] = True
    return ok[-1]
lo, hi = 0, (n - 1) * (1 + max(a) - min(a))
while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
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
  console.log(`[import-manual-batch-29] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-29] wrote ${OUT}`);
