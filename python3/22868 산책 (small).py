import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
visit = [False] * n
prev = [-1] * n
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append(b)
    adj[b].append(a)

for i in range(n):
    adj[i].sort()

s, e = map(int, input().split())
s, e = s-1, e-1

answer = []

def bfs(s, e, visit):
    visit[s] = True
    prev[s] = s
    q = deque()
    q.append((s, 0))
    while q:
        cur, cnt = q.popleft()

        for ele in adj[cur]:
            if not visit[ele]:
                prev[ele] = cur
                if ele == e:
                    return cnt + 1
                visit[ele] = True
                q.append((ele, cnt + 1))

answer.append(bfs(s, e, visit))
back_visit = [False] * n
val = e
while prev[val] != val:
    back_visit[val] = True
    val = prev[val]
answer.append(bfs(e, s, back_visit))
print(answer[0] + answer[1])
