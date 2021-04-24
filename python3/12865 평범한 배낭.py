import sys
input = sys.stdin.readline

n,k = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(k+1)
ary.sort()
for weight, val in ary:
    for j in range(k, weight-1,-1):
        dp[j] = max(dp[j], dp[j-weight] + val)

print(dp[k])
