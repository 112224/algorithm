import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
dist = [-1] * n
prev = [-1] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append((b, c))
    adj[b].append((a, c))

for i in range(n):
    adj[i].sort()

s, e = map(int, input().split())
s, e = s-1, e-1

answer = 0

def dijkstra(s, e, dist, visit):
    prev[s] = s
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if cur_dist > dist[cur]:
            continue
        if cur == e:
            return cur_dist
        for ele, cost in adj[cur]:
            if visit:
                if visit[ele]:
                    continue
            if dist[ele] == -1 or dist[ele] > cur_dist + cost:
                dist[ele] = cur_dist + cost
                prev[ele] = cur
                heapq.heappush(heap, (cur_dist + cost, ele))

answer += dijkstra(s, e, dist, None)

visit = [False] * n
dist = [-1] * n
val = e
while prev[val] != val:
    visit[val] = True
    val = prev[val]
answer+=dijkstra(e, s, dist, visit)
print(answer)
