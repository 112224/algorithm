input = __import__('sys').stdin.readline
import heapq

n, m, r = map(int, input().split())
nums = list(map(int, input().split()))
adj = [[] for _ in range(n)]

for _ in range(r):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append((b, c))
    adj[b].append((a, c))

def dijkstra(m, start):
    dist = [-1] * n
    dist[start] = 0
    ret = 0
    heap = [(0, start)]

    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if cur_dist > dist[cur]:
            continue
        ret += nums[cur]
        for v, c in adj[cur]:
            if cur_dist + c > m: continue
            if dist[v] == -1 or dist[v] > cur_dist + c:
                dist[v] = cur_dist + c
                heapq.heappush(heap, (dist[v], v))
    return ret
ans = 0
for i in range(n):
    ans = max(ans, dijkstra(m, i))
print(ans)