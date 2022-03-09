import heapq
def dijkstra(adj, n, idx):
    dist = [-1] * n
    dist[idx] = 0
    heap = [(0, idx)]
    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if cur_dist > dist[cur]:continue
        for cost, nc in adj[cur]:
            if dist[nc] == -1 or dist[cur] + cost < dist[nc]:
                dist[nc] = dist[cur] + cost
                heapq.heappush(heap, (dist[nc], nc))
    return dist

def solution(n, s, a, b, fares):
    answer = -1
    adj = [[] for _ in range(n)]

    for c, d, f in fares:
        c, d = c-1, d-1
        adj[c].append((f, d))
        adj[d].append((f, c))
    a_dist = dijkstra(adj, n, a-1)
    b_dist = dijkstra(adj, n, b-1)
    s_dist = dijkstra(adj, n, s-1)

    for i in range(n):
        if -1 in [a_dist[i], b_dist[i], s_dist[i]]: continue
        val = a_dist[i] + b_dist[i] + s_dist[i]
        if answer == -1 or val < answer:
            answer = val

    return answer


print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
