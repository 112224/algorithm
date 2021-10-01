input = __import__('sys').stdin.readline
import bisect

n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
ary.sort()
lis = []
pos = [0] * n
cnt = 0
for i in range(n):
    x, y = ary[i]
    if not lis or lis[-1] < y:
        lis.append(y)
        pos[i] = cnt
        cnt += 1
    else:
        lo = bisect.bisect_left(lis, y)
        pos[i] = lo
        lis[lo] = y

ans = []
cnt -= 1
for i in range(n-1, -1, -1):
    if pos[i] != cnt:
        ans.append(ary[i][0])
    else:
        cnt -= 1
print(len(ans))
for ele in ans[::-1]:
    print(ele)
