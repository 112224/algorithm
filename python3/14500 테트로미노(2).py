input = __import__('sys').stdin.readline
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(visit, board, n, m, cnt, ret, x, y):
    if cnt == 4:
        return ret
    ans = 0
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = True
            ans = max(ans, dfs(visit, board, n, m, cnt + 1, ret + board[nx][ny], nx, ny))
            visit[nx][ny] = False
    return ans


def plus_shape(board, n, m, x, y):
    ret = board[x][y]
    smallest = 1001
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        tmp = board[nx][ny] if 0 <= nx < n and 0 <= ny < m else 0
        if tmp < smallest:
            smallest = tmp
        ret += tmp
    return ret - smallest


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    ret = -1
    for i in range(n):
        for j in range(m):
            visit[i][j] = True

            ret = max(ret, dfs(visit, board, n, m, 1, board[i][j], i, j))
            ret = max(ret, plus_shape(board, n, m, i, j))
            visit[i][j] = False
    return ret


print(solve())
