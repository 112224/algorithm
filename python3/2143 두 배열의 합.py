input = __import__('sys').stdin.readline
import bisect

t = int(input())
n = int(input())
ary1 = list(map(int, input().split()))
m = int(input())
ary2 = list(map(int, input().split()))
s1 = [0] * (n + 1)
s2 = [0] * (m + 1)
# [0, i] 까지의 합 (배열 인덱스 1 ~ n 기준)
for i in range(1, n+1):
    s1[i] = s1[i-1] + ary1[i-1]
for i in range(1, m+1):
    s2[i] = s2[i-1] + ary2[i-1]
pre1 = []
pre2 = []
# [i, j] => s[j] - s[i - 1] j > i 인 경우만
for j in range(n+1):
    for i in range(j):
        pre1.append(s1[j] - s1[i])
for j in range(m+1):
    for i in range(j):
        pre2.append(s2[j] - s2[i])
pre1.sort()
pre2.sort()
ans = 0
M = len(pre2)
for ele in pre1:
    val = t - ele
    lo = bisect.bisect_left(pre2, val)
    if lo < M and pre2[lo] == val:
        hi = bisect.bisect_right(pre2, val)
        ans += hi - lo
print(ans)
