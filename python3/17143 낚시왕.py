input = __import__('sys').stdin.readline

R, C, M = map(int, input().split())
di = [(-1, 0), (1,0), (0, 1), (0, -1)]

board = [[-1] * C for _ in range(R)]
visit = [False] * M
fish = []
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in [1, 2]:
        s %= (R-1)*2
    else:
        s %= (C-1)*2
    fish.append([r-1, c-1, s, d - 1, z])
    board[r-1][c-1] = i

def catch_fish(pos, visit):
    ret = -1
    for i in range(R):
        if board[i][pos] != -1:
            ret = board[i][pos]
            board[i][pos] = 0
            visit[ret] = True
            return ret
    return ret

def move_fish(fish, visit):
    moved_board = [[-1] * C for _ in range(R)]
    for i in range(len(fish)):
        if visit[i]: continue
        r, c, s, d, z = fish[i]
        nr, nc = r, c
        for _ in range(s):
            nr += di[d][0]
            nc += di[d][1]
            if 0 <= nr < R and 0 <= nc < C: continue
            if d == 0: d = 1
            elif d == 1: d = 0
            elif d == 2: d = 3
            elif d == 3: d = 2
            nr += di[d][0] * 2
            nc += di[d][1] * 2

        if moved_board[nr][nc] != -1:
            prev = moved_board[nr][nc]
            if fish[prev][4] > z:
                visit[i] = True
                continue
            else:
                visit[prev] = True
        moved_board[nr][nc] = i
        fish[i] = [nr, nc, s, d, z]
    return moved_board

pos = 0
ans = 0
while pos < C:
    cur = catch_fish(pos, visit)
    if cur != -1:
        ans += fish[cur][4]
    board = move_fish(fish, visit)
    pos += 1
print(ans)