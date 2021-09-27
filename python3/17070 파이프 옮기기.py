input = __import__('sys').stdin.readline

di = [(0, 1), (1, 0), (1, 1)]
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def check(board, x, y, nx, ny):
    if 0<=nx<n and 0<=ny<n:
        return board[x][y] == board[nx][y] == board[x][ny] == board[nx][ny] == 0
    else:
        return False

memo = [[[0] * 3 for _ in range(n)] for _ in range(n)]
memo[0][1][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(3):
            for p in range(3):
                if k + p == 1: continue
                dx, dy = di[p]
                ni, nj = i + dx, j + dy
                if check(board, i, j, ni, nj):
                    memo[ni][nj][p] += memo[i][j][k]

print(sum(memo[n-1][n-1]))
