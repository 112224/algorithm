input = __import__('sys').stdin.readline

n, m, h = map(int, input().split())

sol = [i for i in range(n)]
board = [[0] * n for _ in range(h)]
change = [list(map(int, input().split())) for _ in range(m)]

for a, b in change:
    a, b = a - 1, b - 1
    board[a][b] = 1
    board[a][b+1] = 2

candi = []
for i in range(h):
    for j in range(n-1):
        if not board[i][j] and not board[i][j+1]:
            candi.append((i, j))

def checker():
    ary = [i for i in range(n)]
    for i in range(h):
        for j in range(n - 1):
            if board[i][j] == 1:
                # 해당 부분에 간선이 있다면? 스왑
                ary[j], ary[j+1] = ary[j+1], ary[j]
    ret = 0
    for i in range(n):
        if ary[i] != sol[i]:
            ret += 1
    return ret

combination = []
def combi(r, n, idx, ret):
    if r == 0:
        combination.append(ret)
        return
    if n - idx < r:
        return
    combi(r, n, idx + 1, ret)
    combi(r-1, n, idx + 1, ret + [idx])

det = checker()
if det == 0:
    print(0)
elif det > 6:
    print(-1)
else:
    for i in range(1, 4):
        combi(i, len(candi), 0, [])
    ans = -1
    for ret in combination:
        flag = True
        for k in ret:
            x, y = candi[k]
            if board[x][y] != 0:
                flag = False
                break
            board[x][y] = 1
            board[x][y+1] = 2
        if flag and checker() == 0:
            ans = len(ret)
            break
        for k in ret:
            x, y = candi[k]
            board[x][y] = 0
            board[x][y+1] = 0
    print(ans)