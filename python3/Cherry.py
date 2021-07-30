import sys
input = sys.stdin.readline

tc = int(input())

def divide(st, ed, ary):
    if ed - st < 1:
        return 0
    if ed - st == 1:
        return ary[st]*ary[ed]

    ret = max(ary[st:ed+1]) * min(ary[st:ed+1])
    

for _ in range(tc):
    n = int(input())
    ary = list(map(int, input().split()))


    large, small = max(ary[:2]), min(ary[:2])
    ret = large * small
    for i in range(2,n):
        if ary[i] > large:
            print("check1", large, small, ary[i])
            large = ary[i]
            ret = max(ret, large*small)
        elif ary[i] > small:
            print("check2", large, small, ary[i])
            small = ary[i]
            large = 0
    ary.reverse()
    large, small = max(ary[:2]), min(ary[:2])
    ret = max(ret, large*small)
    for i in range(2,n):
        if ary[i] > large:
            print("check1", large, small, ary[i])
            large = ary[i]
            ret = max(ret, large*small)
        elif ary[i] > small:
            print("check2", large, small, ary[i])
            small = ary[i]
            large = 0

    print(ret, '\n')



