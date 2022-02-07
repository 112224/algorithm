input = __import__('sys').stdin.readline
di = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simulation(board, visit, n, m, r, c, d):
    for i in range(4):
        nd = (d - i - 1) % 4
        nr, nc = r + di[nd][0], c + di[nd][1]
        if not visit[nr][nc] and board[nr][nc] == 0:
            return nr, nc, nd
    nr, nc = r + di[(d + 2) % 4][0], c + di[(d + 2) % 4][1]
    if board[nr][nc] != 1:
        return nr, nc, d
    return r, c, d


def solve():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    ret = 0
    while True:
        visit[r][c] = True
        ret += 1
        nr, nc, nd = simulation(board, visit, n, m, r, c, d)
        if nr == r and nc == c and nd == d:
            break
        if visit[nr][nc]:
            ret -= 1
        r, c, d = nr, nc, nd
    return ret


print(solve())
