input = __import__('sys').stdin.readline

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def check(ary):
    for i in range(9):
        if ary[i] == ary[i+1] or ary[i] == (ary[i+1] + 2) % 4:
            return False
    return True

def move(board, direction, ball):
    escape, is_move = False, False
    x, y = ball[0], ball[1]
    while True:
        nx, ny = x+di[direction][0], y+di[direction][1]
        if board[nx][ny] == '#':
            break
        if board[nx][ny] == 'O':
            escape = True
            break
        x, y = nx, ny
        is_move = True
    return escape, [x, y], is_move
def simulation(board, directions, r, b):
    ret, success = -1, False

    for i in range(10):
        direction = directions[i]
        red_escape, nr, red_move = move(board, direction, r)
        blue_escape, nb, blue_move = move(board, direction, b)
        if blue_escape:
            break
        elif red_escape:
            ret = i+1
            success = True
        elif not red_move and not blue_move:
            break
        if nr[0] == nb[0] and nr[1] == nb[1]:
            if abs(r[0]-nr[0]) + abs(r[1]-nr[1]) > abs(b[0]-nb[0]) + abs(b[1]-nb[1]):
                nr[0], nr[1] = nr[0] - di[direction][0], nr[1] - di[direction][1]
            else:
                nb[0], nb[1] = nb[0] - di[direction][0], nb[1] - di[direction][1]
        r, b = nr, nb

    return ret, success


def solve():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    ret = -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                r = [i, j]
                board[i][j] = '.'
            if board[i][j] == 'B':
                b = [i, j]
                board[i][j] = '.'

    for val in range(1<<20):
        directions = []
        for _ in range(10):
            directions.append(val & 3)
            val >>= 2
        if check(directions):
            ans, good = simulation(board, directions, r, b)
            if good and (ans < ret or ret == -1) :
                ret = ans
    return ret

print(solve())