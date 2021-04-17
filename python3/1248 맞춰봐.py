import sys
input = sys.stdin.readline


def check(idx):
    s = 0
    for i in range(idx,-1,-1):
        s += ans[i]
        if sign[i][idx] == 0:
            if s != 0:
                return False
        elif sign[i][idx] == 1:
            if s <= 0:
                return False
        elif sign[i][idx] == -1:
            if s >= 0:
                return False
    return True


def go(idx):
    if idx == n:
        return True
    if sign[idx][idx] == 0:
        ans[idx] = 0
        return check(idx) and go(idx+1)
    for i in range(1,11):
        ans[idx] = i * sign[idx][idx]
        if check(idx) and go(idx+1):
            return True
    return False


n = int(input())
s = list(input().strip())

sign = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '+':
            sign[i][j] = 1
        elif s[cnt] == '-':
            sign[i][j] = -1
        cnt += 1

ans = [0] * n
go(0)
print(' '.join(map(str, ans)))