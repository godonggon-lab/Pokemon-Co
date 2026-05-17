import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const OUT = path.join(DATA_DIR, "problems-extra.json");

const MANUAL_PROBLEMS = [
  {
    id: "1159",
    slug: "string-1159",
    categorySlug: "string",
    title: "농구 경기",
    code: `import sys
from collections import Counter

n = int(sys.stdin.readline())
counter = Counter(sys.stdin.readline().strip()[0] for _ in range(n))
answer = ''.join(ch for ch in sorted(counter) if counter[ch] >= 5)
print(answer if answer else 'PREDAJA')
`
  },
  {
    id: "1259",
    slug: "string-1259",
    categorySlug: "string",
    title: "팰린드롬수",
    code: `import sys

out = []
for line in sys.stdin:
    s = line.strip()
    if s == '0':
        break
    out.append('yes' if s == s[::-1] else 'no')
print('\\n'.join(out))
`
  },
  {
    id: "10808",
    slug: "string-10808",
    categorySlug: "string",
    title: "알파벳 개수",
    code: `import sys

s = sys.stdin.readline().strip()
counts = [0] * 26
for ch in s:
    counts[ord(ch) - 97] += 1
print(*counts)
`
  },
  {
    id: "10809",
    slug: "string-10809",
    categorySlug: "string",
    title: "알파벳 찾기",
    code: `import sys

s = sys.stdin.readline().strip()
print(*[s.find(chr(97 + i)) for i in range(26)])
`
  },
  {
    id: "10988",
    slug: "string-10988",
    categorySlug: "string",
    title: "팰린드롬인지 확인하기",
    code: `import sys

s = sys.stdin.readline().strip()
print(1 if s == s[::-1] else 0)
`
  },
  {
    id: "1213",
    slug: "string-1213",
    categorySlug: "string",
    title: "Palindrome Maker",
    code: `import sys
from collections import Counter

s = sys.stdin.readline().strip()
counter = Counter(s)
odd = [ch for ch in sorted(counter) if counter[ch] % 2 == 1]
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    left = ''.join(ch * (counter[ch] // 2) for ch in sorted(counter))
    mid = odd[0] if odd else ''
    print(left + mid + left[::-1])
`
  },
  {
    id: "1718",
    slug: "string-1718",
    categorySlug: "string",
    title: "Cipher",
    code: `import sys

plain = sys.stdin.readline().rstrip('\\n')
key = sys.stdin.readline().strip()
out = []
for i, ch in enumerate(plain):
    if ch == ' ':
        out.append(' ')
    else:
        shift = ord(key[i % len(key)]) - ord('a') + 1
        out.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
print(''.join(out))
`
  },
  {
    id: "2941",
    slug: "string-2941",
    categorySlug: "string",
    title: "Croatia Alphabet",
    code: `import sys

s = sys.stdin.readline().strip()
for token in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(token, '*')
print(len(s))
`
  },
  {
    id: "11655",
    slug: "string-11655",
    categorySlug: "string",
    title: "ROT13",
    code: `import sys

s = sys.stdin.readline().rstrip('\\n')
out = []
for ch in s:
    if 'a' <= ch <= 'z':
        out.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
    elif 'A' <= ch <= 'Z':
        out.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
    else:
        out.append(ch)
print(''.join(out))
`
  },
  {
    id: "11656",
    slug: "string-11656",
    categorySlug: "string",
    title: "Suffix Array",
    code: `import sys

s = sys.stdin.readline().strip()
print('\\n'.join(sorted(s[i:] for i in range(len(s)))))
`
  },
  {
    id: "9933",
    slug: "string-9933",
    categorySlug: "string",
    title: "Password",
    code: `import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]
seen = set(words)
for word in words:
    if word[::-1] in seen:
        print(len(word), word[len(word) // 2])
        break
`
  },
  {
    id: "11478",
    slug: "string-11478",
    categorySlug: "string",
    title: "Distinct Substrings",
    code: `import sys

s = sys.stdin.readline().strip()
answer = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        answer.add(s[i:j])
print(len(answer))
`
  },
  {
    id: "14405",
    slug: "string-14405",
    categorySlug: "string",
    title: "Pikachu",
    code: `import sys

s = sys.stdin.readline().strip()
i = 0
ok = True
while i < len(s):
    if s.startswith('pi', i):
        i += 2
    elif s.startswith('ka', i):
        i += 2
    elif s.startswith('chu', i):
        i += 3
    else:
        ok = False
        break
print('YES' if ok else 'NO')
`
  },
  {
    id: "15927",
    slug: "string-15927",
    categorySlug: "string",
    title: "Palindrome Not Palindrome",
    code: `import sys

s = sys.stdin.readline().strip()
if s != s[::-1]:
    print(len(s))
elif len(set(s)) == 1:
    print(-1)
else:
    print(len(s) - 1)
`
  },
  {
    id: "16916",
    slug: "string-16916",
    categorySlug: "string",
    title: "Substring",
    code: `import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
print(1 if p in s else 0)
`
  },
  {
    id: "1622",
    slug: "string-1622",
    categorySlug: "string",
    title: "Common Permutation",
    code: `import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
out = []
for i in range(0, len(lines), 2):
    if i + 1 >= len(lines):
        break
    a = Counter(lines[i])
    b = Counter(lines[i + 1])
    chars = []
    for ch in sorted(set(a) & set(b)):
        chars.append(ch * min(a[ch], b[ch]))
    out.append(''.join(chars))
print('\\n'.join(out))
`
  },
  {
    id: "1972",
    slug: "string-1972",
    categorySlug: "string",
    title: "Surprising Strings",
    code: `import sys

out = []
for line in sys.stdin:
    s = line.strip()
    if s == '*':
        break
    ok = True
    for d in range(1, len(s)):
        seen = set()
        for i in range(len(s) - d):
            pair = s[i] + s[i + d]
            if pair in seen:
                ok = False
                break
            seen.add(pair)
        if not ok:
            break
    out.append(f"{s} is {'surprising' if ok else 'NOT surprising'}.")
print('\\n'.join(out))
`
  },
  {
    id: "2671",
    slug: "string-2671",
    categorySlug: "string",
    title: "Submarine",
    code: `import re
import sys

s = sys.stdin.readline().strip()
print('SUBMARINE' if re.fullmatch(r'(100+1+|01)+', s) else 'NOISE')
`
  },
  {
    id: "2852",
    slug: "string-2852",
    categorySlug: "string",
    title: "NBA Basketball",
    code: `import sys

def to_sec(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s

def fmt(sec):
    return f"{sec // 60:02d}:{sec % 60:02d}"

n = int(sys.stdin.readline())
score = [0, 0]
lead_time = [0, 0]
last = 0
for _ in range(n):
    team, t = sys.stdin.readline().split()
    now = to_sec(t)
    if score[0] > score[1]:
        lead_time[0] += now - last
    elif score[1] > score[0]:
        lead_time[1] += now - last
    score[int(team) - 1] += 1
    last = now
if score[0] > score[1]:
    lead_time[0] += 48 * 60 - last
elif score[1] > score[0]:
    lead_time[1] += 48 * 60 - last
print(fmt(lead_time[0]))
print(fmt(lead_time[1]))
`
  },
  {
    id: "3613",
    slug: "string-3613",
    categorySlug: "string",
    title: "Java vs C++",
    code: `import sys

s = sys.stdin.readline().strip()

def error():
    print('Error!')
    raise SystemExit

if not s or s[0] == '_' or s[-1] == '_' or s[0].isupper() or '__' in s:
    error()

has_under = '_' in s
has_upper = any(ch.isupper() for ch in s)

if has_under and has_upper:
    error()

if has_under:
    parts = s.split('_')
    if any(not part or not part.islower() for part in parts):
        error()
    print(parts[0] + ''.join(part.capitalize() for part in parts[1:]))
else:
    out = []
    for ch in s:
        if ch.isupper():
            out.append('_')
            out.append(ch.lower())
        else:
            out.append(ch)
    print(''.join(out))
`
  },
  {
    id: "5534",
    slug: "string-5534",
    categorySlug: "string",
    title: "Signboard",
    code: `import sys

n = int(sys.stdin.readline())
target = sys.stdin.readline().strip()
answer = 0
for _ in range(n):
    board = sys.stdin.readline().strip()
    ok = False
    for start in range(len(board)):
        for step in range(1, len(board) + 1):
            end = start + step * (len(target) - 1)
            if end >= len(board):
                break
            if ''.join(board[start + step * i] for i in range(len(target))) == target:
                ok = True
                break
        if ok:
            break
    answer += int(ok)
print(answer)
`
  },
  {
    id: "6996",
    slug: "string-6996",
    categorySlug: "string",
    title: "Anagrams",
    code: `import sys
from collections import Counter

t = int(sys.stdin.readline())
out = []
for _ in range(t):
    a, b = sys.stdin.readline().split()
    if Counter(a) == Counter(b):
        out.append(f"{a} & {b} are anagrams.")
    else:
        out.append(f"{a} & {b} are NOT anagrams.")
print('\\n'.join(out))
`
  },
  {
    id: "9536",
    slug: "string-9536",
    categorySlug: "string",
    title: "What Does the Fox Say",
    code: `import sys

t = int(sys.stdin.readline())
answers = []
for _ in range(t):
    recorded = sys.stdin.readline().split()
    known = set()
    while True:
        line = sys.stdin.readline().strip()
        if line == 'what does the fox say?':
            break
        known.add(line.split()[-1])
    answers.append(' '.join(sound for sound in recorded if sound not in known))
print('\\n'.join(answers))
`
  },
  {
    id: "13022",
    slug: "string-13022",
    categorySlug: "string",
    title: "Wolf Word",
    code: `import sys

s = sys.stdin.readline().strip()
i = 0
ok = True
while i < len(s):
    cnt = 0
    while i < len(s) and s[i] == 'w':
        cnt += 1
        i += 1
    if cnt == 0:
        ok = False
        break
    for ch in 'olf':
        now = 0
        while i < len(s) and s[i] == ch:
            now += 1
            i += 1
        if now != cnt:
            ok = False
            break
    if not ok:
        break
print(1 if ok and i == len(s) else 0)
`
  },
  {
    id: "20944",
    slug: "string-20944",
    categorySlug: "string",
    title: "Palindrome Wall",
    code: `import sys

n = int(sys.stdin.readline())
print('a' * n)
`
  },
  {
    id: "1188",
    slug: "math-1188",
    categorySlug: "math",
    title: "Food Critics",
    code: `import math
import sys

n, m = map(int, sys.stdin.readline().split())
print(m - math.gcd(n, m))
`
  },
  {
    id: "1456",
    slug: "math-1456",
    categorySlug: "math",
    title: "Almost Prime",
    code: `import math
import sys

a, b = map(int, sys.stdin.readline().split())
limit = int(math.isqrt(b))
is_prime = [True] * (limit + 1)
if limit >= 0:
    is_prime[0:2] = [False, False]
for i in range(2, int(math.isqrt(limit)) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False
answer = 0
for p in range(2, limit + 1):
    if not is_prime[p]:
        continue
    value = p * p
    while value <= b:
        if value >= a:
            answer += 1
        if value > b // p:
            break
        value *= p
print(answer)
`
  },
  {
    id: "1669",
    slug: "math-1669",
    categorySlug: "math",
    title: "Monkey",
    code: `import math
import sys

x, y = map(int, sys.stdin.readline().split())
d = y - x
if d == 0:
    print(0)
else:
    k = math.isqrt(d)
    if k * k == d:
        print(2 * k - 1)
    elif d <= k * k + k:
        print(2 * k)
    else:
        print(2 * k + 1)
`
  },
  {
    id: "2168",
    slug: "math-2168",
    categorySlug: "math",
    title: "Tile Diagonal",
    code: `import math
import sys

x, y = map(int, sys.stdin.readline().split())
print(x + y - math.gcd(x, y))
`
  },
  {
    id: "2436",
    slug: "math-2436",
    categorySlug: "math",
    title: "Common Divisor",
    code: `import math
import sys

g, l = map(int, sys.stdin.readline().split())
target = l // g
best = (g, l)
for a in range(1, math.isqrt(target) + 1):
    if target % a == 0:
        b = target // a
        if math.gcd(a, b) == 1:
            best = (g * a, g * b)
print(*best)
`
  }
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

async function main() {
  const existingExtra = await readJson(OUT, []);
  const bySlug = new Map(existingExtra.map((problem) => [problem.slug, problem]));

  for (const item of MANUAL_PROBLEMS) {
    bySlug.set(item.slug, {
      id: item.id,
      slug: item.slug,
      categorySlug: item.categorySlug,
      sources: [
        {
          lang: "python",
          file: `local/oracle/${item.slug}.py`,
          code: item.code
        }
      ],
      link: `https://www.acmicpc.net/problem/${item.id}`,
      authors: ["dongjun"],
      hash: stableHash(`extra:${item.slug}`),
      createdAt: Date.now()
    });
    console.log(`[import-manual-strings] imported ${item.slug} (${item.title})`);
  }

  const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
  await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
  console.log(`[import-manual-strings] wrote ${OUT}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
