import heapq

def solution(alp, cop, problems):
    answer = 400
    
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    max_alp, max_cop = 0, 0
    for a, b, c, d, e in problems:
        if max_alp < a:
            max_alp = a
        if max_cop < b:
            max_cop = b
    
    max_status = 151
    dist = [[-1] * max_status for _ in range(max_status)]
    dist[alp][cop] = 0
    heap = [[0, alp, cop]]
    
    while heap:
        cur_d, cur_alp, cur_cop = heapq.heappop(heap)

        if cur_d > dist[cur_alp][cur_cop]:
            continue
        for a, b, c, d, e in problems:
            if cur_alp >= a and cur_cop >= b and not (c == 0 and d == 0):
                ni = cur_alp + c if cur_alp + c < max_status else 150
                nj = cur_cop + d if cur_cop + d < max_status else 150
                nd = cur_d + e

                if dist[ni][nj] == -1 or dist[ni][nj] > cur_d + e:
                    dist[ni][nj] = nd
                    heapq.heappush(heap, [nd, ni, nj])

    for i in range(max_alp, max_status):
        for j in range(max_cop, max_status):
            if dist[i][j] != -1 and answer > dist[i][j]:
                answer = dist[i][j]

    return answer

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(150, 0, [[0, 150, 3, 3, 4]]))
print(solution(0 ,0, [[150, 150, 30, 30, 1], [150, 0, 30, 30, 1]]))