import sys
import bisect
input = sys.stdin.readline

n = int(input())
ary = list(map(int,input().split()))
x = int(input())

ary.sort()

cnt = 0
for i in range(n):
    t1 = bisect.bisect_left(ary, x-ary[i], lo = i)
    t2 = bisect.bisect_right(ary, x-ary[i], lo = i)
    t1 = t1 if t1>i else i+1
    for j in range(t1,t2):
        if ary[i] + ary[j] == x:
            cnt += 1

print(cnt)