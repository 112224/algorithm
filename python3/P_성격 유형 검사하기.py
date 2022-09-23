from collections import defaultdict

def solution(survey, choices):
    answer = ''
    result = defaultdict(int)

    for question, ret in zip(survey, choices):
        question = list(question)
        score = 4 - ret
        result[question[0]] += score

    check = list('RTCFJMAN')
    for i in range(0,8,2):
        val = check[i + 1] if result[check[i+1]] > result[check[i]] else check[i]
        answer+=val


    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))