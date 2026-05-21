import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["10427", "prefix_sum-10427", "prefix_sum", "Debt", `import sys
input = sys.stdin.readline
t = int(input())
answers = []
for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    arr = sorted(data[1:])
    prefix = [0]
    for value in arr:
        prefix.append(prefix[-1] + value)
    total = 0
    for size in range(1, n + 1):
        best = 10 ** 30
        for end in range(size, n + 1):
            cost = arr[end - 1] * size - (prefix[end] - prefix[end - size])
            best = min(best, cost)
        total += best
    answers.append(str(total))
print('\\n'.join(answers))
`],
  ["18866", "prefix_sum-18866", "prefix_sum", "Young Days", `import sys
input = sys.stdin.readline
n = int(input())
happy = [0] * n
tired = [0] * n
for i in range(n):
    happy[i], tired[i] = map(int, input().split())
inf = 10 ** 30
pref_min_h = [inf] * n
pref_max_t = [-inf] * n
cur_h = inf
cur_t = -inf
for i in range(n):
    if happy[i]:
        cur_h = min(cur_h, happy[i])
    if tired[i]:
        cur_t = max(cur_t, tired[i])
    pref_min_h[i] = cur_h
    pref_max_t[i] = cur_t
suf_max_h = [-inf] * n
suf_min_t = [inf] * n
cur_h = -inf
cur_t = inf
for i in range(n - 1, -1, -1):
    if happy[i]:
        cur_h = max(cur_h, happy[i])
    if tired[i]:
        cur_t = min(cur_t, tired[i])
    suf_max_h[i] = cur_h
    suf_min_t[i] = cur_t
answer = -1
for k in range(1, n):
    if pref_min_h[k - 1] > suf_max_h[k] and pref_max_t[k - 1] < suf_min_t[k]:
        answer = k
print(answer)
`],
  ["19566", "prefix_sum-19566", "prefix_sum", "Range Average", `import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
counter = defaultdict(int)
counter[0] = 1
prefix = 0
answer = 0
for idx, value in enumerate(arr, 1):
    prefix += value
    key = prefix - idx * k
    answer += counter[key]
    counter[key] += 1
print(answer)
`],
  ["22859", "implementation-22859", "implementation", "HTML Parsing", `import re, sys
source = sys.stdin.readline().strip()
main = re.search(r'<main>(.*)</main>', source).group(1)
for title, body in re.findall(r'<div title="(.*?)">(.*?)</div>', main):
    print(f'title : {title}')
    for paragraph in re.findall(r'<p>(.*?)</p>', body):
        text = re.sub(r'<.*?>', '', paragraph)
        text = re.sub(r'\\s+', ' ', text.strip())
        print(text)
`],
  ["22860", "implementation-22860", "implementation", "Folder Cleanup", `import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
children = defaultdict(list)
for _ in range(n + m):
    parent, child, is_folder = input().split()
    children[parent].append((child, is_folder == '1'))

def collect(folder):
    names = set()
    total = 0
    stack = [folder]
    while stack:
        cur = stack.pop()
        for name, is_folder in children[cur]:
            if is_folder:
                stack.append(name)
            else:
                names.add(name)
                total += 1
    return len(names), total

q = int(input())
out = []
for _ in range(q):
    folder = input().strip().split('/')[-1]
    out.append('%d %d' % collect(folder))
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
  console.log(`[import-manual-batch-09] imported ${slug} (${title})`);
}

const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-09] wrote ${OUT}`);
