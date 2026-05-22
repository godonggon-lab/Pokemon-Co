import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["7795", "binary_search-7795", "binary_search", "Eat or Be Eaten", `import bisect, sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    out.append(str(sum(bisect.bisect_left(b, x) for x in a)))
print('\\n'.join(out))
`],
  ["8983", "binary_search-8983", "binary_search", "Hunting", `import bisect, sys
input = sys.stdin.readline
m, n, l = map(int, input().split())
guns = sorted(map(int, input().split()))
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    i = bisect.bisect_left(guns, x)
    ok = False
    for j in (i - 1, i):
        if 0 <= j < m and abs(guns[j] - x) + y <= l:
            ok = True
    ans += ok
print(ans)
`],
  ["9007", "binary_search-9007", "binary_search", "Canoe Race", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(4)]
    ab = sorted(a + b for a in arr[0] for b in arr[1])
    cd = sorted(c + d for c in arr[2] for d in arr[3])
    l, r = 0, len(cd) - 1
    best = ab[0] + cd[0]
    while l < len(ab) and r >= 0:
        s = ab[l] + cd[r]
        if abs(k - s) < abs(k - best) or (abs(k - s) == abs(k - best) and s < best):
            best = s
        if s < k:
            l += 1
        else:
            r -= 1
    out.append(str(best))
