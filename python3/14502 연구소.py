input = __import__('sys').stdin.readline
from collections import deque

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(board, infected, n, m):
    visit = [[False] * m for _ in range(n)]
    q = deque(infected)
    cnt = 0
    while q:
        cnt += 1
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    return cnt


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    total_safe = 0
    infected = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                total_safe += 1
            elif board[i][j] == 2:
                infected.append((i, j))
    total_safe += len(infected)
    ret = 100
    for i in range(n * m):
        x1, y1 = divmod(i, m)
        if board[x1][y1] != 0: continue
        board[x1][y1] = 1
        for j in range(i + 1, n * m):
            x2, y2 = divmod(j, m)
            if board[x2][y2] != 0: continue
            board[x2][y2] = 1
            for k in range(j + 1, n * m):
                x3, y3 = divmod(k, m)
                if board[x3][y3] != 0: continue
                board[x3][y3] = 1
                ret = min(ret, bfs(board, infected, n, m))
                board[x3][y3] = 0
            board[x2][y2] = 0
        board[x1][y1] = 0
    return total_safe - ret - 3


print(solve())
