import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1633", "dynamic_programming_1-1633", "dynamic_programming_1", "Best Team", `import sys
players = [tuple(map(int, line.split())) for line in sys.stdin if line.strip()]
dp = [[-1] * 16 for _ in range(16)]
dp[0][0] = 0
for white, black in players:
    nxt = [row[:] for row in dp]
    for w in range(16):
        for b in range(16):
            if dp[w][b] < 0:
                continue
            if w < 15:
                nxt[w + 1][b] = max(nxt[w + 1][b], dp[w][b] + white)
            if b < 15:
                nxt[w][b + 1] = max(nxt[w][b + 1], dp[w][b] + black)
    dp = nxt
print(dp[15][15])
`],
  ["2121", "binary_search-2121", "binary_search", "Net", `import sys
input = sys.stdin.readline
n = int(input())
w, h = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
s = set(points)
ans = 0
for x, y in points:
    if (x + w, y) in s and (x, y + h) in s and (x + w, y + h) in s:
        ans += 1
print(ans)
`],
  ["2660", "shortest_path-2660", "shortest_path", "President", `import sys
input = sys.stdin.readline
n = int(input())
INF = 10**9
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    d[a - 1][b - 1] = d[b - 1][a - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
scores = [max(row) for row in d]
best = min(scores)
cands = [i + 1 for i, x in enumerate(scores) if x == best]
print(best, len(cands))
print(*cands)
`],
  ["2661", "backtracking-2661", "backtracking", "Good Sequence", `import sys
n = int(sys.stdin.readline())
def good(s):
    for length in range(1, len(s) // 2 + 1):
        if s[-length:] == s[-2 * length:-length]:
            return False
    return True
def dfs(s):
    if len(s) == n:
        print(s)
        raise SystemExit
    for ch in "123":
        ns = s + ch
        if good(ns):
            dfs(ns)
dfs("")
`],
  ["2665", "graph_traversal-2665", "graph_traversal", "Maze", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
grid = [input().strip() for _ in range(n)]
dist = [[10**9] * n for _ in range(n)]
dist[0][0] = 0
dq = deque([(0, 0)])
while dq:
    x, y = dq.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            cost = 1 if grid[nx][ny] == "0" else 0
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost
                (dq.append if cost else dq.appendleft)((nx, ny))
print(dist[n - 1][n - 1])
`],
  ["2668", "graph_traversal-2668", "graph_traversal", "Number Picking", `import sys
input = sys.stdin.readline
n = int(input())
a = [0] + [int(input()) for _ in range(n)]
ans = []
for start in range(1, n + 1):
    seen = set()
    x = start
    while x not in seen:
        seen.add(x)
        x = a[x]
    if x == start:
        ans.append(start)
print(len(ans))
print("\\n".join(map(str, ans)))
`],
  ["2866", "binary_search-2866", "binary_search", "String Cut", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
rows = [input().strip() for _ in range(r)]
cols = ["".join(rows[i][j] for i in range(r)) for j in range(c)]
ans = 0
for cut in range(r):
    seen = set()
    ok = True
    for col in cols:
        tail = col[cut:]
        if tail in seen:
            ok = False
            break
        seen.add(tail)
    if ok:
        ans = cut
    else:
        break
print(ans)
`],
  ["3055", "graph_traversal-3055", "graph_traversal", "Escape", `from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
water = deque()
q = deque()
for i in range(r):
    for j in range(c):
        if grid[i][j] == "*":
            water.append((i, j))
        elif grid[i][j] == "S":
            q.append((i, j, 0))
            grid[i][j] = "."
while q:
    for _ in range(len(water)):
        x, y = water.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == ".":
                grid[nx][ny] = "*"
                water.append((nx, ny))
    for _ in range(len(q)):
        x, y, d = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if grid[nx][ny] == "D":
                    print(d + 1)
                    raise SystemExit
                if grid[nx][ny] == ".":
                    grid[nx][ny] = "S"
                    q.append((nx, ny, d + 1))
print("KAKTUS")
`],
  ["3980", "backtracking-3980", "backtracking", "Selection", `import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    a = [list(map(int, input().split())) for _ in range(11)]
    best = 0
    used = [False] * 11
    def dfs(player, total):
        nonlocal_best[0] = max(nonlocal_best[0], total) if player == 11 else nonlocal_best[0]
        if player == 11:
            return
        for pos in range(11):
            if not used[pos] and a[player][pos]:
                used[pos] = True
                dfs(player + 1, total + a[player][pos])
                used[pos] = False
    nonlocal_best = [0]
    dfs(0, 0)
    out.append(str(nonlocal_best[0]))
print("\\n".join(out))
`],
  ["4803", "tree-4803", "tree", "Trees", `import sys
input = sys.stdin.readline
case = 1
out = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = list(range(n + 1))
    cycle = [False] * (n + 1)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for _ in range(m):
        a, b = map(int, input().split())
        ra, rb = find(a), find(b)
        if ra == rb:
            cycle[ra] = True
        else:
            parent[rb] = ra
            cycle[ra] = cycle[ra] or cycle[rb]
    roots = set(find(i) for i in range(1, n + 1))
    trees = sum(not cycle[find(r)] for r in roots)
    if trees == 0:
        msg = "No trees."
    elif trees == 1:
        msg = "There is one tree."
    else:
        msg = f"A forest of {trees} trees."
    out.append(f"Case {case}: {msg}")
    case += 1
print("\\n".join(out))
`],
  ["5427", "graph_traversal-5427", "graph_traversal", "Fire", `from collections import deque
import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    w, h = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    fire = deque()
    q = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "*":
                fire.append((i, j))
            elif grid[i][j] == "@":
                q.append((i, j, 0))
                grid[i][j] = "."
    escaped = None
    while q and escaped is None:
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == ".":
                    grid[nx][ny] = "*"
                    fire.append((nx, ny))
        for _ in range(len(q)):
            x, y, d = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w):
                    escaped = d + 1
                    break
                if grid[nx][ny] == ".":
                    grid[nx][ny] = "@"
                    q.append((nx, ny, d + 1))
            if escaped is not None:
                break
    out.append(str(escaped) if escaped is not None else "IMPOSSIBLE")
print("\\n".join(out))
`],
  ["5582", "dynamic_programming_2-5582", "dynamic_programming_2", "Common Substring", `import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
prev = [0] * (len(b) + 1)
ans = 0
for i in range(1, len(a) + 1):
    cur = [0] * (len(b) + 1)
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            cur[j] = prev[j - 1] + 1
            ans = max(ans, cur[j])
    prev = cur
print(ans)
`],
  ["5639", "tree-5639", "tree", "Binary Search Tree", `import sys
pre = [int(x) for x in sys.stdin.read().split()]
sys.setrecursionlimit(10**6)
out = []
def build(l, r):
    if l >= r:
        return
    root = pre[l]
    mid = l + 1
    while mid < r and pre[mid] < root:
        mid += 1
    build(l + 1, mid)
    build(mid, r)
    out.append(str(root))
build(0, len(pre))
print("\\n".join(out))
`],
  ["6443", "backtracking-6443", "backtracking", "Anagram", `from collections import Counter
import sys
input = sys.stdin.readline
out = []
for _ in range(int(input())):
    s = input().strip()
    cnt = Counter(s)
    chars = sorted(cnt)
    cur = []
    def dfs():
        if len(cur) == len(s):
            out.append("".join(cur))
            return
        for ch in chars:
            if cnt[ch]:
                cnt[ch] -= 1
                cur.append(ch)
                dfs()
                cur.pop()
                cnt[ch] += 1
    dfs()
print("\\n".join(out))
`],
  ["6603", "backtracking-6603", "backtracking", "Lotto", `import itertools, sys
out = []
for line in sys.stdin:
    data = list(map(int, line.split()))
    if data[0] == 0:
        break
    nums = data[1:]
    for comb in itertools.combinations(nums, 6):
        out.append(" ".join(map(str, comb)))
    out.append("")
print("\\n".join(out).rstrip())
`],
  ["7490", "backtracking-7490", "backtracking", "Zero", `import sys
input = sys.stdin.readline
def value(expr):
    return eval(expr.replace(" ", ""))
out = []
for tc in range(int(input())):
    n = int(input())
    res = []
    def dfs(i, expr):
        if i == n:
            if value(expr) == 0:
                res.append(expr)
            return
        for op in (" ", "+", "-"):
            dfs(i + 1, expr + op + str(i + 1))
    dfs(1, "1")
    out.extend(res)
    if tc != 0 or True:
        out.append("")
print("\\n".join(out).rstrip())
`],
  ["7511", "disjoint_set-7511", "disjoint_set", "Social Network", `import sys
input = sys.stdin.readline
out = []
for case in range(1, int(input()) + 1):
    n = int(input())
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
    for _ in range(int(input())):
        a, b = map(int, input().split())
        union(a, b)
    out.append(f"Scenario {case}:")
    for _ in range(int(input())):
        a, b = map(int, input().split())
        out.append("1" if find(a) == find(b) else "0")
    out.append("")
print("\\n".join(out))
`],
  ["9019", "graph_traversal-9019", "graph_traversal", "DSLR", `from collections import deque
import sys
input = sys.stdin.readline
def solve(a, b):
    prev = [-1] * 10000
    how = [""] * 10000
    q = deque([a])
    prev[a] = a
    while q:
        x = q.popleft()
        if x == b:
            break
        nxts = ((x * 2) % 10000, "D"), ((x - 1) % 10000, "S"), ((x % 1000) * 10 + x // 1000, "L"), ((x % 10) * 1000 + x // 10, "R")
        for nx, op in nxts:
            if prev[nx] == -1:
                prev[nx] = x
                how[nx] = op
                q.append(nx)
    ops = []
    cur = b
    while cur != a:
        ops.append(how[cur])
        cur = prev[cur]
    return "".join(reversed(ops))
print("\\n".join(solve(*map(int, input().split())) for _ in range(int(input()))))
`],
  ["10159", "shortest_path-10159", "shortest_path", "Scale", `import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
reach = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    reach[a - 1][b - 1] = True
for k in range(n):
    for i in range(n):
        if reach[i][k]:
            for j in range(n):
                reach[i][j] = reach[i][j] or reach[k][j]
out = []
for i in range(n):
    known = sum(1 for j in range(n) if i != j and (reach[i][j] or reach[j][i]))
    out.append(str(n - 1 - known))
print("\\n".join(out))
`],
  ["10942", "dynamic_programming_2-10942", "dynamic_programming_2", "Palindrome", `import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = True
for i in range(1, n):
    dp[i][i + 1] = a[i] == a[i + 1]
for length in range(3, n + 1):
    for l in range(1, n - length + 2):
        r = l + length - 1
        dp[l][r] = a[l] == a[r] and dp[l + 1][r - 1]
out = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    out.append("1" if dp[s][e] else "0")
print("\\n".join(out))
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
  console.log(`[import-manual-batch-22] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-22] wrote ${OUT}`);
