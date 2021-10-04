input = __import__('sys').stdin.readline
from collections import deque

di = [(1,0), (0, 1), (1, 1),(-1, 0), (0, -1), (-1, -1), (1, -1),(-1, 1)]
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

def solve(board):
    q = deque()
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'W':
                q.append((i, j))
                visit[i][j] = True
    black = []
    candi = []
    while q:
        # j, i 순
        y, x = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <=ny < n and not visit[ny][nx]:
                visit[ny][nx] = True
                if board[ny][nx] == '.':
                    candi.append((nx, ny))
                elif board[ny][nx] == 'B':
                    black.append((nx, ny))
    ans, sx, sy = -1, -1, -1
    candi.sort()
    for y, x in candi:
        ret = 0
        for dx, dy in di:
            cnt = 1
            flag = False
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or n<=nx or n <= ny:
                    break
                if board[ny][nx] == '.':
                    break
                if board[ny][nx] == 'B':
                    flag = True
                    break
                cnt += 1
                nx += dx
                ny += dy

            if flag:
                ret += cnt - 1
        if ans < ret:
            ans = ret
            sx, sy = x, y

    return ans, sx, sy
ans, x, y = solve(board)
if ans != 0:
    print(x, y)
    print(ans)
else:
    print('PASS')
