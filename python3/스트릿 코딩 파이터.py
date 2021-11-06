input = __import__('sys').stdin.readline

score = list(map(int, input().split()))
n = int(input())

ans = 0
for _ in range(n):
    ary = [0] * 3
    for _ in range(3):
        tmp = list(map(int, input().split()))
        for k in range(3):
            ary[k] += tmp[k]
    ret = 0
    for k in range(3):
        ret += ary[k] * score[k]
    if ans < ret:
        ans = ret
print(ans)