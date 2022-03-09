from bisect import bisect_left


def find_idx(s):
    if s == '-': return 0
    if s == 'python': return 3
    if s in ['cpp', 'backend', 'junior', 'chicken']: return 1
    if s in ['java', 'frontend', 'senior', 'pizza']: return 2
    return int(s)


def solution(info, queries):
    answer = []
    score_table = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]

    for appli in info:
        appli = appli.split()
        lang, job, rud, food, score = [find_idx(x) for x in appli]

        for i in [0, lang]:
            for j in [0, job]:
                for k in [0, rud]:
                    for p in [0, food]:
                        score_table[i][j][k][p].append(score)
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for p in range(3):
                    score_table[i][j][k][p].sort()

    for query in queries:
        query = query.replace('and', '')
        query = query.split()
        lang, job, rud, food, score = [find_idx(x) for x in query]
        ret = len(score_table[lang][job][rud][food]) - bisect_left(score_table[lang][job][rud][food], score)
        answer.append(ret)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
