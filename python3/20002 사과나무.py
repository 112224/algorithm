import sys
input = sys.stdin.readline

n = int(input())
benefit = [list(map(int , input().split())) for _ in range(n)]
sums = [[0]*n for _ in range(n)]

answer = sums[0][0] = benefit[0][0]
for i in range(1, n):
    sums[i][0] = sums[i-1][0] + benefit[i][0]
    sums[0][i] = sums[0][i-1] + benefit[0][i]