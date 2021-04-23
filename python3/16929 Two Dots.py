import sys
input = sys.stdin.readline
from collections import deque
di = [(0,1),(1,0),(-1,0),(0,-1)]

n,m = map(int, input().split())
ary = [list(input().strip()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]


def bfs(i, j):
    visit[i][j] = True
    q = deque()
    q.append((i,j,-1,-1))

    while q:
        x, y, px, py = q.popleft()

        for dx,dy in di:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if nx != px and ny != py and ary[x][y] == ary[nx][ny] and visit[nx][ny]:
                    return True
                if ary[x][y] == ary[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx,ny,x,y))
    return False


def solve():
    flag = False
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                flag = bfs(i, j)
                if flag:
                    return flag
    return flag


ans = solve()
if ans:
    print('Yes')
else:
    print('No')

