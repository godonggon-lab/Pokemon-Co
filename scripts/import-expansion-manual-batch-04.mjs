import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["11663", "binary_search-11663", "binary_search", "Line Segment Points", `import bisect, sys
input = sys.stdin.readline
n, m = map(int, input().split())
points = sorted(map(int, input().split()))
out = []
for _ in range(m):
    a, b = map(int, input().split())
    out.append(str(bisect.bisect_right(points, b) - bisect.bisect_left(points, a)))
print('\\n'.join(out))
`],
  ["11728", "two_pointer-11728", "two_pointer", "Merge Arrays", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*(sorted(a + b)))
`],
  ["2293", "dynamic_programming_1-2293", "dynamic_programming_1", "Coin 1", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    coin = int(input())
    for value in range(coin, k + 1):
        dp[value] += dp[value - coin]
print(dp[k])
`],
  ["12026", "dynamic_programming_1-12026", "dynamic_programming_1", "BOJ Street", `import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
order = {'B': 'O', 'O': 'J', 'J': 'B'}
INF = 10 ** 18
dp = [INF] * n
dp[0] = 0
for i in range(n):
    if dp[i] == INF:
        continue
    for j in range(i + 1, n):
        if s[j] == order[s[i]]:
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
print(-1 if dp[-1] == INF else dp[-1])
`],
  ["13422", "two_pointer-13422", "two_pointer", "Thief", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == m:
        out.append(str(1 if sum(arr) < k else 0))
        continue
    window = sum(arr[:m])
    answer = 1 if window < k else 0
    doubled = arr + arr
    for i in range(1, n):
        window += doubled[i + m - 1] - doubled[i - 1]
        if window < k:
            answer += 1
    out.append(str(answer))
print('\\n'.join(out))
`],
  ["14284", "shortest_path-14284", "shortest_path", "Connect Edges 2", `import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())
dist = [10 ** 18] * (n + 1)
dist[s] = 0
pq = [(0, s)]
while pq:
    cost, node = heapq.heappop(pq)
    if cost != dist[node]:
        continue
    for nxt, weight in graph[node]:
        nc = cost + weight
        if nc < dist[nxt]:
            dist[nxt] = nc
            heapq.heappush(pq, (nc, nxt))
print(dist[t])
`],
  ["2637", "topological_sorting-2637", "topological_sorting", "Toy Assembly", `import sys
from functools import lru_cache
input = sys.stdin.readline
n = int(input())
m = int(input())
needs = [[] for _ in range(n + 1)]
is_mid = [False] * (n + 1)
for _ in range(m):
    x, y, k = map(int, input().split())
    needs[x].append((y, k))
    is_mid[x] = True
@lru_cache(None)
def calc(part):
    if not needs[part]:
        return {part: 1}
    total = {}
    for sub, count in needs[part]:
        for base, amount in calc(sub).items():
            total[base] = total.get(base, 0) + amount * count
    return total
answer = calc(n)
print('\\n'.join(f"{part} {answer[part]}" for part in sorted(answer)))
`],
  ["7453", "binary_search-7453", "binary_search", "Four Values Whose Sum is 0", `import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
    w, x, y, z = map(int, input().split())
    a.append(w); b.append(x); c.append(y); d.append(z)
left = Counter(x + y for x in a for y in b)
answer = 0
for x in c:
    for y in d:
        answer += left.get(-(x + y), 0)
print(answer)
`],
  ["1507", "shortest_path-1507", "shortest_path", "Road Construction", `import sys
