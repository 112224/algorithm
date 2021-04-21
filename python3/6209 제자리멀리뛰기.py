import sys
input = sys.stdin.readline

d,n,m = map(int, input().split())

dol = [d] + [int(input()) for _ in range(n)]
dol.sort()
lo, hi = 1, dol[-1]

ans = 0
while lo <= hi:
    mid = (lo+hi)//2
    pos, cnt = 0, 0
    for ele in dol:
        if ele - pos >= mid:
            pos = ele
            cnt += 1
    if cnt >= n-m+1:
        ans = mid
        lo = mid+1
    else:
        hi = mid-1

print(ans)