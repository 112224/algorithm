input = __import__('sys').stdin.readline
from operator import itemgetter

def lower_bound(a, x, opt):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][opt] < x: lo = mid+1
        else: hi = mid
    return lo
def upper_bound(a, x, opt):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid][opt]: hi = mid
        else: lo = mid+1
    return lo

d = 10
tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = 0
    points = [list(map(int, input().split())) for _ in range(n)]
    points.sort()
    for px, py in points:
        l = lower_bound(points, px, 0)
        h = upper_bound(points, px + d, 0)
        candi = points[l:h + 1]
        if len(candi) <= ans: continue
        # y좌표 기준으로 sort
        candi.sort(key=itemgetter(1))

        # y좌표 기준으로 lower, upper
        l = lower_bound(candi, py - d, 1)
        h = upper_bound(candi, py + d, 1)
        candi = candi[l:h + 1]
        m = len(candi)
        if m <= ans: continue
        # 현재 점을 px, py를 정사각형의 변 위의 점으로 만들기

        for y1 in range(py - 10, py + 1):
            ret = 0
            for x, y in candi:
                if y > y1 + 10: break
                if px <= x <= px + 10 and y1 <= y <= y1 + 10:
                    ret += 1
            ans = max(ans, ret)

    print(ans)