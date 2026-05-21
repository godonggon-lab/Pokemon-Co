import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["17142", "graph_traversal-17142", "graph_traversal", "Laboratory 3", `import itertools, sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
viruses = []
empty = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            viruses.append((i, j))
        elif board[i][j] == 0:
            empty += 1
if empty == 0:
    print(0)
    sys.exit()
answer = 10 ** 9
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for starts in itertools.combinations(viruses, m):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for r, c in starts:
        dist[r][c] = 0
        q.append((r, c))
    infected = 0
    last = 0
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                if board[nr][nc] == 0:
                    infected += 1
                    last = dist[nr][nc]
                q.append((nr, nc))
    if infected == empty:
        answer = min(answer, last)
print(-1 if answer == 10 ** 9 else answer)
`],
  ["17406", "implementation-17406", "implementation", "Array Rotation 4", `import itertools, sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
ops = [tuple(map(int, input().split())) for _ in range(k)]

def rotate(arr, op):
    r, c, s = op
    r -= 1
    c -= 1
    for layer in range(1, s + 1):
        top, left = r - layer, c - layer
        bottom, right = r + layer, c + layer
        prev = arr[top][left]
        for i in range(top + 1, bottom + 1):
            arr[i][left], prev = prev, arr[i][left]
        for j in range(left + 1, right + 1):
            arr[bottom][j], prev = prev, arr[bottom][j]
        for i in range(bottom - 1, top - 1, -1):
            arr[i][right], prev = prev, arr[i][right]
        for j in range(right - 1, left - 1, -1):
            arr[top][j], prev = prev, arr[top][j]

answer = 10 ** 9
for order in itertools.permutations(ops):
    arr = [row[:] for row in origin]
    for op in order:
        rotate(arr, op)
    answer = min(answer, min(sum(row) for row in arr))
print(answer)
`],
  ["17470", "implementation-17470", "implementation", "Array Rotation 5", `import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ops = list(map(int, input().split()))

def op1(a):
    return a[::-1]

def op2(a):
    return [row[::-1] for row in a]

def op3(a):
    return [list(row) for row in zip(*a[::-1])]

def op4(a):
    return [list(row) for row in zip(*a)][::-1]

def split(a):
    h, w = len(a) // 2, len(a[0]) // 2
    return [
        [row[:w] for row in a[:h]],
        [row[w:] for row in a[:h]],
        [row[:w] for row in a[h:]],
        [row[w:] for row in a[h:]],
    ]

def merge(parts):
    top = [parts[0][i] + parts[1][i] for i in range(len(parts[0]))]
    bottom = [parts[2][i] + parts[3][i] for i in range(len(parts[2]))]
    return top + bottom

def op5(a):
    p = split(a)
    return merge([p[2], p[0], p[3], p[1]])

def op6(a):
    p = split(a)
    return merge([p[1], p[3], p[0], p[2]])

funcs = {1: op1, 2: op2, 3: op3, 4: op4, 5: op5, 6: op6}
for op in ops:
    arr = funcs[op](arr)
print('\\n'.join(' '.join(map(str, row)) for row in arr))
`],
  ["20327", "implementation-20327", "implementation", "Array Rotation 6", `import sys
input = sys.stdin.readline
n, r = map(int, input().split())
size = 1 << n
arr = [list(map(int, input().split())) for _ in range(size)]

def rotate_clock(block):
    return [list(row) for row in zip(*block[::-1])]

def rotate_counter(block):
    return [list(row) for row in zip(*block)][::-1]

def apply_inside(a, level, op):
    b = 1 << level
    out = [row[:] for row in a]
    for sr in range(0, size, b):
        for sc in range(0, size, b):
            block = [row[sc:sc + b] for row in a[sr:sr + b]]
            if op == 1:
                block = block[::-1]
            elif op == 2:
                block = [row[::-1] for row in block]
            elif op == 3:
                block = rotate_clock(block)
            elif op == 4:
                block = rotate_counter(block)
            for i in range(b):
                out[sr + i][sc:sc + b] = block[i]
    return out

def apply_whole(a, level, op):
    b = 1 << level
    count = size // b
    blocks = [[None] * count for _ in range(count)]
    for i in range(count):
        for j in range(count):
            blocks[i][j] = [row[j * b:(j + 1) * b] for row in a[i * b:(i + 1) * b]]
    if op == 5:
        blocks = blocks[::-1]
    elif op == 6:
        blocks = [row[::-1] for row in blocks]
    elif op == 7:
        blocks = [list(row) for row in zip(*blocks[::-1])]
    elif op == 8:
        blocks = [list(row) for row in zip(*blocks)][::-1]
    out = [[0] * size for _ in range(size)]
    for i in range(count):
        for j in range(count):
            for x in range(b):
                out[i * b + x][j * b:(j + 1) * b] = blocks[i][j][x]
    return out

for _ in range(r):
    op, level = map(int, input().split())
    if op <= 4:
        arr = apply_inside(arr, level, op)
    else:
        arr = apply_whole(arr, level, op)
print('\\n'.join(' '.join(map(str, row)) for row in arr))
`],
  ["21277", "implementation-21277", "implementation", "Puzzle", `import sys
input = sys.stdin.readline
n1, m1 = map(int, input().split())
a = [input().strip() for _ in range(n1)]
n2, m2 = map(int, input().split())
b = [input().strip() for _ in range(n2)]

def cells(grid):
    return [(i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch == '1']

def rotate(grid):
    return [''.join(row) for row in zip(*grid[::-1])]

answer = 10 ** 9
base = cells(a)
for _ in range(4):
    other = cells(b)
    for dr in range(-len(b), len(a) + 1):
        for dc in range(-len(b[0]), len(a[0]) + 1):
            moved = [(r + dr, c + dc) for r, c in other]
            if set(base) & set(moved):
                continue
            all_cells = base + moved
            min_r = min(r for r, _ in all_cells)
            max_r = max(r for r, _ in all_cells)
            min_c = min(c for _, c in all_cells)
            max_c = max(c for _, c in all_cells)
            answer = min(answer, (max_r - min_r + 1) * (max_c - min_c + 1))
    b = rotate(b)
print(answer)
`],
  ["21944", "data_structure2-21944", "data_structure2", "Problem Recommendation System Version 2", `import bisect, sys
input = sys.stdin.readline
n = int(input())
problems = {}
by_group = {}
all_items = []

def add_item(p, l, g):
    problems[p] = (l, g)
    item = (l, p)
    by_group.setdefault(g, [])
    bisect.insort(by_group[g], item)
    bisect.insort(all_items, item)

def remove_item(p):
    l, g = problems.pop(p)
    item = (l, p)
    by_group[g].pop(bisect.bisect_left(by_group[g], item))
    all_items.pop(bisect.bisect_left(all_items, item))

for _ in range(n):
    p, l, g = map(int, input().split())
    add_item(p, l, g)
m = int(input())
out = []
for _ in range(m):
    parts = input().split()
    cmd = parts[0]
    if cmd == 'add':
        add_item(int(parts[1]), int(parts[2]), int(parts[3]))
    elif cmd == 'solved':
        remove_item(int(parts[1]))
    elif cmd == 'recommend':
        g, x = int(parts[1]), int(parts[2])
        out.append(str(by_group[g][-1][1] if x == 1 else by_group[g][0][1]))
    elif cmd == 'recommend2':
        x = int(parts[1])
        out.append(str(all_items[-1][1] if x == 1 else all_items[0][1]))
    else:
        x, l = int(parts[1]), int(parts[2])
        if x == 1:
            idx = bisect.bisect_left(all_items, (l, -1))
            out.append(str(all_items[idx][1] if idx < len(all_items) else -1))
        else:
            idx = bisect.bisect_left(all_items, (l, -1)) - 1
            out.append(str(all_items[idx][1] if idx >= 0 else -1))
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
  console.log(`[import-manual-batch-07] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-07] wrote ${OUT}`);
