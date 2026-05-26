import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const PROBLEMS=[
["5569","dynamic_programming_2-5569","dynamic_programming_2","Commute Route",`import sys
w,h=map(int,sys.stdin.readline().split()); MOD=100000
dp=[[[[0]*2 for _ in range(2)] for __ in range(w+1)] for ___ in range(h+1)]
for x in range(2,w+1): dp[1][x][0][0]=1
for y in range(2,h+1): dp[y][1][1][0]=1
for y in range(1,h+1):
 for x in range(1,w+1):
  if y==1 or x==1: continue
  dp[y][x][0][0]=(dp[y][x-1][0][0]+dp[y][x-1][0][1])%MOD
  dp[y][x][0][1]=dp[y][x-1][1][0]
  dp[y][x][1][0]=(dp[y-1][x][1][0]+dp[y-1][x][1][1])%MOD
  dp[y][x][1][1]=dp[y-1][x][0][0]
print(sum(dp[h][w][d][t] for d in range(2) for t in range(2))%MOD)
`],
["6987","backtracking-6987","backtracking","World Cup",`import sys
games=[(i,j) for i in range(6) for j in range(i+1,6)]
def possible(arr,idx=0):
 if idx==15: return all(x==0 for row in arr for x in row)
 a,b=games[idx]
 for ra,rb in ((0,2),(1,1),(2,0)):
  if arr[a][ra] and arr[b][rb]:
   arr[a][ra]-=1; arr[b][rb]-=1
   if possible(arr,idx+1): return True
   arr[a][ra]+=1; arr[b][rb]+=1
 return False
nums=list(map(int,sys.stdin.read().split())); out=[]
for k in range(0,len(nums),18):
 arr=[nums[k+i*3:k+i*3+3] for i in range(6)]
 out.append('1' if sum(map(sum,arr))==30 and possible(arr) else '0')
print(' '.join(out))
`],
["2922","string-2922","string","Joyful Word",`import sys
s=sys.stdin.readline().strip(); vowels=set('AEIOU')
from functools import lru_cache
@lru_cache(None)
def dfs(i,v,c,has_l):
 if v>=3 or c>=3: return 0
 if i==len(s): return 1 if has_l else 0
 ch=s[i]; ans=0
 choices=[]
 if ch=='_': choices=[('A',5),('B',20),('L',1)]
 else: choices=[(ch,1)]
 for x,m in choices:
  if x in vowels: ans+=m*dfs(i+1,v+1,0,has_l or x=='L')
  else: ans+=m*dfs(i+1,0,c+1,has_l or x=='L')
 return ans
print(dfs(0,0,0,False))
`],
["16432","graph_traversal-16432","graph_traversal","Rice Cake Tiger",`import sys
input=sys.stdin.readline
n=int(input()); days=[]
for _ in range(n):
 data=list(map(int,input().split())); days.append(data[1:])
path=[]
def dfs(d,prev):
 if d==n: return True
 for x in days[d]:
  if x!=prev:
   path.append(x)
   if dfs(d+1,x): return True
   path.pop()
 return False
print('\\n'.join(map(str,path)) if dfs(0,0) else -1)
`],
["16571","backtracking-16571","backtracking","Tic Tac Toe",`import sys
b=[list(map(int,sys.stdin.readline().split())) for _ in range(3)]
def win(p):
 lines=b+[[b[i][j] for i in range(3)] for j in range(3)]+[[b[i][i] for i in range(3)], [b[i][2-i] for i in range(3)]]
 return any(all(x==p for x in line) for line in lines)
turn=1 if sum(r.count(1) for r in b)==sum(r.count(2) for r in b) else 2
def solve(p):
 if win(3-p): return -1
 best=-2; moved=False
 for i in range(3):
  for j in range(3):
   if b[i][j]==0:
    moved=True; b[i][j]=p; best=max(best,-solve(3-p)); b[i][j]=0
 return 0 if not moved else best
r=solve(turn); print('W' if r==1 else ('L' if r==-1 else 'D'))
`],
["17136","backtracking-17136","backtracking","Colored Paper",`import sys
a=[list(map(int,sys.stdin.readline().split())) for _ in range(10)]
left=[0,5,5,5,5,5]; ans=26
def can(x,y,s):
 return x+s<=10 and y+s<=10 and all(a[i][j] for i in range(x,x+s) for j in range(y,y+s))
def fill(x,y,s,v):
 for i in range(x,x+s):
  for j in range(y,y+s): a[i][j]=v
def dfs(cnt):
 global ans
 if cnt>=ans: return
 pos=None
 for i in range(10):
  for j in range(10):
   if a[i][j]: pos=(i,j); break
  if pos: break
 if not pos: ans=min(ans,cnt); return
 x,y=pos
 for s in range(5,0,-1):
  if left[s] and can(x,y,s):
   left[s]-=1; fill(x,y,s,0); dfs(cnt+1); fill(x,y,s,1); left[s]+=1
dfs(0); print(ans if ans<26 else -1)
`],
["17141","graph_traversal-17141","graph_traversal","Laboratory 2",`from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); g=[list(map(int,input().split())) for _ in range(n)]
vir=[(i,j) for i in range(n) for j in range(n) if g[i][j]==2]; blanks=sum(g[i][j]==0 for i in range(n) for j in range(n))
INF=10**9; ans=INF
for comb in combinations(vir,m):
 d=[[-1]*n for _ in range(n)]; q=deque(comb)
 for x,y in comb: d[x][y]=0
 mx=0; seen=0
 while q:
  x,y=q.popleft()
  if g[x][y]==0: seen+=1; mx=max(mx,d[x][y])
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
   nx,ny=x+dx,y+dy
   if 0<=nx<n and 0<=ny<n and g[nx][ny]!=1 and d[nx][ny]==-1:
    d[nx][ny]=d[x][y]+1; q.append((nx,ny))
 if seen==blanks: ans=min(ans,mx)
print(ans if ans<INF else -1)
`],
["17255","data_structure2-17255","data_structure2","N으로 만들기",`import sys
s=sys.stdin.readline().strip(); seen=set()
def dfs(l,r,path):
 if l==0 and r==len(s)-1: seen.add(path); return
 if l>0: dfs(l-1,r,path+' '+s[l-1:r+1])
 if r+1<len(s): dfs(l,r+1,path+' '+s[l:r+2])
for i in range(len(s)): dfs(i,i,s[i])
print(len(seen))
`],
["19585","trie-19585","trie","Legend",`import sys
input=sys.stdin.readline
c,n=map(int,input().split()); colors={input().strip() for _ in range(c)}; names={input().strip() for _ in range(n)}
out=[]
for _ in range(int(input())):
 s=input().strip(); ok=False
 for i in range(1,len(s)):
  if s[:i] in colors and s[i:] in names: ok=True; break
 out.append('Yes' if ok else 'No')
print('\\n'.join(out))
`],
["19645","dynamic_programming_2-19645","dynamic_programming_2","Ham Choi",`import sys
n=int(sys.stdin.readline()); a=list(map(int,sys.stdin.readline().split())); s=sum(a)
dp={(0,0)}
for x in a:
 ndp=set(dp)
 for p,q in dp:
  ndp.add((p+x,q)); ndp.add((p,q+x))
 dp=ndp
print(max(min(p,q,s-p-q) for p,q in dp if p+q<=s))
`],
["20166","trie-20166","trie","String Hell",`from collections import defaultdict
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split()); g=[input().strip() for _ in range(n)]
queries=[input().strip() for _ in range(k)]; maxlen=max(map(len,queries)); cnt=defaultdict(int)
def dfs(x,y,s):
 cnt[s]+=1
 if len(s)==maxlen: return
 for dx in (-1,0,1):
  for dy in (-1,0,1):
   if dx or dy:
    nx=(x+dx)%n; ny=(y+dy)%m; dfs(nx,ny,s+g[nx][ny])
for i in range(n):
 for j in range(m): dfs(i,j,g[i][j])
print('\\n'.join(str(cnt[q]) for q in queries))
`],
["20208","backtracking-20208","backtracking","Mint Choco Milk",`from itertools import permutations
import sys
input=sys.stdin.readline
n,m,h=map(int,input().split()); milk=[]; home=None
for i in range(n):
 row=list(map(int,input().split()))
 for j,v in enumerate(row):
  if v==1: home=(i,j)
  elif v==2: milk.append((i,j))
ans=0
for order in permutations(milk):
 hp=m; x,y=home; cnt=0
 for nx,ny in order:
  d=abs(x-nx)+abs(y-ny)
  if hp<d: break
  hp=hp-d+h; x,y=nx,ny; cnt+=1
  if hp>=abs(x-home[0])+abs(y-home[1]): ans=max(ans,cnt)
print(ans)
`],
["20442","two_pointer-20442","two_pointer","ㅋㅋ루ㅋㅋ",`import sys
s=sys.stdin.readline().strip(); pos=[i for i,ch in enumerate(s) if ch=='R']
pref=[0]
for ch in s: pref.append(pref[-1]+(ch=='K'))
ans=min(pref[-1]*2+0,0)
l=0; r=len(pos)-1
while l<=r:
 k=min(pref[pos[l]], pref[len(s)]-pref[pos[r]+1])
 ans=max(ans, r-l+1+2*k)
 if pref[pos[l]] < pref[len(s)]-pref[pos[r]+1]: l+=1
 else: r-=1
print(ans)
`],
["20542","dynamic_programming_2-20542","dynamic_programming_2","Dictation",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=input().strip(); b=input().strip()
def same(x,y): return x==y or (x in 'ij' and y in 'ij') or (x in 'vl' and y in 'vl')
dp=[[10**9]*(m+1) for _ in range(n+1)]
for i in range(n+1): dp[i][0]=i
for j in range(m+1): dp[0][j]=j
for i in range(1,n+1):
 for j in range(1,m+1):
  dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if same(a[i-1],b[j-1]) else 1))
