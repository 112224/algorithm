input = __import__('sys').stdin.readline

n = 10
di = [(-1, 0), (0, 0), (1, 0) ,(0, -1), (0, 1)]
board = [list(input().rstrip()) for _ in range(n)]

# 같은 지역은 최대 한 번만
for i in range(n):
    for j in range(n):
        if board[i][j] == 'O':
            cnt = 0
            rcnt = 0
            for dx, dy in di:
                nx, ny = i + dx, j + dy
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 'O':
                        cnt += 1
                    else:
                        rcnt += 1
            if rcnt == 0: