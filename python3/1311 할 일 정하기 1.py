input = __import__('sys').stdin.readline
M = 25 * 10**4
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1<<n) for _ in range(n)]
Full = (1 << n) - 1
def recursive(cur, worked):
    if worked == Full: return 0
    if dp[cur][worked] != -1: return dp[cur][worked]
    dp[cur][worked] = M
    for i in range(n):
        if worked & (1<<i): continue
        dp[cur][worked] = min(dp[cur][worked], recursive(cur + 1, worked | (1<<i)) + work[cur][i])
    return dp[cur][worked]

print(recursive(0, 0))