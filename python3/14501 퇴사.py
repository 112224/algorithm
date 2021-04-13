import sys
input = sys.stdin.readline

n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)


def go(days):
    if days > n:
        return -987654321
    if days == n:
        return 0
    if dp[days] != 0:
        return dp[days]
    dp[days] = max(go(days+1), go(days+ary[days][0]) + ary[days][1])
    return dp[days]


print(go(0))