import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coi = []
board = [list(input().strip()) for _ in range(n)]
xdi = [0,0,1,-1]
ydi = [1,-1,0,0]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coi.append((i,j))


def solve(coin, cnt, prev):
    if cnt>=10:
        return -1
    ret = -1
    for i in range(4):
        #if (prev+i)%4 == 1:
        #    if prev != -1:
        #        continue
        f = [False] * 2
        move = [False] * 2
        tmp = []
        for j in range(2):
            x,y = coin[j]
            nx, ny = x+xdi[i], y+ydi[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                f[j] = True
                continue
            elif board[nx][ny] != '#':
                move[j] = True
            elif board[nx][ny] == '#':
                nx, ny = x, y
            tmp.append((nx,ny))

        if f[0] ^ f[1]:
            return cnt + 1
        elif (f[0] and f[1]) or (tmp[0] == tmp[1]):
            continue
        elif move[0] or move[1]:
            val = solve(tmp, cnt+1, i)
            if  val != -1 and (val< ret or ret == -1):
                ret = val
    return ret

ans = solve(coi, 0, -1)
print(ans)
