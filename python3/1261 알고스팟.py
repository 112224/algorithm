import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(m)]
visit = [[-1]*n for _ in range(m)]

di = [(-1,0),(0,-1),(1,0),(0,1)]
q = deque()
visit[0][0] = 0
q.append((0,0))

while q:
    x, y = q.popleft()
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0<=nx<m and 0<=ny<n:
            if visit[nx][ny] == -1:
                if maze[nx][ny] == '0':
                    visit[nx][ny] = visit[x][y]
                    q.appendleft((nx,ny))
                else:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))

print(visit[m-1][n-1])