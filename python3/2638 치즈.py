from collections import deque
input = __import__('sys').stdin.readline
di = [(0,1), (1,0), (0,-1),(-1,0)]
n, m = map(int,input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def bfs(board, n, m):
    q = deque()
    q.append((0, 0))
    visit = [[0] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1:
                    visit[nx][ny] += 1
                elif board[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = -1
                    q.append((nx, ny))
    flag = False
    for i in range(n):
        for j in range(m):
            if visit[i][j] >= 2:
                flag = True
                board[i][j] = 0
    return 1 if flag else 0

ans = 0
while bfs(board, n, m):
    ans += 1
print(ans)