input = __import__('sys').stdin.readline
from collections import deque

tc = int(input())
for _ in range(tc):
    visit = [[False] * 401 for _ in range(401)]
    s, t = map(int, input().split())
    q = deque()
    visit[s][t] = 0
    q.append((s, t))
    while q:
        ns, nt = q.popleft()
        if ns == nt:
            print(visit[ns][nt])
            break
        if 0<= ns * 2 <= 400 and 0 <= nt + 3 <= 400 and not visit[ns*2][nt + 3]:
            visit[ns*2][nt+3] = visit[ns][nt] + 1
            q.append((ns*2, nt + 3))
        if 0 <= ns + 1 <= 100 and not visit[ns+1][nt]:
            visit[ns+1][nt] = visit[ns][nt] + 1
            q.append((ns + 1, nt))