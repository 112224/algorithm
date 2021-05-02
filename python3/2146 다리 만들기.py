import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
di = [(0,1),(1,0),(0,-1),(-1,0)]

tja = []
for i in range(n):
    for j in range(n):
        if land[i][j] == 1 and not visit[i][j]:
            visit[i][j] = True
            ret = []
            q = deque()
            q.append((i,j))
            while q:
                x,y = q.popleft()
                ret.append((x,y))

                for dx, dy in di:
                    nx, ny, = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if not visit[nx][ny] and land[nx][ny] == 1:
                            visit[nx][ny] = True
                            q.append((nx,ny))
            tja.append(ret)
m = len(tja)
ans = 10000
for i in range(m):
    for j in range(i+1, m):
        ele1, ele2 = tja[i], tja[j]
        for e1 in ele1:
            for e2 in ele2:
                ans = min(ans, abs(e1[0]-e2[0]) + abs(e1[1] - e2[1]))

print(ans - 1)