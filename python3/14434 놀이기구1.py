input = __import__('sys').stdin.readline
from bisect import bisect_right
n,m,k,q = map(int,input().split())
cut = list(map(int, input().split()))
grow = [[] for _ in range(n)]
ary = list(map(int, input().split()))
for i, ele in enumerate(ary):
    grow[ele - 1].append(i)

match = [list(map(int, input().split())) for _ in range(q)]

ans = [0] * k
for i, j, h in match:
    i, j, h = i-1, j-1, cut[h-1]

    lo, hi = -1, k
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        li = min(len(grow[i]), bisect_right(grow[i], mid))
        lj = min(len(grow[j]), bisect_right(grow[j], mid))
        if li + lj >= h:
            hi = mid
        else:
            lo = mid
    if hi < k:
        ans[hi] += 1
for i in range(1, k):
    ans[i] += ans[i-1]
for ele in ans:
    print(ele)