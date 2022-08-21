# from collections import defaultdict
#
# def solution(n, results):
#     answer = 0
#     win, lose = defaultdict(set), defaultdict(set)
#     for winner, loser in results:
#         winner, loser = winner -1 , loser -1
#         win[winner].add(loser)
#         lose[loser].add(winner)
#
#     for i in range(n):
#         for winner_ in win[i]: lose[winner_].update(lose[i])
#         for loser_ in lose[i]: win[loser_].update(win[i])
#
#     for i in range(n):
#         if len(win[i]) + len(lose[i]) == n-1: answer += 1
#
#     return answer

def solution(n, results):
    answer = 0
    graph = [[-1] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for a, b in results:
        a, b = a-1,b-1
        graph[a][b] = 1
        graph[b][a] = 2

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] != -1: continue
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == 2 and graph[k][j] == 2:
                    graph[i][j] = 2
    for i in range(n):
        if -1 not in graph[i]: answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))