import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const PROBLEMS=[
["1045","minimum_spanning_tree-1045","minimum_spanning_tree","Road",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=[input().strip() for _ in range(n)]
edges=[(i,j) for i in range(n) for j in range(i+1,n) if a[i][j]=='Y']
if len(edges)<m: print(-1); sys.exit()
p=list(range(n)); deg=[0]*n; chosen=[]
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
for i,j in edges:
 ri,rj=f(i),f(j)
 if ri!=rj:
  p[rj]=ri; deg[i]+=1; deg[j]+=1; chosen.append((i,j))
if len(chosen)!=n-1 or m<n-1: print(-1); sys.exit()
used=set(chosen)
for e in edges:
 if len(chosen)==m: break
 if e not in used:
  i,j=e; deg[i]+=1; deg[j]+=1; chosen.append(e)
print(*deg)
`],
["1301","dynamic_programming_2-1301","dynamic_programming_2","Bead Craft",`from functools import lru_cache
import sys
input=sys.stdin.readline
n=int(input()); cnt=[int(input()) for _ in range(n)]
@lru_cache(None)
def dp(state,last1,last2):
 if sum(state)==0: return 1
 res=0; st=list(state)
 for i in range(n):
  if st[i] and i!=last1 and i!=last2:
   st[i]-=1; res+=dp(tuple(st),i,last1); st[i]+=1
 return res
print(dp(tuple(cnt),-1,-1))
`],
["1469","backtracking-1469","backtracking","Shom Sequence",`import sys
n=int(input()); nums=sorted(map(int,input().split())); arr=[-1]*(2*n); ans=None
def dfs(idx):
 global ans
 if ans is not None: return
 if idx==n: ans=arr[:]; return
 x=nums[idx]
 for i in range(2*n-x-1):
  j=i+x+1
  if arr[i]==arr[j]==-1:
   arr[i]=arr[j]=x; dfs(idx+1); arr[i]=arr[j]=-1
dfs(0)
print(-1 if ans is None else ' '.join(map(str,ans)))
`],
["2211","shortest_path-2211","shortest_path","Network Recovery",`import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b,c=map(int,input().split()); g[a].append((b,c)); g[b].append((a,c))
d=[10**18]*(n+1); par=[0]*(n+1); d[1]=0; pq=[(0,1)]
while pq:
 c,x=heapq.heappop(pq)
 if c!=d[x]: continue
 for y,w in g[x]:
  if d[y]>c+w:
   d[y]=c+w; par[y]=x; heapq.heappush(pq,(d[y],y))
print(n-1)
for i in range(2,n+1): print(i,par[i])
`],
["2233","tree-2233","tree","Apple Tree",`import sys
input=sys.stdin.readline
n=int(input()); s=input().strip(); x,y=map(int,input().split())
parent=[0]*(n+1); depth=[0]*(n+1); interval=[[0,0] for _ in range(n+1)]
cur=0; last=0
for i,ch in enumerate(s,1):
 if ch=='0':
  last+=1; parent[last]=cur; depth[last]=depth[cur]+1; cur=last; interval[last][0]=i
 else:
  interval[cur][1]=i; cur=parent[cur]
a=b=0
for i in range(1,n+1):
 if x in interval[i]: a=i
 if y in interval[i]: b=i
while depth[a]>depth[b]: a=parent[a]
while depth[b]>depth[a]: b=parent[b]
while a!=b: a=parent[a]; b=parent[b]
print(*interval[a])
`],
["2374","divide_and_conquer-2374","divide_and_conquer","Make Same Number",`import sys
input=sys.stdin.readline
n=int(input()); a=[int(input()) for _ in range(n)]
def solve(l,r,base):
 if l>r: return 0
 mx=max(a[l:r+1]); idx=a.index(mx,l,r+1); res=mx-base
 res+=solve(l,idx-1,mx)+solve(idx+1,r,mx)
 return res
print(solve(0,n-1,0))
`],
["2406","minimum_spanning_tree-2406","minimum_spanning_tree","Stable Network",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); p=list(range(n+1))
def f(x):
 while p[x]!=x: p[x]=p[p[x]]; x=p[x]
 return x
for _ in range(m):
 a,b=map(int,input().split()); p[f(b)]=f(a)
w=[list(map(int,input().split())) for _ in range(n)]
edges=[(w[i-1][j-1],i,j) for i in range(2,n+1) for j in range(i+1,n+1)]
ans=[]; cost=0
for c,i,j in sorted(edges):
 ri,rj=f(i),f(j)
 if ri!=rj: p[rj]=ri; cost+=c; ans.append((i,j))
print(cost,len(ans))
for i,j in ans: print(i,j)
`],
["3165","backtracking-3165","backtracking","Five",`n,k=map(int,input().split()); x=n+1
while str(x).count('5')<k: x+=1
print(x)
`],
["13902","dynamic_programming_2-13902","dynamic_programming_2","Opening 2",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); wok=list(map(int,input().split())); sizes=set(wok)
for i in range(m):
 for j in range(i+1,m): sizes.add(wok[i]+wok[j])
INF=10**9; dp=[INF]*(n+1); dp[0]=0
for i in range(1,n+1):
 for s in sizes:
  if i>=s: dp[i]=min(dp[i],dp[i-s]+1)
print(-1 if dp[n]==INF else dp[n])
`],
["15918","backtracking-15918","backtracking","Langford Sequence",`import sys
n,x,y=map(int,input().split()); arr=[0]*(2*n+1); fixed=y-x-1; arr[x]=arr[y]=fixed; used=[False]*(n+1); used[fixed]=True; ans=0
def dfs(num):
 global ans
 while num<=n and used[num]: num+=1
 if num>n: ans+=1; return
 for i in range(1,2*n-num):
  j=i+num+1
  if j<=2*n and arr[i]==arr[j]==0:
   arr[i]=arr[j]=num; used[num]=True; dfs(num+1); used[num]=False; arr[i]=arr[j]=0
dfs(1); print(ans)
`]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()}); console.log(`[import-manual-batch-36] imported ${slug} (${title})`);}
await fs.writeFile(OUT,JSON.stringify([...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug)),null,2),"utf8");
console.log(`[import-manual-batch-36] wrote ${OUT}`);
