import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1003", "dynamic_programming_1-1003", "dynamic_programming_1", "Fibonacci Function", `import sys
t = int(sys.stdin.readline())
dp = [(1, 0), (0, 1)]
for _ in range(2, 41):
    a0, a1 = dp[-2]
    b0, b1 = dp[-1]
    dp.append((a0 + b0, a1 + b1))
out = []
for _ in range(t):
    n = int(sys.stdin.readline())
    out.append(f"{dp[n][0]} {dp[n][1]}")
print('\\n'.join(out))
`],
  ["1018", "brute_force-1018", "brute_force", "Repaint Chessboard", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
ans = 64
for r in range(n - 7):
    for c in range(m - 7):
        for first in 'WB':
            cnt = 0
            for i in range(8):
                for j in range(8):
                    expected = first if (i + j) % 2 == 0 else ('B' if first == 'W' else 'W')
                    cnt += board[r + i][c + j] != expected
            ans = min(ans, cnt)
print(ans)
`],
  ["1059", "brute_force-1059", "brute_force", "Good Interval", `import sys
input = sys.stdin.readline
l = int(input())
s = sorted(map(int, input().split()))
n = int(input())
if n in s:
    print(0)
else:
    low = 0
    high = 1001
    for x in s:
        if x < n:
            low = x
        elif x > n:
            high = x
            break
    print((n - low) * (high - n) - 1)
`],
  ["1065", "brute_force-1065", "brute_force", "Hansu", `import sys
n = int(sys.stdin.readline())
ans = 0
for x in range(1, n + 1):
    d = list(map(int, str(x)))
    if len(d) <= 2 or d[1] - d[0] == d[2] - d[1]:
        ans += 1
print(ans)
`],
  ["1072", "binary_search-1072", "binary_search", "Game", `import sys
x, y = map(int, sys.stdin.readline().split())
z = y * 100 // x
if z >= 99:
    print(-1)
else:
    lo, hi = 1, 10 ** 9
    while lo < hi:
        mid = (lo + hi) // 2
        if (y + mid) * 100 // (x + mid) > z:
            hi = mid
        else:
            lo = mid + 1
    print(lo)
`],
  ["1120", "brute_force-1120", "brute_force", "String", `import sys
a, b = sys.stdin.readline().split()
ans = len(a)
for start in range(len(b) - len(a) + 1):
    ans = min(ans, sum(x != y for x, y in zip(a, b[start:start + len(a)])))
print(ans)
`],
  ["1149", "dynamic_programming_1-1149", "dynamic_programming_1", "RGB Street", `import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 0, 0]
for _ in range(n):
    r, g, b = map(int, input().split())
    dp = [r + min(dp[1], dp[2]), g + min(dp[0], dp[2]), b + min(dp[0], dp[1])]
print(min(dp))
`],
  ["1251", "brute_force-1251", "brute_force", "Word Split", `import sys
s = sys.stdin.readline().strip()
best = None
for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        t = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if best is None or t < best:
            best = t
print(best)
`],
  ["1254", "brute_force-1254", "brute_force", "Palindrome Making", `import sys
s = sys.stdin.readline().strip()
for i in range(len(s)):
    tail = s[i:]
    if tail == tail[::-1]:
        print(len(s) + i)
        break
`],
  ["1303", "graph_traversal-1303", "graph_traversal", "War - Battle", `from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(m)]
seen = [[False] * n for _ in range(m)]
power = {'W': 0, 'B': 0}
for r in range(m):
    for c in range(n):
        if seen[r][c]:
            continue
        color = board[r][c]
        seen[r][c] = True
        q = deque([(r, c)])
        size = 0
        while q:
            x, y = q.popleft()
            size += 1
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not seen[nx][ny] and board[nx][ny] == color:
                    seen[nx][ny] = True
                    q.append((nx, ny))
        power[color] += size * size
print(power['W'], power['B'])
`],
  ["1309", "dynamic_programming_1-1309", "dynamic_programming_1", "Zoo", `import sys
n = int(sys.stdin.readline())
empty = left = right = 1
for _ in range(2, n + 1):
    empty, left, right = (empty + left + right) % 9901, (empty + right) % 9901, (empty + left) % 9901
print((empty + left + right) % 9901)
`],
  ["1374", "greedy-1374", "greedy", "Classroom", `import heapq, sys
input = sys.stdin.readline
n = int(input())
lectures = sorted(tuple(map(int, input().split())) for _ in range(n))
heap = []
ans = 0
for _, start, end in lectures:
    while heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    ans = max(ans, len(heap))
print(ans)
`],
  ["1411", "brute_force-1411", "brute_force", "Similar Words", `import sys
input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]
def pattern(w):
    m = {}
    nxt = 0
    out = []
    for ch in w:
        if ch not in m:
            m[ch] = nxt
            nxt += 1
        out.append(m[ch])
    return tuple(out)
patterns = [pattern(w) for w in words]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += patterns[i] == patterns[j]
print(ans)
`],
  ["1421", "brute_force-1421", "brute_force", "Cutting Logs", `import sys
input = sys.stdin.readline
n, c, w = map(int, input().split())
logs = [int(input()) for _ in range(n)]
ans = 0
for length in range(1, max(logs) + 1):
    profit = 0
    for log in logs:
        pieces = log // length
        if pieces == 0:
            continue
        cuts = pieces - 1 if log % length == 0 else pieces
        gain = pieces * length * w - cuts * c
        if gain > 0:
            profit += gain
    ans = max(ans, profit)
print(ans)
`],
  ["1474", "greedy-1474", "greedy", "Making Sentence", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]
