input = __import__('sys').stdin.readline
from collections import deque

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

v = 0
x, y = 0, 0
body = deque()
l = int(input())
trans = [list(input().split()) for _ in range(l)]
trans = [[int(x), y] for x, y in trans]

ans = 0
trans_idx = 0
while True:
    ans += 1
    dx, dy = di[v]
    nx, ny = x + dx, y + dy
    if 0 > nx or n <= nx or 0 > ny or n <= ny: break
    flag = False
    for bx, by in body:
        if nx == bx and ny == by:
            flag = True
            break
    if flag: break
    body.append((x, y))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        body.popleft()
    x, y = nx, ny
    if trans_idx < len(trans):
        ct, cv = trans[trans_idx]
        if ct == ans:
            trans_idx += 1
            if cv == 'L': v = (v+3)%4
            else: v = (v+1)%4

print(ans)
