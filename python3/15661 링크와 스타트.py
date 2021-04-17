import sys
input = sys.stdin.readline

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]


def go(start, link, idx):
    if idx == n:
        if start and link:
            t1, t2 = 0, 0
            for p1 in start:
                for p2 in start:
                    t1 += stat[p1][p2]

            for p1 in link:
                for p2 in link:
                    t2 += stat[p1][p2]
            return abs(t1-t2)
        return 987654321
    ret = 987654321
    ret = min(ret, go(start+[idx], link, idx+1), go(start, link+[idx], idx+1))

    return ret


print(go([], [], 0))