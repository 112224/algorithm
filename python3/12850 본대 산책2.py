input = __import__('sys').stdin.readline
MOD = 10**9 + 7
board = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
    ]

def multi(b1, b2):
    return [[sum(b1[i][k]*b2[k][j] % MOD for k in range(8)) % MOD for j in range(8)] for i in range(8)]

# 정대각 행렬
board2 = [[0]*8 for _ in range(8)]
for i in range(8):
    board2[i][i] = 1
n = int(input())

while n>0:
    if n & 1:
        board2 = multi(board2, board)
        n -= 1
    board = multi(board, board)
    n >>= 1

print(board2[0][0])