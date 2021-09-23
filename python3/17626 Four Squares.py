input = __import__('sys').stdin.readline
from bisect import bisect_left
n = int(input())
squ_num = []
for i in range(1, n+1):
    val = i**2
    if val > n:
        break
    squ_num.append(val)

memo = [-1] * (n+1)
memo[0] = 0
def get_count(memo, squ_num, val, cnt):
    if memo[val] != -1:
        return memo[val]
    if cnt == 4:
        return 10
    idx = bisect_left(squ_num, val)
    idx = min(len(squ_num) - 1, idx)
    ret = 10
    for i in range(idx, -1, -1):
        ele = squ_num[i]
        if ele > val:
            continue
        if cnt < 4:
            ret = min(ret, get_count(memo, squ_num, val - ele, cnt + 1))
    memo[val] = ret + 1
    return memo[val]

get_count(memo, squ_num, n, 0)
print(memo[n])
