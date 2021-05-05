import sys
input = sys.stdin.readline

n = int(input())
energy = list(map(int, input().split()))

def solve(en):
    m = len(en)
    if m == 2:
        return 0

    ret = 1
    for i in range(1,m-1):
        ret = max(ret, solve(en[:i] + en[i+1:]) + energy[en[i-1]] * energy[en[i+1]])
    return ret

ans = solve(list(range(n)))
print(ans)
