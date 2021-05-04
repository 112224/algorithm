import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

b = list(map(int, input().split()))
pri = [0]*(n+1)
for i in range(1,n+1):
    pri[b[i-1]] = i
for ele in adj:
    ele.sort(key = lambda x: pri[x])
visit = [False]*(n+1)
q = deque()
q.append(1)
visit[1] = True
ret = []
while q:
    x = q.popleft()
    ret.append(x)
    for ele in adj[x]:
        if not visit[ele]:
            visit[ele] = True
            q.append(ele)

ans = 1
for i,j in zip(b,ret):
    if i!=j:
        ans = 0
        break
print(ans)