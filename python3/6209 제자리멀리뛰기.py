import sys
input = sys.stdin.readline

d,n,m = map(int, input().split())

dol = [int(input()) for _ in range(n)]
dol.sort()
lo, hi = 1, dol[-1]

ans = 0
while lo < hi:
    mid = (lo+hi)//2
    pos, cnt = 0, 0
    for ele in dol:
        if ele - pos <= mid:
            cnt += 1
        else:
            pos = ele
    if cnt <= m:
        ans = mid
        hi = mid
    else:
        lo = mid