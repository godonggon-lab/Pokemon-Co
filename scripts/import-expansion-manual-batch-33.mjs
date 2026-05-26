import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
["1553","backtracking-1553","backtracking","Domino",`import sys
a=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(7)]
used=[[False]*8 for _ in range(8)]; seen=[[False]*8 for _ in range(7)]
ans=0
def dfs(pos):
 global ans
 if pos==56: ans+=1; return
 x,y=divmod(pos,8)
 if seen[x][y]: dfs(pos+1); return
 seen[x][y]=True
 for dx,dy in ((1,0),(0,1)):
  nx,ny=x+dx,y+dy
  if 0<=nx<7 and 0<=ny<8 and not seen[nx][ny]:
   u,v=sorted((a[x][y],a[nx][ny]))
   if not used[u][v]:
    used[u][v]=seen[nx][ny]=True
    dfs(pos+1)
    used[u][v]=False; seen[nx][ny]=False
 seen[x][y]=False
dfs(0); print(ans)
`],
["1799","backtracking-1799","backtracking","Bishop",`import sys
input=sys.stdin.readline
n=int(input()); board=[list(map(int,input().split())) for _ in range(n)]
cells=[[],[]]
for i in range(n):
 for j in range(n):
  if board[i][j]: cells[(i+j)&1].append((i,j))
def solve(arr):
 d1=[False]*(2*n); d2=[False]*(2*n); best=0
 def dfs(idx,cnt):
  nonlocal best
  if idx==len(arr): best=max(best,cnt); return
  if cnt+len(arr)-idx<=best: return
  x,y=arr[idx]
  if not d1[x+y] and not d2[x-y+n]:
   d1[x+y]=d2[x-y+n]=True; dfs(idx+1,cnt+1); d1[x+y]=d2[x-y+n]=False
  dfs(idx+1,cnt)
 dfs(0,0); return best
print(solve(cells[0])+solve(cells[1]))
`],
["1941","backtracking-1941","backtracking","Seven Princesses",`from itertools import combinations
from collections import deque
import sys
b=[sys.stdin.readline().strip() for _ in range(5)]
S=[i for i in range(25) if b[i//5][i%5]=='S']; Y=[i for i in range(25) if b[i//5][i%5]=='Y']
ans=0
for sc in range(4,min(7,len(S))+1):
 for ss in combinations(S,sc):
  for yy in combinations(Y,7-sc):
   comb=ss+yy
   s=set(comb); q=deque([comb[0]]); seen={comb[0]}
   while q:
    p=q.popleft(); x,y=divmod(p,5)
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy; np=nx*5+ny
     if 0<=nx<5 and 0<=ny<5 and np in s and np not in seen:
      seen.add(np); q.append(np)
   if len(seen)==7: ans+=1
print(ans)
`],
["2151","graph_traversal-2151","graph_traversal","Mirror Installation",`import heapq,sys
input=sys.stdin.readline
n=int(input()); a=[list(input().strip()) for _ in range(n)]
doors=[]
for i in range(n):
 for j in range(n):
  if a[i][j]=='#': doors.append((i,j))
INF=10**9; dist=[[[INF]*4 for _ in range(n)] for __ in range(n)]
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
sx,sy=doors[0]; ex,ey=doors[1]; pq=[]
for d in range(4): dist[sx][sy][d]=0; heapq.heappush(pq,(0,sx,sy,d))
while pq:
 c,x,y,d=heapq.heappop(pq)
 if c!=dist[x][y][d]: continue
 nx,ny=x+dirs[d][0],y+dirs[d][1]
 if not (0<=nx<n and 0<=ny<n) or a[nx][ny]=='*': continue
 opts=[d]
 if a[nx][ny]=='!': opts += ([2,3] if d<2 else [0,1])
 for nd in set(opts):
  nc=c+(nd!=d)
  if dist[nx][ny][nd]>nc:
   dist[nx][ny][nd]=nc; heapq.heappush(pq,(nc,nx,ny,nd))
print(min(dist[ex][ey]))
`],
["2239","backtracking-2239","backtracking","Sudoku",`import sys
a=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(9)]
zeros=[(i,j) for i in range(9) for j in range(9) if a[i][j]==0]
row=[0]*9; col=[0]*9; box=[0]*9
for i in range(9):
 for j in range(9):
  v=a[i][j]
  if v:
   bit=1<<v; row[i]|=bit; col[j]|=bit; box[i//3*3+j//3]|=bit
def dfs(k):
 if k==len(zeros):
  print('\\n'.join(''.join(map(str,r)) for r in a)); sys.exit()
 best=k; mask=0; bc=10
 for t in range(k,len(zeros)):
  i,j=zeros[t]; m=(~(row[i]|col[j]|box[i//3*3+j//3]))&0b1111111110; c=m.bit_count()
  if c<bc: best=t; mask=m; bc=c
 zeros[k],zeros[best]=zeros[best],zeros[k]
 i,j=zeros[k]; b=i//3*3+j//3; m=(~(row[i]|col[j]|box[b]))&0b1111111110
 for v in range(1,10):
  bit=1<<v
  if m&bit:
   a[i][j]=v; row[i]|=bit; col[j]|=bit; box[b]|=bit
   dfs(k+1)
   row[i]^=bit; col[j]^=bit; box[b]^=bit; a[i][j]=0
 zeros[k],zeros[best]=zeros[best],zeros[k]
dfs(0)
`],
["2307","shortest_path-2307","shortest_path","Roadblock",`import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
def dij(block=None,trace=False):
 INF=10**9; d=[INF]*(n+1); par=[0]*(n+1); d[1]=0; pq=[(0,1)]
 while pq:
  cost,x=heapq.heappop(pq)
  if cost!=d[x]: continue
  for y,w in g[x]:
   if block and ((x,y)==block or (y,x)==block): continue
   if d[y]>cost+w:
    d[y]=cost+w; par[y]=x; heapq.heappush(pq,(d[y],y))
 return (d[n],par) if trace else d[n]
base,par=dij(trace=True)
if base>=10**9: print(-1); sys.exit()
path=[]; cur=n
while cur!=1: path.append((cur,par[cur])); cur=par[cur]
ans=0
for e in path:
 v=dij(e)
 if v>=10**9: print(-1); sys.exit()
 ans=max(ans,v-base)
print(ans)
`],
["2933","simulation-2933","simulation","Mineral",`from collections import deque
import sys
input=sys.stdin.readline
r,c=map(int,input().split()); a=[list(input().strip()) for _ in range(r)]
n=int(input()); hs=list(map(int,input().split()))
def fall():
 seen=[[False]*c for _ in range(r)]; q=deque()
 for j in range(c):
  if a[r-1][j]=='x': seen[r-1][j]=True; q.append((r-1,j))
 while q:
  x,y=q.popleft()
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
   nx,ny=x+dx,y+dy
   if 0<=nx<r and 0<=ny<c and a[nx][ny]=='x' and not seen[nx][ny]:
    seen[nx][ny]=True; q.append((nx,ny))
 cluster=[(i,j) for i in range(r) for j in range(c) if a[i][j]=='x' and not seen[i][j]]
 if not cluster: return
 for i,j in cluster: a[i][j]='.'
 drop=0
 while True:
  if any(i+drop+1>=r or a[i+drop+1][j]=='x' for i,j in cluster): break
  drop+=1
 for i,j in cluster: a[i+drop][j]='x'
for t,h in enumerate(hs):
 row=r-h; rng=range(c) if t%2==0 else range(c-1,-1,-1)
 for j in rng:
  if a[row][j]=='x': a[row][j]='.'; break
 fall()
print('\\n'.join(''.join(row) for row in a))
`],
["5446","trie-5446","trie","File Delete",`import sys
input=sys.stdin.readline
class Node:
 def __init__(self): self.ch={}; self.delete=False; self.keep=False
def put(root,s,flag):
 cur=root
 for c in s:
  cur=cur.ch.setdefault(c,Node())
 setattr(cur,flag,True)
def mark_keep(node):
 keep=node.keep; delete=node.delete
 for child in node.ch.values():
  ck,cd=mark_keep(child); keep=ck or keep; delete=cd or delete
 node.keep=keep; node.delete=delete; return keep,delete
def solve(node):
 if node.delete and not node.keep: return 1
 return sum(solve(v) for v in node.ch.values())
for _ in range(int(input())):
 root=Node()
 for __ in range(int(input())): put(root,input().strip(),'delete')
 for __ in range(int(input())): put(root,input().strip(),'keep')
 mark_keep(root); print(solve(root))
`],
["5624","dynamic_programming_2-5624","dynamic_programming_2","Good Numbers",`import sys
input=sys.stdin.readline
n=int(input()); a=list(map(int,input().split()))
pairs=set(); ans=0
for i,x in enumerate(a):
 ok=False
 for j in range(i):
  if x-a[j] in pairs: ok=True; break
 if ok: ans+=1
 for j in range(i+1): pairs.add(a[j]+x)
print(ans)
`],
["9202","trie-9202","trie","Boggle",`import sys
lines=[line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
pos=0; score=[0,0,0,1,1,2,3,5,11]
w=int(lines[pos]); pos+=1; words=lines[pos:pos+w]; pos+=w
def exists(board,word):
 L=len(word); seen=[[False]*4 for _ in range(4)]
 def dfs(x,y,k):
  if board[x][y]!=word[k]: return False
  if k==L-1: return True
  seen[x][y]=True
  for dx in (-1,0,1):
   for dy in (-1,0,1):
    if dx==0 and dy==0: continue
    nx,ny=x+dx,y+dy
    if 0<=nx<4 and 0<=ny<4 and not seen[nx][ny] and dfs(nx,ny,k+1):
     seen[x][y]=False; return True
  seen[x][y]=False; return False
 return any(dfs(i,j,0) for i in range(4) for j in range(4))
b=int(lines[pos]); pos+=1
for bi in range(b):
 board=lines[pos:pos+4]; pos+=4
 found=sorted({wd for wd in words if exists(board,wd)})
 total=sum(score[len(wd)] for wd in found); best=''
 for wd in found:
  if len(wd)>len(best) or (len(wd)==len(best) and wd<best): best=wd
 print(total,best,len(found))
`],
["10597","backtracking-10597","backtracking","Permutation",`import sys
s=sys.stdin.readline().strip(); n=9 if len(s)<=9 else (len(s)-9)//2+9
used=[False]*(n+1); ans=[]
def dfs(idx):
 if idx==len(s):
  if len(ans)==n: print(*ans); sys.exit()
  return
 for l in (1,2):
  if idx+l<=len(s):
   v=int(s[idx:idx+l])
   if 1<=v<=n and not used[v]:
    used[v]=True; ans.append(v); dfs(idx+l); ans.pop(); used[v]=False
dfs(0)
`],
["10653","dynamic_programming_2-10653","dynamic_programming_2","Marathon 2",`import sys
input=sys.stdin.readline
n,k=map(int,input().split()); p=[tuple(map(int,input().split())) for _ in range(n)]
INF=10**12; dp=[[INF]*(k+1) for _ in range(n)]; dp[0][0]=0
def dist(a,b): return abs(p[a][0]-p[b][0])+abs(p[a][1]-p[b][1])
for i in range(1,n):
 for j in range(k+1):
  for prev in range(i):
   skip=i-prev-1
   if j>=skip: dp[i][j]=min(dp[i][j],dp[prev][j-skip]+dist(prev,i))
print(min(dp[-1]))
`],
["12908","backtracking-12908","backtracking","Teleport",`import sys
it=list(map(int,sys.stdin.read().split()))
pts=[(it[0],it[1]),(it[2],it[3])]; tele=[]
for i in range(4,16,4):
 a=(it[i],it[i+1]); b=(it[i+2],it[i+3]); tele.append((len(pts),len(pts)+1)); pts+= [a,b]
n=len(pts); d=[[abs(pts[i][0]-pts[j][0])+abs(pts[i][1]-pts[j][1]) for j in range(n)] for i in range(n)]
for a,b in tele: d[a][b]=d[b][a]=min(d[a][b],10)
for k in range(n):
 for i in range(n):
  for j in range(n):
   d[i][j]=min(d[i][j],d[i][k]+d[k][j])
print(d[0][1])
`],
["15683","simulation-15683","simulation","Surveillance",`import sys,itertools,copy
input=sys.stdin.readline
n,m=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]
cctv=[(i,j,a[i][j]) for i in range(n) for j in range(m) if 1<=a[i][j]<=5]
dirs=[(-1,0),(0,1),(1,0),(0,-1)]
sets={1:[[0],[1],[2],[3]],2:[[0,2],[1,3]],3:[[0,1],[1,2],[2,3],[3,0]],4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],5:[[0,1,2,3]]}
ans=n*m
def watch(b,x,y,ds):
 for d in ds:
  nx,ny=x+dirs[d][0],y+dirs[d][1]
  while 0<=nx<n and 0<=ny<m and b[nx][ny]!=6:
   if b[nx][ny]==0: b[nx][ny]=7
   nx+=dirs[d][0]; ny+=dirs[d][1]
def dfs(idx,b):
 global ans
 if idx==len(cctv):
  ans=min(ans,sum(row.count(0) for row in b)); return
 x,y,t=cctv[idx]
 for ds in sets[t]:
  nb=[row[:] for row in b]; watch(nb,x,y,ds); dfs(idx+1,nb)
dfs(0,a); print(ans)
`],
["16235","simulation-16235","simulation","Tree Investment",`import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); add=[list(map(int,input().split())) for _ in range(n)]
food=[[5]*n for _ in range(n)]; trees=[[[] for _ in range(n)] for __ in range(n)]
for _ in range(m):
 x,y,z=map(int,input().split()); trees[x-1][y-1].append(z)
for _ in range(k):
 breed=[]
 for i in range(n):
  for j in range(n):
   if trees[i][j]:
    trees[i][j].sort(); alive=[]; dead=0
    for age in trees[i][j]:
     if food[i][j]>=age:
      food[i][j]-=age; alive.append(age+1)
      if (age+1)%5==0: breed.append((i,j))
     else: dead+=age//2
    food[i][j]+=dead; trees[i][j]=alive
 for x,y in breed:
  for dx in (-1,0,1):
   for dy in (-1,0,1):
    if dx or dy:
     nx,ny=x+dx,y+dy
     if 0<=nx<n and 0<=ny<n: trees[nx][ny].append(1)
 for i in range(n):
  for j in range(n): food[i][j]+=add[i][j]
print(sum(len(trees[i][j]) for i in range(n) for j in range(n)))
`],
["17140","simulation-17140","simulation","Two-dimensional Array Operation",`from collections import Counter
import sys
r,c,k=map(int,sys.stdin.readline().split()); r-=1; c-=1
a=[list(map(int,sys.stdin.readline().split())) for _ in range(3)]
def op(rows):
 out=[]; mx=0
 for row in rows:
  cnt=Counter(x for x in row if x)
  nr=[]
  for num,co in sorted(cnt.items(), key=lambda x:(x[1],x[0])): nr += [num,co]
  nr=nr[:100]; mx=max(mx,len(nr)); out.append(nr)
 for row in out: row += [0]*(mx-len(row))
 return out
for t in range(101):
 if r<len(a) and c<len(a[0]) and a[r][c]==k: print(t); break
 if t==100: print(-1); break
 if len(a)>=len(a[0]): a=op(a)
 else: a=[list(x) for x in zip(*op([list(x) for x in zip(*a)]))]
`],
["17143","simulation-17143","simulation","Fishing King",`import sys
input=sys.stdin.readline
R,C,M=map(int,input().split()); sharks={}
for _ in range(M):
 r,c,s,d,z=map(int,input().split()); sharks[(r-1,c-1)]=[s,d-1,z]
dirs=[(-1,0),(1,0),(0,1),(0,-1)]
ans=0
for col in range(C):
 for row in range(R):
  if (row,col) in sharks:
   ans+=sharks.pop((row,col))[2]; break
 new={}
 for (x,y),(s,d,z) in sharks.items():
  speed=s%(2*(R-1)) if d<2 and R>1 else s%(2*(C-1)) if d>=2 and C>1 else 0
  for _ in range(speed):
   nx,ny=x+dirs[d][0],y+dirs[d][1]
   if not (0<=nx<R and 0<=ny<C):
    d=1-d if d<2 else 5-d
    nx,ny=x+dirs[d][0],y+dirs[d][1]
   x,y=nx,ny
  if (x,y) not in new or new[(x,y)][2]<z: new[(x,y)]=[s,d,z]
 sharks=new
print(ans)
`],
["17779","simulation-17779","simulation","Gerrymandering 2",`import sys
input=sys.stdin.readline
n=int(input()); a=[list(map(int,input().split())) for _ in range(n)]
total=sum(map(sum,a)); ans=10**9
for x in range(n):
 for y in range(n):
  for d1 in range(1,n):
   for d2 in range(1,n):
    if x+d1+d2>=n or y-d1<0 or y+d2>=n: continue
    area=[[0]*n for _ in range(n)]
    for i in range(d1+1): area[x+i][y-i]=area[x+d2+i][y+d2-i]=5
    for i in range(d2+1): area[x+i][y+i]=area[x+d1+i][y-d1+i]=5
    for i in range(x+1,x+d1+d2):
     inside=False
     for j in range(n):
      if area[i][j]==5: inside=not inside
      if inside: area[i][j]=5
    p=[0]*5
    for r in range(n):
     for c in range(n):
      if area[r][c]==5: p[4]+=a[r][c]
      elif r<x+d1 and c<=y: p[0]+=a[r][c]
      elif r<=x+d2 and c>y: p[1]+=a[r][c]
      elif r>=x+d1 and c<y-d1+d2: p[2]+=a[r][c]
      else: p[3]+=a[r][c]
    ans=min(ans,max(p)-min(p))
print(ans)
`],
["17822","simulation-17822","simulation","Circle Rotation",`from collections import deque
import sys
input=sys.stdin.readline
n,m,t=map(int,input().split()); a=[deque(map(int,input().split())) for _ in range(n)]
for _ in range(t):
 x,d,k=map(int,input().split())
 for i in range(x-1,n,x): a[i].rotate(k if d==0 else -k)
 rem=set()
 for i in range(n):
  for j in range(m):
   if a[i][j]==0: continue
   for ni,nj in ((i,(j+1)%m),(i,(j-1)%m),(i-1,j),(i+1,j)):
    if 0<=ni<n and a[ni][nj]==a[i][j]: rem.add((i,j)); rem.add((ni,nj))
 if rem:
  for i,j in rem: a[i][j]=0
 else:
  vals=[v for row in a for v in row if v]
  if vals:
   avg=sum(vals)/len(vals)
   for i in range(n):
    for j in range(m):
     if a[i][j]:
      if a[i][j]>avg: a[i][j]-=1
      elif a[i][j]<avg: a[i][j]+=1
print(sum(map(sum,a)))
`],
["20055","simulation-20055","simulation","Conveyor Belt",`from collections import deque
import sys
n,k=map(int,sys.stdin.readline().split()); belt=deque(map(int,sys.stdin.readline().split())); robot=deque([False]*n); step=0
while True:
 step+=1; belt.rotate(1); robot.rotate(1); robot[-1]=False
 for i in range(n-2,-1,-1):
  if robot[i] and not robot[i+1] and belt[i+1]>0:
   robot[i]=False; robot[i+1]=True; belt[i+1]-=1
 robot[-1]=False
 if belt[0]>0: robot[0]=True; belt[0]-=1
 if sum(1 for x in belt if x==0)>=k: print(step); break
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
    createdAt: Date.now(),
  });
  console.log(`[import-manual-batch-33] imported ${slug} (${title})`);
}
await fs.writeFile(
  OUT,
  JSON.stringify([...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug)), null, 2),
  "utf8",
);
console.log(`[import-manual-batch-33] wrote ${OUT}`);
