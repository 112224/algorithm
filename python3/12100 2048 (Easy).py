import sys
input = sys.stdin.readline

di = [(0,1),(1,0),(0,-1),(-1,0)]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def gene(k):
    a = [0]*5
    for i in range(5):
        a[i] = (k&3)
        k >>= 2
    return a


def mer(k, ary):
    global ans

    dx, dy = di[k]
    if abs(dx):
        for y in range(n):
            if dx == -1:
                move(k, ary, 0, y)
                for x in range(n-1):
                    if ary[x][y] == 0:
                        continue
                    if ary[x][y] == ary[x+1][y]:
                        ary[x][y] *= 2
                        ans = max(ans, ary[x][y])
                        ary[x+1][y] = 0
                        move(k, ary, x+1, y)
            else:
                move(k, ary, n-1, y)
                for x in range(n-1,0,-1):
                    if ary[x][y] == 0:
                        continue
                    if ary[x][y] == ary[x-1][y]:
                        ary[x][y] *= 2
                        ans = max(ans, ary[x][y])
                        ary[x-1][y] = 0
                        move(k, ary, x-1, y)
    else:
        for x in range(n):
            if dy == -1:
                move(k, ary, x, 0)
                for y in range(n-1):
                    if ary[x][y] == 0:
                        continue
                    if ary[x][y] == ary[x][y+1]:
                        ary[x][y] *= 2
                        ans = max(ans, ary[x][y])
                        ary[x][y + 1] = 0
                        move(k, ary, x, y+1)
            else:
                move(k, ary, x, n-1)
                for y in range(n-1,0,-1):
                    if ary[x][y] == 0:
                        continue
                    if ary[x][y] == ary[x][y-1]:
                        ary[x][y] *= 2
                        ans = max(ans, ary[x][y])
                        ary[x][y - 1] = 0
                        move(k, ary, x, y-1)



def move(k, ary, px, py):
    dx, dy = di[k]
    if abs(dx):
        y = py
        if dx == -1:
            cnt = px
            for x in range(px, n):
                if ary[x][y] != 0:
                    if cnt != x:
                        ary[cnt][y], ary[x][y] = ary[x][y], ary[cnt][y]
                    cnt += 1
        else:
            cnt = px
            for x in range(px, -1, -1):
                if ary[x][y] != 0:
                    if cnt != x:
                        ary[cnt][y], ary[x][y] = ary[x][y], ary[cnt][y]
                    cnt -= 1
    else:
        x = px
        if dy == -1:
            cnt = py
            for y in range(py, n):
                if ary[x][y] != 0:
                    if cnt != y:
                        ary[x][cnt], ary[x][y] = ary[x][y], ary[x][cnt]
                    cnt += 1
        else:
            cnt = py
            for y in range(py, -1, -1):
                if ary[x][y] != 0:
                    if cnt != y:
                        ary[x][cnt], ary[x][y] = ary[x][y], ary[x][cnt]
                    cnt -= 1


def solve(dis):
    ary = [ele[:] for ele in board]
    for k in dis:
        mer(k, ary)


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, board[i][j])
for i in range(1<<10):
    dis = gene(i)
    solve(dis)
print(ans)