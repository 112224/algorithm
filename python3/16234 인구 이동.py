input = __import__('sys').stdin.readline
from sys import setrecursionlimit
#기본값 1000임에 주의하자
setrecursionlimit(3000)
di = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dfs(board, visit, n, l, r, x, y, union):
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visit[nx][ny] and l <= abs(board[x][y] - board[nx][ny]) <= r:
                visit[nx][ny] = True
                union.append((nx, ny))
                dfs(board, visit, n, l, r, nx, ny, union)


def simulation(board, n, l, r):
    visit = [[False] * n for _ in range(n)]
    flag = False
    for x in range(n):
        for y in range(n):
            if not visit[x][y]:
                visit[x][y] = True
                union = [(x, y)]
                dfs(board, visit, n, l, r, x, y, union)
                if len(union) > 1:
                    flag = True
                    union_size = 0
                    for ux, uy in union:
                        union_size += board[ux][uy]
                    union_size //= len(union)
                    for ux, uy in union:
                        board[ux][uy] = union_size
    return flag


def solve():
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ret = 0
    while simulation(board, n, l, r):
        ret += 1
    return ret


print(solve())
