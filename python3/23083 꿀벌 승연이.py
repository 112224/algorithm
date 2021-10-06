input = __import__('sys').stdin.readline

n, m = map(int, input().split())
board = [[0]* m for _ in range(n)]
di = [[(1,0), (0, 1), (1, 1)],[(1, 0), (-1, 1), (0, 1)]]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = -1
MOD = 10**9 + 7
memo = [[0]* m for _ in range(n)]
memo[0][0] = 1
for j in range(m):
    idx = (j+1)%2
    for i in range(n):
        if board[i][j] == -1:
            continue
        for dx, dy in di[idx]:
            nx, ny = i + dx, j + dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] != -1:
                memo[nx][ny] += memo[i][j]
                memo[nx][ny] %= MOD
print(memo[n-1][m-1])