import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

tmp_ans = list(map(int, input().split()))

level = [0] * (n+1)
visit = [False]*(n+1)
ans = []
q = deque()
visit[1] = True
q.append(1)

while q:
    now = q.popleft()
    ans.append(now)

    for ele in adj[now]:
        if not visit[ele]:
            visit[ele] = True
            level[ele] = level[now] + 1
            q.append(ele)

ret = 1
for i, j in zip(ans, tmp_ans):
    if level[i] != level[j]:
        ret = 0
        break
print(ret)