spaces = m - sum(map(len, words))
gaps = n - 1
base, extra = divmod(spaces, gaps)
parts = [words[0]]
for i in range(1, n):
    add = base
    if words[i][0].islower() and extra > 0:
        add += 1
        extra -= 1
    parts.append('_' * add)
    parts.append(words[i])
for i in range(len(parts) - 2, 0, -2):
    if extra > 0:
        parts[i] += '_'
        extra -= 1
print(''.join(parts))
`],
  ["1484", "two_pointer-1484", "two_pointer", "Diet", `import sys
g = int(sys.stdin.readline())
left, right = 1, 2
out = []
while left < right and right <= 100000:
    diff = right * right - left * left
    if diff == g:
        out.append(str(right))
        left += 1
        right += 1
    elif diff < g:
        right += 1
    else:
        left += 1
print('\\n'.join(out) if out else -1)
`],
  ["1487", "brute_force-1487", "brute_force", "Product", `import sys
input = sys.stdin.readline
n = int(input())
buyers = [tuple(map(int, input().split())) for _ in range(n)]
best_price = 0
best_profit = 0
for price, _ in buyers:
    profit = sum(price - cost for want, cost in buyers if want >= price and price > cost)
    if profit > best_profit or (profit == best_profit and profit and price < best_price):
        best_profit = profit
        best_price = price
print(best_price if best_profit > 0 else 0)
`],
  ["1503", "brute_force-1503", "brute_force", "Three Numbers", `import sys
n, s = map(int, sys.stdin.readline().split())
bad = set(map(int, sys.stdin.readline().split())) if s else set()
good = [x for x in range(1, 1002) if x not in bad]
good_set = set(good)
ans = 10 ** 18
for a in good:
    for b in good:
        target = n // (a * b)
        for c in range(max(1, target - 2), min(1001, target + 2) + 1):
            if c not in good_set:
                continue
            ans = min(ans, abs(n - a * b * c))
print(ans)
`],
  ["1527", "brute_force-1527", "brute_force", "Lucky Numbers", `import sys
a, b = map(int, sys.stdin.readline().split())
ans = 0
def dfs(x):
    global ans
    if x > b:
        return
    if x >= a:
        ans += 1
    dfs(x * 10 + 4)
    dfs(x * 10 + 7)
dfs(0)
print(ans)
`],
  ["1543", "brute_force-1543", "brute_force", "Document Search", `import sys
doc = sys.stdin.readline().rstrip('\\n')
word = sys.stdin.readline().rstrip('\\n')
i = ans = 0
while i <= len(doc) - len(word):
    if doc[i:i + len(word)] == word:
        ans += 1
        i += len(word)
    else:
        i += 1
print(ans)
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
  console.log(`[import-manual-batch-12] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-12] wrote ${OUT}`);
