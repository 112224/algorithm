import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

n = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

b = list(map(int, input().split()))
pri = [0]*(n+1)
for i in range(1,n+1):
    pri[b[i-1]]= i
for ele in adj:
    ele.sort(key= lambda x: pri[x])

ret = []
visit = [False]*(n+1)
visit[1] = True
def dfs(n):
    ret.append(n)
    for ele in adj[n]:
        if not visit[ele]:
            visit[ele] = True
            dfs(ele)
dfs(1)

ans = 1
for i,j in zip(ret, b):
    if i!=j:
        ans = 0
        break
print(ans)