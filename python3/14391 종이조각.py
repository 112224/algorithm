import sys
input = sys.stdin.readline

n, m = map(int, input().split())
piece = [list(map(int, list(input().strip()))) for _ in range(n)]

ans = 0
for s in range(1<<(n*m)):
    ret = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m + j
            if s&(1<<k) == 0:
                cur = cur*10 + piece[i][j]
            else:
                ret += cur
                cur = 0
        ret += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m + j
            if s&(1<<k) != 0:
                cur = cur*10 + piece[i][j]
            else:
                ret += cur
                cur = 0
        ret += cur
    ans = max(ans, ret)
print(ans)