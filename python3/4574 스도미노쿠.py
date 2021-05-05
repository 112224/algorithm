import sys
input = sys.stdin.readline

di = [(0,1),(1,0)]


def convert(chs):
    chs = list(chs)
    x = ord(chs[0]) - ord('A')
    y = ord(chs[1]) - ord('1')
    return x, y


def setin(x, y, a, flag):
    cr[x][a] = cc[y][a] = cb[(x // 3) * 3 + y // 3][a] = flag
    board[x][y] = a if flag else 0


def check(x, y, a):
    return not (cr[x][a] or cc[y][a] or cb[(x // 3) * 3 + y // 3][a])


def solve(cnt):
    if cnt == 81:
        for ele in board:
            print(''.join(map(str, ele)))
        return True

    x, y = cnt//9, cnt%9
    if board[x][y] != 0:
        return solve(cnt+1)

    else:
        for dx, dy in di:
            nx, ny = x+dx, y+dy
            if 0<=nx<9 and 0<=ny<9:
                if board[nx][ny] != 0:
                    continue
                for i in range(1,10):
                    for j in range(1,10):
                        if i == j or domino[i][j]:
                            continue
                        if check(x,y,i) and check(nx,ny,j):
                            setin(x,y,i,True)
                            setin(nx,ny,j,True)
                            domino[i][j] = domino[j][i] = True
                            if solve(cnt+1):
                                return True
                            setin(x,y,i,False)
                            setin(nx,ny,j,False)
                            domino[i][j] = domino[j][i] = False
    return False


tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [[0]*9 for _ in range(9)]
    domino = [[False]* 10 for _ in range(10)]
    cr = [[False]* 10 for _ in range(10)]
    cc = [[False]* 10 for _ in range(10)]
    cb = [[False]* 10 for _ in range(10)]
    for _ in range(n):
        tmp = input().split()
        a, b = int(tmp[0]), int(tmp[2])
        domino[a][b] = domino[b][a] = True

        x,y = convert(tmp[1])
        setin(x,y,a,True)
        x,y = convert(tmp[3])
        setin(x,y,b,True)

    pos = input().split()
    for val, chs in zip(range(1,10), pos):
        x, y = convert(chs)
        setin(x,y,val,True)

    print('Puzzle {}'.format(tc))
    solve(0)
    tc += 1