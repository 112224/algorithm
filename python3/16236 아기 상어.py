input = __import__('sys').stdin.readline
from collections import deque
di = [(-1,0),(0,-1),(1,0),(0,1)]

# bfs로 방문할 수 있는 지점 중에서, 먹이가 있는 곳
def find_fish(x, y, board, cur_size, n):
    visit = [[-1] * n for _ in range(n)]
    q = deque()
    visit[x][y] = 0
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for dx, dy in di:
            nx, ny = cx + dx, cy + dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny] <= cur_size and visit[nx][ny] == -1:
                visit[nx][ny] = visit[cx][cy] + 1
                q.append((nx, ny))
    nx, ny = -1, -1
    ret = -1
    for i in range(n):
        for j in range(n):
            if visit[i][j] != -1 and board[i][j] < cur_size and board[i][j] != 0:
                if ret == -1 or ret > visit[i][j]:
                    nx, ny = i, j
                    ret = visit[i][j]
    return nx, ny, ret

n = int(input())
board = [[0] * n for _ in range(n)]
x, y = -1, -1

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, ele in enumerate(tmp):
        if ele == 9:
            x, y = i, j
            ele = 0
        board[i][j] = ele
now_size = 2
ans = 0
cnt = 0
while True:
    nx, ny, ret = find_fish(x, y, board, now_size, n)
    if nx == -1:
        break
    board[nx][ny] = 0
    x, y = nx, ny
    ans += ret
    cnt += 1
    if cnt == now_size:
        now_size += 1
        cnt = 0
print(ans)
