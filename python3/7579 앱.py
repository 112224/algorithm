import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

Max = sum(v)
dp = [0]*(Max+1)

for i in range(n):
    for j in range(Max,v[i]-1,-1):
        dp[j] = max(dp[j], dp[j-v[i]] + w[i])

for i in range(Max+1):
    if dp[i]>=m:
        print(i)
        break