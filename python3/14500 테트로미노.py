input = __import__('sys').stdin.readline
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def calculator(pre_sum, x1, y1, x2, y2):
    return pre_sum[x2][y2] - pre_sum[x1][y2] - pre_sum[x2][y1] + pre_sum[x1][y1]


def get_sum(pre_sum, board, i, j):
    pi, pj = i + 1, j + 1
    ary = [-1, -1, -1, -1, -1]
    if pi >= 4: ary[0] = calculator(pre_sum, pi - 4, pj - 1, pi, pj)
    if pj >= 4: ary[1] = calculator(pre_sum, pi - 1, pj - 4, pi, pj)
    if pi >= 2 and pj >= 2: ary[2] = calculator(pre_sum, pi - 2, pj - 2, pi, pj)
    if pi >= 2 and pj >= 3:
        val = calculator(pre_sum, pi - 2, pj - 3, pi, pj)
        ary[3] = val - min(board[i - 1][j - 1] + board[i - 1][j - 2], board[i][j - 1] + board[i][j - 2],
                           board[i - 1][j - 1] + board[i - 1][j], board[i][j - 1] + board[i][j],
                           board[i - 1][j - 2] + board[i - 1][j], board[i][j - 2] + board[i][j],
                           board[i - 1][j - 2] + board[i][j], board[i][j - 2] + board[i - 1][j]
                           )
    if pi >= 3 and pj >= 2:
        val = calculator(pre_sum, pi - 3, pj - 2, pi, pj)
        ary[4] = val - min(board[i - 1][j - 1] + board[i - 2][j - 1], board[i - 1][j] + board[i - 2][j],
                           board[i - 1][j - 1] + board[i][j - 1], board[i - 1][j] + board[i][j],
                           board[i][j - 1] + board[i - 2][j - 1], board[i][j] + board[i - 2][j],
                           board[i - 2][j - 1] + board[i][j], board[i - 2][j] + board[i][j - 1])
    return max(ary)


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pre_sum = [[0] * (m + 1) for _ in range(n + 1)]
    ret = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + board[i - 1][j - 1]
            ret = max(ret, get_sum(pre_sum, board, i - 1, j - 1))
    return ret


print(solve())
