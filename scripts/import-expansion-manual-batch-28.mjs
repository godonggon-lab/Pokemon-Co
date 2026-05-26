import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1943", "dynamic_programming_2-1943", "dynamic_programming_2", "Coin Distribution", `import sys
input = sys.stdin.readline
out = []
for _ in range(3):
    n = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(n)]
    total = sum(v * c for v, c in coins)
    if total % 2:
        out.append("0")
        continue
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for value, count in coins:
        for cur in range(target, -1, -1):
            if not dp[cur]:
                continue
            for k in range(1, count + 1):
                nxt = cur + value * k
                if nxt > target:
                    break
                dp[nxt] = True
    out.append("1" if dp[target] else "0")
print("\\n".join(out))
`],
  ["2631", "dynamic_programming_2-2631", "dynamic_programming_2", "Line Up", `import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
`],
  ["3108", "disjoint_set-3108", "disjoint_set", "Logo", `import sys
input = sys.stdin.readline
n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
def touches(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
        return False
    if ax1 < bx1 and bx2 < ax2 and ay1 < by1 and by2 < ay2:
        return False
    if bx1 < ax1 and ax2 < bx2 and by1 < ay1 and ay2 < by2:
        return False
    return True
def on_origin(r):
    x1, y1, x2, y2 = r
    return (x1 <= 0 <= x2 and (y1 == 0 or y2 == 0)) or (y1 <= 0 <= y2 and (x1 == 0 or x2 == 0))
for i in range(n):
    for j in range(i):
        if touches(rects[i], rects[j]):
            union(i, j)
components = len({find(i) for i in range(n)})
print(components - (1 if any(on_origin(r) for r in rects) else 0))
`],
  ["8980", "greedy-8980", "greedy", "Delivery", `import sys
input = sys.stdin.readline
n, c = map(int, input().split())
m = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(m)]
boxes.sort(key=lambda x: (x[1], x[0]))
load = [0] * (n + 1)
ans = 0
for s, e, amount in boxes:
    can = min(amount, c - max(load[s:e]))
    if can <= 0:
        continue
    for i in range(s, e):
        load[i] += can
    ans += can
print(ans)
`],
  ["10423", "minimum_spanning_tree-10423", "minimum_spanning_tree", "Electricity", `import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
plants = set(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]
parent = list(range(n + 1))
for p in plants:
    parent[p] = 0
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
ans = 0
for u, v, w in sorted(edges, key=lambda x: x[2]):
    ru, rv = find(u), find(v)
    if ru == rv:
        continue
    parent[rv] = ru
    ans += w
