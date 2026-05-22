import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1548", "brute_force-1548", "brute_force", "Partial Triangle Sequence", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
ans = min(n, 2)
for i in range(n):
    for j in range(i + 2, n):
        if a[i] + a[i + 1] > a[j]:
            ans = max(ans, j - i + 1)
print(ans)
`],
  ["1711", "brute_force-1711", "brute_force", "Right Triangle", `import sys
input = sys.stdin.readline
n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = p[i]; x2, y2 = p[j]; x3, y3 = p[k]
            v = [((x2-x1, y2-y1), (x3-x1, y3-y1)), ((x1-x2, y1-y2), (x3-x2, y3-y2)), ((x1-x3, y1-y3), (x2-x3, y2-y3))]
            if any(a*c + b*d == 0 for (a,b), (c,d) in v):
                ans += 1
print(ans)
`],
  ["2225", "dynamic_programming_2-2225", "dynamic_programming_2", "Sum Decomposition", `import sys
n, k = map(int, sys.stdin.readline().split())
mod = 1000000000
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1
for i in range(1, k + 1):
    acc = 0
    for s in range(n + 1):
        acc = (acc + dp[i - 1][s]) % mod
        dp[i][s] = acc
print(dp[k][n])
`],
  ["2302", "dynamic_programming_1-2302", "dynamic_programming_1", "Theater Seats", `import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]
fib = [1] * (n + 2)
fib[1] = 1
for i in range(2, n + 2):
    fib[i] = fib[i - 1] + fib[i - 2]
ans = 1
prev = 0
for x in vip + [n + 1]:
    ans *= fib[x - prev - 1]
    prev = x
print(ans)
`],
  ["2304", "brute_force-2304", "brute_force", "Warehouse Polygon", `import sys
input = sys.stdin.readline
n = int(input())
p = sorted(tuple(map(int, input().split())) for _ in range(n))
max_h = max(h for _, h in p)
max_positions = [x for x, h in p if h == max_h]
left_max_x = max_positions[0]
right_max_x = max_positions[-1]
area = (right_max_x - left_max_x + 1) * max_h
cur_x, cur_h = p[0]
for x, h in p:
    if x > left_max_x:
        break
    if h > cur_h:
        area += (x - cur_x) * cur_h
        cur_x, cur_h = x, h
cur_x, cur_h = p[-1]
for x, h in reversed(p):
    if x < right_max_x:
        break
    if h > cur_h:
        area += (cur_x - x) * cur_h
        cur_x, cur_h = x, h
