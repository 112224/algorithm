input = __import__('sys').stdin.readline
di = [(0, 1), (-1, 0), (0, -1), (1, 0)]
directions = [[], [0, 1, 2, 3], [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)],
              [(0, 1, 2), (1, 2, 3), (3, 0, 1), (2, 3, 0)], [(0, 1, 2, 3)]]


def count_area(board, x, y, op, idx, dirs):
    ret = 0
    n, m = len(board), len(board[0])
    if op == 1: dirs = [dirs]
    for ele in dirs:
        dx, dy = di[ele][0], di[ele][1]
        nx, ny = x + dx, y + dy
        while True:
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = -idx - 1
                    ret += 1
                nx, ny = nx + dx, ny + dy
            else:
                break
    return ret


def clear_board(board, x, y, op, idx, dirs):
    n, m = len(board), len(board[0])
    if op == 1: dirs = [dirs]
    for ele in dirs:
        dx, dy = di[ele][0], di[ele][1]
        nx, ny = x + dx, y + dy
        while True:
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == -idx - 1:
                    board[nx][ny] = 0
                nx, ny = nx + dx, ny + dy
            else:
                break


def recursive(board, cctvs, cctv_num, idx):
    if cctv_num == idx:
        return 0

    x, y, op = cctvs[idx]
    ret = -1
    for dirs in directions[op]:
        cnt = count_area(board, x, y, op, idx, dirs)
        ret = max(ret, cnt + recursive(board, cctvs, cctv_num, idx + 1))
        clear_board(board, x, y, op, idx, dirs)
    return ret


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cctvs = [[i, j, board[i][j]] for j in range(m) for i in range(n) if 1 <= board[i][j] <= 5]

    ret = 0
    for ary in board:
        ret += ary.count(0)

    return ret - recursive(board, cctvs, len(cctvs), 0)


print(solve())
