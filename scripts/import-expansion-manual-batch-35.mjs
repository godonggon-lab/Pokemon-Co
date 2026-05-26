import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const PROBLEMS=[
["1240","tree-1240","tree","Distance Between Nodes",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(n-1):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
for _ in range(m):
 s,e=map(int,input().split()); q=deque([(s,0)]); seen={s}
 while q:
  x,d=q.popleft()
  if x==e: print(d); break
  for y,w in g[x]:
   if y not in seen: seen.add(y); q.append((y,d+w))
`],
["1359","brute_force-1359","brute_force","Lottery",`from math import comb
n,m,k=map(int,input().split())
tot=comb(n,m); good=sum(comb(m,i)*comb(n-m,m-i) for i in range(k,m+1) if 0<=m-i<=n-m)
print(good/tot)
`],
["1446","shortest_path-1446","shortest_path","Shortcut",`import sys
input=sys.stdin.readline
n,d=map(int,input().split()); shortcuts=[tuple(map(int,input().split())) for _ in range(n)]
dist=list(range(d+1))
for i in range(d+1):
 if i: dist[i]=min(dist[i],dist[i-1]+1)
 for a,b,c in shortcuts:
  if a==i and b<=d and dist[b]>dist[a]+c: dist[b]=dist[a]+c
print(dist[d])
`],
["1535","dynamic_programming_2-1535","dynamic_programming_2","Hello",`import sys
input=sys.stdin.readline
n=int(input()); hp=list(map(int,input().split())); joy=list(map(int,input().split()))
dp=[0]*100
for h,j in zip(hp,joy):
 for v in range(99,h-1,-1): dp[v]=max(dp[v],dp[v-h]+j)
print(max(dp))
`],
["1577","dynamic_programming_2-1577","dynamic_programming_2","Road Count",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); k=int(input()); bad=set()
for _ in range(k):
 a,b,c,d=map(int,input().split()); bad.add(tuple(sorted(((a,b),(c,d)))))
dp=[[0]*(m+1) for _ in range(n+1)]; dp[0][0]=1
for i in range(n+1):
 for j in range(m+1):
  if i and tuple(sorted(((i-1,j),(i,j)))) not in bad: dp[i][j]+=dp[i-1][j]
  if j and tuple(sorted(((i,j-1),(i,j)))) not in bad: dp[i][j]+=dp[i][j-1]
print(dp[n][m])
`],
["1581","brute_force-1581","brute_force","Rockstar",`from functools import lru_cache
cnt=tuple(map(int,input().split()))
@lru_cache(None)
def f(a,b,c,d,last):
 best=0; arr=[a,b,c,d]; types=[(0,0),(0,1),(1,0),(1,1)]
 for i,(s,e) in enumerate(types):
  if arr[i] and (last==2 or last==s):
   arr[i]-=1; best=max(best,1+f(*arr,e)); arr[i]+=1
 return best
print(f(*cnt,2))
`],
["2411","dynamic_programming_2-2411","dynamic_programming_2","Eating Items",`import sys
input=sys.stdin.readline
n,m,a,b=map(int,input().split()); items=[tuple(map(int,input().split())) for _ in range(a)]; obs={tuple(map(int,input().split())) for _ in range(b)}
pts=[(1,1)]+sorted(items)+[(n,m)]
ans=1
def ways(s,t):
 (x1,y1),(x2,y2)=s,t
 if x1>x2 or y1>y2: return 0
 dp=[[0]*(y2-y1+1) for _ in range(x2-x1+1)]; dp[0][0]=1
 for i in range(x1,x2+1):
  for j in range(y1,y2+1):
   if (i,j) in obs: dp[i-x1][j-y1]=0; continue
   if i>x1: dp[i-x1][j-y1]+=dp[i-x1-1][j-y1]
   if j>y1: dp[i-x1][j-y1]+=dp[i-x1][j-y1-1]
 return dp[-1][-1]
for p,q in zip(pts,pts[1:]): ans*=ways(p,q)
print(ans)
`],
["2613","binary_search-2613","binary_search","Number Grouping",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=list(map(int,input().split()))
def ok(x):
 cnt=1; s=0
 for v in a:
  if v>x: return False
  if s+v>x: cnt+=1; s=v
  else: s+=v
 return cnt<=m
lo,hi=max(a),sum(a)
while lo<hi:
 mid=(lo+hi)//2
 if ok(mid): hi=mid
 else: lo=mid+1
limit=lo; groups=[]; s=0; c=0; rem=m
for i,v in enumerate(a):
 if s+v>limit or n-i<rem:
  groups.append(c); rem-=1; s=v; c=1
 else:
  s+=v; c+=1
groups.append(c)
print(limit); print(*groups)
`],
["2922","backtracking-2922","backtracking","Pleasant Word",`s=input().strip(); V=set('AEIOU')
ans=0
def dfs(i,v,c,hasL,mul):
 global ans
 if v>=3 or c>=3: return
 if i==len(s):
  if hasL: ans+=mul
  return
 ch=s[i]
 if ch=='_':
  dfs(i+1,v+1,0,hasL,mul*5)
  dfs(i+1,0,c+1,True,mul)
  dfs(i+1,0,c+1,hasL,mul*20)
 elif ch in V: dfs(i+1,v+1,0,hasL,mul)
 else: dfs(i+1,0,c+1,hasL or ch=='L',mul)
dfs(0,0,0,False,1); print(ans)
`],
["8972","simulation-8972","simulation","Crazy Arduino",`import sys
input=sys.stdin.readline
r,c=map(int,input().split()); board=[list(input().strip()) for _ in range(r)]; moves=input().strip()
dirs=[(0,0),(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]
ardu=[]; ix=iy=0
for i in range(r):
 for j in range(c):
  if board[i][j]=='I': ix,iy=i,j
  elif board[i][j]=='R': ardu.append((i,j))
for turn,ch in enumerate(moves,1):
 dx,dy=dirs[int(ch)]; ix+=dx; iy+=dy
 if (ix,iy) in ardu: print('kraj',turn); sys.exit()
 mp={}
 for x,y in ardu:
  best=min(((abs(ix-(x+dx))+abs(iy-(y+dy)),x+dx,y+dy) for dx,dy in dirs[1:] if dx or dy))
  _,nx,ny=best
  if (nx,ny)==(ix,iy): print('kraj',turn); sys.exit()
  mp[(nx,ny)]=mp.get((nx,ny),0)+1
 ardu=[p for p,v in mp.items() if v==1]
out=[['.']*c for _ in range(r)]; out[ix][iy]='I'
for x,y in ardu: out[x][y]='R'
print('\\n'.join(''.join(row) for row in out))
`],
["9944","backtracking-9944","backtracking","NxM Board Complete",`import sys
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
case=1
while True:
 line=sys.stdin.readline()
 if not line: break
 n,m=map(int,line.split()); a=[list(sys.stdin.readline().strip()) for _ in range(n)]
 empty=sum(row.count('.') for row in a); ans=10**9
 def dfs(x,y,left,cnt):
  global ans
  if left==0:
   ans=min(ans,cnt); return
  if cnt>=ans: return
  for dx,dy in dirs:
   nx,ny=x+dx,y+dy; moved=[]
   while 0<=nx<n and 0<=ny<m and a[nx][ny]=='.':
    a[nx][ny]='*'; moved.append((nx,ny)); nx+=dx; ny+=dy
   if moved:
    dfs(moved[-1][0],moved[-1][1],left-len(moved),cnt+1)
    for px,py in moved: a[px][py]='.'
 if empty==1: ans=0
 else:
  for i in range(n):
   for j in range(m):
    if a[i][j]=='.':
     a[i][j]='*'; dfs(i,j,empty-1,0); a[i][j]='.'
 print(f'Case {case}:', ans if ans<10**9 else -1); case+=1
`],
["11780","shortest_path-11780","shortest_path","Floyd 2",`import sys
input=sys.stdin.readline
n=int(input()); m=int(input()); INF=10**12; d=[[INF]*(n+1) for _ in range(n+1)]; nxt=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1): d[i][i]=0
for _ in range(m):
 a,b,c=map(int,input().split())
 if d[a][b]>c: d[a][b]=c; nxt[a][b]=b
for k in range(1,n+1):
 for i in range(1,n+1):
  for j in range(1,n+1):
   if d[i][j]>d[i][k]+d[k][j]: d[i][j]=d[i][k]+d[k][j]; nxt[i][j]=nxt[i][k]
for i in range(1,n+1): print(*[0 if d[i][j]==INF else d[i][j] for j in range(1,n+1)])
for i in range(1,n+1):
 for j in range(1,n+1):
  if i==j or not nxt[i][j]: print(0)
  else:
   path=[i]; cur=i
   while cur!=j: cur=nxt[cur][j]; path.append(cur)
   print(len(path),*path)
`],
["13913","graph_traversal-13913","graph_traversal","Hide and Seek 4",`from collections import deque
n,k=map(int,input().split()); MAX=100000; par=[-2]*(MAX+1); par[n]=-1; q=deque([n])
while q:
 x=q.popleft()
 if x==k: break
 for y in (x-1,x+1,x*2):
  if 0<=y<=MAX and par[y]==-2: par[y]=x; q.append(y)
path=[]; cur=k
while cur!=-1: path.append(cur); cur=par[cur]
path.reverse(); print(len(path)-1); print(*path)
`],
["16939","simulation-16939","simulation","2x2x2 Cube",`a=list(map(int,input().split()))
faces=[(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(16,17,18,19),(20,21,22,23)]
def ok(x): return all(len({x[i] for i in f})==1 for f in faces)
cycles=[(0,2,6,4,16,18,10,8),(1,3,7,5,17,19,11,9),(0,1,9,8,20,21,13,12),(2,3,11,10,22,23,15,14),(4,5,8,10,23,22,14,12),(6,7,9,11,21,20,15,13)]
for cy in cycles:
 for shift in (2,6):
  b=a[:]; vals=[a[i] for i in cy]
  for idx,pos in enumerate(cy): b[pos]=vals[(idx-shift)%8]
  if ok(b): print(1); raise SystemExit
print(0)
`],
["16986","brute_force-16986","brute_force","Insider RSP",`import sys,itertools
input=sys.stdin.readline
n,k=map(int,input().split()); win=[list(map(int,input().split())) for _ in range(n)]; seq=[[],list(map(lambda x:int(x)-1,input().split())),list(map(lambda x:int(x)-1,input().split()))]
def can(order):
 idx=[0,0,0]; score=[0,0,0]; p1,p2=0,1
 while True:
  if score[0]>=k: return True
  if score[1]>=k or score[2]>=k: return False
  if idx[0]>=n: return False
  h1=order[idx[0]] if p1==0 else seq[p1][idx[p1]]
  h2=order[idx[0]] if p2==0 else seq[p2][idx[p2]]
  idx[p1]+=1; idx[p2]+=1
  if win[h1][h2]==2: w=p1
  elif win[h1][h2]==0: w=p2
  else: w=max(p1,p2)
  score[w]+=1; p1,p2=w,3-p1-p2
for order in itertools.permutations(range(n)):
 if can(order): print(1); break
else: print(0)
`],
["18500","simulation-18500","simulation","Mineral 2",`from collections import deque
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
   if 0<=nx<r and 0<=ny<c and a[nx][ny]=='x' and not seen[nx][ny]: seen[nx][ny]=True; q.append((nx,ny))
 cl=[(i,j) for i in range(r) for j in range(c) if a[i][j]=='x' and not seen[i][j]]
 if not cl: return
 for i,j in cl: a[i][j]='.'
 drop=0
 while not any(i+drop+1>=r or a[i+drop+1][j]=='x' for i,j in cl): drop+=1
 for i,j in cl: a[i+drop][j]='x'
for t,h in enumerate(hs):
 row=r-h; rng=range(c) if t%2==0 else range(c-1,-1,-1)
 for j in rng:
  if a[row][j]=='x': a[row][j]='.'; break
 fall()
print('\\n'.join(''.join(row) for row in a))
`],
["18809","simulation-18809","simulation","Gaaaaaaaaaarden",`from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
n,m,g,r=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]; cand=[(i,j) for i in range(n) for j in range(m) if a[i][j]==2]; ans=0
for chosen in combinations(range(len(cand)),g+r):
 for greens in combinations(chosen,g):
  state=[[None]*m for _ in range(n)]; q=deque()
  for idx in chosen:
   x,y=cand[idx]; color=1 if idx in greens else 2; state[x][y]=(0,color); q.append((x,y,0,color))
  flowers=0
  while q:
   x,y,t,c=q.popleft()
   if state[x][y][1]==3: continue
   for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
    nx,ny=x+dx,y+dy
    if 0<=nx<n and 0<=ny<m and a[nx][ny]!=0:
     if state[nx][ny] is None:
      state[nx][ny]=(t+1,c); q.append((nx,ny,t+1,c))
     elif state[nx][ny][0]==t+1 and state[nx][ny][1] not in (c,3):
      state[nx][ny]=(t+1,3); flowers+=1
  ans=max(ans,flowers)
print(ans)
`],
["19581","tree-19581","tree","Second Tree Diameter",`from collections import deque
import sys
input=sys.stdin.readline
n=int(input()); g=[[] for _ in range(n+1)]
for _ in range(n-1):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
def dist(s):
 d=[-1]*(n+1); d[s]=0; q=deque([s])
 while q:
  x=q.popleft()
  for y,w in g[x]:
   if d[y]<0: d[y]=d[x]+w; q.append(y)
 return d
best=[]
for i in range(1,n+1):
 d=dist(i)
 for j in range(i+1,n+1): best.append(d[j])
best.sort(reverse=True); print(best[1])
`],
["19641","tree-19641","tree","Nested Set Model",`import sys
input=sys.stdin.readline
n=int(input()); g=[[] for _ in range(n+1)]
for _ in range(n):
 arr=list(map(int,input().split())); x=arr[0]; g[x]=sorted(v for v in arr[1:] if v!=-1)
root=int(input()); ans={}; t=1
def dfs(x,p):
 global t
 l=t; t+=1
 for y in g[x]:
  if y!=p: dfs(y,x)
 r=t; t+=1; ans[x]=(l,r)
dfs(root,0)
for x in sorted(ans): print(x,*ans[x])
`],
["22861","simulation-22861","simulation","Folder Cleanup Large",`from collections import defaultdict
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); dirs=defaultdict(list); files=defaultdict(list)
for _ in range(n+m):
 p,c,isdir=input().split()
 if isdir=='1': dirs[p].append(c)
 else: files[p].append(c)
def calc(folder):
 kinds=set(files[folder]); total=len(files[folder])
 for child in dirs[folder]:
  k,t=calc(child); kinds|=k; total+=t
 return kinds,total
for _ in range(int(input())):
 q=input().strip().split('/')[-1]; k,t=calc(q); print(len(k),t)
`]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()}); console.log(`[import-manual-batch-35] imported ${slug} (${title})`);}
await fs.writeFile(OUT,JSON.stringify([...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug)),null,2),"utf8");
console.log(`[import-manual-batch-35] wrote ${OUT}`);
