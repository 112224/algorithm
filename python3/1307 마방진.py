input = __import__('sys').stdin.readline
n = int(input())
def odd(n):
    board = [[0] * n for _ in range(n)]
    x, y = 0, n // 2
    board[x][y] = 1
    for i in range(2, n * n + 1):
        nx, ny = (x - 1) % n, (y + 1) % n
        if board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
        else:
            board[(x + 1) % n][y] = i
            x, y = (x + 1) % n, y
    return board
def four_even(n):
    board = [[0] * n for _ in range(n)]
    cnt = n*n
    st = []
    l, h = n//4, n - n//4
    for i in range(n):
        c1 = l <= i < h
        for j in range(n):
            c2 = l <= j < h
            if c1 ^ c2:
                board[i][j] = cnt
            else:
                st.append(cnt)
            cnt -= 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i][j] = st.pop()
    return board
def checker_(n, board):
    t_board = list(map(list, zip(*board)))
    ret = sum(board[0])
    t1 = 0
    t2 = 0
    for i in range(n):
        t1 += board[i][i]
        t2 += board[i][n - 1 - i]
    for i in range(n):
        if ret != sum(board[0]) or ret != sum(t_board[0]):
            print(n, n%2, n%4)
            break
    if ret != t1 or ret != t2:
        print(n, n%2, n%4)
    pp = []
    for i in range(n):
        for j in range(n):
            pp.append(board[i][j])
    if len(set(pp)) < n*n:
        print(n, n%2, n%4)
while n <= 300:
    ans = []
    if n % 2:
        ans = odd(n)
    elif n % 4 == 0:
        ans = four_even(n)
    else:
        k = n//2
        val = n*n//4
        p = k//2
        tmp = odd(k)
        st = [(0, 0), (0, k), (k, 0), (k, k)]
        ans = [[0] * n for _ in range(n)]
        rec = [[[0] * 4 for _ in range(n)] for _ in range(n)]
        for i in range(k):
            for j in range(k):
                if i == p:
                    if j == p:
                        rec[i][j][0] = 3 * val
                    else:
                        rec[i][j][2] = 3 * val
                else:
                    if j < p:
                        rec[i][j][0] = 3 * val
                    else:
                        rec[i][j][2] = 3 * val
        ed = k//2 - 1
        for i in range(k):
            for j in range(k):
                if j < k - ed:
                    rec[i][j][1] = 2 * val
                    rec[i][j][3] = val
                else:
                    rec[i][j][1] = val
                    rec[i][j][3] = 2 * val
        for p in range(4):
            dx, dy = st[p]
            for i in range(k):
                for j in range(k):
                    ans[i + dx][j + dy] = rec[i][j][p] + tmp[i][j]
    checker_(n, ans)
    print(f'{n} done!, {sum(ans[0])}, {(n*n + 1)* n // 2}')
    if sum(ans[0]) != (n*n + 1)* n // 2:
        print('!!!!!!!!!!!!!!!!!!!!!', n)
    n += 1