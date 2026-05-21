import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["1080", "greedy-1080", "greedy", "Matrix", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            ans += 1
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    a[r][c] ^= 1
print(ans if a == b else -1)
`],
  ["1343", "greedy-1343", "greedy", "Polyomino", `import sys
s = sys.stdin.readline().strip()
parts = s.split('.')
out = []
possible = True
for part in parts:
    if len(part) % 2:
        possible = False
        break
    out.append('AAAA' * (len(part) // 4) + 'BB' * ((len(part) % 4) // 2))
print(-1 if not possible else '.'.join(out))
`],
  ["1439", "greedy-1439", "greedy", "Flip", `import sys
s = sys.stdin.readline().strip()
groups = {'0': 0, '1': 0}
prev = ''
for ch in s:
    if ch != prev:
        groups[ch] += 1
        prev = ch
print(min(groups.values()))
`],
  ["1449", "greedy-1449", "greedy", "Repairman Hang Seung", `import sys
input = sys.stdin.readline
n, l = map(int, input().split())
leaks = sorted(map(int, input().split()))
ans = 0
covered = -1
for leak in leaks:
    if leak > covered:
        ans += 1
        covered = leak + l - 1
print(ans)
`],
  ["1455", "greedy-1455", "greedy", "Switching Bulbs", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
ans = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if board[i][j]:
            ans += 1
            for r in range(i + 1):
                for c in range(j + 1):
                    board[r][c] ^= 1
print(ans)
`],
  ["1715", "greedy-1715", "greedy", "Card Sorting", `import heapq, sys
input = sys.stdin.readline
n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
ans = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a + b
    heapq.heappush(heap, a + b)
print(ans)
`],
  ["1744", "greedy-1744", "greedy", "Number Grouping", `import sys
input = sys.stdin.readline
n = int(input())
positives = []
negatives = []
ones = 0
zero = 0
for _ in range(n):
    x = int(input())
    if x > 1:
        positives.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zero += 1
    else:
        negatives.append(x)
positives.sort(reverse=True)
negatives.sort()
ans = ones
for i in range(0, len(positives) - 1, 2):
    ans += positives[i] * positives[i + 1]
if len(positives) % 2:
    ans += positives[-1]
for i in range(0, len(negatives) - 1, 2):
    ans += negatives[i] * negatives[i + 1]
if len(negatives) % 2 and zero == 0:
    ans += negatives[-1]
print(ans)
`],
  ["1946", "greedy-1946", "greedy", "New Recruits", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    people = sorted(tuple(map(int, input().split())) for _ in range(n))
    best = 10 ** 9
    count = 0
    for _, interview in people:
        if interview < best:
            best = interview
            count += 1
    out.append(str(count))
print('\\n'.join(out))
`],
  ["2138", "greedy-2138", "greedy", "Bulbs and Switches", `import sys
n = int(sys.stdin.readline())
start = list(map(int, sys.stdin.readline().strip()))
target = list(map(int, sys.stdin.readline().strip()))

def solve(first):
    arr = start[:]
    count = 0
    if first:
        count += 1
        for i in range(min(2, n)):
            arr[i] ^= 1
    for i in range(1, n):
        if arr[i - 1] != target[i - 1]:
            count += 1
            for j in (i - 1, i, i + 1):
                if 0 <= j < n:
                    arr[j] ^= 1
    return count if arr == target else 10 ** 9

ans = min(solve(False), solve(True))
print(ans if ans != 10 ** 9 else -1)
`],
  ["2847", "greedy-2847", "greedy", "Game Making", `import sys
input = sys.stdin.readline
n = int(input())
scores = [int(input()) for _ in range(n)]
ans = 0
for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        target = scores[i + 1] - 1
        ans += scores[i] - target
        scores[i] = target
print(ans)
`],
  ["6068", "greedy-6068", "greedy", "Time Management", `import sys
input = sys.stdin.readline
n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort(key=lambda x: x[1], reverse=True)
time = 10 ** 9
for duration, deadline in jobs:
    time = min(time, deadline) - duration
print(time if time >= 0 else -1)
`],
  ["11047", "greedy-11047", "greedy", "Coin 0", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0
for coin in reversed(coins):
    ans += k // coin
    k %= coin
print(ans)
`],
  ["11509", "greedy-11509", "greedy", "Balloon Archer", `import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
arrows = {}
ans = 0
for h in heights:
    if arrows.get(h, 0):
        arrows[h] -= 1
        arrows[h - 1] = arrows.get(h - 1, 0) + 1
    else:
        ans += 1
        arrows[h - 1] = arrows.get(h - 1, 0) + 1
print(ans)
`],
  ["12782", "greedy-12782", "greedy", "Secret Email", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    a, b = input().split()
    zero_to_one = one_to_zero = 0
    for x, y in zip(a, b):
        if x == '0' and y == '1':
            zero_to_one += 1
        elif x == '1' and y == '0':
            one_to_zero += 1
    out.append(str(max(zero_to_one, one_to_zero)))
print('\\n'.join(out))
`],
  ["13413", "greedy-13413", "greedy", "Othello Rebuild", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    bw = wb = 0
    for x, y in zip(a, b):
        if x == 'B' and y == 'W':
            bw += 1
        elif x == 'W' and y == 'B':
            wb += 1
    out.append(str(max(bw, wb)))
print('\\n'.join(out))
`],
  ["14400", "greedy-14400", "greedy", "Convenience Store 2", `import sys
input = sys.stdin.readline
n = int(input())
xs, ys = [], []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()
mx = xs[n // 2]
my = ys[n // 2]
print(sum(abs(x - mx) for x in xs) + sum(abs(y - my) for y in ys))
`],
  ["16162", "greedy-16162", "greedy", "Singing Contest", `import sys
input = sys.stdin.readline
n, a, d = map(int, input().split())
notes = list(map(int, input().split()))
want = a
ans = 0
for note in notes:
    if note == want:
        ans += 1
        want += d
print(ans)
`],
  ["16206", "greedy-16206", "greedy", "Roll Cake", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort(key=lambda x: (x % 10 != 0, x))
ans = 0
for cake in cakes:
    while cake > 10 and m > 0:
        cake -= 10
        m -= 1
        ans += 1
    if cake == 10:
        ans += 1
print(ans)
`],
  ["17615", "greedy-17615", "greedy", "Ball Gathering", `import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
ans = n
for color in 'RB':
    total = s.count(color)
    left = 0
    while left < n and s[left] == color:
        left += 1
    right = 0
    while right < n and s[n - 1 - right] == color:
        right += 1
    ans = min(ans, total - left, total - right)
print(ans)
`],
  ["19939", "greedy-19939", "greedy", "Distributing Balls", `import sys
n, k = map(int, sys.stdin.readline().split())
minimum = k * (k + 1) // 2
if n < minimum:
    print(-1)
else:
    remain = n - minimum
    print(k - 1 + (1 if remain % k else 0))
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
  console.log(`[import-manual-batch-11] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-11] wrote ${OUT}`);
