input = __import__('sys').stdin.readline
from itertools import combinations


def simulation(board, h, idx):
    val = idx
    for j in range(h):
        if board[j][val] == 1:
            val += 1
        elif board[j][val] == 2:
            val -= 1
    return val


def get_diff(board, n, h):
    ret = 0
    for i in range(n):
        ret += 1 if simulation(board, h, i) != i else 0
    return ret


def rollback(board, combi):
    for x, y in combi:
        board[x][y] = 0
        board[x][y + 1] = 0


def check(board, combi):
    ret = True
    for x, y in combi:
        if board[x][y] != 0:
            ret = False
            break
        board[x][y] = 1
        board[x][y + 1] = 2
    if not ret:
        rollback(board, combi)
    return ret


def solve():
    n, m, h = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(m)]
    board = [[0 for _ in range(n)] for _ in range(h)]
    for x, y in edge:
        x, y = x - 1, y - 1
        board[x][y] = 1
        board[x][y + 1] = 2

    val = get_diff(board, n, h)
    if val == 0:
        return 0
    elif val > 6:
        return -1

    candi = []
    for i in range(h):
        for j in range(n - 1):
            if board[i][j] == 0 and board[i][j + 1] == 0:
                candi.append((i, j))

    for k in range(1, 4):
        for combi in combinations(candi, k):
            if not check(board, combi): continue
            if get_diff(board, n, h) == 0:
                return k
            rollback(board, combi)
    return -1


print(solve())
