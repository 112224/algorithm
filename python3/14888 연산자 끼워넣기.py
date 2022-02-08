input = __import__('sys').stdin.readline
def cal(v1, v2, op):
    if op == 0:
        return v1 + v2
    elif op == 1:
        return v1 - v2
    elif op == 2:
        return v1 * v2
    elif op == 3:
        if v1 < 0:
            v1 = -v1
            return -(v1 // v2)
        else:
            return v1 // v2


def recursive(ans, ary, opers, n, idx, ret):
    if idx == n:
        ans[0] = max(ans[0], ret)
        ans[1] = min(ans[1], ret)
        return

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            recursive(ans, ary, opers, n, idx + 1, cal(ret, ary[idx], i))
            opers[i] += 1
    return


def solve():
    n = int(input())
    ary = list(map(int, input().split()))
    num_of_operator = list(map(int, input().split()))

    ans = [-1 * 10 ** 9, 10 ** 9]
    recursive(ans, ary, num_of_operator, n, 1, ary[0])

    print(f'{ans[0]}\n{ans[1]}')


solve()
