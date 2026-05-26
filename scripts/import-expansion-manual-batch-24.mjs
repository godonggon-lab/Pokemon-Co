import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["14594", "simulation-14594", "simulation", "Dongbang Project", `import sys
input = sys.stdin.readline
n = int(input())
walls = [1] * n
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x - 1, y - 1):
        walls[i] = 0
print(sum(walls))
`],
  ["15723", "shortest_path-15723", "shortest_path", "n-dimension", `import sys
input = sys.stdin.readline
reach = [[False] * 26 for _ in range(26)]
for _ in range(int(input())):
    a, _, b = input().split()
    reach[ord(a) - 97][ord(b) - 97] = True
for k in range(26):
    for i in range(26):
        if reach[i][k]:
            for j in range(26):
                reach[i][j] = reach[i][j] or reach[k][j]
out = []
for _ in range(int(input())):
    a, _, b = input().split()
    out.append("T" if reach[ord(a) - 97][ord(b) - 97] else "F")
print("\\n".join(out))
`],
  ["15789", "disjoint_set-15789", "disjoint_set", "CTP Kingdom", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
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
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
c, h, k = map(int, input().split())
enemy = find(h)
root = find(c)
others = sorted((size[find(i)] for i in range(1, n + 1) if find(i) == i and find(i) not in (root, enemy)), reverse=True)
print(size[root] + sum(others[:k]))
`],
  ["15831", "two_pointer-15831", "two_pointer", "Junhyun Likes Cats", `import sys
input = sys.stdin.readline
n, b, w = map(int, input().split())
s = input().strip()
ans = left = black = white = 0
for right, ch in enumerate(s):
    black += ch == "B"
    white += ch == "W"
    while black > b:
        black -= s[left] == "B"
        white -= s[left] == "W"
        left += 1
    if white >= w:
        ans = max(ans, right - left + 1)
print(ans)
`],
  ["15900", "tree-15900", "tree", "Tree Escape", `import sys
input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
stack = [(1, 0, 0)]
total = 0
while stack:
    x, p, d = stack.pop()
    leaf = True
    for nx in g[x]:
        if nx != p:
            leaf = False
            stack.append((nx, x, d + 1))
    if leaf:
        total += d
print("Yes" if total % 2 else "No")
`],
  ["15991", "dynamic_programming_1-15991", "dynamic_programming_1", "1,2,3 Add 6", `import sys
MOD = 1000000009
MAX = 100000
dp = [0] * (MAX + 1)
dp[0] = dp[1] = 1
dp[2] = 2
for n in range(3, MAX + 1):
    dp[n] = (dp[n - 2] + dp[n - 4] if n >= 4 else dp[n - 2]) % MOD
    dp[n] = (dp[n] + (dp[n - 6] if n >= 6 else 0)) % MOD
print("\\n".join(str(dp[int(sys.stdin.readline())]) for _ in range(int(sys.stdin.readline()))))
`],
  ["16434", "binary_search-16434", "binary_search", "Dragon and Dungeon", `import sys
input = sys.stdin.readline
n, atk0 = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(n)]
def survive(max_hp):
    hp = max_hp
    atk = atk0
    for t, a, h in rooms:
        if t == 1:
            hits = (h + atk - 1) // atk
            hp -= a * (hits - 1)
            if hp <= 0:
                return False
        else:
            atk += a
            hp = min(max_hp, hp + h)
    return True
