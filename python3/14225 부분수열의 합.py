n = int(input())
ary = list(map(int,input().split()))

visit = [False]*(100000*20+20)

for i in range((1<<n)):
    ret = 0
    for j in range(n):
        if i & (1<<j):
            ret += ary[j]
    visit[ret] = True

for i in range(2000020):
    if not visit[i]:
        print(i)
        break