input = __import__('sys').stdin.readline

n,m,b = map(int,input().split())

ary = []
for i in range(n):
    tmp = list(map(int, input().split()))
    ary.extend(tmp)

total = n*m
ary.sort(reverse=True)
bmin, bmax = min(ary), max(ary)

ans = [987654321, -1]
for val in range(bmax, bmin-1, -1):
    tmp_b = b
    t = 0
    for ele in ary:
        diff = val - ele
        if diff > 0:
            tmp_b -= diff
            t += diff
        else:
            tmp_b -= diff
            t -= 2 * diff
    if tmp_b >= 0:
        if ans[0] > t:
            ans = [t, val]

print(*ans)

