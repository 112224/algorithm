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


# from itertools import combinations_with_replacement
#
# def calculator(a1, a_idx):
#     ret = 0
#     a2 = [0]*11
#     for val in a_idx:
#         a2[10 - val] += 1
#     for i in range(11):
#         if a1[i] == 0 and a2[i] == 0:continue
#         if a1[i] < a2[i]:
#             ret += 10 - i
#         else:
#             ret -= 10 - i
#     return ret
#
# def solution(n, info):
#     answer = -1
#     ret = []
#     for ary in combinations_with_replacement(range(11), n):
#         diff = calculator(info, ary)
#         if diff > answer:
#             answer = diff
#             ret = ary
#     if answer > 0:
#         info2 = [0] * 11
#         for ele in ret:
#             info2[10 - ele] += 1
#         return info2
#     return [-1]