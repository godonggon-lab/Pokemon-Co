import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["11123", "graph_traversal-11123", "graph_traversal", "Sheep", `from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    h, w = map(int, input().split())
    g = [list(input().strip()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] != '#':
                continue
            ans += 1
            g[i][j] = '.'
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and g[nx][ny] == '#':
                        g[nx][ny] = '.'
                        q.append((nx, ny))
    out.append(str(ans))
print('\\n'.join(out))
`],
  ["11170", "brute_force-11170", "brute_force", "Zero Count", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    out.append(str(sum(str(x).count('0') for x in range(n, m + 1))))
print('\\n'.join(out))
`],
  ["11502", "brute_force-11502", "brute_force", "Three Primes", `import sys
input = sys.stdin.readline
sieve = [True] * 1001
sieve[0] = sieve[1] = False
for i in range(2, 32):
    if sieve[i]:
        for j in range(i*i, 1001, i):
            sieve[j] = False
primes = [i for i in range(2, 1001) if sieve[i]]
t = int(input())
out = []
for _ in range(t):
    k = int(input())
    found = None
    for a in primes:
        if found: break
        for b in primes:
            c = k - a - b
            if c >= 2 and c <= 1000 and sieve[c]:
                found = f"{a} {b} {c}"
                break
    out.append(found or "0")
print('\\n'.join(out))
`],
  ["11561", "binary_search-11561", "binary_search", "Stepping Stones", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lo, hi = 1, 2_000_000_000
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * (mid + 1) // 2 <= n:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    out.append(str(ans))
print('\\n'.join(out))
`],
  ["11568", "dynamic_programming_1-11568", "dynamic_programming_1", "Increasing Subsequence", `import bisect, sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
lis = []
for x in a:
    i = bisect.bisect_left(lis, x)
    if i == len(lis):
        lis.append(x)
    else:
        lis[i] = x
print(len(lis))
`],
  ["11687", "binary_search-11687", "binary_search", "Factorial Zero", `import sys
m = int(sys.stdin.readline())
def zeros(x):
    s = 0
    while x:
        x //= 5
        s += x
    return s
lo, hi = 0, 5 * m + 5
while lo < hi:
    mid = (lo + hi) // 2
    if zeros(mid) >= m:
        hi = mid
    else:
        lo = mid + 1
print(lo if zeros(lo) == m else -1)
`],
  ["12101", "backtracking-12101", "backtracking", "1, 2, 3 Add 2", `import sys
n, k = map(int, sys.stdin.readline().split())
out = []
def dfs(total, parts):
    if total == n:
        out.append('+'.join(map(str, parts)))
        return
    if total > n:
        return
    for x in (1, 2, 3):
        dfs(total + x, parts + [x])
dfs(0, [])
print(out[k - 1] if k <= len(out) else -1)
`],
  ["12761", "graph_traversal-12761", "graph_traversal", "Stone Bridge", `from collections import deque
import sys
a, b, n, m = map(int, sys.stdin.readline().split())
dist = [-1] * 100001
dist[n] = 0
q = deque([n])
while q:
    x = q.popleft()
    if x == m:
        break
    for nx in (x - 1, x + 1, x - a, x + a, x - b, x + b, x * a, x * b):
        if 0 <= nx <= 100000 and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
print(dist[m])
`],
  ["12851", "graph_traversal-12851", "graph_traversal", "Hide and Seek 2", `from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
dist = [-1] * 100001
ways = [0] * 100001
dist[n] = 0
ways[n] = 1
q = deque([n])
while q:
    x = q.popleft()
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= 100000:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                ways[nx] = ways[x]
                q.append(nx)
            elif dist[nx] == dist[x] + 1:
                ways[nx] += ways[x]
print(dist[k])
print(ways[k])
`],
  ["12919", "brute_force-12919", "brute_force", "A and B 2", `import sys
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
ans = 0
def dfs(cur):
    global ans
    if ans:
        return
    if len(cur) == len(s):
        ans = int(cur == s)
        return
    if cur.endswith('A'):
        dfs(cur[:-1])
    if cur.startswith('B'):
        dfs(cur[1:][::-1])
dfs(t)
print(ans)
`],
  ["13398", "dynamic_programming_2-13398", "dynamic_programming_2", "Continuous Sum 2", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
keep = a[0]
drop = -10**18
ans = a[0]
for x in a[1:]:
    drop = max(keep, drop + x)
    keep = max(x, keep + x)
    ans = max(ans, keep, drop)
print(ans)
`],
  ["13702", "binary_search-13702", "binary_search", "Beer", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
lo, hi = 0, max(a)
while lo < hi:
    mid = (lo + hi + 1) // 2
    if mid and sum(x // mid for x in a) >= k:
        lo = mid
    else:
        hi = mid - 1
print(lo)
`],
  ["14225", "brute_force-14225", "brute_force", "Subset Sum", `import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
seen = set()
def dfs(i, total):
    if i == n:
        seen.add(total)
        return
    dfs(i + 1, total)
    dfs(i + 1, total + a[i])
dfs(0, 0)
x = 1
while x in seen:
    x += 1
print(x)
`],
  ["14248", "graph_traversal-14248", "graph_traversal", "Jump Jump", `from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
s = int(input()) - 1
seen = [False] * n
seen[s] = True
q = deque([s])
while q:
    x = q.popleft()
    for nx in (x - a[x], x + a[x]):
        if 0 <= nx < n and not seen[nx]:
            seen[nx] = True
            q.append(nx)
print(sum(seen))
`],
  ["14501", "brute_force-14501", "brute_force", "Resignation", `import sys
input = sys.stdin.readline
n = int(input())
t, p = [0]*(n+1), [0]*(n+1)
for i in range(n):
    t[i], p[i] = map(int, input().split())
dp = [0] * (n + 2)
for day in range(n - 1, -1, -1):
    dp[day] = dp[day + 1]
    if day + t[day] <= n:
        dp[day] = max(dp[day], p[day] + dp[day + t[day]])
print(dp[0])
`],
  ["14575", "binary_search-14575", "binary_search", "Duel", `import sys
input = sys.stdin.readline
n, t = map(int, input().split())
limits = [tuple(map(int, input().split())) for _ in range(n)]
if sum(l for l, _ in limits) > t or sum(r for _, r in limits) < t:
    print(-1)
else:
    lo, hi = 0, 10**9
    while lo < hi:
        mid = (lo + hi) // 2
        low = sum(l for l, _ in limits)
        high = sum(min(r, mid) for _, r in limits)
        if high >= t and all(l <= mid for l, _ in limits):
            hi = mid
        else:
            lo = mid + 1
    print(lo)
`],
  ["14627", "binary_search-14627", "binary_search", "Green Onion Chicken", `import sys
input = sys.stdin.readline
s, c = map(int, input().split())
a = [int(input()) for _ in range(s)]
lo, hi = 1, max(a)
while lo <= hi:
    mid = (lo + hi) // 2
    if sum(x // mid for x in a) >= c:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(sum(a) - ans * c)
`],
  ["14912", "brute_force-14912", "brute_force", "Number Frequency", `import sys
n, d = sys.stdin.readline().split()
n = int(n)
print(sum(str(i).count(d) for i in range(1, n + 1)))
`],
  ["15565", "two_pointer-15565", "two_pointer", "Cute Ryan", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
pos = [i for i, x in enumerate(a) if x == 1]
if len(pos) < k:
    print(-1)
else:
    print(min(pos[i + k - 1] - pos[i] + 1 for i in range(len(pos) - k + 1)))
`],
  ["15624", "dynamic_programming_1-15624", "dynamic_programming_1", "Fibonacci 7", `import sys
n = int(sys.stdin.readline())
mod = 1000000007
a, b = 0, 1
for _ in range(n):
    a, b = b, (a + b) % mod
print(a)
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
  console.log(`[import-manual-batch-16] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-16] wrote ${OUT}`);
