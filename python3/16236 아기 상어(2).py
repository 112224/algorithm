input = __import__('sys').stdin.readline
from collections import deque

di = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(board, n, shark, cur_size):
    visit = [[-1] * n for _ in range(n)]
    sx, sy = shark

    q = deque([(sx, sy)])
    visit[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] <= cur_size and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    ret = -1
    for i in range(n):
        for j in range(n):
            if visit[i][j] > 0 and 0 < board[i][j] < cur_size:
                if ret == -1 or visit[i][j] < ret:
                    nx, ny = i, j
                    ret = visit[i][j]
    if ret != -1:
        board[nx][ny] = 0
        shark[0], shark[1] = nx, ny
    return ret


def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    shark = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 9]
    x, y = shark[0]
    shark = [x, y]
    board[x][y] = 0

    ret = 0
    cnt, cur_size = 0, 2
    while True:
        move_cnt = bfs(board, n, shark, cur_size)
        if move_cnt == -1: break
        cnt += 1
        ret += move_cnt
        if cnt == cur_size:
            cur_size += 1
            cnt = 0
    return ret


print(solve())
