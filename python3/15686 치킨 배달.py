input = __import__('sys').stdin.readline
from itertools import combinations


def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_min_dist(homes, store):
    ret = 0
    for p1 in homes:
        v = 500
        for p2 in store:
            v = min(v, get_dist(p1, p2))
        ret += v
    return ret


def solve():
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    homes = []
    store = []
    # 1 <= len(homes) < 2N
    # m <= len(store) <= 13
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                homes.append((i, j))
            elif city[i][j] == 2:
                store.append((i, j))
    ret = -1
    for remain in combinations(store, m):
        cur_ans = get_min_dist(homes, remain)
        if ret == -1 or cur_ans < ret:
            ret = cur_ans
    return ret


print(solve())
