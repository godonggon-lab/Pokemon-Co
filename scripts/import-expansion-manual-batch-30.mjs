import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
  ["2234", "graph_traversal-2234", "graph_traversal", "Castle", `from collections import deque
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
room=[[-1]*m for _ in range(n)]
sizes=[]
dirs=[(0,-1),( -1,0),(0,1),(1,0)]
for i in range(n):
    for j in range(m):
        if room[i][j]!=-1: continue
        idx=len(sizes); q=deque([(i,j)]); room[i][j]=idx; cnt=0
        while q:
            x,y=q.popleft(); cnt+=1
            for bit,(dx,dy) in enumerate(dirs):
                if a[x][y]&(1<<bit): continue
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and room[nx][ny]==-1:
                    room[nx][ny]=idx; q.append((nx,ny))
        sizes.append(cnt)
best=max(sizes); merged=best
for i in range(n):
    for j in range(m):
        for dx,dy in ((1,0),(0,1)):
            ni,nj=i+dx,j+dy
            if ni<n and nj<m and room[i][j]!=room[ni][nj]:
                merged=max(merged,sizes[room[i][j]]+sizes[room[ni][nj]])
print(len(sizes)); print(best); print(merged)
`],
  ["2250", "tree-2250", "tree", "Tree Height and Width", `import sys
input=sys.stdin.readline
n=int(input())
children={}; has_parent=set()
for _ in range(n):
    x,l,r=map(int,input().split()); children[x]=(l,r)
    if l!=-1: has_parent.add(l)
    if r!=-1: has_parent.add(r)
root=next(x for x in children if x not in has_parent)
level_pos={}
col=0
def dfs(x,level):
    global col
    if x==-1: return
    l,r=children[x]
    dfs(l,level+1)
    col+=1
    level_pos.setdefault(level,[]).append(col)
    dfs(r,level+1)
dfs(root,1)
ans=(1,1)
for lv,arr in level_pos.items():
    width=max(arr)-min(arr)+1
    if width>ans[1]: ans=(lv,width)
print(*ans)
`],
  ["3665", "topological_sorting-3665", "topological_sorting", "Final Ranking", `from collections import deque
import sys
input=sys.stdin.readline
out=[]
for _ in range(int(input())):
    n=int(input()); rank=list(map(int,input().split()))
    adj=[[False]*(n+1) for _ in range(n+1)]
    indeg=[0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            adj[rank[i]][rank[j]]=True; indeg[rank[j]]+=1
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if adj[a][b]:
            adj[a][b]=False; adj[b][a]=True; indeg[b]-=1; indeg[a]+=1
        else:
            adj[b][a]=False; adj[a][b]=True; indeg[a]-=1; indeg[b]+=1
    q=deque([i for i in range(1,n+1) if indeg[i]==0]); res=[]; amb=False
    for _ in range(n):
        if not q: res=None; break
        if len(q)>1: amb=True
        x=q.popleft(); res.append(x)
        for y in range(1,n+1):
            if adj[x][y]:
                indeg[y]-=1
                if indeg[y]==0: q.append(y)
    out.append("IMPOSSIBLE" if res is None else ("?" if amb else " ".join(map(str,res))))
print("\\n".join(out))
`],
  ["5670", "trie-5670", "trie", "Cellphone Typing", `import sys
lines=sys.stdin.read().splitlines(); idx=0; outs=[]
while idx<len(lines):
    if lines[idx]=="": idx+=1; continue
    n=int(lines[idx]); idx+=1
    words=lines[idx:idx+n]; idx+=n
    trie={}
    end="*"
    for w in words:
        node=trie
        for ch in w: node=node.setdefault(ch,{})
        node[end]={}
    total=0
    for w in words:
        node=trie; cnt=0
        for i,ch in enumerate(w):
            if i==0 or len(node)>1 or end in node: cnt+=1
            node=node[ch]
        total+=cnt
    outs.append(f"{total/n:.2f}")
print("\\n".join(outs))
`],
  ["6087", "graph_traversal-6087", "graph_traversal", "Laser Communication", `from collections import deque
import sys
input=sys.stdin.readline
w,h=map(int,input().split())
g=[input().strip() for _ in range(h)]
cs=[(i,j) for i in range(h) for j in range(w) if g[i][j]=='C']
(sx,sy),(tx,ty)=cs
INF=10**9; dist=[[[INF]*4 for _ in range(w)] for __ in range(h)]
q=deque()
for d in range(4): dist[sx][sy][d]=0; q.append((sx,sy,d))
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
while q:
    x,y,d=q.popleft()
    for nd,(dx,dy) in enumerate(dirs):
        nx,ny=x+dx,y+dy
        if not(0<=nx<h and 0<=ny<w) or g[nx][ny]=='*': continue
        cost=dist[x][y][d]+(d!=nd)
        if dist[nx][ny][nd]>cost:
            dist[nx][ny][nd]=cost
            (q.append if d!=nd else q.appendleft)((nx,ny,nd))
print(min(dist[tx][ty]))
`],
  ["6416", "tree-6416", "tree", "Is It A Tree", `import sys
nums=list(map(int,sys.stdin.read().split())); i=0; case=1; out=[]
while i<len(nums):
    edges=[]; nodes=set(); indeg={}
    while i<len(nums):
        a,b=nums[i],nums[i+1]; i+=2
        if a==-1 and b==-1:
            print("\\n".join(out)); raise SystemExit
        if a==0 and b==0: break
        edges.append((a,b)); nodes.update((a,b)); indeg[b]=indeg.get(b,0)+1; indeg.setdefault(a,0)
    ok=True
    roots=[x for x in nodes if indeg.get(x,0)==0]
    if edges:
        ok=len(roots)==1 and all(indeg.get(x,0)<=1 for x in nodes) and len(edges)==len(nodes)-1
    out.append(f"Case {case} is {'a tree.' if ok else 'not a tree.'}"); case+=1
print("\\n".join(out))
`],
  ["7682", "backtracking-7682", "backtracking", "Tic Tac Toe", `import sys
def win(s,ch):
    lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(s[i]==ch for i in line) for line in lines)
out=[]
for s in sys.stdin.read().split():
    if s=="end": break
    x=s.count('X'); o=s.count('O'); wx=win(s,'X'); wo=win(s,'O')
    ok=False
    if x==o+1 and wx and not wo: ok=True
    if x==o and wo and not wx: ok=True
    if x==5 and o==4 and not wx and not wo: ok=True
    out.append("valid" if ok else "invalid")
print("\\n".join(out))
`],
  ["9489", "tree-9489", "tree", "Cousins", `import sys
out=[]; data=sys.stdin.read().split(); it=iter(data)
for n_s in it:
    n=int(n_s); k=int(next(it))
    if n==0 and k==0: break
    arr=[int(next(it)) for _ in range(n)]
    parent=[-1]*n; p=-1
    for i in range(1,n):
        if i==1 or arr[i]!=arr[i-1]+1: p+=1
        parent[i]=p
    idx=arr.index(k); gp=parent[parent[idx]] if parent[idx]!=-1 else -1
    ans=sum(1 for i in range(n) if parent[i]!=parent[idx] and parent[i]!=-1 and parent[parent[i]]==gp)
    out.append(str(ans))
print("\\n".join(out))
`],
  ["12896", "tree-12896", "tree", "Scruge Minho", `from collections import deque
import sys
input=sys.stdin.readline
n=int(input()); g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split()); g[a].append(b); g[b].append(a)
def far(s):
    d=[-1]*(n+1); d[s]=0; q=deque([s])
    while q:
        x=q.popleft()
        for y in g[x]:
            if d[y]==-1: d[y]=d[x]+1; q.append(y)
    v=max(range(1,n+1), key=lambda i:d[i]); return v,d[v]
a,_=far(1); b,diam=far(a)
print((diam+1)//2)
`],
  ["13459", "simulation-13459", "simulation", "Bead Escape", `from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); board=[list(input().strip()) for _ in range(n)]
for i in range(n):
 for j in range(m):
  if board[i][j]=='R': rx,ry=i,j; board[i][j]='.'
  if board[i][j]=='B': bx,by=i,j; board[i][j]='.'
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
def move(x,y,dx,dy):
 c=0
 while board[x+dx][y+dy]!='#' and board[x][y]!='O':
  x+=dx; y+=dy; c+=1
 return x,y,c
q=deque([(rx,ry,bx,by,0)]); seen={(rx,ry,bx,by)}
while q:
 rx,ry,bx,by,t=q.popleft()
 if t>=10: continue
 for dx,dy in dirs:
  nrx,nry,rc=move(rx,ry,dx,dy); nbx,nby,bc=move(bx,by,dx,dy)
  if board[nbx][nby]=='O': continue
  if board[nrx][nry]=='O': print(1); raise SystemExit
  if (nrx,nry)==(nbx,nby):
   if rc>bc: nrx-=dx; nry-=dy
   else: nbx-=dx; nby-=dy
  st=(nrx,nry,nbx,nby)
  if st not in seen: seen.add(st); q.append((*st,t+1))
print(0)
`],
  ["13460", "simulation-13460", "simulation", "Bead Escape 2", `from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); board=[list(input().strip()) for _ in range(n)]
for i in range(n):
 for j in range(m):
  if board[i][j]=='R': rx,ry=i,j; board[i][j]='.'
  if board[i][j]=='B': bx,by=i,j; board[i][j]='.'
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
def move(x,y,dx,dy):
 c=0
 while board[x+dx][y+dy]!='#' and board[x][y]!='O':
  x+=dx; y+=dy; c+=1
 return x,y,c
q=deque([(rx,ry,bx,by,0)]); seen={(rx,ry,bx,by)}
while q:
 rx,ry,bx,by,t=q.popleft()
 if t>=10: continue
 for dx,dy in dirs:
  nrx,nry,rc=move(rx,ry,dx,dy); nbx,nby,bc=move(bx,by,dx,dy)
  if board[nbx][nby]=='O': continue
  if board[nrx][nry]=='O': print(t+1); raise SystemExit
  if (nrx,nry)==(nbx,nby):
   if rc>bc: nrx-=dx; nry-=dy
   else: nbx-=dx; nby-=dy
  st=(nrx,nry,nbx,nby)
  if st not in seen: seen.add(st); q.append((*st,t+1))
print(-1)
`],
  ["13905", "minimum_spanning_tree-13905", "minimum_spanning_tree", "Sebu", `import sys
input=sys.stdin.readline
n,m=map(int,input().split()); s,e=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(m)]
p=list(range(n+1))
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
for a,b,c in sorted(edges,key=lambda x:-x[2]):
 ra,rb=f(a),f(b)
 if ra!=rb: p[rb]=ra
 if f(s)==f(e): print(c); break
else: print(0)
`],
  ["13908", "backtracking-13908", "backtracking", "Password", `import sys,itertools
data=list(map(int,sys.stdin.read().split()))
n,m=data[0],data[1]; req=set(data[2:])
ans=0
for p in itertools.product(range(10), repeat=n):
 if req.issubset(p): ans+=1
print(ans)
`],
  ["13911", "shortest_path-13911", "shortest_path", "House Hunting", `import heapq,sys
input=sys.stdin.readline
v,e=map(int,input().split()); g=[[] for _ in range(v+1)]
for _ in range(e):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
m,x=map(int,input().split()); mac=list(map(int,input().split()))
s,y=map(int,input().split()); star=list(map(int,input().split()))
INF=10**18
def dij(starts):
 d=[INF]*(v+1); q=[]
 for st in starts: d[st]=0; heapq.heappush(q,(0,st))
 while q:
  dist,node=heapq.heappop(q)
  if dist!=d[node]: continue
  for nxt,w in g[node]:
   nd=dist+w
   if nd<d[nxt]: d[nxt]=nd; heapq.heappush(q,(nd,nxt))
 return d
dm,ds=dij(mac),dij(star); special=set(mac+star); ans=INF
for i in range(1,v+1):
 if i not in special and dm[i]<=x and ds[i]<=y: ans=min(ans,dm[i]+ds[i])
print(ans if ans<INF else -1)
`],
  ["14657", "tree-14657", "tree", "Junwon's Journey", `from collections import deque
import sys,math
input=sys.stdin.readline
n,t=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(n-1):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
def far(s):
 d=[-1]*(n+1); d[s]=0; q=deque([s])
 while q:
  x=q.popleft()
  for y,w in g[x]:
   if d[y]==-1: d[y]=d[x]+w; q.append(y)
 v=max(range(1,n+1), key=lambda i:d[i]); return v,d[v]
a,_=far(1); _,diam=far(a)
print((diam+t-1)//t)
`],
  ["15653", "simulation-15653", "simulation", "Bead Escape 4", `from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); board=[list(input().strip()) for _ in range(n)]
for i in range(n):
 for j in range(m):
  if board[i][j]=='R': rx,ry=i,j; board[i][j]='.'
  if board[i][j]=='B': bx,by=i,j; board[i][j]='.'
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
def move(x,y,dx,dy):
 c=0
 while board[x+dx][y+dy]!='#' and board[x][y]!='O':
  x+=dx; y+=dy; c+=1
 return x,y,c
q=deque([(rx,ry,bx,by,0)]); seen={(rx,ry,bx,by)}
while q:
 rx,ry,bx,by,t=q.popleft()
 for dx,dy in dirs:
  nrx,nry,rc=move(rx,ry,dx,dy); nbx,nby,bc=move(bx,by,dx,dy)
  if board[nbx][nby]=='O': continue
  if board[nrx][nry]=='O': print(t+1); raise SystemExit
  if (nrx,nry)==(nbx,nby):
   if rc>bc: nrx-=dx; nry-=dy
   else: nbx-=dx; nby-=dy
  st=(nrx,nry,nbx,nby)
  if st not in seen: seen.add(st); q.append((*st,t+1))
print(-1)
`],
  ["15684", "backtracking-15684", "backtracking", "Ladder Manipulation", `import sys
input=sys.stdin.readline
n,m,h=map(int,input().split()); a=[[False]*(n+1) for _ in range(h+1)]
for _ in range(m):
 x,y=map(int,input().split()); a[x][y]=True
def ok():
 for start in range(1,n+1):
  cur=start
  for r in range(1,h+1):
   if a[r][cur]: cur+=1
   elif cur>1 and a[r][cur-1]: cur-=1
  if cur!=start: return False
 return True
def dfs(pos,cnt,limit):
 if cnt==limit: return ok()
 for idx in range(pos,h*(n-1)):
  r=idx//(n-1)+1; c=idx%(n-1)+1
  if a[r][c] or (c>1 and a[r][c-1]) or (c<n-1 and a[r][c+1]): continue
  a[r][c]=True
  if dfs(idx+1,cnt+1,limit): return True
  a[r][c]=False
 return False
for lim in range(4):
 if dfs(0,0,lim): print(lim); break
else: print(-1)
`],
  ["15685", "simulation-15685", "simulation", "Dragon Curve", `import sys
input=sys.stdin.readline
n=int(input()); grid=[[False]*101 for _ in range(101)]
dirs=[(1,0),(0,-1),(-1,0),(0,1)]
for _ in range(n):
 x,y,d,g=map(int,input().split()); seq=[d]
 for _ in range(g): seq += [(v+1)%4 for v in reversed(seq)]
 grid[y][x]=True
 for v in seq:
  dx,dy=dirs[v]; x+=dx; y+=dy; grid[y][x]=True
ans=0
for i in range(100):
 for j in range(100):
  if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]: ans+=1
print(ans)
`],
  ["16988", "graph_traversal-16988", "graph_traversal", "Baaaaaaaaaduk2", `from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); board=[list(map(int,input().split())) for _ in range(n)]
zeros=[(i,j) for i in range(n) for j in range(m) if board[i][j]==0]
def score(picks):
 for x,y in picks: board[x][y]=1
 seen=[[False]*m for _ in range(n)]; total=0
 for i in range(n):
  for j in range(m):
   if board[i][j]!=2 or seen[i][j]: continue
   q=deque([(i,j)]); seen[i][j]=True; cnt=0; liberty=False
   while q:
    x,y=q.popleft(); cnt+=1
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy
     if 0<=nx<n and 0<=ny<m:
      if board[nx][ny]==0: liberty=True
      elif board[nx][ny]==2 and not seen[nx][ny]: seen[nx][ny]=True; q.append((nx,ny))
   if not liberty: total+=cnt
 for x,y in picks: board[x][y]=0
 return total
ans=0
for picks in combinations(zeros,2): ans=max(ans,score(picks))
print(ans)
`],
  ["17135", "simulation-17135", "simulation", "Castle Defense", `from itertools import combinations
import sys
input=sys.stdin.readline
n,m,d=map(int,input().split()); orig=[list(map(int,input().split())) for _ in range(n)]
def play(cols):
 board=[row[:] for row in orig]; killed=0
 for turn in range(n):
  targets=set()
  for c in cols:
   best=None
   for i in range(n-1,-1,-1):
    for j in range(m):
     if board[i][j] and abs(n-i)+abs(c-j)<=d:
      cand=(abs(n-i)+abs(c-j),j,i)
      if best is None or cand<best: best=cand
   if best: targets.add((best[2],best[1]))
  for x,y in targets:
   if board[x][y]: board[x][y]=0; killed+=1
  board.pop(); board.insert(0,[0]*m)
 return killed
print(max(play(cols) for cols in combinations(range(m),3)))
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
    id, slug, categorySlug,
    sources: [{ lang: "python", file: `local/oracle/${slug}.py`, code }],
    link: `https://www.acmicpc.net/problem/${id}`,
    authors: ["dongjun"],
    hash: stableHash(`extra:${slug}`),
    createdAt: Date.now()
  });
  console.log(`[import-manual-batch-30] imported ${slug} (${title})`);
}
const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
console.log(`[import-manual-batch-30] wrote ${OUT}`);
