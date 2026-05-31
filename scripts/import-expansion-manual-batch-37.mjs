import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  [
    "13707",
    "dynamic_programming_2-13707",
    "dynamic_programming_2",
    "Sum Decomposition 2",
    `import sys
MOD=1000000000
n,k=map(int,sys.stdin.readline().split())
dp=[0]*(n+1)
dp[0]=1
for _ in range(k):
    nd=[0]*(n+1)
    s=0
    for i in range(n+1):
        s=(s+dp[i])%MOD
        nd[i]=s
    dp=nd
print(dp[n])
`,
  ],
  [
    "20495",
    "binary_search-20495",
    "binary_search",
    "Sequence and Hunting",
    `import bisect,sys
input=sys.stdin.readline
n=int(input())
data=[tuple(map(int,input().split())) for _ in range(n)]
lo=sorted(x-d for x,d in data)
hi=sorted(x+d for x,d in data)
out=[]
for x,d in data:
    best=n-bisect.bisect_right(lo,x+d)+1
    worst=n-bisect.bisect_left(hi,x-d)
    out.append(f"{best} {worst}")
print("\\n".join(out))
`,
  ],
  [
    "22946",
    "graph_traversal-22946",
    "graph_traversal",
    "Moving on Circles 1",
    `from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
circles=[None]+[tuple(map(int,input().split())) for _ in range(n)]
parent=[0]*(n+1)
for i in range(1,n+1):
    xi,yi,ri=circles[i]
    best=0
    best_r=10**30
    for j in range(1,n+1):
        if i==j: continue
        xj,yj,rj=circles[j]
        if rj<=ri: continue
        if (xi-xj)**2+(yi-yj)**2 < (rj-ri)**2 and rj<best_r:
            best=j
            best_r=rj
    parent[i]=best
g=[[] for _ in range(n+1)]
for i in range(1,n+1):
    g[i].append(parent[i])
    g[parent[i]].append(i)
def far(src):
    dist=[-1]*(n+1)
    dist[src]=0
    q=deque([src])
    while q:
        x=q.popleft()
        for y in g[x]:
            if dist[y]==-1:
                dist[y]=dist[x]+1
                q.append(y)
    node=max(range(1,n+1), key=lambda v: dist[v])
    return node,dist[node]
if n==0:
    print(0)
else:
    a,_=far(1)
    _,ans=far(a)
    print(ans)
`,
  ],
  [
    "22948",
    "graph_traversal-22948",
    "graph_traversal",
    "Moving on Circles 2",
    `from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
items=[]
for _ in range(n):
    idx,x,r=map(int,input().split())
    items.append((idx,x-r,x+r))
a,b=map(int,input().split())
ids=[idx for idx,_,_ in items]
by_id={idx:(l,r) for idx,l,r in items}
parent={idx:0 for idx in ids}
for i,l,r in items:
    best=0
    best_len=10**30
    for j,lj,rj in items:
        if i==j: continue
        if lj<l and r<rj and rj-lj<best_len:
            best=j
            best_len=rj-lj
    parent[i]=best
g={0:[]}
for idx in ids:
    g.setdefault(idx,[])
for idx,p in parent.items():
    g[idx].append(p)
    g.setdefault(p,[]).append(idx)
prev={a:None}
q=deque([a])
while q:
    x=q.popleft()
    if x==b: break
    for y in g[x]:
        if y not in prev:
            prev[y]=x
            q.append(y)
path=[]
cur=b
while cur is not None:
    if cur!=0:
        path.append(cur)
    cur=prev[cur]
path.reverse()
print(len(path))
print(*path)
`,
  ],
  [
    "22949",
    "graph_traversal-22949",
    "graph_traversal",
    "Rotating Maze Search",
    `from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
size=4*n
arr=[[['' for _ in range(size)] for _ in range(size)] for _ in range(4)]
start=None
def rot_pos(r,c):
    br=r//4*4
    bc=c//4*4
    rr=r%4
    cc=c%4
    return br+cc,bc+3-rr
for r in range(size):
    row=input().strip()
    for c in range(size):
        ch=row[c]
        arr[0][r][c]=ch
        if ch=='S':
            start=(r,c,0,0)
        tr,tc=r,c
        for d in range(1,4):
            tr,tc=rot_pos(tr,tc)
            arr[d][tr][tc]=ch
def div(r,c):
    if r<0 or c<0 or r>=size or c>=size:
        return -1
    return r//4*4+c//4
dr=[0,1,-1,0,0]
dc=[0,0,0,1,-1]
q=deque([start])
seen={(0,start[0],start[1])}
while q:
    r,c,d,dist=q.popleft()
    if arr[d][r][c]=='E':
        print(dist)
        break
    cur_div=div(r,c)
    for k in range(5):
        nr=r+dr[k]
        nc=c+dc[k]
        ndv=div(nr,nc)
        if ndv==-1:
            continue
        nd=(d+1)%4 if ndv==cur_div else 1
        nr,nc=rot_pos(nr,nc)
        state=(nd,nr,nc)
        if state in seen or arr[nd][nr][nc]=='#':
            continue
        seen.add(state)
        q.append((nr,nc,nd,dist+1))
else:
    print(-1)
`,
  ],
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
const bySlug = new Map(existing.map((p) => [p.slug, p]));

for (const [id, slug, categorySlug, title, code] of PROBLEMS) {
  bySlug.set(slug, {
    id,
    slug,
    categorySlug,
    sources: [{ lang: "python", file: `local/oracle/${slug}.py`, code }],
    link: `https://www.acmicpc.net/problem/${id}`,
    authors: ["dongjun"],
    hash: stableHash(`extra:${slug}`),
    createdAt: Date.now(),
  });
  console.log(`[import-manual-batch-37] imported ${slug} (${title})`);
}

await fs.writeFile(
  OUT,
  JSON.stringify(
    [...bySlug.values()].sort(
      (a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug),
    ),
    null,
    2,
  ),
  "utf8",
);
console.log(`[import-manual-batch-37] wrote ${OUT}`);
