input = __import__('sys').stdin.readline
from itertools import combinations


def cal(status, member, hn):
    ret = 0
    for i in range(hn):
        for j in range(hn):
            ret += status[member[i]][member[j]]
    return ret


def rcal(status, member, n):
    is_contain = [False] * n
    for ele in member: is_contain[ele] = True

    r_team = [i for i in range(n) if not is_contain[i]]
    return cal(status, r_team, n // 2)


def solve():
    n = int(input())
    status = [list(map(int, input().split())) for _ in range(n)]
    ret = 10 ** 5
    hn = n // 2
    for combi in combinations(list(range(n)), hn):
        ret = min(ret, abs(cal(status, combi, hn) - rcal(status, combi, n)))
    return ret


print(solve())
