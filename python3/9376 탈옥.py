import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())

di = [(0,1),(1,0),(0,-1),(-1,0)]


def bfs(op, pos):
    x, y = pos
    visit[x][y][op] = 0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                ch = ary[nx][ny]
                if ch != '*' and visit[nx][ny][op] == -1:
                    if ch == '#':
                        visit[nx][ny][op] = visit[x][y][op] + 1
                        q.append((nx, ny))
                    else:
                        visit[nx][ny][op] = visit[x][y][op]
                        q.appendleft((nx, ny))


for _ in range(tc):
    n, m = map(int, input().split())
    ary = ['.'+input().strip()+'.' for _ in range(n)]
    n, m = n + 2, m + 2
    ary = ['.'*m] + ary + ['.'*m]
    visit = [[[-1]*3 for _ in range(m)] for _ in range(n)]

    pos = [(0,0)]
    for i in range(n):
        for j in range(m):
            if ary[i][j] == '$':
                pos.append((i, j))
    for i in range(3):
        bfs(i, pos[i])

    ans = 10000
    for i in range(n):
        for j in range(m):
            val = sum(visit[i][j])
            if ary[i][j] == '#':
                val -= 2
            if val >= 0 and ans > val:
                ans = val
    print(ans)