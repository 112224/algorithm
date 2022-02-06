input = __import__('sys').stdin.readline
di = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def rolling(dice, Q):
    if Q == 0:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif Q == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif Q == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

def simulation(board, x, y, n, m, Q, dice):
    Q -= 1
    nx, ny = x + di[Q][0], y + di[Q][1]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
        rolling(dice, Q)
        print(dice[5])
        if board[x][y] == 0:
            board[x][y] = dice[0]
        else:
            dice[0] = board[x][y]
            board[x][y] = 0
    return x, y

def solve():
    n,m,x,y,k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    query = list(map(int, input().split()))
    # index 밑 뒷 오  왼  앞  위
    dice = [0, 0, 0, 0, 0, 0]
    for ele in query:
        x, y = simulation(board, x, y, n, m, ele, dice)

    return

solve()

