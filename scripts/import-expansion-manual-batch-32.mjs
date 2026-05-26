import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const PROBLEMS=[
["1030","divide_and_conquer-1030","divide_and_conquer","Fractal Plane",`import sys
s,n,k,r1,r2,c1,c2=map(int,sys.stdin.readline().split())
def black(r,c,size,level):
 if level==0: return False
 unit=size//n; a=r//unit; b=c//unit; lo=(n-k)//2; hi=lo+k
 if lo<=a<hi and lo<=b<hi: return True
 return black(r%unit,c%unit,unit,level-1)
size=n**s
print('\\n'.join(''.join('1' if black(r,c,size,s) else '0' for c in range(c1,c2+1)) for r in range(r1,r2+1)))
`],
["1219","shortest_path-1219","shortest_path","Salesman",`import sys
input=sys.stdin.readline
n,s,e,m=map(int,input().split()); edges=[tuple(map(int,input().split())) for _ in range(m)]; earn=list(map(int,input().split()))
INF=-10**18; dist=[INF]*n; dist[s]=earn[s]
for i in range(n+100):
 updated=False
 for a,b,c in edges:
  if dist[a]==INF: continue
  val=dist[a]-c+earn[b]
  if dist[b]<val:
   dist[b]=10**18 if i>=n-1 else val; updated=True
  if dist[a]==10**18: dist[b]=10**18
if dist[e]==INF: print('gg')
elif dist[e]==10**18: print('Gee')
else: print(dist[e])
`],
["1277","shortest_path-1277","shortest_path","Power Plant",`import heapq,math,sys
input=sys.stdin.readline
n,w=map(int,input().split()); limit=float(input()); pts=[None]+[tuple(map(int,input().split())) for _ in range(n)]
g=[[] for _ in range(n+1)]
for _ in range(w):
 a,b=map(int,input().split()); g[a].append((b,0)); g[b].append((a,0))
for i in range(1,n+1):
 for j in range(i+1,n+1):
  d=math.hypot(pts[i][0]-pts[j][0],pts[i][1]-pts[j][1])
  if d<=limit: g[i].append((j,d)); g[j].append((i,d))
dist=[10**18]*(n+1); dist[1]=0; q=[(0,1)]
while q:
 d,x=heapq.heappop(q)
 if d!=dist[x]: continue
 for y,w in g[x]:
  nd=d+w
  if nd<dist[y]: dist[y]=nd; heapq.heappush(q,(nd,y))
print(int(dist[n]*1000))
`],
["1445","shortest_path-1445","shortest_path","Sunday Morning Date",`import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=[list(input().strip()) for _ in range(n)]
near=[[False]*m for _ in range(n)]
for i in range(n):
 for j in range(m):
  if a[i][j]=='g':
   for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
    x,y=i+dx,j+dy
    if 0<=x<n and 0<=y<m and a[x][y]=='.': near[x][y]=True
  if a[i][j]=='S': s=(i,j)
  if a[i][j]=='F': f=(i,j)
dist=[[(10**9,10**9)]*m for _ in range(n)]; dist[s[0]][s[1]]=(0,0); q=[(0,0,*s)]
while q:
 g,b,x,y=heapq.heappop(q)
 if (g,b)!=dist[x][y]: continue
 for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
  nx,ny=x+dx,y+dy
  if 0<=nx<n and 0<=ny<m:
   ng,nb=g+(a[nx][ny]=='g'), b+(near[nx][ny] and a[nx][ny] not in 'SF')
   if (ng,nb)<dist[nx][ny]: dist[nx][ny]=(ng,nb); heapq.heappush(q,(ng,nb,nx,ny))
print(*dist[f[0]][f[1]])
`],
["1944","minimum_spanning_tree-1944","minimum_spanning_tree","Robot Key",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); grid=[input().strip() for _ in range(n)]
pts=[(i,j) for i in range(n) for j in range(n) if grid[i][j] in 'SK']; idx={p:i for i,p in enumerate(pts)}
edges=[]
for si,sj in pts:
 d=[[-1]*n for _ in range(n)]; d[si][sj]=0; q=deque([(si,sj)])
 while q:
  x,y=q.popleft()
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
   nx,ny=x+dx,y+dy
   if 0<=nx<n and 0<=ny<n and grid[nx][ny]!='1' and d[nx][ny]==-1:
    d[nx][ny]=d[x][y]+1; q.append((nx,ny))
 for p in pts:
  if p!=(si,sj) and d[p[0]][p[1]]!=-1: edges.append((d[p[0]][p[1]],idx[(si,sj)],idx[p]))
p=list(range(len(pts)))
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
ans=cnt=0
for w,a,b in sorted(edges):
 ra,rb=f(a),f(b)
 if ra!=rb: p[rb]=ra; ans+=w; cnt+=1
print(ans if cnt==len(pts)-1 else -1)
`],
["2194","graph_traversal-2194","graph_traversal","Move Unit",`from collections import deque
import sys
input=sys.stdin.readline
n,m,a,b,k=map(int,input().split()); ps=[[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
 x,y=map(int,input().split()); ps[x][y]=1
for i in range(1,n+1):
 for j in range(1,m+1): ps[i][j]+=ps[i-1][j]+ps[i][j-1]-ps[i-1][j-1]
sr,sc=map(int,input().split()); er,ec=map(int,input().split())
def ok(x,y):
 if x<1 or y<1 or x+a-1>n or y+b-1>m: return False
 return ps[x+a-1][y+b-1]-ps[x-1][y+b-1]-ps[x+a-1][y-1]+ps[x-1][y-1]==0
d=[[-1]*(m+1) for _ in range(n+1)]; d[sr][sc]=0; q=deque([(sr,sc)])
while q:
 x,y=q.popleft()
 if (x,y)==(er,ec): print(d[x][y]); break
 for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
  nx,ny=x+dx,y+dy
  if 1<=nx<=n and 1<=ny<=m and d[nx][ny]==-1 and ok(nx,ny): d[nx][ny]=d[x][y]+1; q.append((nx,ny))
else: print(-1)
`],
["2263","tree-2263","tree","Tree Traversal",`import sys
sys.setrecursionlimit(10**6); input=sys.stdin.readline
n=int(input()); ino=list(map(int,input().split())); post=list(map(int,input().split())); pos={v:i for i,v in enumerate(ino)}; out=[]
def rec(il,ir,pl,pr):
 if il>ir: return
 root=post[pr]; out.append(root); k=pos[root]; left=k-il
 rec(il,k-1,pl,pl+left-1); rec(k+1,ir,pl+left,pr-1)
rec(0,n-1,0,n-1); print(*out)
`],
["2982","shortest_path-2982","shortest_path","Old Berland Language",`import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split()); a,b,k,g=map(int,input().split()); route=list(map(int,input().split()))
graph=[[] for _ in range(n+1)]; weight={}
for _ in range(m):
 x,y,l=map(int,input().split()); graph[x].append((y,l)); graph[y].append((x,l)); weight[(x,y)]=weight[(y,x)]=l
busy={}; t=0
for u,v in zip(route,route[1:]): busy[(u,v)]=busy[(v,u)]=(t,t+weight[(u,v)]); t+=weight[(u,v)]
d=[10**18]*(n+1); d[a]=k; pq=[(k,a)]
while pq:
 time,x=heapq.heappop(pq)
 if time!=d[x]: continue
 for y,w in graph[x]:
  nt=time
  if (x,y) in busy:
   s,e=busy[(x,y)]
   if s<=nt<e: nt=e
  nt+=w
  if nt<d[y]: d[y]=nt; heapq.heappush(pq,(nt,y))
print(d[b]-k)
`],
["9370","shortest_path-9370","shortest_path","Unconfirmed Destination",`import heapq,sys
input=sys.stdin.readline
def dij(n,g,s):
 d=[10**15]*(n+1); d[s]=0; q=[(0,s)]
 while q:
  dist,x=heapq.heappop(q)
  if dist!=d[x]: continue
  for y,w in g[x]:
   nd=dist+w
   if nd<d[y]: d[y]=nd; heapq.heappush(q,(nd,y))
 return d
out=[]
for _ in range(int(input())):
 n,m,t=map(int,input().split()); s,g,h=map(int,input().split()); graph=[[] for _ in range(n+1)]; gh=0
 for _ in range(m):
  a,b,d=map(int,input().split()); graph[a].append((b,d)); graph[b].append((a,d))
  if {a,b}=={g,h}: gh=d
 cand=[int(input()) for _ in range(t)]
 ds,dg,dh=dij(n,graph,s),dij(n,graph,g),dij(n,graph,h)
 ans=sorted(x for x in cand if ds[x]==ds[g]+gh+dh[x] or ds[x]==ds[h]+gh+dg[x])
 out.append(' '.join(map(str,ans)))
print('\\n'.join(out))
`],
["14923","graph_traversal-14923","graph_traversal","Maze Escape",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); hx,hy=map(lambda x:int(x)-1,input().split()); ex,ey=map(lambda x:int(x)-1,input().split()); a=[list(map(int,input().split())) for _ in range(n)]
d=[[[-1]*2 for _ in range(m)] for __ in range(n)]; d[hx][hy][0]=0; q=deque([(hx,hy,0)])
while q:
 x,y,b=q.popleft()
 if (x,y)==(ex,ey): print(d[x][y][b]); break
 for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
  nx,ny=x+dx,y+dy
  if 0<=nx<n and 0<=ny<m:
   nb=b+a[nx][ny]
   if nb<2 and d[nx][ny][nb]==-1: d[nx][ny][nb]=d[x][y][b]+1; q.append((nx,ny,nb))
else: print(-1)
`],
["16118","shortest_path-16118","shortest_path","Moonlight Fox",`import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b,d=map(int,input().split()); d*=2; g[a].append((b,d)); g[b].append((a,d))
def fox():
 d=[10**18]*(n+1); d[1]=0; q=[(0,1)]
 while q:
  dist,x=heapq.heappop(q)
  if dist!=d[x]: continue
  for y,w in g[x]:
   if dist+w<d[y]: d[y]=dist+w; heapq.heappush(q,(d[y],y))
 return d
fd=fox(); wd=[[10**18]*2 for _ in range(n+1)]; wd[1][0]=0; q=[(0,1,0)]
while q:
 dist,x,state=heapq.heappop(q)
 if dist!=wd[x][state]: continue
 for y,w in g[x]:
  nw=w//2 if state==0 else w*2; ns=1-state
  if dist+nw<wd[y][ns]: wd[y][ns]=dist+nw; heapq.heappush(q,(wd[y][ns],y,ns))
print(sum(fd[i]<min(wd[i]) for i in range(2,n+1)))
`],
["16202","minimum_spanning_tree-16202","minimum_spanning_tree","MST Game",`import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); edges=[(i+1,*map(int,input().split())) for i in range(m)]
def mst(start):
 p=list(range(n+1))
 def f(x):
  while p[x]!=x: p[x]=p[p[x]]; x=p[x]
  return x
 cost=cnt=0
 for w,a,b in edges[start:]:
  ra,rb=f(a),f(b)
  if ra!=rb: p[rb]=ra; cost+=w; cnt+=1
 return cost if cnt==n-1 else 0
print(*[mst(i) for i in range(k)])
`],
["16985","graph_traversal-16985","graph_traversal","Maaaaaaaaaze",`from itertools import permutations,product
from collections import deque
import sys
data=[[list(map(int,sys.stdin.readline().split())) for _ in range(5)] for __ in range(5)]
def rot(layer):
 return [[layer[4-j][i] for j in range(5)] for i in range(5)]
rots=[]
for lay in data:
 arr=[lay]
 for _ in range(3): arr.append(rot(arr[-1]))
 rots.append(arr)
ans=10**9
for perm in permutations(range(5)):
 for rs in product(range(4), repeat=5):
  if ans==12:
   print(12); sys.exit()
  cube=[rots[perm[i]][rs[i]] for i in range(5)]
  if not cube[0][0][0] or not cube[4][4][4]: continue
  d=[[[-1]*5 for _ in range(5)] for __ in range(5)]; d[0][0][0]=0; q=deque([(0,0,0)])
  while q:
   z,x,y=q.popleft()
   if d[z][x][y]>=ans: continue
   if (z,x,y)==(4,4,4): ans=min(ans,d[z][x][y]); break
   for dz,dx,dy in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
    nz,nx,ny=z+dz,x+dx,y+dy
    if 0<=nz<5 and 0<=nx<5 and 0<=ny<5 and cube[nz][nx][ny] and d[nz][nx][ny]==-1:
     d[nz][nx][ny]=d[z][x][y]+1; q.append((nz,nx,ny))
print(ans if ans<10**9 else -1)
`],
["17216","dynamic_programming_2-17216","dynamic_programming_2","Most Valuable Player",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); val=[0]+list(map(int,input().split())); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b=map(int,input().split()); g[b].append(a)
sys.setrecursionlimit(10**6)
dp=[None]*(n+1)
def f(x):
 if dp[x] is not None: return dp[x]
 dp[x]=val[x]+max([f(y) for y in g[x]] or [0]); return dp[x]
print(max(f(i) for i in range(1,n+1)))
`],
["17472","minimum_spanning_tree-17472","minimum_spanning_tree","Bridge Making 2",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]
idx=0; seen=[[False]*m for _ in range(n)]
for i in range(n):
 for j in range(m):
  if a[i][j]==1 and not seen[i][j]:
   idx+=1; seen[i][j]=True; a[i][j]=idx; q=deque([(i,j)])
   while q:
    x,y=q.popleft()
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy
     if 0<=nx<n and 0<=ny<m and a[nx][ny]==1 and not seen[nx][ny]:
      seen[nx][ny]=True; a[nx][ny]=idx; q.append((nx,ny))
edges=[]
for i in range(n):
 for j in range(m):
  if a[i][j]>0:
   for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
    x,y=i+dx,j+dy; l=0
    while 0<=x<n and 0<=y<m and a[x][y]==0: l+=1; x+=dx; y+=dy
    if 0<=x<n and 0<=y<m and a[x][y]!=a[i][j] and l>=2: edges.append((l,a[i][j],a[x][y]))
p=list(range(idx+1))
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
ans=cnt=0
for w,u,v in sorted(edges):
 ru,rv=f(u),f(v)
 if ru!=rv: p[rv]=ru; ans+=w; cnt+=1
print(ans if cnt==idx-1 else -1)
`],
["18769","minimum_spanning_tree-18769","minimum_spanning_tree","Grid MST",`import sys
it=iter(map(int,sys.stdin.read().split())); t=next(it); outs=[]
for _ in range(t):
 r=next(it); c=next(it); edges=[]; node=lambda i,j:i*c+j
 for i in range(r):
  for j in range(c-1): edges.append((next(it),node(i,j),node(i,j+1)))
 for i in range(r-1):
  for j in range(c): edges.append((next(it),node(i,j),node(i+1,j)))
 p=list(range(r*c))
 def f(x):
  while p[x]!=x: p[x]=p[p[x]]; x=p[x]
  return x
 ans=0
 for w,a,b in sorted(edges):
  ra,rb=f(a),f(b)
  if ra!=rb: p[rb]=ra; ans+=w
 outs.append(str(ans))
print('\\n'.join(outs))
`],
["20182","shortest_path-20182","shortest_path","Golmok Captain",`import heapq,sys
input=sys.stdin.readline
n,m,a,b,c=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 x,y,z=map(int,input().split()); g[x].append((y,z)); g[y].append((x,z))
def ok(limit):
 d=[10**18]*(n+1); d[a]=0; q=[(0,a)]
 while q:
  cost,x=heapq.heappop(q)
  if cost!=d[x]: continue
  for y,w in g[x]:
   if w>limit: continue
   nd=cost+w
   if nd<d[y]: d[y]=nd; heapq.heappush(q,(nd,y))
 return d[b]<=c
lo,hi=1,10**9; ans=-1
while lo<=hi:
 mid=(lo+hi)//2
 if ok(mid): ans=mid; hi=mid-1
 else: lo=mid+1
print(ans)
`],
["20183","shortest_path-20183","shortest_path","Gold Mine",`import heapq,sys
input=sys.stdin.readline
n,m,a,b,c=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 x,y,z=map(int,input().split()); g[x].append((y,z)); g[y].append((x,z))
def ok(limit):
 d=[10**18]*(n+1); d[a]=0; q=[(0,a)]
 while q:
  cost,x=heapq.heappop(q)
  if cost!=d[x]: continue
  for y,w in g[x]:
   if w>limit: continue
   nd=cost+w
   if nd<d[y]: d[y]=nd; heapq.heappush(q,(nd,y))
 return d[b]<=c
lo,hi=1,10**9; ans=-1
while lo<=hi:
 mid=(lo+hi)//2
 if ok(mid): ans=mid; hi=mid-1
 else: lo=mid+1
print(ans)
`],
["21609","simulation-21609","simulation","Shark Middle School",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]
def gravity():
 for j in range(n):
  empty=n-1
  for i in range(n-1,-1,-1):
   if a[i][j]==-2: continue
   if a[i][j]==-1: empty=i-1
   else:
    a[empty][j],a[i][j]=a[i][j],-2; empty-=1
