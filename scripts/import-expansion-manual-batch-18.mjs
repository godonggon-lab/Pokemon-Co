import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["2670", "dynamic_programming_1-2670", "dynamic_programming_1", "Continuous Product", `import sys
input = sys.stdin.readline
n = int(input())
best = cur = float(input())
for _ in range(n - 1):
    x = float(input())
    cur = max(x, cur * x)
    best = max(best, cur)
print(f"{best:.3f}")
`],
  ["2758", "dynamic_programming_2-2758", "dynamic_programming_2", "Lotto", `import sys
input = sys.stdin.readline
dp = [[0] * 2001 for _ in range(11)]
for j in range(1, 2001):
    dp[1][j] = 1
for i in range(2, 11):
    acc = 0
    for j in range(1, 2001):
        if j % 2 == 0:
            acc += dp[i - 1][j // 2]
        dp[i][j] = acc
t = int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    out.append(str(sum(dp[n][1:m + 1])))
print('\\n'.join(out))
`],
  ["2876", "dynamic_programming_1-2876", "dynamic_programming_1", "Graphic Rating", `import sys
input = sys.stdin.readline
n = int(input())
cur = [0] * 6
best_len, best_score = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    nxt = [0] * 6
    nxt[a] = cur[a] + 1
    nxt[b] = max(nxt[b], cur[b] + 1)
    cur = nxt
    for score in range(1, 6):
        if cur[score] > best_len or (cur[score] == best_len and score < best_score):
            best_len, best_score = cur[score], score
print(best_len, best_score)
`],
  ["3020", "binary_search-3020", "binary_search", "Firefly", `import bisect, sys
input = sys.stdin.readline
n, h = map(int, input().split())
bottom, top = [], []
for i in range(n):
    x = int(input())
    if i % 2 == 0:
        bottom.append(x)
    else:
        top.append(x)
bottom.sort()
top.sort()
best = n + 1
count = 0
for height in range(1, h + 1):
    hit = len(bottom) - bisect.bisect_left(bottom, height)
    hit += len(top) - bisect.bisect_left(top, h - height + 1)
    if hit < best:
        best, count = hit, 1
    elif hit == best:
        count += 1
print(best, count)
`],
  ["3151", "two_pointer-3151", "two_pointer", "Together", `import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
ans = 0
for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        s = a[i] + a[l] + a[r]
        if s == 0:
            if a[l] == a[r]:
                cnt = r - l + 1
                ans += cnt * (cnt - 1) // 2
                break
            lc = rc = 1
            while l + 1 < r and a[l] == a[l + 1]:
                lc += 1; l += 1
            while r - 1 > l and a[r] == a[r - 1]:
                rc += 1; r -= 1
            ans += lc * rc
            l += 1; r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1
print(ans)
`],
  ["4095", "dynamic_programming_2-4095", "dynamic_programming_2", "Largest Square", `import sys
input = sys.stdin.readline
out = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    best = 0
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j, x in enumerate(row, 1):
            if x:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                best = max(best, dp[i][j])
    out.append(str(best))
print('\\n'.join(out))
`],
  ["4485", "shortest_path-4485", "shortest_path", "Zelda", `import heapq, sys
input = sys.stdin.readline
case = 1
out = []
while True:
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    dist = [[10**9] * n for _ in range(n)]
    dist[0][0] = a[0][0]
    heap = [(a[0][0], 0, 0)]
    while heap:
        d, x, y = heapq.heappop(heap)
        if d != dist[x][y]:
            continue
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + a[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(heap, (nd, nx, ny))
    out.append(f"Problem {case}: {dist[n-1][n-1]}")
    case += 1
print('\\n'.join(out))
`],
  ["5972", "shortest_path-5972", "shortest_path", "Delivery", `import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c)); g[b].append((a, c))
dist = [10**18] * (n + 1)
dist[1] = 0
heap = [(0, 1)]
while heap:
    d, x = heapq.heappop(heap)
    if d != dist[x]:
        continue
    for y, w in g[x]:
        nd = d + w
        if nd < dist[y]:
            dist[y] = nd
            heapq.heappush(heap, (nd, y))
print(dist[n])
`],
  ["6118", "graph_traversal-6118", "graph_traversal", "Hide and Seek", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b); g[b].append(a)
