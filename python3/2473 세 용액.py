input = __import__('sys').stdin.readline
n = int(input())
ary = list(map(int, input().split()))
ary.sort()
ret = abs(ary[0] + ary[1] + ary[n-1])
ans = [0, 1, n - 1]
for i in range(n):
    l, r = i+1, n-1
    while l < r:
        val = ary[l] + ary[r] + ary[i]
        if abs(val) < abs(ret):
            ret = abs(val)
            ans = [i, l, r]
        if val < 0:
            l += 1
        elif val == 0:
            break
        else:
            r -= 1

ans = [ary[x] for x in ans]
print(*ans)