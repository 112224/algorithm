input = __import__('sys').stdin.readline

di = [(1,1),(-1,-1),(1,-1),(-1,1)]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
color = [[0] * n for _ in range(n)]
visited = [False] * (n*n)

for i in range(n):
    for j in range(n):
        if (i + j) % 2:
            color[i][j] = 1

def check(visited, r, c):
    for dx, dy in di:
        x, y = r + dx, c + dy
        while 0<=x<n and 0<=y<n:
            if visited[x*n + y]: return False
            x += dx
            y += dy
    return True

ans = [0, 0]
def recursive(board, visited, v, col, cnt):
    ans[col] = max(ans[col], cnt)
    for x in range(v + 1, n*n):
        r, c = divmod(x, n)
        if color[r][c] != col or board[r][c] != 1:
            continue
        if check(visited, r, c):
            visited[x] = True
            recursive(board, visited, x, col, cnt + 1)
            visited[x] = False

recursive(board, visited, -1, 0 ,0)
recursive(board, visited, 0, 1, 0)
print(sum(ans))
