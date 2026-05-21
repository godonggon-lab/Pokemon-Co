import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["4446", "string-4446", "string", "ROT13", `import sys
vowels = 'aiyeou'
consonants = 'bkxznhdcwgpvjqtsrlmf'
out = []
for line in sys.stdin.read().splitlines():
    chars = []
    for ch in line:
        lower = ch.lower()
        if lower in vowels:
            nxt = vowels[(vowels.index(lower) + 3) % len(vowels)]
            chars.append(nxt.upper() if ch.isupper() else nxt)
        elif lower in consonants:
            nxt = consonants[(consonants.index(lower) + 10) % len(consonants)]
            chars.append(nxt.upper() if ch.isupper() else nxt)
        else:
            chars.append(ch)
    out.append(''.join(chars))
print('\\n'.join(out))
`],
  ["9242", "string-9242", "string", "Bomb Defusal", `import sys
patterns = [
    ['***', '* *', '* *', '* *', '***'],
    ['  *', '  *', '  *', '  *', '  *'],
    ['***', '  *', '***', '*  ', '***'],
    ['***', '  *', '***', '  *', '***'],
    ['* *', '* *', '***', '  *', '  *'],
    ['***', '*  ', '***', '  *', '***'],
    ['***', '*  ', '***', '* *', '***'],
    ['***', '  *', '  *', '  *', '  *'],
    ['***', '* *', '***', '* *', '***'],
    ['***', '* *', '***', '  *', '***'],
]
rows = sys.stdin.read().splitlines()
try:
    count = (len(rows[0]) + 1) // 4
    digits = []
    for idx in range(count):
        block = [row[idx * 4:idx * 4 + 3] for row in rows[:5]]
        digits.append(patterns.index(block))
    value = int(''.join(map(str, digits)))
    print('BEER!!' if value % 6 == 0 else 'BOOM!!')
except Exception:
    print('BOOM!!')
`],
  ["19844", "string-19844", "string", "Word Count", `import sys
s = sys.stdin.readline().strip()
parts = s.replace(' ', '-').split('-')
prefixes = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
vowels = set('aeiouh')
answer = len(parts)
for part in parts:
    for prefix in prefixes:
        if part.startswith(prefix) and len(part) > len(prefix) and part[len(prefix)] in vowels:
            answer += 1
            break
print(answer)
`],
  ["19948", "string-19948", "string", "Poet Youngjae", `import sys
poem = sys.stdin.readline().rstrip('\\n')
space = int(sys.stdin.readline())
counts = list(map(int, sys.stdin.readline().split()))

def use_text(text):
    prev = ''
    for ch in text:
        if ch == ' ':
            continue
        lower = ch.lower()
        if lower == prev:
            continue
        idx = ord(lower) - 97
        counts[idx] -= 1
        if counts[idx] < 0:
            return False
        prev = lower
    return True

words = poem.split()
title = ''.join(word[0].upper() for word in words)
if poem.count(' ') > space or not use_text(poem) or not use_text(title):
    print(-1)
else:
    print(title)
`],
  ["20210", "string-20210", "string", "File Explorer", `import functools, sys
input = sys.stdin.readline
order = {ch: i for i, ch in enumerate('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')}

def tokens(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            result.append(('num', s[i:j]))
            i = j
        else:
            result.append(('chr', s[i]))
            i += 1
    return result

def cmp(a, b):
    ta, tb = tokens(a), tokens(b)
    for x, y in zip(ta, tb):
        if x[0] != y[0]:
            return -1 if x[0] == 'num' else 1
        if x[0] == 'chr':
            if x[1] != y[1]:
                return order[x[1]] - order[y[1]]
        else:
            ax = x[1].lstrip('0') or '0'
            by = y[1].lstrip('0') or '0'
            if len(ax) != len(by):
                return len(ax) - len(by)
            if ax != by:
                return -1 if ax < by else 1
            az = len(x[1]) - len(x[1].lstrip('0'))
            bz = len(y[1]) - len(y[1].lstrip('0'))
            if az != bz:
                return az - bz
    return len(ta) - len(tb)

n = int(input())
arr = [input().strip() for _ in range(n)]
print('\\n'.join(sorted(arr, key=functools.cmp_to_key(cmp))))
`],
  ["22858", "implementation-22858", "implementation", "Restore Original", `import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))
for _ in range(k):
    prev = [0] * n
    for i in range(n):
        prev[d[i] - 1] = s[i]
    s = prev
print(*s)
`],
  ["22943", "math-22943", "math", "Number", `import itertools, sys
k, m = map(int, sys.stdin.readline().split())
limit = 10 ** k
prime = [True] * limit
prime[0] = prime[1] = False
for i in range(2, int((limit - 1) ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit, i):
            prime[j] = False
primes = [i for i in range(2, limit) if prime[i]]
sum_ok = [False] * limit
for i, a in enumerate(primes):
    for b in primes[i + 1:]:
        value = a + b
        if value >= limit:
            break
        sum_ok[value] = True
mul_ok = [False] * limit
for i, a in enumerate(primes):
    if a * a >= limit:
        break
    for b in primes[i:]:
        value = a * b
        if value >= limit:
            break
        mul_ok[value] = True
answer = 0
for perm in itertools.permutations('0123456789', k):
    if perm[0] == '0':
        continue
    value = int(''.join(perm))
    reduced = value
    while reduced % m == 0:
        reduced //= m
    if sum_ok[value] and mul_ok[reduced]:
        answer += 1
print(answer)
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
  console.log(`[import-manual-batch-08] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-08] wrote ${OUT}`);
