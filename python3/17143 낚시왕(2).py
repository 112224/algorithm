input = __import__('sys').stdin.readline
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def change_direction(r, c, x, y, d):
    if x == 0 and d == 0:
        d = 1
    elif x == r - 1 and d == 1:
        d = 0
    elif y == 0 and d == 3:
        d = 2
    elif y == c - 1 and d == 2:
        d = 3
    return d


def fisher_move(board, n, col):
    ret = 0
    for i in range(n):
        if board[i][col] == [-1, -1, -1]: continue
        ret += board[i][col][2]
        board[i][col][0], board[i][col][1], board[i][col][2] = -1, -1, -1
        break

    return ret


def shark_move(board, r, c):
    next_state = [[[-1, -1, -1]] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            tmp = board[i][j]
            if tmp == [-1, -1, -1]: continue
            s, d, z = tmp
            direction = di[d]
            nx, ny = i, j
            for _ in range(s):
                nd = change_direction(r, c, nx, ny, d)
                if d != nd:
                    d = nd
                    direction = di[d]
                nx += direction[0]
                ny += direction[1]
            if next_state[nx][ny][2] < z:
                next_state[nx][ny] = [s, d, z]
    return next_state


def solve():
    r, c, m = map(int, input().split())
    board = [[[-1, -1, -1]] * c for _ in range(r)]

    for _ in range(m):
        x, y, s, d, z = map(int, input().split())
        x, y, d = x - 1, y - 1, d - 1
        if d in [0, 1]:
            s %= 2 * (r - 1)
        else:
            s %= 2 * (c - 1)
        board[x][y] = [s, d, z]

    ret = 0
    for col in range(c):
        ret += fisher_move(board, r, col)
        board = shark_move(board, r, c)
    return ret


print(solve())
