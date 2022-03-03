input = __import__('sys').stdin.readline
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def diffusion(board, n, m):
    next_state = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0: continue
            val = board[i][j] // 5
            for dx, dy in di:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1:
                    next_state[i][j] -= val
                    next_state[nx][ny] += val

    for i in range(n):
        for j in range(m):
            board[i][j] += next_state[i][j]


def advection(board, n, m, cleaner):
    x = cleaner[0]
    for i in range(x - 1, 0, -1): board[i][0] = board[i - 1][0]
    for i in range(m - 1): board[0][i] = board[0][i + 1]
    for i in range(x): board[i][m - 1] = board[i + 1][m - 1]
    for i in range(m - 1, 1, -1): board[x][i] = board[x][i - 1]
    board[x][1] = 0

    x = cleaner[1]
    for i in range(x + 1, n - 1): board[i][0] = board[i + 1][0]
    for i in range(m - 1): board[n - 1][i] = board[n - 1][i + 1]
    for i in range(n - 1, x, -1): board[i][m - 1] = board[i - 1][m - 1]
    for i in range(m - 1, 1, -1):  board[x][i] = board[x][i - 1]
    board[x][1] = 0


def solve():
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    cleaner = [i for i in range(r) if board[i][0] == -1]

    for _ in range(t):
        diffusion(board, r, c)
        advection(board, r, c, cleaner)

    ret = 0
    for i in range(r):
        ret += sum(board[i])

    return ret + 2


print(solve())
