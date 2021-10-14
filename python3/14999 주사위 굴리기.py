input = __import__('sys').stdin.readline

# 각 면
tmp = [1, 2, 3, 4, 5, 6]
dice = [0, 0, 0, 0, 0, 0]
# 각 방향별 위치
dice_pos = [
    [3, 2, 6, 1, 5, 4],
    [4, 2, 1, 6, 5, 3],
    [2, 6, 3, 4, 1, 5],
    [5, 1, 3, 4, 6, 2]
]
match = dict()
for i, key in enumerate(tmp):
    match[key] = i
for i in range(4):
    dice_pos[i] = [match[x] for x in dice_pos[i]]

def change(d):
    return [dice[x] for x in dice_pos[d-1]]

di = [(0, 1), (0, -1), (-1, 0), (1, 0)]
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


move = list(map(int, input().split()))
for d in move:
    dx, dy = di[d-1]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        dice = change(d)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[0]
        else:
            dice[0] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[5])
        x, y = nx, ny