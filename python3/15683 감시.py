input = __import__('sys').stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
di = [(1,0), (0,1), (-1,0), (0,-1)]
cctv_direction = [
    [[0],[1],[2],[3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    [[0,1,2,3]]
]
total = 0
cctvs = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            total += 1
        elif 0 < board[i][j] < 6:
            cctvs.append((i, j))
k = len(cctvs)

def board_set(directions, x, y, a, b):
    ret = 0
    for d in directions:
        dx, dy = di[d]
        nx, ny = x + dx, y + dy
        while 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == a:
                board[nx][ny] = b
                ret += 1
            elif board[nx][ny] == 6:
                break
            nx += dx
            ny += dy
    return ret

def recursive(idx):
    if idx == k:
        return 0
    x, y = cctvs[idx]
    ctyp = cctv_direction[board[x][y] - 1]
    rd = 0
    for dr in ctyp:
        val = board_set(dr, x, y, 0, -(idx+1))
        delta = recursive(idx + 1)
        rd = max(rd, val + delta)
        board_set(dr, x, y, -(idx+1), 0)
    return rd
ans = recursive(0)

print(total - ans)