def add_count(ban, key):
    if key in ban:
        ban[key] += 1
    else:
        ban[key] = 1


def report_process(id_list, report):
    result = dict()
    ban_list = dict()

    for s in report:
        user, ban_id = s.split()
        if user in result:
            if ban_id in result[user]: continue
            result[user].add(ban_id)
            add_count(ban_list, ban_id)
        else:
            result[user] = set([ban_id])
            add_count(ban_list, ban_id)

    return result, ban_list


def solution(id_list, report, k):
    answer = []

    result, ban_list = report_process(id_list, report)
    for user in id_list:
        cnt = 0
        for ban_id in result[user]:
            if ban_id in ban_list and ban_list[ban_id] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))