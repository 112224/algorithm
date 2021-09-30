input = __import__('sys').stdin.readline
n = int(input())
def odd(n):
    board = [[0] * n for _ in range(n)]
    x, y = 0, n // 2
    board[x][y] = 1
    for i in range(2, n * n + 1):
        nx, ny = (x - 1 + n) % n, (y + 1 + n) % n
        if board[nx][ny] == 0:
            board[nx][ny] = i
            x, y = nx, ny
        else:
            board[(x + 1 + n) % n][y] = i
            x, y = (x + 1 + n) % n, y
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


ans = []
if n % 2:
    ans = odd(n)
elif n % 4 == 0:
    ans = four_even(n)
else:
    k = n//2
    qua = n//4
    val = n*n//4
    ans = [[0] * n for _ in range(n)]
    tmp = odd(k)
    for i in range(k):
        for j in range(k):
            if j < qua:
                ans[i][j] = 3 * val
    ans[qua][0] = 0
    ans[qua][qua] = 3 * val
    for i in range(k, n):
        for j in range(k):
            if ans[i - k][j] == 0:
                ans[i][j] = 3 * val
    for i in range(k):
        for j in range(k, n):
            ans[i][j] = val  if n - qua < j else 2 * val
    for i in range(k, n):
        for j in range(k, n):
            ans[i][j] = 2 * val if ans[i - k][j] == val else val

    for dx, dy in [(0, 0), (0, k), (k, 0), (k, k)]:
        for i in range(k):
            for j in range(k):
                ans[i + dx][j + dy] += tmp[i][j]

for ele in ans:
    print(*ele)