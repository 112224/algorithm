import sys
input = sys.stdin.readline
sys.setrecursionlimit(4000)

from collections import deque

n = int(input())
adj = [[] for _ in range(n+1)]
visit = [0]*n
ans = [0]*n

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append(b)
    adj[b].append(a)


def dfs(idx, pare):
    if visit[idx] == 1:
        return idx
    visit[idx] = 1
    ret = -1
    for ele in adj[idx]:
        if ele != pare:
            ret = dfs(ele, idx)
            if ret == -2:
                return -2
            elif ret >= 0:
                visit[idx] = 2
                return  ret if idx != ret else -2
    return -1


dfs(0,-1)
check = [False] * n
q = deque()
for i in range(n):
    if visit[i] == 2:
        check[i] = True
        q.append(i)
    else:
        ans[i] = -1


while q:
    now = q.popleft()
    for ele in adj[now]:
        if ans[ele] == -1:
            ans[ele] = ans[now] + 1
            q.append(ele)

print(' '.join(map(str, ans)))