import sys
input = sys.stdin.readline

memo = [0]*12

def go(sum):
    if sum == 0:
        return 1
    if sum<0:
        return 0
    if memo[sum] != 0:
        return memo[sum]

    for i in range(1,4):
        memo[sum] += go(sum-i)
    return memo[sum]

tc = int(input())
go(11)

for _ in range(tc):
    n = int(input())
    print(memo[n])