print(dp[n][m])
`],
["21922","simulation-21922","simulation","Undergraduate Researcher Minsang",`import sys
input=sys.stdin.readline
n,m=map(int,input().split()); a=[list(map(int,input().split())) for _ in range(n)]
seen=[[[False]*4 for _ in range(m)] for __ in range(n)]; cell=[[False]*m for _ in range(n)]
dirs=[(-1,0),(0,1),(1,0),(0,-1)]
def ndir(d,t):
 if t==1: return {0:2,2:0}.get(d,d)
 if t==2: return {1:3,3:1}.get(d,d)
 if t==3: return [1,0,3,2][d]
 if t==4: return [3,2,1,0][d]
 return d
for i in range(n):
 for j in range(m):
  if a[i][j]==9:
   for d in range(4):
    x,y,cd=i,j,d
    while 0<=x<n and 0<=y<m and not seen[x][y][cd]:
     seen[x][y][cd]=True; cell[x][y]=True; cd=ndir(cd,a[x][y]); dx,dy=dirs[cd]; x+=dx; y+=dy
print(sum(map(sum,cell)))
`],
["21925","dynamic_programming_2-21925","dynamic_programming_2","Even Palindrome",`import sys
input=sys.stdin.readline
n=int(input()); a=list(map(int,input().split()))
pal=[[False]*n for _ in range(n)]
for l in range(n):
 for r in range(l,n):
  if (r-l+1)%2==0 and a[l:r+1]==a[l:r+1][::-1]: pal[l][r]=True
