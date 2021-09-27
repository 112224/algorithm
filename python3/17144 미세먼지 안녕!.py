input = __import__('sys').stdin.readline

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c, t = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for i in range(r):
    if board[i][0] == -1:
        cleaner.append(i)

def confusion(board, r, c):
    tmp = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j]>=5:
                val = board[i][j] // 5
                for dx, dy in di:
                    nx, ny = i + dx, j + dy
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                        tmp[nx][ny] += val
                        board[i][j] -= val
    for i in range(r):
        for j in range(c):
            board[i][j] += tmp[i][j]

def clean(board, r, c, cleaner):
    x1, y1 = cleaner[0] - 1, 0
    while x1 != cleaner[0] or y1 != 1:
        if x1 - 1 >= 0 and y1 == 0:
            board[x1][y1] = board[x1 - 1][y1]
            x1 -= 1
        elif x1 == 0 and y1 + 1 < c:
            board[x1][y1] = board[x1][y1 + 1]
            y1 += 1
        elif y1 == c - 1 and x1 + 1 <= cleaner[0]:
            board[x1][y1] = board[x1 + 1][y1]
            x1 += 1
        elif x1 == cleaner[0] and y1 - 2 >= 0:
            board[x1][y1] = board[x1][y1 - 1]
            y1 -= 1
    board[x1][y1] = 0
    x1, y1 = cleaner[1] + 1, 0
    while x1 != cleaner[1] or y1 != 1:
        if x1 + 1 < r and y1 == 0:
            board[x1][y1] = board[x1 + 1][y1]
            x1 += 1
        elif x1 == r - 1 and y1 + 1 < c:
            board[x1][y1] = board[x1][y1 + 1]
            y1 += 1
        elif y1 == c - 1 and x1 - 1 >= cleaner[1]:
            board[x1][y1] = board[x1 - 1][y1]
            x1 -= 1
        elif x1 == cleaner[1] and y1 - 2 >= 0:
            board[x1][y1] = board[x1][y1 - 1]
            y1 -= 1
    board[x1][y1] = 0


for _ in range(t):
    confusion(board, r, c)
    clean(board,r, c, cleaner)
ans = 0
for ele in board:
    ans += sum(ele)
print(ans + 2)