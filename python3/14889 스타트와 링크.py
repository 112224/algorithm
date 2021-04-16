import sys
input = sys.stdin.readline

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

check = [False] * (n+1)


def go(start, idx):
    if idx >= n:
        return 987654321
    if len(start) == n//2:
        link = []
        for i in range(n):
            if not check[i]:
                link.append(i)
        t1 , t2 = 0, 0
        for i in range(n//2):
            for j in range(n//2):
                t1 += stat[start[i]][start[j]]
        for i in range(n//2):
            for j in range(n//2):
                t2 += stat[link[i]][link[j]]
        return abs(t1-t2)

    ret = 987654321
    check[idx] = True
    ret = min(ret,go(start+[idx], idx+1))
    check[idx] = False
    ret = min(ret, go(start, idx+1))

    return ret

print(go([],0))