input = sys.stdin.readline
n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
keep = [[True] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                raise SystemExit
            if dist[i][j] == dist[i][k] + dist[k][j]:
                keep[i][j] = False
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if keep[i][j]:
            answer += dist[i][j]
print(answer)
`],
  ["12931", "greedy-12931", "greedy", "Double Addition", `import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
while any(arr):
    for i in range(n):
        if arr[i] % 2:
            arr[i] -= 1
            answer += 1
    if any(arr):
        arr = [x // 2 for x in arr]
        answer += 1
print(answer)
`],
  ["18234", "greedy-18234", "greedy", "Carrots", `import sys
input = sys.stdin.readline
n, t = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
items.sort(key=lambda x: x[1])
start = t - n
print(sum(w + p * (start + i) for i, (w, p) in enumerate(items)))
`],
  ["2571", "prefix_sum-2571", "prefix_sum", "Colored Paper 3", `import sys
input = sys.stdin.readline
board = [[0] * 100 for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for r in range(y, y + 10):
        for c in range(x, x + 10):
            board[r][c] = 1
height = [0] * 100
answer = 0
for r in range(100):
    for c in range(100):
        height[c] = height[c] + 1 if board[r][c] else 0
    stack = []
    for i in range(101):
        cur = height[i] if i < 100 else 0
        while stack and height[stack[-1]] > cur:
            h = height[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            answer = max(answer, h * (i - left))
        stack.append(i)
print(answer)
`],
  ["3673", "prefix_sum-3673", "prefix_sum", "Divisible Subarrays", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    counts = [0] * d
    counts[0] = 1
    prefix = 0
    answer = 0
    for value in arr:
        prefix = (prefix + value) % d
        answer += counts[prefix]
        counts[prefix] += 1
    out.append(str(answer))
print('\\n'.join(out))
`],
  ["5549", "prefix_sum-5549", "prefix_sum", "Planet Exploration", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
k = int(input())
maps = [input().strip() for _ in range(r)]
prefix = [[[0, 0, 0] for _ in range(c + 1)] for _ in range(r + 1)]
idx = {'J': 0, 'O': 1, 'I': 2}
for i in range(1, r + 1):
    for j in range(1, c + 1):
        for z in range(3):
            prefix[i][j][z] = prefix[i - 1][j][z] + prefix[i][j - 1][z] - prefix[i - 1][j - 1][z]
        prefix[i][j][idx[maps[i - 1][j - 1]]] += 1
out = []
for _ in range(k):
    a, b, x, y = map(int, input().split())
    out.append(' '.join(str(prefix[x][y][z] - prefix[a - 1][y][z] - prefix[x][b - 1][z] + prefix[a - 1][b - 1][z]) for z in range(3)))
print('\\n'.join(out))
`],
  ["10713", "prefix_sum-10713", "prefix_sum", "Train", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
route = list(map(int, input().split()))
diff = [0] * (n + 1)
for a, b in zip(route, route[1:]):
    if a > b:
        a, b = b, a
    diff[a] += 1
    diff[b] -= 1
answer = 0
count = 0
for i in range(1, n):
    count += diff[i]
    a, b, c = map(int, input().split())
    answer += min(count * a, count * b + c)
print(answer)
`],
  ["14476", "prefix_sum-14476", "prefix_sum", "Maximum GCD", `import math, sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
prefix = [0] * (n + 1)
suffix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = math.gcd(prefix[i], arr[i])
for i in range(n - 1, -1, -1):
    suffix[i] = math.gcd(suffix[i + 1], arr[i])
best = (-1, -1)
for i in range(n):
    g = math.gcd(prefix[i], suffix[i + 1])
    if arr[i] % g != 0 and g > best[0]:
        best = (g, arr[i])
print(-1 if best[0] == -1 else f"{best[0]} {best[1]}")
`],
  ["17390", "prefix_sum-17390", "prefix_sum", "Must Solve This", `import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = sorted(map(int, input().split()))
prefix = [0]
for value in arr:
    prefix.append(prefix[-1] + value)
out = []
for _ in range(q):
    l, r = map(int, input().split())
    out.append(str(prefix[r] - prefix[l - 1]))
print('\\n'.join(out))
`],
  ["17123", "prefix_sum-17123", "prefix_sum", "Array Play", `import sys
input = sys.stdin.readline
t = int(input())
answers = []
for _ in range(t):
    n, m = map(int, input().split())
    row = [0] * n
    col = [0] * n
    for i in range(n):
        values = list(map(int, input().split()))
        row[i] = sum(values)
        for j, value in enumerate(values):
            col[j] += value
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1 - 1, r2):
            row[i] += (c2 - c1 + 1) * v
        for j in range(c1 - 1, c2):
            col[j] += (r2 - r1 + 1) * v
    answers.append(' '.join(map(str, row)))
    answers.append(' '.join(map(str, col)))
print('\\n'.join(answers))
`],
  ["20002", "dynamic_programming_2-20002", "dynamic_programming_2", "Apple Orchard", `import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = grid[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
answer = -10 ** 18
for size in range(1, n + 1):
    for i in range(size, n + 1):
        for j in range(size, n + 1):
            total = prefix[i][j] - prefix[i - size][j] - prefix[i][j - size] + prefix[i - size][j - size]
            answer = max(answer, total)
print(answer)
`],
  ["17128", "implementation-17128", "implementation", "Cow on the Information Island", `import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = list(map(int, input().split()))
products = []
for i in range(n):
    value = 1
    for j in range(4):
        value *= a[(i + j) % n]
    products.append(value)
score = sum(products)
out = []
for query in queries:
    idx = query - 1
    for start in range(idx - 3, idx + 1):
        pos = start % n
        score -= 2 * products[pos]
        products[pos] *= -1
    out.append(str(score))
print('\\n'.join(out))
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
  console.log(`[import-manual-batch-04] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-04] wrote ${OUT}`);
