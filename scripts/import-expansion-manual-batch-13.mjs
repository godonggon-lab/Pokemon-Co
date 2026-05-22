import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1644", "two_pointer-1644", "two_pointer", "Prime Sum", `import sys
n = int(sys.stdin.readline())
if n < 2:
    print(0)
else:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i in range(n + 1) if sieve[i]]
    left = total = ans = 0
    for right in range(len(primes)):
        total += primes[right]
        while total > n and left <= right:
            total -= primes[left]
            left += 1
        if total == n:
            ans += 1
    print(ans)
`],
  ["1655", "data_structure2-1655", "data_structure2", "Say Median", `import heapq, sys
input = sys.stdin.readline
n = int(input())
low, high = [], []
out = []
for _ in range(n):
    x = int(input())
    if len(low) == len(high):
        heapq.heappush(low, -x)
    else:
        heapq.heappush(high, x)
    if high and -low[0] > high[0]:
        a = -heapq.heappop(low)
        b = heapq.heappop(high)
        heapq.heappush(low, -b)
        heapq.heappush(high, a)
    out.append(str(-low[0]))
print('\\n'.join(out))
`],
  ["1660", "dynamic_programming_1-1660", "dynamic_programming_1", "Captain Lee", `import sys
n = int(sys.stdin.readline())
tetra = []
s = 0
for i in range(1, 200):
    s += i * (i + 1) // 2
    if s > n:
        break
    tetra.append(s)
dp = [10 ** 9] * (n + 1)
dp[0] = 0
for x in tetra:
    for v in range(x, n + 1):
        dp[v] = min(dp[v], dp[v - x] + 1)
print(dp[n])
`],
  ["1668", "brute_force-1668", "brute_force", "Trophy", `import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
def count(seq):
    best = ans = 0
    for x in seq:
        if x > best:
            best = x
            ans += 1
    return ans
print(count(a))
print(count(reversed(a)))
`],
  ["1699", "dynamic_programming_1-1699", "dynamic_programming_1", "Sum of Squares", `import sys
n = int(sys.stdin.readline())
dp = list(range(n + 1))
for i in range(1, int(n ** 0.5) + 1):
    sq = i * i
    for v in range(sq, n + 1):
        if dp[v] > dp[v - sq] + 1:
            dp[v] = dp[v - sq] + 1
print(dp[n])
`],
  ["1713", "simulation-1713", "simulation", "Candidate Recommendation", `import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
recs = list(map(int, input().split()))
frames = {}
time = 0
for student in recs:
    time += 1
    if student in frames:
        count, first = frames[student]
        frames[student] = (count + 1, first)
        continue
    if len(frames) == n:
        victim = min(frames, key=lambda s: (frames[s][0], frames[s][1]))
        del frames[victim]
    frames[student] = (1, time)
