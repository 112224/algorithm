import sys
input = sys.stdin.readline

n = int(input())
benefit = [list(map(int , input().split())) for _ in range(n)]
sums = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        sums[i+1][j+1] = benefit[i][j] + sums[i+1][j] + sums[i][j+1] - sums[i][j]


