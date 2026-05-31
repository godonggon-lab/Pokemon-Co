import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const PROBLEMS=[
["1729","backtracking-1729","backtracking","Interesting Numbers",`n=int(input())
def s(x): return sum(map(int,str(x)))
print(sum(1 for i in range(1,n+1) if i%s(i)==0))
`],
["2058","dynamic_programming_on_trees-2058","dynamic_programming_on_trees","Atomic Energy",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); states=[int(input()) for _ in range(n)]; e=[int(input()) for _ in range(m)]
S=set(states); g={x:[] for x in states}
for x in states:
 for d in e:
  for y in (x-d,x+d):
   if y in S: g[x].append(y)
seen=set()
def dfs(x):
 seen.add(x); take=x; skip=0
 for y in g[x]:
  if y not in seen:
   a,b=dfs(y); take+=b; skip+=max(a,b)
 return take,skip
ans=0
for x in states:
 if x not in seen:
  ans+=max(dfs(x))
print(ans)
`],
["4315","tree-4315","tree","Marbles on a Tree",`import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
outs=[]
while True:
 n=int(input())
 if n==0: break
 g=[[] for _ in range(n+1)]; mar=[0]*(n+1)
 for _ in range(n):
  row=list(map(int,input().split()))
  node,m,k=row[:3]; mar[node]=m
  for c in row[3:]:
   g[node].append(c); g[c].append(node)
 ans=0
 def dfs(x,p):
  global ans
  bal=mar[x]-1
  for y in g[x]:
   if y!=p:
    b=dfs(y,x); ans+=abs(b); bal+=b
  return bal
 dfs(1,0); outs.append(str(ans))
print("\\n".join(outs))
`],
["4933","tree-4933","tree","Newton's Apple",`import sys
input=sys.stdin.readline
def parse(tokens,idx):
 val=tokens[idx]; idx-=1
 if val=="nil": return ("nil",),idx
 right,idx=parse(tokens,idx)
 left,idx=parse(tokens,idx)
 kids=sorted([left,right])
 return (val,tuple(kids)),idx
t=int(input()); out=[]
for _ in range(t):
 a=input().split(); b=input().split()
 if len(a)!=len(b): out.append("false"); continue
 ta,_=parse(a,len(a)-1); tb,_=parse(b,len(b)-1)
 out.append("true" if ta==tb else "false")
print("\\n".join(out))
`],
["10421","backtracking-10421","backtracking","Complete the Formula",`import itertools,sys
input=sys.stdin.readline
n=int(input()); s=list(map(int,input().split())); k=int(input()); digs=list(map(str,input().split()))
def ok(num,ln):
 st=str(num)
 return len(st)==ln and all(ch in digs for ch in st)
ans=0
for a in map(lambda x:int(''.join(x)), itertools.product(digs, repeat=s[0])):
 for b in map(lambda x:int(''.join(x)), itertools.product(digs, repeat=s[1])):
  bs=str(b)[::-1]
  if all(ok(a*int(bs[i]),s[2+i]) for i in range(s[1])) and ok(a*b,s[-1]):
   ans+=1
print(ans)
`],
["12912","tree-12912","tree","Tree Modification",`import sys
input=sys.stdin.readline
n=int(input()); g=[{} for _ in range(n)]; edges=[]
for _ in range(n-1):
 a,b,w=map(int,input().split()); g[a][b]=w; g[b][a]=w; edges.append((a,b,w))
def diameter_sum():
 vis=[0]*n; total=0
 def far(st,tag):
  stack=[(st,0)]; vis[st]+=1; best=(st,0)
  while stack:
   x,d=stack.pop()
   if d>best[1]: best=(x,d)
   for y,w in g[x].items():
    if vis[y]==tag:
     vis[y]+=1; stack.append((y,d+w))
  return best
 for i in range(n):
  if vis[i]==0:
   a,_=far(i,0); _,d=far(a,1); total+=d
 return total
ans=diameter_sum()
for a,b,w in edges:
 del g[a][b]; del g[b][a]
 ans=max(ans,diameter_sum()+w)
 g[a][b]=w; g[b][a]=w
print(ans)
`],
["12978","dynamic_programming_on_trees-12978","dynamic_programming_on_trees","Scrooge Minho 2",`import sys
input=sys.stdin.readline
sys.setrecursionlimit(300000)
n=int(input()); g=[[] for _ in range(n+1)]
for _ in range(n-1):
 a,b=map(int,input().split()); g[a].append(b); g[b].append(a)
def dfs(x,p):
 take=1; skip=0
 for y in g[x]:
  if y!=p:
   a,b=dfs(y,x); take+=min(a,b); skip+=a
 return take,skip
print(min(dfs(1,0)))
`],
["14945","dynamic_programming_2-14945","dynamic_programming_2","Playing with Fire",`MOD=10007
n=int(input())
if n==1: print(0); raise SystemExit
dp=[[0]*(n+2) for _ in range(n+1)]
dp[2][1]=2
for i in range(3,n+1):
 for d in range(1,i):
  dp[i][d]=(dp[i-1][d]*2+dp[i-1][d-1]+dp[i-1][d+1])%MOD
print(sum(dp[n][1:n])%MOD)
`],
["15779","brute_force-15779","brute_force","Zigzag",`n=int(input()); a=list(map(int,input().split()))
if n<=2: print(n); raise SystemExit
best=cur=2
for i in range(n-2):
 if (a[i]<=a[i+1]<=a[i+2]) or (a[i]>=a[i+1]>=a[i+2]): cur=2
 else: cur+=1
 best=max(best,cur)
print(best)
`],
["20162","dynamic_programming_1-20162","dynamic_programming_1","Snack Party",`n=int(input()); a=[int(input()) for _ in range(n)]
dp=a[:]; ans=0
for i in range(n):
 ans=max(ans,dp[i])
 for j in range(i+1,n):
  if a[i]<a[j]: dp[j]=max(dp[j],dp[i]+a[j])
print(ans)
`],
["20667","dynamic_programming_2-20667","dynamic_programming_2","Chrome",`import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); tabs=[tuple(map(int,input().split())) for _ in range(n)]
INF=-10**18; dp=[[INF]*501 for _ in range(m+1)]; dp[0][0]=0
for cpu,mem,imp in tabs:
 nd=[row[:] for row in dp]
 for c in range(m+1):
  for p in range(501-imp):
   if dp[c][p]!=INF:
    nc=min(m,c+cpu); nd[nc][p+imp]=max(nd[nc][p+imp],dp[c][p]+mem)
 dp=nd
for p,v in enumerate(dp[m]):
 if v>=k: print(p); break
else: print(-1)
`],
["21279","two_pointer-21279","two_pointer","Miner Hoseok",`import sys
input=sys.stdin.readline
n,c=map(int,input().split()); pts=[tuple(map(int,input().split())) for _ in range(n)]
xs=sorted(set([0]+[x for x,_,_ in pts])); ys=sorted(set([0]+[y for _,y,_ in pts])); ans=0
for X in xs:
 for Y in ys:
  inside=[v for x,y,v in pts if x<=X and y<=Y]
  if len(inside)<=c: ans=max(ans,sum(inside))
print(ans)
`]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()}); console.log(`[import-manual-batch-38] imported ${slug} (${title})`);}
await fs.writeFile(OUT,JSON.stringify([...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug)),null,2),"utf8");
console.log(`[import-manual-batch-38] wrote ${OUT}`);
