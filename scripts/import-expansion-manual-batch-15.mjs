import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["2635", "brute_force-2635", "brute_force", "Number Continuing", `import sys
n = int(sys.stdin.readline())
best = []
for second in range(1, n + 1):
    seq = [n, second]
    while seq[-2] - seq[-1] >= 0:
        seq.append(seq[-2] - seq[-1])
    if len(seq) > len(best):
        best = seq
print(len(best))
print(' '.join(map(str, best)))
`],
  ["2688", "dynamic_programming_2-2688", "dynamic_programming_2", "Non-Decreasing Numbers", `import sys
input = sys.stdin.readline
dp = [[0] * 10 for _ in range(65)]
for d in range(10):
    dp[1][d] = 1
for length in range(2, 65):
    for d in range(10):
        dp[length][d] = sum(dp[length - 1][d:])
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    out.append(str(sum(dp[n])))
print('\\n'.join(out))
`],
  ["3040", "brute_force-3040", "brute_force", "Snow White", `from itertools import combinations
import sys
a = [int(sys.stdin.readline()) for _ in range(9)]
for comb in combinations(a, 7):
    if sum(comb) == 100:
        print('\\n'.join(map(str, comb)))
        break
`],
  ["3067", "dynamic_programming_2-3067", "dynamic_programming_2", "Coins", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for v in range(coin, target + 1):
            dp[v] += dp[v - coin]
    out.append(str(dp[target]))
print('\\n'.join(out))
`],
  ["4811", "dynamic_programming_2-4811", "dynamic_programming_2", "Pills", `import sys
dp = [[0] * 31 for _ in range(31)]
def solve(w, h):
    if w == 0:
        return 1
    if dp[w][h]:
        return dp[w][h]
    ans = solve(w - 1, h + 1)
    if h:
        ans += solve(w, h - 1)
    dp[w][h] = ans
    return ans
out = []
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    out.append(str(solve(n, 0)))
print('\\n'.join(out))
`],
  ["5052", "trie-5052", "trie", "Phone List", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    nums = sorted(input().strip() for _ in range(n))
    ok = True
    for a, b in zip(nums, nums[1:]):
        if b.startswith(a):
            ok = False
            break
    out.append("YES" if ok else "NO")
print('\\n'.join(out))
`],
  ["5212", "simulation-5212", "simulation", "Global Warming", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]
next_land = []
for i in range(r):
    row = []
    for j in range(c):
        if grid[i][j] == '.':
            row.append('.')
            continue
        sea = 0
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if not (0 <= ni < r and 0 <= nj < c) or grid[ni][nj] == '.':
                sea += 1
        row.append('.' if sea >= 3 else 'X')
    next_land.append(row)
cells = [(i, j) for i in range(r) for j in range(c) if next_land[i][j] == 'X']
if not cells:
    print()
else:
    r1, r2 = min(i for i, _ in cells), max(i for i, _ in cells)
    c1, c2 = min(j for _, j in cells), max(j for _, j in cells)
    print('\\n'.join(''.join(next_land[i][c1:c2 + 1]) for i in range(r1, r2 + 1)))
`],
  ["5671", "brute_force-5671", "brute_force", "Hotel Room", `import sys
out = []
for line in sys.stdin:
    if not line.strip():
        continue
    n, m = map(int, line.split())
    ans = 0
    for x in range(n, m + 1):
        s = str(x)
        ans += len(s) == len(set(s))
    out.append(str(ans))
print('\\n'.join(out))
`],
  ["5883", "brute_force-5883", "brute_force", "IPhone 9S", `import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
for remove in set(a):
    cur = best = 0
    prev = None
    for x in a:
        if x == remove:
            continue
        if x == prev:
            cur += 1
        else:
            prev = x
            cur = 1
        best = max(best, cur)
    ans = max(ans, best)
print(ans)
`],
  ["5904", "divide_and_conquer-5904", "divide_and_conquer", "Moo Game", `import sys
