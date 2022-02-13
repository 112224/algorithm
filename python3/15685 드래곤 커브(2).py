input = __import__('sys').stdin.readline
d_curve = [[0]]
di = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def make_curve(gen):
    nd_curve = d_curve[gen - 1][:]
    for val in d_curve[gen - 1][::-1]:
        nd_curve.append((val + 1) % 4)
    d_curve.append(nd_curve)


def rotate(gen, dir):
    ret = d_curve[gen][:]
    for i in range(len(ret)):
        ret[i] = (ret[i] + dir) % 4

    return ret


def set_board(board, x, y, d, g):
    curve = rotate(g, d)
    board[y][x] = True
    for ele in curve:
        x, y = x + di[ele][0], y + di[ele][1]
        board[y][x] = True


def solve():
    n = int(input())
    curves_info = [list(map(int, input().split())) for _ in range(n)]
    board = [[False] * 101 for _ in range(101)]

    for i in range(1, 11):
        make_curve(i)

    for x, y, d, g in curves_info:
        set_board(board, x, y, d, g)
    ret = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                ret += 1
    return ret


print(solve())
