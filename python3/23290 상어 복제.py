input = __import__('sys').stdin.readline

di = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_di = [(-1, 0), (0, -1), (1, 0), (0, 1)]
m, s = map(int, input().split())
fish = [[[0] * 8 for _ in range(4)] for _ in range(4)]
egg = [[[0] * 8 for _ in range(4)] for _ in range(4)]
vanish = [[-100] * 4 for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    fish[x-1][y-1][d-1] += 1

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1

for t in range(s):
    for i in range(4):
        for j in range(4):
            egg[i][j] = fish[i][j]

    next_level = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for ori_d in range(8):
                if not fish[i][j][ori_d]: continue
                flag = False
                for k in range(8):
                    d = (ori_d - k) % 8
                    dx, dy = di[d]
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if vanish[nx][ny] >= t - 2 or (sx == nx and sy == ny): continue
                        flag = True
                        next_level[nx][ny][d] += fish[i][j][ori_d]
                        break
                if not flag:
                    next_level[i][j][ori_d] += fish[i][j][ori_d]

    fish = [[col[:] for col in row] for row in next_level]

    ret, moves = -1, []
    for i in range(1 << 6):
        flag = False
        cur = 0
        d1, d2, d3 = i >> 4, (i >> 2) & 3, i & 3
        ary = [shark_di[d1], shark_di[d2], shark_di[d3]]
        visit = [[False] * 4 for _ in range(4)]
        nx, ny = sx, sy
        for dx, dy in ary:
            nx += dx
            ny += dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    cur += sum(fish[nx][ny])
            else:
                flag = True
                break
        if not flag and ret < cur:
            ret = cur
            moves = ary

    for dx, dy in moves:
        sx += dx
        sy += dy
        if sum(fish[sx][sy]) != 0:
            vanish[sx][sy] = t
        fish[sx][sy] = [0] * 8

    for i in range(4):
        for j in range(4):
            for k in range(8):
                fish[i][j][k] += egg[i][j][k]
                egg[i][j][k] = 0

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(fish[i][j])
print(ans)