print(area)
`],
  ["2343", "binary_search-2343", "binary_search", "Guitar Lesson", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
lo, hi = max(a), sum(a)
while lo < hi:
    mid = (lo + hi) // 2
    cnt = 1
    cur = 0
    for x in a:
        if cur + x > mid:
            cnt += 1
            cur = 0
        cur += x
    if cnt <= m:
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["2435", "brute_force-2435", "brute_force", "Temperature", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
cur = sum(a[:k])
ans = cur
for i in range(k, n):
    cur += a[i] - a[i - k]
    ans = max(ans, cur)
print(ans)
`],
  ["2491", "dynamic_programming_1-2491", "dynamic_programming_1", "Sequence", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
inc = dec = ans = 1
for i in range(1, n):
    inc = inc + 1 if a[i - 1] <= a[i] else 1
    dec = dec + 1 if a[i - 1] >= a[i] else 1
    ans = max(ans, inc, dec)
print(ans)
`],
  ["2531", "two_pointer-2531", "two_pointer", "Rotating Sushi", `import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
cnt = [0] * (d + 1)
kind = 0
for i in range(k):
    if cnt[a[i]] == 0:
        kind += 1
    cnt[a[i]] += 1
ans = kind + (1 if cnt[c] == 0 else 0)
for start in range(1, n):
    out = a[start - 1]
    cnt[out] -= 1
    if cnt[out] == 0:
        kind -= 1
    inn = a[(start + k - 1) % n]
    if cnt[inn] == 0:
        kind += 1
    cnt[inn] += 1
    ans = max(ans, kind + (1 if cnt[c] == 0 else 0))
print(ans)
`],
  ["2583", "graph_traversal-2583", "graph_traversal", "Area", `from collections import deque
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
grid = [[False] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = True
areas = []
for r in range(m):
    for c in range(n):
        if grid[r][c]:
            continue
        grid[r][c] = True
        q = deque([(r, c)])
        size = 0
        while q:
            x, y = q.popleft()
            size += 1
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not grid[nx][ny]:
                    grid[nx][ny] = True
                    q.append((nx, ny))
        areas.append(size)
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))
`],
  ["2644", "graph_traversal-2644", "graph_traversal", "Kinship", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
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
    for y in g[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
print(dist[b])
`],
  ["2792", "binary_search-2792", "binary_search", "Jewelry Box", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
lo, hi = 1, max(a)
while lo < hi:
    mid = (lo + hi) // 2
    need = sum((x + mid - 1) // mid for x in a)
    if need <= n:
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["2961", "brute_force-2961", "brute_force", "Delicious Food", `import sys
input = sys.stdin.readline
n = int(input())
ing = [tuple(map(int, input().split())) for _ in range(n)]
ans = 10 ** 18
for mask in range(1, 1 << n):
    sour = 1
    bitter = 0
    for i in range(n):
        if mask >> i & 1:
            sour *= ing[i][0]
            bitter += ing[i][1]
    ans = min(ans, abs(sour - bitter))
print(ans)
`],
  ["3085", "brute_force-3085", "brute_force", "Candy Game", `import sys
input = sys.stdin.readline
n = int(input())
a = [list(input().strip()) for _ in range(n)]
def best():
    res = 1
    for i in range(n):
        row = col = 1
        for j in range(1, n):
            row = row + 1 if a[i][j] == a[i][j - 1] else 1
            col = col + 1 if a[j][i] == a[j - 1][i] else 1
            res = max(res, row, col)
    return res
ans = best()
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            ans = max(ans, best())
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        if i + 1 < n:
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            ans = max(ans, best())
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
print(ans)
`],
  ["3184", "graph_traversal-3184", "graph_traversal", "Sheep", `from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
sheep = wolves = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == '#':
            continue
        q = deque([(i, j)])
        s = w = 0
        if a[i][j] == 'o':
            s += 1
        elif a[i][j] == 'v':
            w += 1
        a[i][j] = '#'
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != '#':
                    if a[nx][ny] == 'o':
                        s += 1
                    elif a[nx][ny] == 'v':
                        w += 1
                    a[nx][ny] = '#'
                    q.append((nx, ny))
        if s > w:
            sheep += s
        else:
            wolves += w
print(sheep, wolves)
`],
  ["3187", "graph_traversal-3187", "graph_traversal", "Shepherd", `from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
sheep = wolves = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == '#':
            continue
        q = deque([(i, j)])
        s = w = 0
        if a[i][j] == 'k':
            s += 1
        elif a[i][j] == 'v':
            w += 1
        a[i][j] = '#'
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != '#':
                    if a[nx][ny] == 'k':
                        s += 1
                    elif a[nx][ny] == 'v':
                        w += 1
                    a[nx][ny] = '#'
                    q.append((nx, ny))
        if s > w:
            sheep += s
        else:
            wolves += w
print(sheep, wolves)
`],
  ["3273", "two_pointer-3273", "two_pointer", "Two Sum", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
x = int(input())
l, r = 0, n - 1
ans = 0
while l < r:
    s = a[l] + a[r]
    if s == x:
        ans += 1
        l += 1
        r -= 1
    elif s < x:
        l += 1
    else:
        r -= 1
print(ans)
`],
  ["4097", "dynamic_programming_1-4097", "dynamic_programming_1", "Profit", `import sys
input = sys.stdin.readline
out = []
while True:
    n = int(input())
    if n == 0:
        break
    best = cur = int(input())
    for _ in range(n - 1):
        x = int(input())
        cur = max(x, cur + x)
        best = max(best, cur)
    out.append(str(best))
print('\\n'.join(out))
`],
  ["5014", "graph_traversal-5014", "graph_traversal", "Startlink", `from collections import deque
import sys
f, s, g, u, d = map(int, sys.stdin.readline().split())
dist = [-1] * (f + 1)
dist[s] = 0
q = deque([s])
while q:
    x = q.popleft()
    for nx in (x + u, x - d):
        if 1 <= nx <= f and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
print(dist[g] if dist[g] != -1 else "use the stairs")
`],
  ["5567", "graph_traversal-5567", "graph_traversal", "Wedding", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dist = [-1] * (n + 1)
dist[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    for y in g[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
print(sum(1 for d in dist[2:] if 1 <= d <= 2))
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
  console.log(`[import-manual-batch-14] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-14] wrote ${OUT}`);
