input = __import__('sys').stdin.readline


def rotate(board, idx, step, direction):
    l_rota = 0 if idx == 0 or direction == 1 else 0 if board[idx - 1][2] == board[idx][6] else -step
    r_rota = 0 if idx == 3 or direction == -1 else 0 if board[idx][2] == board[idx + 1][6] else -step

    if step == 1:
        board[idx] = [board[idx][-1]] + board[idx][:-1]
    else:
        board[idx] = board[idx][1:] + [board[idx][0]]

    if l_rota != 0: rotate(board, idx - 1, l_rota, -1)
    if r_rota != 0: rotate(board, idx + 1, r_rota, 1)

    return


def solve():
    board = [list(map(int, list(input().rstrip()))) for _ in range(4)]
    k = int(input())
    rotate_info = [list(map(int, input().split())) for _ in range(k)]
    for idx, step in rotate_info:
        rotate(board, idx - 1, step, 0)
    ret = 0
    for i in range(4):
        if board[i][0] == 1:
            ret += (1 << i)

    return ret


print(solve())
