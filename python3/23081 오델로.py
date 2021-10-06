input = __import__('sys').stdin.readline

di = [(1,0), (0, 1), (1, 1),(-1, 0), (0, -1), (-1, -1), (1, -1),(-1, 1)]
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

ans = 0
cx, cy = -1, -1
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            ret = 0
            for dy, dx in di:
                tmp = 0
                ny, nx = i + dy, j + dx
                while 0<=ny<n and 0 <=nx<n:
                    if board[ny][nx] == '.':
                        tmp = 0
                        break
                    elif board[ny][nx] == 'W':
                        tmp += 1
                    elif board[ny][nx] == 'B':
                        ret += tmp
                        break
                    ny += dy
                    nx += dx
            if ans < ret:
                ans = ret
                cy, cx = j, i
if ans == 0:
    print('PASS')
else:
    print(cy, cx)
    print(ans)