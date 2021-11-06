input = __import__('sys').stdin.readline

n = int(input())
names = set()
cnt = dict()
for _ in range(n):
    que = list(input().split())
    if que[0] in names: continue
    names.add(que[0])

    if que[1] in cnt:
        cnt[que[1]][int(que[2])] += 1
        cnt[que[1]][int(que[3])] -= 1
    else:
        cnt[que[1]] = [0] * 50005
        cnt[que[1]][int(que[2])] += 1
        cnt[que[1]][int(que[3])] -= 1

ans = [0, '',0,0]
for key in sorted(cnt):
    ary = cnt[key]
    for i in range(1, 50001):
        ary[i] += ary[i-1]
    cur = 0
    st, ed = 0, 0
    flag = False
    for i in range(50005):
        if ary[i] > cur:
            cur = ary[i]
            st = i
            flag = False
        elif not flag and ary[i] < cur:
            ed = i
            flag = True
    if cur > ans[0]:
        ans = [cur, key, st, ed]

print(*ans[1:])
