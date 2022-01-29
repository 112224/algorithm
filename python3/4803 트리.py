# boj.kr/4803
# 트리

input = __import__('sys').stdin.readline


def find(pare, change, c):
    change.add(c)
    if pare[c] == c or pare[c] == -1:
        return pare[c]
    return find(pare, change, pare[c])

def solve(n, edges):
    pare = [i for i in range(n)]

    for a, b in edges:
        change = set()
        pa = find(pare, change, a-1)
        pb = find(pare, change, b-1)
        val = -1 if pa == -1 or pb == -1 or pa == pb else pa
        for ele in change:
            pare[ele] = val


    ret = 0
    for i in range(n):
        if i == pare[i]:
            ret += 1
    return ret

TC = 0
while True:
    TC += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    edges = [list(map(int, input().split())) for _ in range(m)]

    ans = solve(n,edges)

    print(f'Case {TC}:', end=' ')
    if ans == 0:
        print('No trees.')
    elif ans == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {ans} trees.')
