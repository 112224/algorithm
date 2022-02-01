input = __import__('sys').stdin.readline
#di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def push(game, n, direct):
    if direct <= 1:
        st, ed, step = n-1, -1, -1
    else:
        st, ed, step = 0, n, 1

    for i in range(n):
        py = -1
        for j in range(st, ed, step):
            if py != -1 and game[i][j] == game[i][py]:
                game[i][py] <<= 1
                game[i][j] = -1
                py = -1
            if game[i][j] not in [-1, 0]:
                py = j
    for i in range(n):
        prev = st
        for j in range(st, ed, step):
            if game[i][j] == -1:
                game[i][j] = 0
            if game[i][j] != 0:
                game[i][j], game[i][prev] = game[i][prev], game[i][j]
                prev += step

def simulation(board, n, directions):
    game = [board[i][:] for i in range(n)]
    ret = 0
    for ele in directions:
        if ele in [1, 3]:
            game = list(map(list, zip(*game)))
        push(game, n, ele)
        if ele in [1, 3]:
            game = list(map(list, zip(*game)))
    for ary in game:
        for ele in ary:
            if ele > ret:
                ret = ele

    return ret


def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    ret = -1
    for i in range(1<<10):
        directions = []
        for _ in range(5):
            directions.append(i & 3)
            i >>= 2
        ans = simulation(board, n, directions)
        if ret < ans:
            ret = ans

    return ret

print(solve())