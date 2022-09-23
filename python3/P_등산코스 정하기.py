import heapq


def solution(n, paths, gates, summits):
    adj = [[] for _ in range(n+1)]

    for i, j, w in paths:
        adj[i].append([w, j])
        adj[j].append([w, i])

    summits.sort()
    check_summit = [False] * (n + 1)

    dist = [-1] * (n + 1)
    for summit in summits:
        check_summit[summit] = True
    for gate in gates:
        dist[gate] = 0
    heap = [[0, x] for x in gates]

    while heap:
        cur_d, cur = heapq.heappop(heap)
        if cur_d > dist[cur] or check_summit[cur]:
            continue

        for w, v in adj[cur]:
            nd = max(w, cur_d)
            if dist[v] == -1 or dist[v] > nd:
                dist[v] = nd
                heapq.heappush(heap, [nd, v])

    answer = [0, 10 ** 9]
    for summit in summits:
        if dist[summit] != -1 and answer[1] > dist[summit]:
            answer = [summit, dist[summit]]

    return answer


print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
               [3, 7], [1, 5]))