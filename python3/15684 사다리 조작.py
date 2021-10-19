input = __import__('sys').stdin.readline

n, m, h = map(int, input().split())

sol = [i for i in range(n)]
board = [[False] * (n-1) for _ in range(h)]
change = [list(map(int, input().split())) for _ in range(m)]

for a, b in change:
    a, b = a - 1, b - 1
    board[a][b] = True

global ans
ans = -1

def checker():
    ary = [i for i in range(n)]
    for i in range(h):
        for j in range(n - 1):
            if board[i][j]:
                # 해당 부분에 간선이 있다면? 스왑
                ary[j], ary[j+1] = ary[j+1], ary[j]
    return ary == sol

def recursive(idx, cnt):
    global ans
    x, y = divmod(idx, n - 1)
    if ans != -1 and cnt >= ans: return
    # 놓을 수 있는 횟수를 다 썼거나, idx의 최대값에 도달했다면
    if idx >= (n-1)*h or cnt == 3:
        if checker():
            ans = cnt if ans == -1 else min(ans, cnt)
        return
    # 0<=b<=n-2
    if y == n - 2:
        recursive(idx + 1, cnt)
        if not board[x][y]:
            board[x][y] = True
            recursive(idx + 1, cnt + 1)
            board[x][y] = False
    else:
        if not board[x][y]:
            recursive(idx + 1, cnt)
            if not board[x][y+1]:
                board[x][y] = True
                recursive(idx + 2, cnt + 1)
                board[x][y] = False
        else:
            recursive(idx + 2, cnt)

recursive(0, 0)
print(ans)