input = __import__('sys').stdin.readline

Or, Oc, m = map(int, input().split())
di = [(), (-1, 0), (1,0), (0, 1), (-1, 0)]
board = [[-1] * Oc for _ in range(Or)]
visit = [False] * m
fish = []
for i in range(m):
    r,c,s,d,z = map(int, input().split())
    fish.append([r-1,c-1,s,d,z])
    board[r-1][c-1] = i

def catch_fish(pos, visit):
    ret = -1
    for i in range(Or):
        if board[i][pos] != -1:
            ret = board[i][pos]
            board[i][pos] = 0
            visit[ret] = True
            return ret
    return ret

def move_fish(fish, visit, Or, Oc):
    moved_board = [[-1] * Oc for _ in range(Or)]
    for i in range(len(fish)):
        if visit[i]: continue
        r, c, s, d, z = fish[i]
        dr, dc = di[d]
        nr, nc = r + dr *s, c + dc * s
        rr, rc = divmod(nr, Or)
        if rr % 2 == 0:
            nr = rc
        else:
            nr = Or - 1 - rc
        cr, cc = divmod(nc, Oc)
        if cr % 2 == 0:
            nc = cc
        else:
            nc = Oc - 1 - cc
        if moved_board[nr][nc] != -1:
            val = moved_board[nr][nc]
            if fish[val][4] < d:
                visit[val] = True
                moved_board[nr][nc] = i
            else:
                visit[i] = True
                continue
        moved_board[nr][nc] = i
        fish[i] = [nr, nc, s, d, z]
    return moved_board

pos = 0
ans = 0
while pos < c:
    cur = catch_fish(pos, visit)
    if cur != -1:
        ans += fish[cur][4]
    board = move_fish(fish, visit, Or, Oc)
    pos += 1
print(ans)


