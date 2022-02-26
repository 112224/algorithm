# 파이썬에서 재귀는 그렇게 선호하지 않으므로 다른 방식 작성
input = __import__('sys').stdin.readline
from collections import deque

di = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(board, visit, day, n, l, r, union):
    q = deque(union)
    ret = 0
    while q:
        x, y = q.popleft()
        ret += board[x][y]
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] != day and l <= abs(board[x][y] - board[nx][ny]) <= r:
                    visit[nx][ny] = day
                    union.append((nx, ny))
                    q.append((nx, ny))

    return ret


def simulation(board, visit, candi, ret, n, l, r):
    flag = False
    next_candi = []
    for x, y in candi:
        if visit[x][y] != ret:
            visit[x][y] = ret
            union = [(x, y)]
            total = bfs(board, visit, ret, n, l, r, union)
            if len(union) > 1:
                flag = True
                total //= len(union)
                for ux, uy in union:
                    board[ux][uy] = total
                next_candi.extend(union)

    candi = next_candi
    return flag


def solve():
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[-1] * n for _ in range(n)]
    ret = 0
    candi = [(x, y) for x in range(n) for y in range(n)]
    while simulation(board, visit, candi, ret, n, l, r):
        ret += 1
    return ret


print(solve())
