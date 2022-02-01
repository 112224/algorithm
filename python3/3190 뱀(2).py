input = __import__('sys').stdin.readline
from collections import deque

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(board, n, q, direction):
    x, y = q[0]
    nx, ny = x + di[direction][0], y + di[direction][1]
    if nx < 0 or n <= nx or ny < 0 or n <= ny: return False
    if board[nx][ny] == 2: return False
    q.appendleft((nx, ny))
    if board[nx][ny] != 1:
        x, y = q.pop()
        board[x][y] = 0
    board[nx][ny] = 2
    return True


def simulation(board, n, apple, rotate_info):
    for x, y in apple:
        board[x-1][y-1] = 1
    sx, sy = 0, 0
    board[0][0] = 2
    q = deque()
    q.append((sx, sy))

    time = 0
    d = 0
    for sec, direction in rotate_info:
        sec = int(sec)
        while time < sec:
            time += 1
            if not move(board, n, q, d):
                return time
        d = (d-1)%4 if direction == 'L' else (d+1) % 4

    while True:
        time += 1
        if not move(board, n, q, d):
            return time


def solve():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    k = int(input())
    apple = [list(map(int, input().split())) for _ in range(k)]
    l = int(input())
    rotate_info = [input().split() for _ in range(l)]

    return simulation(board, n, apple, rotate_info)

print(solve())