print(' '.join(map(str, sorted(frames))))
`],
  ["1743", "graph_traversal-1743", "graph_traversal", "Avoid The Lakes", `from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [[False] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = True
ans = 0
for r in range(n):
    for c in range(m):
        if not grid[r][c]:
            continue
        grid[r][c] = False
        q = deque([(r, c)])
        size = 0
        while q:
            x, y = q.popleft()
            size += 1
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                    grid[nx][ny] = False
                    q.append((nx, ny))
        ans = max(ans, size)
print(ans)
`],
  ["1759", "backtracking-1759", "backtracking", "Password Making", `from itertools import combinations
import sys
l, c = map(int, sys.stdin.readline().split())
letters = sorted(sys.stdin.readline().split())
vowels = set('aeiou')
out = []
for comb in combinations(letters, l):
    v = sum(ch in vowels for ch in comb)
    if v >= 1 and l - v >= 2:
        out.append(''.join(comb))
print('\\n'.join(out))
`],
  ["1766", "topological_sorting-1766", "topological_sorting", "Problem Set", `import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indeg[b] += 1
heap = [i for i in range(1, n + 1) if indeg[i] == 0]
heapq.heapify(heap)
out = []
while heap:
    x = heapq.heappop(heap)
    out.append(str(x))
    for y in g[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            heapq.heappush(heap, y)
print(' '.join(out))
`],
  ["1780", "divide_and_conquer-1780", "divide_and_conquer", "Paper Count", `import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = {-1: 0, 0: 0, 1: 0}
def solve(r, c, size):
    first = a[r][c]
    ok = True
    for i in range(r, r + size):
        for j in range(c, c + size):
            if a[i][j] != first:
                ok = False
                break
        if not ok:
            break
    if ok:
        ans[first] += 1
        return
    step = size // 3
    for dr in range(3):
        for dc in range(3):
            solve(r + dr * step, c + dc * step, step)
solve(0, 0, n)
print(ans[-1])
print(ans[0])
print(ans[1])
`],
  ["1863", "data_structure-1863", "data_structure", "Skyline Easy", `import sys
input = sys.stdin.readline
n = int(input())
stack = []
ans = 0
for _ in range(n):
    _, h = map(int, input().split())
    while stack and stack[-1] > h:
        stack.pop()
        ans += 1
    if h and (not stack or stack[-1] < h):
        stack.append(h)
while stack:
    stack.pop()
    ans += 1
print(ans)
`],
  ["1895", "brute_force-1895", "brute_force", "Filter", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
ans = 0
for i in range(r - 2):
    for j in range(c - 2):
        vals = []
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                vals.append(a[x][y])
        vals.sort()
        ans += vals[4] >= t
print(ans)
`],
  ["1915", "dynamic_programming_2-1915", "dynamic_programming_2", "Largest Square", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
best = 0
for i in range(1, n + 1):
    row = input().strip()
    for j, ch in enumerate(row, 1):
        if ch == '1':
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            best = max(best, dp[i][j])
print(best * best)
`],
  ["1916", "shortest_path-1916", "shortest_path", "Minimum Cost", `import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
s, e = map(int, input().split())
dist = [10 ** 18] * (n + 1)
dist[s] = 0
heap = [(0, s)]
while heap:
    d, x = heapq.heappop(heap)
    if d != dist[x]:
        continue
    if x == e:
        break
    for y, w in g[x]:
        nd = d + w
        if nd < dist[y]:
            dist[y] = nd
            heapq.heappush(heap, (nd, y))
print(dist[e])
`],
  ["1926", "graph_traversal-1926", "graph_traversal", "Picture", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
count = best = 0
for r in range(n):
    for c in range(m):
        if a[r][c] == 0:
            continue
        count += 1
        a[r][c] = 0
        q = deque([(r, c)])
        size = 0
        while q:
            x, y = q.popleft()
            size += 1
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny]:
                    a[nx][ny] = 0
                    q.append((nx, ny))
        best = max(best, size)
print(count)
print(best)
`],
  ["1932", "dynamic_programming_1-1932", "dynamic_programming_1", "Integer Triangle", `import sys
input = sys.stdin.readline
n = int(input())
dp = []
for i in range(n):
    row = list(map(int, input().split()))
    if i == 0:
        dp = row
    else:
        ndp = [0] * (i + 1)
        for j in range(i + 1):
            best = 0
            if j < i:
                best = max(best, dp[j])
            if j > 0:
                best = max(best, dp[j - 1])
            ndp[j] = best + row[j]
        dp = ndp
print(max(dp))
`],
  ["1965", "dynamic_programming_1-1965", "dynamic_programming_1", "Box", `import bisect, sys
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
  ["2003", "two_pointer-2003", "two_pointer", "Sum of Numbers 2", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
left = total = ans = 0
for right in range(n):
    total += a[right]
    while total > m and left <= right:
        total -= a[left]
        left += 1
    if total == m:
        ans += 1
print(ans)
`],
  ["2011", "dynamic_programming_1-2011", "dynamic_programming_1", "Decode Ways", `import sys
s = sys.stdin.readline().strip()
mod = 1000000
if not s or s[0] == '0':
    print(0)
else:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        two = int(s[i - 2:i])
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= mod
    print(dp[n])
`],
  ["2193", "dynamic_programming_1-2193", "dynamic_programming_1", "Pinary Number", `import sys
n = int(sys.stdin.readline())
dp = [0] * (max(3, n + 1))
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
`]
];

async function readJson(file, fallback) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return fallback;
  }
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
  console.log(`[import-manual-batch-13] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-13] wrote ${OUT}`);
