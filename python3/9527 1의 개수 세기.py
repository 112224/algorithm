input = __import__('sys').stdin.readline

dp = [0] * 60
# dp[i] i자리 bit 일 때 1의 갯수(누적)
dp[1] = 1

for i in range(2, 60):
    dp[i] = dp[i - 1] * 2 + (1 << (i - 1))

a, b = map(int,input().split())

def solve(val):
    ed = bin(val)[2:]
    n = len(ed)
    ret = 0
    for i in range(n):
        cur = n - i - 1
        if ed[i] == '1':
            ret += dp[cur] + val - (1<< cur) + 1
            val -= (1 << cur)
    return ret

print(solve(b) - solve(a - 1))