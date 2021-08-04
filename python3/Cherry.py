import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    ary = list(map(int, input().split()))
    ret = 0
    for i in range(1, n):
        ret = max(ret, ary[i-1] * ary[i])
    print(ret, '\n')



