from itertools import combinations


def solution(orders, course):
    answer = []
    orders = [sorted(x) for x in orders]

    for cnt in course:
        candi = dict()
        for order in orders:
            if len(order) < cnt: continue
            for ele in combinations(order, cnt):
                if ele in candi:
                    candi[ele] += 1
                else:
                    candi[ele] = 1
        if not candi: continue
        choice = max(candi.values())
        if choice < 2: continue
        for key in candi:
            if candi[key] == choice: answer.append(key)
    answer = [''.join(x) for x in answer]
    answer.sort()

    return answer



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))