input = __import__('sys').stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
presum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        presum[i][j] = presum[i][j-1] + board[i-1][j-1]
for j in range(1, n+1):
    for i in range(1, n+1):
        presum[i][j] += presum[i-1][j]
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(presum[x2][y2] - presum[x1-1][y2] - presum[x2][y1-1] + presum[x1-1][y1-1])