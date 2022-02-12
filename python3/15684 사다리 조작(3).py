input = __import__('sys').stdin.readline
from itertools import combinations


def simulation(board, n, h):
    expected = [i for i in range(n)]
    result = [-1 for _ in range(n)]
    for i in range(n):
        val = i
        for j in range(h):
            if board[j][val]:
                val += 1
            elif val > 0 and board[j][val - 1]:
                val -= 1
        result[i] = val
    ret = 0
    for i in range(n):
        ret += 1 if expected[i] != result[i] else 0
    return ret


def check(board, combi):
    ret = True
    for x, y in combi:
        if y > 1 and board[x][y - 1]:
            ret = False
            break
        board[x][y] = True

    if not ret:
        for x, y in combi:
            board[x][y] = False
    return ret


def rollback_board(board, combi):
    for x, y in combi:
        board[x][y] = False


def solve():
    n, m, h = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(m)]
    board = [[False] * n for _ in range(h)]
    for x, y in edge:
        x, y = x - 1, y - 1
        board[x][y] = True
    val = simulation(board, n, h)
    if val == 0:
        return 0
    elif val > 6:
        return -1
    candi = []
    for i in range(h):
        for j in range(n - 1):
            if board[i][j] or (j > 0 and board[i][j - 1]):
                continue
            candi.append((i, j))

    for k in range(1, 4):
        for combi in combinations(candi, k):
            if not check(board, combi): continue
            if simulation(board, n, h) == 0:
                return k
            rollback_board(board, combi)

    return -1


print(solve())