n = int(sys.stdin.readline())
length = 3
k = 0
while length < n:
    k += 1
    length = length * 2 + k + 3
while True:
    if k == 0:
        print("moo"[n - 1])
        break
    prev = (length - k - 3) // 2
    mid = k + 3
    if n <= prev:
        length = prev
        k -= 1
    elif n <= prev + mid:
        print('m' if n == prev + 1 else 'o')
        break
    else:
        n -= prev + mid
        length = prev
        k -= 1
`],
  ["6159", "two_pointer-6159", "two_pointer", "Costume Party", `import sys
input = sys.stdin.readline
n, s = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
l, r = 0, n - 1
ans = 0
while l < r:
    if a[l] + a[r] <= s:
        ans += r - l
        l += 1
    else:
        r -= 1
print(ans)
`],
  ["9372", "tree-9372", "tree", "Travel", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    out.append(str(n - 1))
print('\\n'.join(out))
`],
  ["9375", "data_structure2-9375", "data_structure2", "Fashion King", `from collections import Counter
import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    counter = Counter()
    for _ in range(n):
        _, kind = input().split()
        counter[kind] += 1
    ans = 1
    for count in counter.values():
        ans *= count + 1
    out.append(str(ans - 1))
print('\\n'.join(out))
`],
  ["9996", "brute_force-9996", "brute_force", "Korea", `import sys
input = sys.stdin.readline
n = int(input())
pattern = input().strip()
prefix, suffix = pattern.split('*')
out = []
for _ in range(n):
    s = input().strip()
    ok = len(s) >= len(prefix) + len(suffix) and s.startswith(prefix) and s.endswith(suffix)
    out.append("DA" if ok else "NE")
print('\\n'.join(out))
`],
  ["10211", "dynamic_programming_1-10211", "dynamic_programming_1", "Maximum Subarray", `import sys
input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cur = best = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    out.append(str(best))
print('\\n'.join(out))
`],
  ["10448", "brute_force-10448", "brute_force", "Eureka", `import sys
tri = [i * (i + 1) // 2 for i in range(1, 46)]
possible = set()
for a in tri:
    for b in tri:
        for c in tri:
            if a + b + c <= 1000:
                possible.add(a + b + c)
t = int(sys.stdin.readline())
print('\\n'.join('1' if int(sys.stdin.readline()) in possible else '0' for _ in range(t)))
`],
  ["10844", "dynamic_programming_1-10844", "dynamic_programming_1", "Easy Stair Numbers", `import sys
n = int(sys.stdin.readline())
mod = 1000000000
dp = [0,1,1,1,1,1,1,1,1,1]
for _ in range(2, n + 1):
    ndp = [0] * 10
    for d in range(10):
        if d > 0:
            ndp[d] += dp[d - 1]
        if d < 9:
            ndp[d] += dp[d + 1]
    dp = [x % mod for x in ndp]
print(sum(dp) % mod)
`],
  ["11051", "dynamic_programming_1-11051", "dynamic_programming_1", "Binomial Coefficient 2", `import sys
n, k = map(int, sys.stdin.readline().split())
mod = 10007
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
    for j in range(1, min(i, k) + 1):
        if j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
print(dp[n][k])
`],
  ["11052", "dynamic_programming_1-11052", "dynamic_programming_1", "Card Buying", `import sys
input = sys.stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - j] + p[j] for j in range(1, i + 1))
print(dp[n])
`],
  ["11057", "dynamic_programming_1-11057", "dynamic_programming_1", "Ascending Numbers", `import sys
n = int(sys.stdin.readline())
mod = 10007
dp = [1] * 10
for _ in range(2, n + 1):
    for i in range(1, 10):
        dp[i] = (dp[i] + dp[i - 1]) % mod
print(sum(dp) % mod)
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
  console.log(`[import-manual-batch-15] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-15] wrote ${OUT}`);
