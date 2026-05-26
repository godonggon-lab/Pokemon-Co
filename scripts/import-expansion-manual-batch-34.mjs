import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "data", "problems-extra.json");

const PROBLEMS = [
["11779","shortest_path-11779","shortest_path","Minimum Cost 2",`import heapq,sys
input=sys.stdin.readline
n=int(input()); m=int(input()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b,c=map(int,input().split()); g[a].append((b,c))
s,e=map(int,input().split()); INF=10**18; d=[INF]*(n+1); par=[0]*(n+1); d[s]=0; pq=[(0,s)]
while pq:
 c,x=heapq.heappop(pq)
 if c!=d[x]: continue
 for y,w in g[x]:
  if d[y]>c+w:
   d[y]=c+w; par[y]=x; heapq.heappush(pq,(d[y],y))
path=[]; cur=e
while cur: path.append(cur); cur=par[cur]
path.reverse()
print(d[e]); print(len(path)); print(*path)
`],
["15728","brute_force-15728","brute_force","Erica",`import sys
n,k,m=map(int,sys.stdin.readline().split()); a=list(map(int,sys.stdin.readline().split())); b=list(map(int,sys.stdin.readline().split()))
for _ in range(m):
 vals=[x*y for x in a for y in b]; vals.sort()
 target=vals[-1]; removed=False
 for i,x in enumerate(a):
  if not removed and any(x*y==target for y in b):
   a.pop(i); removed=True; break
print(max(x*y for x in a for y in b))
`],
["17490","minimum_spanning_tree-17490","minimum_spanning_tree","Bridge",`import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); cost=[0]+list(map(int,input().split())); blocked=set()
for _ in range(m):
 a,b=map(int,input().split())
 if a>b: a,b=b,a
 if a==1 and b==n: blocked.add((n,1))
 else: blocked.add((a,b))
if m<=1: print('YES'); sys.exit()
p=list(range(n+1))
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
for i in range(1,n+1):
 j=i%n+1; e=(n,1) if i==n else (i,j)
 if e in blocked: continue
 a,b=f(i),f(j)
 if a!=b: p[b]=a
best={}
for i in range(1,n+1):
 r=f(i); best[r]=min(best.get(r,10**18),cost[i])
print('YES' if sum(best.values())<=k else 'NO')
`],
["17780","simulation-17780","simulation","New Game",`import sys
input=sys.stdin.readline
n,k=map(int,input().split()); color=[list(map(int,input().split())) for _ in range(n)]
dirs=[(0,1),(0,-1),(-1,0),(1,0)]; pos=[]; board=[[[] for _ in range(n)] for __ in range(n)]
for i in range(k):
 x,y,d=map(int,input().split()); x-=1; y-=1; d-=1; pos.append([x,y,d]); board[x][y].append(i)
def rev(d): return d^1 if d<2 else 5-d
for turn in range(1,1001):
 for i in range(k):
  x,y,d=pos[i]
  if board[x][y][0]!=i: continue
  nx,ny=x+dirs[d][0],y+dirs[d][1]
  if not(0<=nx<n and 0<=ny<n) or color[nx][ny]==2:
   d=rev(d); pos[i][2]=d; nx,ny=x+dirs[d][0],y+dirs[d][1]
   if not(0<=nx<n and 0<=ny<n) or color[nx][ny]==2: continue
  moving=board[x][y]; board[x][y]=[]
  if color[nx][ny]==1: moving=moving[::-1]
  for h in moving: pos[h][0]=nx; pos[h][1]=ny
  board[nx][ny].extend(moving)
  if len(board[nx][ny])>=4: print(turn); sys.exit()
print(-1)
`],
["17837","simulation-17837","simulation","New Game 2",`import sys
input=sys.stdin.readline
n,k=map(int,input().split()); color=[list(map(int,input().split())) for _ in range(n)]
dirs=[(0,1),(0,-1),(-1,0),(1,0)]; pos=[]; board=[[[] for _ in range(n)] for __ in range(n)]
for i in range(k):
 x,y,d=map(int,input().split()); x-=1; y-=1; d-=1; pos.append([x,y,d]); board[x][y].append(i)
def rev(d): return d^1 if d<2 else 5-d
for turn in range(1,1001):
 for i in range(k):
  x,y,d=pos[i]; idx=board[x][y].index(i)
  nx,ny=x+dirs[d][0],y+dirs[d][1]
  if not(0<=nx<n and 0<=ny<n) or color[nx][ny]==2:
   d=rev(d); pos[i][2]=d; nx,ny=x+dirs[d][0],y+dirs[d][1]
   if not(0<=nx<n and 0<=ny<n) or color[nx][ny]==2: continue
  moving=board[x][y][idx:]; board[x][y]=board[x][y][:idx]
  if color[nx][ny]==1: moving=moving[::-1]
  for h in moving: pos[h][0]=nx; pos[h][1]=ny
  board[nx][ny].extend(moving)
  if len(board[nx][ny])>=4: print(turn); sys.exit()
print(-1)
`],
["19235","simulation-19235","simulation","Monomino Domino 2",`import sys
input=sys.stdin.readline
blue=[[0]*4 for _ in range(6)]; green=[[0]*4 for _ in range(6)]; score=0
def put(board,t,x,y):
 cells=[(0,y)] if t==1 else ([(0,y),(0,y+1)] if t==2 else [(0,y),(1,y)])
 r=0
 while True:
  ok=True
  for dx,dy in cells:
   nr=r+dx+1
   if nr>=6 or board[nr][dy]: ok=False
  if ok: r+=1
  else: break
 for dx,dy in cells: board[r+dx][dy]=1
def clear(board):
 global score
 new=[]
 for row in board:
  if sum(row)==4: score+=1
  else: new.append(row)
 while len(new)<6: new.insert(0,[0]*4)
 board[:]=new
 cnt=sum(1 for i in range(2) if any(board[i]))
 for _ in range(cnt): board.pop(); board.insert(0,[0]*4)
def conv(t,x,y):
 return (1,y,3-x) if t==1 else ((3,x,3-y) if t==2 else (2,y,3-x))
for _ in range(int(input())):
 t,x,y=map(int,input().split()); put(green,t,x,y); put(blue,*conv(t,x,y)); clear(green); clear(blue)
print(score); print(sum(map(sum,green))+sum(map(sum,blue)))
`],
["19236","simulation-19236","simulation","Youth Shark",`import copy,sys
data=list(map(int,sys.stdin.read().split())); b=[[None]*4 for _ in range(4)]; fish={}
it=iter(data)
for i in range(4):
 for j in range(4):
  num=next(it); d=next(it)-1; b[i][j]=num; fish[num]=[i,j,d,True]
dirs=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
ans=0
def dfs(board,fs,sx,sy,sd,score):
 global ans
 ans=max(ans,score)
 for num in range(1,17):
  if not fs[num][3]: continue
  x,y,d,_=fs[num]
  for k in range(8):
   nd=(d+k)%8; nx,ny=x+dirs[nd][0],y+dirs[nd][1]
   if 0<=nx<4 and 0<=ny<4 and not(nx==sx and ny==sy):
    other=board[nx][ny]; board[x][y],board[nx][ny]=other,num; fs[num][:3]=[nx,ny,nd]
    if other: fs[other][0]=x; fs[other][1]=y
    break
 for step in range(1,4):
  nx,ny=sx+dirs[sd][0]*step,sy+dirs[sd][1]*step
  if 0<=nx<4 and 0<=ny<4 and board[nx][ny]:
   nb=copy.deepcopy(board); nf=copy.deepcopy(fs); eat=nb[nx][ny]; nd=nf[eat][2]
   nb[nx][ny]=0; nf[eat][3]=False; dfs(nb,nf,nx,ny,nd,score+eat)
first=b[0][0]; d=fish[first][2]; b[0][0]=0; fish[first][3]=False
dfs(b,fish,0,0,d,first); print(ans)
`],
["19237","simulation-19237","simulation","Adult Shark",`import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); grid=[list(map(int,input().split())) for _ in range(n)]; dirs=[0]+[x-1 for x in map(int,input().split())]
prio=[[list(map(lambda x:int(x)-1,input().split())) for _ in range(4)] for __ in range(m)]
dx=[-1,1,0,0]; dy=[0,0,-1,1]; smell=[[[0,0] for _ in range(n)] for __ in range(n)]
for t in range(1,1001):
 for i in range(n):
  for j in range(n):
   if grid[i][j]: smell[i][j]=[grid[i][j],k]
 moves={}
 for i in range(n):
  for j in range(n):
   s=grid[i][j]
   if not s: continue
   cand=None
   for d in prio[s-1][dirs[s]]:
    ni,nj=i+dx[d],j+dy[d]
    if 0<=ni<n and 0<=nj<n and smell[ni][nj][1]==0: cand=(ni,nj,d); break
   if cand is None:
    for d in prio[s-1][dirs[s]]:
     ni,nj=i+dx[d],j+dy[d]
     if 0<=ni<n and 0<=nj<n and smell[ni][nj][0]==s: cand=(ni,nj,d); break
   moves[s]=cand
 grid=[[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):
   if smell[i][j][1]>0: smell[i][j][1]-=1
 for s,(i,j,d) in sorted(moves.items()):
  if grid[i][j]==0: grid[i][j]=s; dirs[s]=d
 if sum(1 for row in grid for v in row if v)==1 and grid and any(1 in row for row in grid):
  print(t); sys.exit()
print(-1)
`],
["19238","simulation-19238","simulation","Start Taxi",`from collections import deque
import sys
input=sys.stdin.readline
n,m,fuel=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]; tx,ty=map(lambda x:int(x)-1,input().split())
dest={}; start={}
for idx in range(m):
 sx,sy,ex,ey=map(lambda x:int(x)-1,input().split()); start[(sx,sy)]=idx; dest[idx]=(ex,ey)
def bfs(sx,sy):
 d=[[-1]*n for _ in range(n)]; d[sx][sy]=0; q=deque([(sx,sy)])
 while q:
  x,y=q.popleft()
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
   nx,ny=x+dx,y+dy
   if 0<=nx<n and 0<=ny<n and a[nx][ny]==0 and d[nx][ny]<0: d[nx][ny]=d[x][y]+1; q.append((nx,ny))
 return d
for _ in range(m):
 d=bfs(tx,ty); cand=[]
 for (sx,sy),idx in start.items():
  if d[sx][sy]>=0: cand.append((d[sx][sy],sx,sy,idx))
 if not cand: print(-1); sys.exit()
 dist,sx,sy,idx=min(cand)
 if fuel<dist: print(-1); sys.exit()
 fuel-=dist; tx,ty=sx,sy; d=bfs(tx,ty); ex,ey=dest[idx]
 if d[ex][ey]<0 or fuel<d[ex][ey]: print(-1); sys.exit()
 fuel+=d[ex][ey]; tx,ty=ex,ey; del start[(sx,sy)]
print(fuel)
`],
["19942","backtracking-19942","backtracking","Diet",`import itertools,sys
input=sys.stdin.readline
n=int(input()); need=list(map(int,input().split())); item=[list(map(int,input().split())) for _ in range(n)]
best=10**18; ans=None
for mask in range(1,1<<n):
 s=[0,0,0,0,0]; idx=[]
 for i in range(n):
  if mask>>i&1:
   idx.append(i+1)
   for j in range(5): s[j]+=item[i][j]
 if all(s[j]>=need[j] for j in range(4)):
  if s[4]<best or (s[4]==best and idx<ans): best=s[4]; ans=idx
if ans is None: print(-1)
else: print(best); print(*ans)
`],
["20056","simulation-20056","simulation","Fireball",`from collections import defaultdict
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); balls=[]
for _ in range(m):
 r,c,mass,s,d=map(int,input().split()); balls.append((r-1,c-1,mass,s,d))
dr=[-1,-1,0,1,1,1,0,-1]; dc=[0,1,1,1,0,-1,-1,-1]
for _ in range(k):
 mp=defaultdict(list)
 for r,c,mass,s,d in balls: mp[((r+dr[d]*s)%n,(c+dc[d]*s)%n)].append((mass,s,d))
 balls=[]
 for (r,c),lst in mp.items():
  if len(lst)==1:
   mass,s,d=lst[0]; balls.append((r,c,mass,s,d))
  else:
   nm=sum(x[0] for x in lst)//5
   if nm==0: continue
   ns=sum(x[1] for x in lst)//len(lst); parity=[x[2]%2 for x in lst]; dirs=[0,2,4,6] if all(p==parity[0] for p in parity) else [1,3,5,7]
   for d in dirs: balls.append((r,c,nm,ns,d))
print(sum(x[2] for x in balls))
`],
["20168","shortest_path-20168","shortest_path","Alley Captain",`import heapq,sys
input=sys.stdin.readline
n,m,a,b,c=map(int,input().split()); g=[[] for _ in range(n+1)]
mx=0
for _ in range(m):
 x,y,w=map(int,input().split()); g[x].append((y,w)); g[y].append((x,w)); mx=max(mx,w)
def ok(limit):
 d=[10**18]*(n+1); d[a]=0; pq=[(0,a)]
 while pq:
  cost,x=heapq.heappop(pq)
  if cost!=d[x]: continue
  for y,w in g[x]:
   if w<=limit and d[y]>cost+w:
    d[y]=cost+w; heapq.heappush(pq,(d[y],y))
 return d[b]<=c
lo,hi,ans=1,mx,-1
while lo<=hi:
 mid=(lo+hi)//2
 if ok(mid): ans=mid; hi=mid-1
 else: lo=mid+1
print(ans)
`],
["20181","dynamic_programming_2-20181","dynamic_programming_2","Wriggling Ho-seok",`import sys
input=sys.stdin.readline
n,k=map(int,input().split()); a=list(map(int,input().split()))
dp=[0]*(n+1); l=0; s=0
for r,x in enumerate(a,1):
 s+=x; dp[r]=max(dp[r],dp[r-1])
 while s>=k:
  dp[r]=max(dp[r],dp[l]+s-k); s-=a[l]; l+=1
print(dp[n])
`],
["20665","simulation-20665","simulation","Reading Room",`import sys
input=sys.stdin.readline
n,t,p=input().split(); n=int(n); t=int(t); p=int(p)-1
def tm(s): return int(s[:2])*60+int(s[2:])
base=tm(input.__self__.readline()[:0] or '0900') if False else 0
reserv=[tuple(map(tm,input().split())) for _ in range(t)]
start=tm('0900'); end=tm('2100'); use=[[-1]*(end-start) for _ in range(n)]
def choose(occ):
 best=(-1,-1)
 for i in range(n):
  if occ[i]: continue
  dist=min([abs(i-j) for j in range(n) if occ[j]] or [10**9])
  key=(dist,-i)
  if key>best: best=key; seat=i
 return seat
for s,e in sorted(reserv):
 occ=[use[i][s-start]>=0 for i in range(n)]
 seat=choose(occ)
 for m in range(s-start,e-start): use[seat][m]=1
print(sum(1 for v in use[p] if v<0))
`],
["20950","backtracking-20950","backtracking","Minsu's Color",`import itertools,sys
input=sys.stdin.readline
n=int(input()); colors=[tuple(map(int,input().split())) for _ in range(n)]; target=tuple(map(int,input().split()))
ans=10**9
for r in range(2,min(7,n)+1):
 for comb in itertools.combinations(colors,r):
  avg=tuple(sum(c[i] for c in comb)//r for i in range(3)); ans=min(ans,sum(abs(avg[i]-target[i]) for i in range(3)))
print(ans)
`],
["21276","topological_sorting-21276","topological_sorting","Genealogy",`from collections import defaultdict,deque
import sys
input=sys.stdin.readline
n=int(input()); names=sorted(input().split()); m=int(input()); indeg={x:0 for x in names}; g=defaultdict(list)
for _ in range(m):
 child,parent=input().split(); g[parent].append(child); indeg[child]+=1
roots=[x for x in names if indeg[x]==0]; q=deque(roots); children={x:[] for x in names}
while q:
 x=q.popleft()
 for y in sorted(g[x]):
  indeg[y]-=1
  if indeg[y]==0: children[x].append(y); q.append(y)
print(len(roots)); print(*roots)
for x in names: print(x,len(children[x]),*sorted(children[x]))
`],
["22865","shortest_path-22865","shortest_path","Farthest Place",`import heapq,sys
input=sys.stdin.readline
n=int(input()); starts=list(map(int,input().split())); m=int(input()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
d=[10**18]*(n+1); pq=[]
for s in starts: d[s]=0; heapq.heappush(pq,(0,s))
while pq:
 c,x=heapq.heappop(pq)
 if c!=d[x]: continue
 for y,w in g[x]:
  if d[y]>c+w: d[y]=c+w; heapq.heappush(pq,(d[y],y))
print(max(range(1,n+1), key=lambda i:(d[i],-i)))
`],
["22866","data_structure-22866","data_structure","Tower View",`import sys
input=sys.stdin.readline
n=int(input()); h=list(map(int,input().split())); cnt=[0]*n; near=[10**9]*n
st=[]
for i in range(n):
 while st and st[-1][0]<=h[i]: st.pop()
 cnt[i]+=len(st)
 if st: near[i]=st[-1][1]
 st.append((h[i],i))
st=[]
for i in range(n-1,-1,-1):
 while st and st[-1][0]<=h[i]: st.pop()
 cnt[i]+=len(st)
 if st and abs(st[-1][1]-i)<abs(near[i]-i): near[i]=st[-1][1]
 st.append((h[i],i))
for i in range(n):
 print(cnt[i], near[i]+1 if cnt[i] else '')
`],
["22868","graph_traversal-22868","graph_traversal","Walk Small",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b=map(int,input().split()); g[a].append(b); g[b].append(a)
for row in g: row.sort()
s,e=map(int,input().split())
def bfs(a,b,ban):
 par=[0]*(n+1); q=deque([a]); par[a]=-1
 while q:
  x=q.popleft()
  if x==b: break
  for y in g[x]:
   if y not in ban and par[y]==0: par[y]=x; q.append(y)
 path=[]; cur=b
 while cur!=-1: path.append(cur); cur=par[cur]
 return path[::-1]
p1=bfs(s,e,set()); ban=set(p1[1:-1]); p2=bfs(e,s,ban)
print(len(p1)+len(p2)-2)
`],
["22870","shortest_path-22870","shortest_path","Walk Large",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b=map(int,input().split()); g[a].append(b); g[b].append(a)
for row in g: row.sort()
s,e=map(int,input().split())
def bfs(a,b,ban):
 par=[0]*(n+1); q=deque([a]); par[a]=-1
 while q:
  x=q.popleft()
  if x==b: break
  for y in g[x]:
   if y not in ban and par[y]==0: par[y]=x; q.append(y)
 path=[]; cur=b
 while cur!=-1: path.append(cur); cur=par[cur]
 return path[::-1]
p1=bfs(s,e,set()); ban=set(p1[1:-1]); p2=bfs(e,s,ban)
print(len(p1)+len(p2)-2)
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
  console.log(`[import-manual-batch-34] imported ${slug} (${title})`);
}
await fs.writeFile(
  OUT,
  JSON.stringify([...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug)), null, 2),
  "utf8",
);
console.log(`[import-manual-batch-34] wrote ${OUT}`);