dist = [-1] * (n + 1)
dist[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    for y in g[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
mx = max(dist)
idx = dist.index(mx)
print(idx, mx, dist.count(mx))
`],
  ["6137", "two_pointer-6137", "two_pointer", "Best Cow Line", `import sys
input = sys.stdin.readline
n = int(input())
s = [input().strip() for _ in range(n)]
l, r = 0, n - 1
out = []
while l <= r:
    left = True
    i, j = l, r
    while i < j and s[i] == s[j]:
        i += 1; j -= 1
    if i < j and s[i] > s[j]:
        left = False
    if left:
        out.append(s[l]); l += 1
    else:
        out.append(s[r]); r -= 1
print('\\n'.join(''.join(out)[i:i+80] for i in range(0, n, 80)))
`],
  ["6209", "binary_search-6209", "binary_search", "Stepping Stones", `import sys
input = sys.stdin.readline
d, n, m = map(int, input().split())
rocks = [0] + sorted(int(input()) for _ in range(n)) + [d]
lo, hi = 1, d
while lo <= hi:
    mid = (lo + hi) // 2
    removed = 0
    last = 0
    for i in range(1, len(rocks)):
        if rocks[i] - rocks[last] < mid:
            removed += 1
        else:
            last = i
    if removed <= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
`],
  ["7562", "graph_traversal-7562", "graph_traversal", "Knight Moves", `from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
out = []
dirs = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    dist = [[-1] * n for _ in range(n)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    out.append(str(dist[tx][ty]))
print('\\n'.join(out))
`],
  ["9084", "dynamic_programming_2-9084", "dynamic_programming_2", "Coin", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for v in range(coin, m + 1):
            dp[v] += dp[v - coin]
    out.append(str(dp[m]))
print('\\n'.join(out))
`],
  ["9205", "shortest_path-9205", "shortest_path", "Beer Walking", `from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n + 2)]
    seen = [False] * (n + 2)
    seen[0] = True
    q = deque([0])
    while q:
        x = q.popleft()
        for i in range(n + 2):
            if not seen[i] and abs(pts[x][0] - pts[i][0]) + abs(pts[x][1] - pts[i][1]) <= 1000:
                seen[i] = True
                q.append(i)
    out.append("happy" if seen[-1] else "sad")
print('\\n'.join(out))
`],
  ["9466", "graph_traversal-9466", "graph_traversal", "Term Project", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    state = [0] * (n + 1)
    team = 0
    for i in range(1, n + 1):
        if state[i]:
            continue
        cur = i
        path = {}
        while not state[cur]:
            path[cur] = len(path)
            state[cur] = 1
            cur = a[cur]
        if cur in path:
            team += len(path) - path[cur]
        for x in path:
            state[x] = 2
    out.append(str(n - team))
print('\\n'.join(out))
`],
  ["10026", "graph_traversal-10026", "graph_traversal", "Color Weakness", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
g = [input().strip() for _ in range(n)]
def count(weak):
    seen = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if seen[i][j]:
                continue
            ans += 1
            seen[i][j] = True
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
                        same = g[nx][ny] == g[i][j] if not weak else (g[nx][ny] == g[i][j] or (g[nx][ny] in 'RG' and g[i][j] in 'RG'))
                        if same:
                            seen[nx][ny] = True
                            q.append((nx, ny))
    return ans
print(count(False), count(True))
`],
  ["11559", "graph_traversal-11559", "graph_traversal", "Puyo Puyo", `from collections import deque
import sys
board = [list(sys.stdin.readline().strip()) for _ in range(12)]
ans = 0
while True:
    seen = [[False]*6 for _ in range(12)]
    groups = []
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.' or seen[i][j]:
                continue
            seen[i][j] = True
            q = deque([(i, j)])
            cells = [(i, j)]
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 12 and 0 <= ny < 6 and not seen[nx][ny] and board[nx][ny] == board[i][j]:
                        seen[nx][ny] = True
                        q.append((nx, ny))
                        cells.append((nx, ny))
            if len(cells) >= 4:
                groups.extend(cells)
    if not groups:
        break
    ans += 1
    for x, y in groups:
        board[x][y] = '.'
    for c in range(6):
        vals = [board[r][c] for r in range(11, -1, -1) if board[r][c] != '.']
        for r in range(12):
            board[11-r][c] = vals[r] if r < len(vals) else '.'
print(ans)
`],
  ["12764", "data_structure2-12764", "data_structure2", "Internet Cafe", `import heapq, sys
input = sys.stdin.readline
n = int(input())
people = sorted(tuple(map(int, input().split())) for _ in range(n))
using = []
free = []
counts = []
for start, end in people:
    while using and using[0][0] <= start:
        _, seat = heapq.heappop(using)
        heapq.heappush(free, seat)
    if free:
        seat = heapq.heappop(free)
    else:
        seat = len(counts)
        counts.append(0)
    counts[seat] += 1
    heapq.heappush(using, (end, seat))
print(len(counts))
print(' '.join(map(str, counts)))
`],
  ["13975", "greedy-13975", "greedy", "File Merge 3", `import heapq, sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += a + b
        heapq.heappush(heap, a + b)
    out.append(str(total))
print('\\n'.join(out))
`],
  ["16401", "binary_search-16401", "binary_search", "Snack Party", `import sys
input = sys.stdin.readline
m, n = map(int, input().split())
a = list(map(int, input().split()))
lo, hi = 1, max(a)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if sum(x // mid for x in a) >= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
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
  console.log(`[import-manual-batch-18] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-18] wrote ${OUT}`);
