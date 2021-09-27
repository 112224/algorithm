input = __import__('sys').stdin.readline
n = int(input())
ary = list(map(int, input().split()))
ret = abs(ary[0] + ary[n - 1])
ans = [0, n-1]
l, r = 0, n - 1
while l<r:
    val = ary[l] + ary[r]
    if abs(val) < ret:
        ret = abs(val)
        ans = [l, r]
    if val > 0:
        r -= 1
    elif val == 0:
        break
    else:
        l += 1
print(ary[ans[0]], ary[ans[1]])