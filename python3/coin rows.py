import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    sums = [[0]*m for _ in range(2)]

    sums[1][0] = board[1][0]
    for j in range(1, m):
        sums[0][j] = sums[0][j-1] + board[0][j]
        sums[1][j] = sums[1][j-1] + board[1][j]

    answer = 1e9
    for j in range(m):
        answer = min(answer, max(sums[1][j-1] if j!=0 else 0, sums[0][m-1] - sums[0][j]))
    print(answer)