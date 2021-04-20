import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])

global ans
ans = 0

''' postorder 순회로 구현 -> recursion error로 실패
def dfs(now):
    global ans
    vals = []
    visit[now] = True
    for ele in adj[now]:
        if not visit[ele[0]]:
            vals.append(dfs(ele[0])+ele[1])
    if vals:
        vals.sort(reverse=True)
        if len(vals)>=2:
            ans = max(ans, vals[0]+vals[1])
        return vals[0]
    else:
        return 0


dfs(1)
print(ans)'''
def bfs(root):
    visit = [False] * (n+1)
    visit[root] = True
    q = deque()
    q.append((root,0))
    ret, idx = 0, 0
    while q:
        now = q.popleft()

        for ele in adj[now[0]]:
            if not visit[ele[0]]:
                visit[ele[0]] = True
                q.append((ele[0], ele[1] + now[1]))
                if ret < ele[1] + now[1]:
                    ret = ele[1] + now[1]
                    idx = ele[0]

    return ret, idx


t1, t2 = bfs(1)
print(bfs(t2)[0])