dp=[-10**9]*(n+1); dp[0]=0
for i in range(n):
 if dp[i]<0: continue
 for j in range(i+1,n,2):
  if pal[i][j]: dp[j+1]=max(dp[j+1],dp[i]+1)
print(dp[n] if dp[n]>=0 else -1)
`],
["21938","graph_traversal-21938","graph_traversal","Image Processing",`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); img=[]
for _ in range(n):
 data=list(map(int,input().split())); img.append([sum(data[i*3:i*3+3])/3 for i in range(m)])
t=int(input()); b=[[v>=t for v in row] for row in img]; ans=0
for i in range(n):
 for j in range(m):
  if b[i][j]:
   ans+=1; b[i][j]=False; q=deque([(i,j)])
   while q:
    x,y=q.popleft()
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy
     if 0<=nx<n and 0<=ny<m and b[nx][ny]: b[nx][ny]=False; q.append((nx,ny))
print(ans)
`],
["21941","dynamic_programming_2-21941","dynamic_programming_2","String Removal",`import sys
input=sys.stdin.readline
s=input().strip(); n=int(input()); bonus=[input().split() for _ in range(n)]; bonus=[(a,int(b)) for a,b in bonus]
dp=[0]*(len(s)+1)
for i in range(len(s)):
 dp[i+1]=max(dp[i+1],dp[i]+1)
 for pat,score in bonus:
  if s.startswith(pat,i): dp[i+len(pat)]=max(dp[i+len(pat)],dp[i]+score)
print(dp[-1])
`],
["21943","brute_force-21943","brute_force","Operation Maximum",`from itertools import permutations
import sys
input=sys.stdin.readline
n=int(input()); nums=list(map(int,input().split())); p,q=map(int,input().split())
groups=q+1; ans=0
def dfs(idx,sums):
 global ans
 if idx==n:
  prod=1
  for x in sums: prod*=x
  ans=max(ans,prod); return
 for i in range(groups):
  sums[i]+=nums[idx]; dfs(idx+1,sums); sums[i]-=nums[idx]
dfs(0,[0]*groups); print(ans)
`],
["22945","binary_search-22945","binary_search","Team Building",`import sys
input=sys.stdin.readline
n=int(input()); a=list(map(int,input().split())); l=0; r=n-1; ans=0
while l<r:
 ans=max(ans,(r-l-1)*min(a[l],a[r]))
 if a[l]<a[r]: l+=1
 else: r-=1
print(ans)
`]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){
 bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()});
 console.log(`[import-manual-batch-31] imported ${slug} (${title})`);
}
const problems=[...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug));
await fs.writeFile(OUT,JSON.stringify(problems,null,2),"utf8");
console.log(`[import-manual-batch-31] wrote ${OUT}`);