print('\\n'.join(out))
`],
  ["10025", "two_pointer-10025", "two_pointer", "Lazy Polar Bear", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ice = [0] * 1000001
for _ in range(n):
    g, x = map(int, input().split())
    ice[x] += g
window = 2 * k + 1
cur = sum(ice[:window])
ans = cur
for i in range(window, len(ice)):
    cur += ice[i] - ice[i - window]
    ans = max(ans, cur)
print(ans)
`],
  ["10472", "brute_force-10472", "brute_force", "Tic Tac Toe", `from collections import deque
import sys
input = sys.stdin.readline
masks = []
for i in range(3):
    for j in range(3):
        mask = 0
        for x, y in ((i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if 0 <= x < 3 and 0 <= y < 3:
                mask ^= 1 << (x * 3 + y)
        masks.append(mask)
dist = [-1] * 512
dist[0] = 0
q = deque([0])
while q:
    x = q.popleft()
    for mask in masks:
        nx = x ^ mask
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
p = int(input())
out = []
for _ in range(p):
    state = 0
    for i in range(3):
        row = input().strip()
        for j, ch in enumerate(row):
            if ch == '*':
                state |= 1 << (i * 3 + j)
    out.append(str(dist[state]))
print('\\n'.join(out))
`],
  ["11054", "dynamic_programming_2-11054", "dynamic_programming_2", "Longest Bitonic Subsequence", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
inc = [1] * n
dec = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            inc[i] = max(inc[i], inc[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[j] < a[i]:
            dec[i] = max(dec[i], dec[j] + 1)
print(max(inc[i] + dec[i] - 1 for i in range(n)))
`],
  ["11060", "dynamic_programming_1-11060", "dynamic_programming_1", "Jump Jump", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
inf = 10 ** 9
dp = [inf] * n
dp[0] = 0
for i in range(n):
    if dp[i] == inf:
        continue
    for j in range(1, a[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[-1] if dp[-1] != inf else -1)
`],
  ["11403", "shortest_path-11403", "shortest_path", "Find Path", `import sys
input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        if g[i][k]:
            for j in range(n):
                if g[k][j]:
                    g[i][j] = 1
print('\\n'.join(' '.join(map(str, row)) for row in g))
`],
  ["11404", "shortest_path-11404", "shortest_path", "Floyd", `import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 10 ** 15
d = [[inf] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = min(d[a - 1][b - 1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
out = []
for row in d:
    out.append(' '.join('0' if x == inf else str(x) for x in row))
print('\\n'.join(out))
`],
  ["14921", "two_pointer-14921", "two_pointer", "Solutions", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
best = a[l] + a[r]
while l < r:
    s = a[l] + a[r]
    if abs(s) < abs(best):
        best = s
    if s < 0:
        l += 1
    else:
        r -= 1
print(best)
`],
  ["15270", "brute_force-15270", "brute_force", "Friend Pairs", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
used = [False] * (n + 1)
ans = 0
def dfs(idx, cnt):
    global ans
    if idx == m:
        ans = max(ans, cnt)
        return
    a, b = edges[idx]
    if not used[a] and not used[b]:
        used[a] = used[b] = True
        dfs(idx + 1, cnt + 2)
        used[a] = used[b] = False
    dfs(idx + 1, cnt)
dfs(0, 0)
print(ans + (1 if ans < n else 0))
`],
  ["15489", "dynamic_programming_1-15489", "dynamic_programming_1", "Pascal Triangle", `import sys
r, c, w = map(int, sys.stdin.readline().split())
comb = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    comb[i][1] = comb[i][i] = 1
    for j in range(2, i):
        comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
ans = 0
for i in range(w):
    for j in range(i + 1):
        ans += comb[r + i][c + j]
print(ans)
`],
  ["15724", "dynamic_programming_2-15724", "dynamic_programming_2", "Jumuljin", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ps = [[0] * (m + 1)]
for _ in range(n):
    row = list(map(int, input().split()))
    acc = [0]
    for x in row:
        acc.append(acc[-1] + x)
    ps.append([ps[-1][j] + acc[j] for j in range(m + 1)])
k = int(input())
out = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    out.append(str(ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]))
print('\\n'.join(out))
`],
  ["15810", "binary_search-15810", "binary_search", "Balloon Factory", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
lo, hi = 0, min(a) * m
while lo < hi:
    mid = (lo + hi) // 2
    if sum(mid // x for x in a) >= m:
        hi = mid
    else:
        lo = mid + 1
print(lo)
`],
  ["15970", "brute_force-15970", "brute_force", "Drawing Arrows", `import sys
input = sys.stdin.readline
n = int(input())
colors = {}
for _ in range(n):
    x, c = map(int, input().split())
    colors.setdefault(c, []).append(x)
ans = 0
for xs in colors.values():
    xs.sort()
    for i, x in enumerate(xs):
        best = 10 ** 9
        if i > 0:
            best = min(best, x - xs[i - 1])
        if i + 1 < len(xs):
            best = min(best, xs[i + 1] - x)
        ans += best
print(ans)
`],
  ["15988", "dynamic_programming_1-15988", "dynamic_programming_1", "1, 2, 3 Add 3", `import sys
input = sys.stdin.readline
mod = 1000000009
t = int(input())
queries = [int(input()) for _ in range(t)]
mx = max(queries)
dp = [0] * (max(4, mx + 1))
dp[0] = 1
for i in range(1, mx + 1):
    dp[i] = ((dp[i - 1] if i >= 1 else 0) + (dp[i - 2] if i >= 2 else 0) + (dp[i - 3] if i >= 3 else 0)) % mod
print('\\n'.join(str(dp[x]) for x in queries))
`],
  ["15992", "dynamic_programming_1-15992", "dynamic_programming_1", "1, 2, 3 Add 7", `import sys
input = sys.stdin.readline
mod = 1000000009
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
mxn = max(n for n, _ in queries)
mxm = max(m for _, m in queries)
dp = [[0] * (mxm + 1) for _ in range(mxn + 1)]
dp[0][0] = 1
for total in range(1, mxn + 1):
    for cnt in range(1, mxm + 1):
        dp[total][cnt] = sum(dp[total - x][cnt - 1] for x in (1, 2, 3) if total >= x) % mod
print('\\n'.join(str(dp[n][m]) for n, m in queries))
`],
  ["15993", "dynamic_programming_1-15993", "dynamic_programming_1", "1, 2, 3 Add 8", `import sys
input = sys.stdin.readline
mod = 1000000009
t = int(input())
queries = [int(input()) for _ in range(t)]
mx = max(queries)
dp = [[0, 0] for _ in range(mx + 1)]
for x in (1, 2, 3):
    if x <= mx:
        dp[x][1] = 1
for total in range(1, mx + 1):
    for x in (1, 2, 3):
        if total > x:
            dp[total][0] = (dp[total][0] + dp[total - x][1]) % mod
            dp[total][1] = (dp[total][1] + dp[total - x][0]) % mod
print('\\n'.join(f"{dp[n][1]} {dp[n][0]}" for n in queries))
`],
  ["16194", "dynamic_programming_1-16194", "dynamic_programming_1", "Card Buying 2", `import sys
input = sys.stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [10 ** 9] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = min(dp[i - j] + p[j] for j in range(1, i + 1))
print(dp[n])
`],
  ["16195", "dynamic_programming_1-16195", "dynamic_programming_1", "1, 2, 3 Add 9", `import sys
input = sys.stdin.readline
mod = 1000000009
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
mxn = max(n for n, _ in queries)
mxm = max(m for _, m in queries)
dp = [[0] * (mxm + 1) for _ in range(mxn + 1)]
dp[0][0] = 1
for total in range(1, mxn + 1):
    for cnt in range(1, mxm + 1):
        dp[total][cnt] = sum(dp[total - x][cnt - 1] for x in (1, 2, 3) if total >= x) % mod
pref = [[0] * (mxm + 1) for _ in range(mxn + 1)]
for n in range(1, mxn + 1):
    acc = 0
    for m in range(1, mxm + 1):
        acc = (acc + dp[n][m]) % mod
        pref[n][m] = acc
print('\\n'.join(str(pref[n][m]) for n, m in queries))
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
  console.log(`[import-manual-batch-17] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-17] wrote ${OUT}`);