def rotate(): return [list(row) for row in zip(*a)][::-1]
score=0
while True:
 seen=[[False]*n for _ in range(n)]; groups=[]
 for i in range(n):
  for j in range(n):
   if a[i][j]>0 and not seen[i][j]:
    color=a[i][j]; q=deque([(i,j)]); seen[i][j]=True; cells=[]; rain=[]; base=(i,j)
    while q:
     x,y=q.popleft(); cells.append((x,y))
     if a[x][y]==0: rain.append((x,y))
     for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<n and not seen[nx][ny] and (a[nx][ny]==0 or a[nx][ny]==color):
       seen[nx][ny]=True; q.append((nx,ny))
    for x,y in rain: seen[x][y]=False
    normals=[c for c in cells if a[c[0]][c[1]]==color]
    if len(cells)>=2: groups.append((len(cells),len(rain),max(normals),cells))
 if not groups: break
 _,_,_,cells=max(groups)
 score+=len(cells)**2
 for x,y in cells: a[x][y]=-2
 gravity(); a=rotate(); gravity()
print(score)
`],
["21940","shortest_path-21940","shortest_path","Middle Meeting Room",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); INF=10**9; d=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1): d[i][i]=0
for _ in range(m):
 a,b,t=map(int,input().split()); d[a][b]=min(d[a][b],t)
k=int(input()); friends=list(map(int,input().split()))
for x in range(1,n+1):
 for i in range(1,n+1):
  for j in range(1,n+1):
   if d[i][j]>d[i][x]+d[x][j]: d[i][j]=d[i][x]+d[x][j]
best=INF; ans=[]
for room in range(1,n+1):
 val=max(d[f][room]+d[room][f] for f in friends)
 if val<best: best=val; ans=[room]
 elif val==best: ans.append(room)
print(*ans)
`]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()}); console.log(`[import-manual-batch-32] imported ${slug} (${title})`);}
await fs.writeFile(OUT,JSON.stringify([...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug)),null,2),"utf8");
console.log(`[import-manual-batch-32] wrote ${OUT}`);
