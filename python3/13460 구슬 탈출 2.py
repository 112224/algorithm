import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

di = [(0,1),(1,0),(0,-1),(-1,0)]

def add(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def gen(k):
    a = [0]*10
    for i in range(10):
        a[i] = (k&3)
        k >>= 2
    return a


def check(dis):
    for i in range(1,10):
        prev = dis[i-1]
        if (prev+2)%4 == dis[i]:
            return False
        elif prev == dis[i]:
            return False
    return True


def move(x, y, k):
    m1 = False
    while True:
        nx, ny = x+di[k][0], y+di[k][1]
        tile = board[nx][ny]
        if tile == '.':
            m1 = True
        elif tile == '#':
            return x, y, m1, False
        elif tile == 'O':
            return x, y, m1, True
        x, y = nx, ny


def solve(r,b, dir):
    global ans
    for i in range(10):
        if ans > 0 and i>=ans:
            return -1
        ele = dir[i]
        rx, ry, rm, rf = move(r[0],r[1], ele)
        bx, by, bm, bf = move(b[0],b[1], ele)
        if bf:
            return -1
        elif rf:
            return i+1
        if not rm and not bm:
            return -1
        if rx == bx and ry == by:
            if abs(rx-r[0]) + abs(ry-r[1]) <abs(rx-b[0]) + abs(ry-b[1]):
                r = rx, ry
                b = add(r, di[(ele+2)%4])
            else:
                b = rx, ry
                r = add(b, di[(ele+2)%4])
        else:
            r = rx, ry
            b = bx, by
    return -1


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r = (i,j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            b = (i,j)
            board[i][j] = '.'

ans = -1
for i in range(1<<20):
    dir = gen(i)
    if check(dir):
        ret = solve(r,b,dir)
        if ret != -1 and (ret < ans or ans == -1):
            ans = ret
print(ans)