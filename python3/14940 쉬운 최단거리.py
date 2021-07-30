import sys
input = sys.stdin.readline
from collections import deque
di = [(0,1),(1,0),(0,-1),(-1,0)]
n, m = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
st = -1,-1

for i in range(n):
    for j in range(m):
        if ary[i][j] == 2:
            st = (i,j)
            dist[i][j] = 0
        elif ary[i][j] == 0:
            dist[i][j] = 0

q = deque()
q.append(st)

while q:
    x, y = q.popleft()
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0<=nx<n and 0<=ny<m:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for ele in dist:
    print(' '.join(map(str, ele)))