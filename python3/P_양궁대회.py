def calculator(info, ryan):
    ret1, ret2 = 0, 0
    for i in range(11):
        if info[i] == ryan[i] == 0: continue
        if info[i] >= ryan[i]: ret1+= 10-i
        else: ret2 += 10 -i
    return ret2 - ret1


def dfs(idx, ary, info, ans, prev):
    dif = calculator(info, ary)
    if dif > 0 and dif > prev[0]:
        prev[0] = dif
        if not ans:
            ans.extend(ary)
        else:
            ans[:] = ary[:]

    if idx == 0:
        return

    val = ary[idx]
    for i in range(1, val+1):
        ary[idx] -= i
        ary[idx - 1] += i
        dfs(idx - 1, ary, info, ans, prev)
        ary[idx] += i
        ary[idx - 1] -= i



def solution(n, info):
    answer = []
    ary = [0]*10 + [n]

    dfs(10, ary, info, answer, [-1])

    return answer if answer else -1

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))