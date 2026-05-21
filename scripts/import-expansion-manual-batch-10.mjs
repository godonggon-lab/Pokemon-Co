import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["2115", "string-2115", "string", "Gallery", `import sys
input = sys.stdin.readline
m, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(m)]
used = [[False] * n for _ in range(m)]
answer = 0
for r in range(m - 1):
    for c in range(n):
        if grid[r][c] == grid[r + 1][c] == 'X' and not used[r][c] and not used[r + 1][c]:
            if c + 1 < n and grid[r][c + 1] == grid[r + 1][c + 1] == '.':
                used[r][c] = used[r + 1][c] = True
                answer += 1
            elif c - 1 >= 0 and grid[r][c - 1] == grid[r + 1][c - 1] == '.':
                used[r][c] = used[r + 1][c] = True
                answer += 1
for r in range(m):
    for c in range(n - 1):
        if grid[r][c] == grid[r][c + 1] == 'X' and not used[r][c] and not used[r][c + 1]:
            if r + 1 < m and grid[r + 1][c] == grid[r + 1][c + 1] == '.':
                used[r][c] = used[r][c + 1] = True
                answer += 1
            elif r - 1 >= 0 and grid[r - 1][c] == grid[r - 1][c + 1] == '.':
                used[r][c] = used[r][c + 1] = True
                answer += 1
print(answer)
`],
  ["2900", "prefix_sum-2900", "prefix_sum", "Program", `import sys
from collections import Counter
input = sys.stdin.readline
n, k = map(int, input().split())
counter = Counter(map(int, input().split()))
arr = [0] * n
for jump, count in counter.items():
    for idx in range(0, n, jump):
        arr[idx] += count
prefix = [0]
for value in arr:
    prefix.append(prefix[-1] + value)
q = int(input())
out = []
for _ in range(q):
    l, r = map(int, input().split())
    out.append(str(prefix[r + 1] - prefix[l]))
print('\\n'.join(out))
`],
  ["3025", "simulation-3025", "simulation", "Throwing Stones", `import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
n = int(input())
for _ in range(n):
    col = int(input()) - 1
    row = 0
    while True:
        if row + 1 == r:
            board[row][col] = 'O'
            break
        if board[row + 1][col] == '.':
            row += 1
        elif board[row + 1][col] in 'XO':
            if col > 0 and board[row][col - 1] == '.' and board[row + 1][col - 1] == '.':
                row += 1
                col -= 1
            elif col + 1 < c and board[row][col + 1] == '.' and board[row + 1][col + 1] == '.':
                row += 1
                col += 1
            else:
                board[row][col] = 'O'
                break
print('\\n'.join(''.join(row) for row in board))
`],
  ["4836", "string-4836", "string", "Dance", `import sys

def check(line):
    steps = line.split()
    broken = [False] * 5
    dip_bad = [False] * len(steps)
    for i, step in enumerate(steps):
        if step == 'dip':
            ok = (i >= 1 and steps[i - 1] == 'jiggle') or (i >= 2 and steps[i - 2] == 'jiggle') or (i + 1 < len(steps) and steps[i + 1] == 'twirl')
            if not ok:
                broken[0] = True
                dip_bad[i] = True
    if len(steps) < 3 or steps[-3:] != ['clap', 'stomp', 'clap']:
        broken[1] = True
    if 'twirl' in steps and 'hop' not in steps:
        broken[2] = True
    if steps and steps[0] == 'jiggle':
        broken[3] = True
    if 'dip' not in steps:
        broken[4] = True
    fixed = [step.upper() if step == 'dip' and dip_bad[i] else step for i, step in enumerate(steps)]
    errors = [str(i + 1) for i, value in enumerate(broken) if value]
    if not errors:
        return 'form ok: ' + line
    if len(errors) == 1:
        prefix = 'form error ' + errors[0] + ': '
    else:
        prefix = 'form errors ' + ', '.join(errors[:-1]) + ' and ' + errors[-1] + ': '
    return prefix + ' '.join(fixed)

print('\\n'.join(check(line) for line in sys.stdin.read().splitlines()))
`],
  ["5875", "prefix_sum-5875", "prefix_sum", "Typo", `import sys
s = sys.stdin.readline().strip()

def valid(value):
    balance = 0
    for ch in value:
        balance += 1 if ch == '(' else -1
        if balance < 0:
            return False
    return balance == 0

answer = 0
for i, ch in enumerate(s):
    flipped = s[:i] + (')' if ch == '(' else '(') + s[i + 1:]
    if valid(flipped):
        answer += 1
print(answer)
`],
  ["16890", "string-16890", "string", "Start-up", `import sys
from collections import deque
a = sorted(sys.stdin.readline().strip())
b = sorted(sys.stdin.readline().strip(), reverse=True)
n = len(a)
left = 0
right = n - 1
answer = [''] * n
a = deque(a[: (n + 1) // 2])
b = deque(b[: n // 2])
for turn in range(n):
    if turn % 2 == 0:
        if b and a[0] >= b[0]:
            answer[right] = a.pop()
            right -= 1
        else:
            answer[left] = a.popleft()
            left += 1
    else:
        if a and b[0] <= a[0]:
            answer[right] = b.pop()
            right -= 1
        else:
            answer[left] = b.popleft()
            left += 1
print(''.join(answer))
`],
  ["21611", "implementation-21611", "implementation", "Blizzard", `import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
spells = [tuple(map(int, input().split())) for _ in range(m)]
center = n // 2
positions = []
r = c = center
for length in range(1, n):
    for dr, dc, cnt in [(0, -1, length), (1, 0, length), (0, 1, length + 1), (-1, 0, length + 1)]:
        for _ in range(cnt):
            r += dr
            c += dc
            if 0 <= r < n and 0 <= c < n:
                positions.append((r, c))
    if len(positions) >= n * n - 1:
        break
positions = positions[: n * n - 1]
dir_map = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
score = [0, 0, 0, 0]

def flatten():
    return [board[r][c] for r, c in positions if board[r][c] != 0]

def write(values):
    for idx, (r, c) in enumerate(positions):
        board[r][c] = values[idx] if idx < len(values) else 0

for d, s in spells:
    dr, dc = dir_map[d]
    for step in range(1, s + 1):
        rr, cc = center + dr * step, center + dc * step
        if 0 <= rr < n and 0 <= cc < n:
            board[rr][cc] = 0
    values = flatten()
    changed = True
    while changed:
        changed = False
        nxt = []
        i = 0
        while i < len(values):
            j = i
            while j < len(values) and values[j] == values[i]:
                j += 1
            if j - i >= 4:
                score[values[i]] += j - i
                changed = True
            else:
                nxt.extend(values[i:j])
            i = j
        values = nxt
    transformed = []
    i = 0
    while i < len(values) and len(transformed) < len(positions):
        j = i
        while j < len(values) and values[j] == values[i]:
            j += 1
        transformed.extend([j - i, values[i]])
        i = j
    write(transformed[: len(positions)])
print(score[1] + score[2] * 2 + score[3] * 3)
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
  console.log(`[import-manual-batch-10] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-10] wrote ${OUT}`);