lo, hi = 1, 10**18
while lo < hi:
    mid = (lo + hi) // 2
    if survive(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["16437", "tree-16437", "tree", "Sheep", `import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
children = [[] for _ in range(n + 1)]
val = [0] * (n + 1)
for i in range(2, n + 1):
    t, a, p = input().split()
    a = int(a); p = int(p)
    val[i] = a if t == "S" else -a
    children[p].append(i)
def dfs(x):
    total = val[x]
    for nx in children[x]:
        total += dfs(nx)
    return max(0, total)
print(dfs(1))
`],
  ["16472", "two_pointer-16472", "two_pointer", "Cat", `import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
cnt = {}
left = ans = 0
for right, ch in enumerate(s):
    cnt[ch] = cnt.get(ch, 0) + 1
    while len(cnt) > n:
        old = s[left]
        cnt[old] -= 1
        if cnt[old] == 0:
            del cnt[old]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)
`],
  ["16508", "brute_force-16508", "brute_force", "Book Buying", `from collections import Counter
import sys
input = sys.stdin.readline
target = Counter(input().strip())
n = int(input())
books = []
for _ in range(n):
    price, title = input().split()
    books.append((int(price), Counter(title)))
ans = 10**9
for mask in range(1, 1 << n):
    cost = 0
    have = Counter()
    for i in range(n):
        if mask & (1 << i):
            cost += books[i][0]
            have += books[i][1]
    if all(have[ch] >= need for ch, need in target.items()):
        ans = min(ans, cost)
print(ans if ans < 10**9 else -1)
`],
  ["16564", "binary_search-16564", "binary_search", "Himchan", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]
lo, hi = min(levels), min(levels) + k + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    need = sum(max(0, mid - x) for x in levels)
    if need <= k:
        lo = mid
    else:
        hi = mid
print(lo)
`],
  ["16724", "disjoint_set-16724", "disjoint_set", "Pied Piper", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
parent = list(range(n * m))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
dirs = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
for i in range(n):
    for j in range(m):
        di, dj = dirs[grid[i][j]]
        ni, nj = i + di, j + dj
        union(i * m + j, ni * m + nj)
print(len({find(i) for i in range(n * m)}))
`],
  ["16922", "backtracking-16922", "backtracking", "Roman Numerals", `import itertools, sys
n = int(sys.stdin.readline())
vals = [1, 5, 10, 50]
seen = set()
for counts in itertools.product(range(n + 1), repeat=4):
    if sum(counts) == n:
        seen.add(sum(c * v for c, v in zip(counts, vals)))
print(len(seen))
`],
  ["16928", "graph_traversal-16928", "graph_traversal", "Snakes and Ladders", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
jump = {}
for _ in range(n + m):
    a, b = map(int, input().split())
    jump[a] = b
dist = [-1] * 101
dist[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    if x == 100:
        break
    for d in range(1, 7):
        nx = x + d
        if nx <= 100:
            nx = jump.get(nx, nx)
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
print(dist[100])
`],
  ["16932", "graph_traversal-16932", "graph_traversal", "Shape Making", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sizes = [0, 0]
label = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            label += 1
            grid[i][j] = label
            q = deque([(i, j)])
            size = 1
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = label
                        size += 1
                        q.append((nx, ny))
            sizes.append(size)
ans = max(sizes)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            seen = set()
            cur = 1
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 1:
                    seen.add(grid[nx][ny])
            for x in seen:
                cur += sizes[x]
            ans = max(ans, cur)
print(ans)
`],
  ["16937", "brute_force-16937", "brute_force", "Two Stickers", `import sys
input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for a, b in (stickers[i], stickers[i][::-1]):
            for c, d in (stickers[j], stickers[j][::-1]):
                if (max(a, c) <= h and b + d <= w) or (a + c <= h and max(b, d) <= w):
                    ans = max(ans, a * b + c * d)
print(ans)
`],
  ["16938", "backtracking-16938", "backtracking", "Camp Preparation", `import itertools, sys
input = sys.stdin.readline
n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for k in range(2, n + 1):
    for comb in itertools.combinations(a, k):
        s = sum(comb)
        if l <= s <= r and max(comb) - min(comb) >= x:
            ans += 1
print(ans)
`],
  ["16947", "graph_traversal-16947", "graph_traversal", "Seoul Subway 2", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
for _ in range(n):
    a, b = map(int, input().split())
    g[a].append(b); g[b].append(a)
    deg[a] += 1; deg[b] += 1
q = deque(i for i in range(1, n + 1) if deg[i] == 1)
cycle = [True] * (n + 1)
while q:
    x = q.popleft()
    cycle[x] = False
    for nx in g[x]:
        deg[nx] -= 1
        if deg[nx] == 1:
            q.append(nx)
dist = [-1] * (n + 1)
q = deque()
for i in range(1, n + 1):
    if cycle[i]:
        dist[i] = 0
        q.append(i)
while q:
    x = q.popleft()
    for nx in g[x]:
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
print(*dist[1:])
`],
  ["16948", "graph_traversal-16948", "graph_traversal", "Death Knight", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dist = [[-1] * n for _ in range(n)]
dist[r1][c1] = 0
q = deque([(r1, c1)])
for_q = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
while q:
    x, y = q.popleft()
    for dx, dy in for_q:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
print(dist[r2][c2])
`],
  ["16951", "brute_force-16951", "brute_force", "Block Height", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = n
for first in range(1, 101):
    for diff in range(-99, 100):
        cnt = 0
        ok = True
        for i, x in enumerate(a):
            target = first + diff * i
            if target < 1:
                ok = False
                break
            if abs(x - target) > 1:
                ok = False
                break
            if x != target:
                cnt += 1
        if ok:
            ans = min(ans, cnt)
print(ans if ans < n else -1)
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
  console.log(`[import-manual-batch-24] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-24] wrote ${OUT}`);