print(ans)
`],
  ["13418", "minimum_spanning_tree-13418", "minimum_spanning_tree", "School Exploration", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m + 1)]
def kruskal(reverse):
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    uphill = used = 0
    for a, b, c in sorted(edges, key=lambda x: x[2], reverse=reverse):
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        parent[rb] = ra
        used += 1
        if c == 0:
            uphill += 1
        if used == n:
            break
    return uphill
best = kruskal(True)
worst = kruskal(False)
print(worst * worst - best * best)
`],
  ["13910", "dynamic_programming_1-13910", "dynamic_programming_1", "Opening", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
woks = list(map(int, input().split()))
sizes = set(woks)
for i in range(m):
    for j in range(i + 1, m):
        sizes.add(woks[i] + woks[j])
INF = 10**9
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for size in sizes:
        if i >= size:
            dp[i] = min(dp[i], dp[i - size] + 1)
print(dp[n] if dp[n] < INF else -1)
`],
  ["14391", "brute_force-14391", "brute_force", "Paper Pieces", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
ans = 0
for mask in range(1 << (n * m)):
    total = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            idx = i * m + j
            if mask & (1 << idx):
                cur = cur * 10 + int(grid[i][j])
            else:
                total += cur
                cur = 0
        total += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            idx = i * m + j
            if mask & (1 << idx):
                total += cur
                cur = 0
            else:
                cur = cur * 10 + int(grid[i][j])
        total += cur
    ans = max(ans, total)
print(ans)
`],
  ["14852", "dynamic_programming_1-14852", "dynamic_programming_1", "Tile Filling 3", `import sys
MOD = 1000000007
n = int(sys.stdin.readline())
dp = [0] * max(3, n + 1)
dp[0], dp[1], dp[2] = 1, 2, 7
extra = dp[0]
for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + 2 * extra) % MOD
    extra = (extra + dp[i - 2]) % MOD
print(dp[n] % MOD)
`],
  ["16400", "dynamic_programming_2-16400", "dynamic_programming_2", "Prime Sums", `import sys
MOD = 123456789
n = int(sys.stdin.readline())
prime = [True] * (n + 1)
if n >= 0:
    prime[0] = False
if n >= 1:
    prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False
dp = [0] * (n + 1)
dp[0] = 1
for p in range(2, n + 1):
    if not prime[p]:
        continue
    for s in range(p, n + 1):
        dp[s] = (dp[s] + dp[s - p]) % MOD
print(dp[n])
`],
  ["16637", "brute_force-16637", "brute_force", "Parentheses", `import sys
n = int(sys.stdin.readline())
expr = sys.stdin.readline().strip()
nums = list(map(int, expr[::2]))
ops = list(expr[1::2])
def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    return a * b
ans = -10**18
def dfs(idx, value):
    global ans
    if idx == len(ops):
        ans = max(ans, value)
        return
    dfs(idx + 1, calc(value, ops[idx], nums[idx + 1]))
    if idx + 1 < len(ops):
        grouped = calc(nums[idx + 1], ops[idx + 1], nums[idx + 2])
        dfs(idx + 2, calc(value, ops[idx], grouped))
dfs(0, nums[0])
print(ans)
`],
  ["16943", "brute_force-16943", "brute_force", "Number Relocation", `from itertools import permutations
import sys
a, b = sys.stdin.readline().split()
limit = int(b)
ans = -1
for p in set(permutations(a)):
    if p[0] == "0":
        continue
    value = int("".join(p))
    if value < limit:
        ans = max(ans, value)
print(ans)
`],
  ["16956", "graph_traversal-16956", "graph_traversal", "Wolves and Sheep", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if grid[i][j] != "S":
            continue
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == "W":
                print(0)
                raise SystemExit
for i in range(r):
    for j in range(c):
        if grid[i][j] == ".":
            grid[i][j] = "D"
print(1)
print("\\n".join("".join(row) for row in grid))
`],
  ["17069", "dynamic_programming_2-17069", "dynamic_programming_2", "Move Pipe 2", `import sys
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
  ["19542", "tree-19542", "tree", "Flyer", `import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, s, d = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
ans = 0
def dfs(x, parent):
    global ans
    depth = 0
    for y in g[x]:
        if y == parent:
            continue
        depth = max(depth, dfs(y, x) + 1)
    if x != s and depth >= d:
        ans += 1
    return depth
dfs(s, 0)
print(ans * 2)
`],
  ["20152", "dynamic_programming_1-20152", "dynamic_programming_1", "Game Addiction", `import sys
h, n = map(int, sys.stdin.readline().split())
if h > n:
    h, n = n, h
size = n + 1
dp = [[0] * size for _ in range(size)]
dp[h][h] = 1
for i in range(h, n + 1):
    for j in range(h, i + 1):
        if i == h and j == h:
            continue
        dp[i][j] = (dp[i - 1][j] if i > h else 0) + (dp[i][j - 1] if j > h else 0)
print(dp[n][n])
`],
  ["20366", "two_pointer-20366", "two_pointer", "Snowman", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
ans = 10**18
for i in range(n - 3):
    for j in range(i + 3, n):
        target = a[i] + a[j]
        l, r = i + 1, j - 1
        while l < r:
            value = a[l] + a[r]
            ans = min(ans, abs(target - value))
            if value < target:
                l += 1
            else:
                r -= 1
print(ans)
`],
  ["20955", "disjoint_set-20955", "disjoint_set", "Emergency Surgery", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n + 1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
cycle = 0
for _ in range(m):
    a, b = map(int, input().split())
    ra, rb = find(a), find(b)
    if ra == rb:
        cycle += 1
    else:
        parent[rb] = ra
components = len({find(i) for i in range(1, n + 1)})
print(cycle + components - 1)
`],
  ["21937", "graph_traversal-21937", "graph_traversal", "Work", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rev = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    rev[b].append(a)
x = int(input())
seen = [False] * (n + 1)
seen[x] = True
q = deque([x])
ans = 0
while q:
    cur = q.popleft()
    for nxt in rev[cur]:
        if not seen[nxt]:
            seen[nxt] = True
            ans += 1
            q.append(nxt)
print(ans)
`],
  ["22857", "dynamic_programming_1-22857", "dynamic_programming_1", "Longest Even Subsequence Small", `import sys
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
  console.log(`[import-manual-batch-28] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-28] wrote ${OUT}`);
