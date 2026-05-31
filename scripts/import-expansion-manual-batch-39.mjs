import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
const __filename=fileURLToPath(import.meta.url), __dirname=path.dirname(__filename), ROOT=path.resolve(__dirname,".."), OUT=path.join(ROOT,"data","problems-extra.json");
const TROMINO=`import sys
input=sys.stdin.readline
k=int(input()); x,y=map(int,input().split())
n=2**k; board=[[0]*n for _ in range(n)]; board[n-y][x-1]=-1; tile=0
def cover(r,c,size,hr,hc):
 global tile
 if size==1: return
 half=size//2; tile+=1; t=tile
 mids=[(r+half-1,c+half-1),(r+half-1,c+half),(r+half,c+half-1),(r+half,c+half)]
 q=(0 if hr<r+half else 2)+(0 if hc<c+half else 1)
 for i,(mr,mc) in enumerate(mids):
  if i!=q: board[mr][mc]=t
 holes=mids[:]; holes[q]=(hr,hc)
 cover(r,c,half,*holes[0]); cover(r,c+half,half,*holes[1])
 cover(r+half,c,half,*holes[2]); cover(r+half,c+half,half,*holes[3])
cover(0,0,n,n-y,x-1)
print("\\n".join(" ".join(map(str,row)) for row in board))
`;
const FROG=`from itertools import permutations
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
frogs=[()]+[tuple(map(int,input().split())) for _ in range(n)]
pref=[set()]
for _ in range(n): pref.append(set(map(int,input().split())))
logs=[tuple(map(int,input().split())) for _ in range(m)]
for arr in permutations(range(1,n+1)):
 if all(i+1 in pref[f] for i,f in enumerate(arr)) and all(frogs[arr[a-1]][t-1]==frogs[arr[b-1]][t-1] for a,b,t in logs):
  print("YES"); print(*arr); break
else:
 print("NO")
`;
const MARBLE=`from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split()); board=[list(input().strip()) for _ in range(n)]
R=B=(-1,-1)
for i in range(n):
 for j in range(m):
  if board[i][j]=='R': R=(i,j); board[i][j]='.'
  elif board[i][j]=='B': B=(i,j); board[i][j]='.'
dirs=[(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
def roll(pos,d):
 r,c=pos; dr,dc=d; cnt=0
 while board[r+dr][c+dc]!='#':
  r+=dr; c+=dc; cnt+=1
  if board[r][c]=='O': return (r,c),cnt,True
 return (r,c),cnt,False
q=deque([(R,B,"")]); seen={(R,B)}
while q:
 r,b,path=q.popleft()
 if len(path)>=10: continue
 for dr,dc,ch in dirs:
  nr,rc,rh=roll(r,(dr,dc)); nb,bc,bh=roll(b,(dr,dc))
  if bh: continue
  if rh:
   print(len(path)+1); print(path+ch); raise SystemExit
  if nr==nb:
   if rc>bc: nr=(nr[0]-dr,nr[1]-dc)
   else: nb=(nb[0]-dr,nb[1]-dc)
  state=(nr,nb)
  if state not in seen:
   seen.add(state); q.append((nr,nb,path+ch))
print(-1)
`;
const MONKEY=`n=int(input())
for bit in range(7):
 print(''.join('A' if ((i>>bit)&1)==0 else 'B' for i in range(n)))
`;
const PROBLEMS=[
["14600","divide_and_conquer-14600","divide_and_conquer","Shower Floor Tiling Small",TROMINO],
["14601","divide_and_conquer-14601","divide_and_conquer","Shower Floor Tiling Large",TROMINO],
["15566","backtracking-15566","backtracking","Frog 1",FROG],
["15644","simulation-15644","simulation","Marble Escape 3",MARBLE],
["16438","divide_and_conquer-16438","divide_and_conquer","Monkey Sports",MONKEY]
];
async function readJson(file,fallback){try{return JSON.parse(await fs.readFile(file,"utf8"));}catch{return fallback;}}
function stableHash(value){return createHash("sha1").update(value).digest("hex").slice(0,12);}
const existing=await readJson(OUT,[]), bySlug=new Map(existing.map(p=>[p.slug,p]));
for(const [id,slug,categorySlug,title,code] of PROBLEMS){bySlug.set(slug,{id,slug,categorySlug,sources:[{lang:"python",file:`local/oracle/${slug}.py`,code}],link:`https://www.acmicpc.net/problem/${id}`,authors:["dongjun"],hash:stableHash(`extra:${slug}`),createdAt:Date.now()}); console.log(`[import-manual-batch-39] imported ${slug} (${title})`);}
await fs.writeFile(OUT,JSON.stringify([...bySlug.values()].sort((a,b)=>Number(a.id)-Number(b.id)||a.slug.localeCompare(b.slug)),null,2),"utf8");
console.log(`[import-manual-batch-39] wrote ${OUT}`);
