import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = 0
visit = [False]*(n+1)
while True:
    q = deque()
    flag = False
    for i in range(1,n+1):
        if not visit[i]:
            visit[i] = True
            q.append(i)
            flag = True
            break

    while q:
        now = q.popleft()
        for ele in adj[now]:
            if not visit[ele]:
                visit[ele] = True
                q.append(ele)

    if not flag:
        break
    else:
        ans += 1
print(ans)