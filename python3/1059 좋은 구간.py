import sys
input = sys.stdin.readline

l = int(input())
ary = list(map(int, input().split()))
n = int(input())
ary.sort()

def solution(ary, n):
    s_val, l_val = 0, 0
    for ele in ary:
        if ele < n:
            s_val = ele
        elif ele > n:
            l_val = ele
            break
        else:
            return 0
    l1 = n - s_val
    l2 = l_val - n
    return max(0, l1*l2 - 1)

print(solution(ary, n))
