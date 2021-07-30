import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
dist = [-1]*(n+1)
prev = [-1]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

dist[1] = 0
heap = []
heapq.heappush(heap, (0, 1))

while heap:
    now_dis, now = heapq.heappop(heap)
    if dist[now] < now_dis:
        continue
    for ed, cost in adj[now]:
        if dist[ed] == -1 or dist[ed] > dist[now] + cost:
            dist[ed] = dist[now] + cost
            prev[ed] = now
            heapq.heappush(heap, (dist[ed], ed))

print(n-1)
for i in range(2, n+1):
    print(i, prev[i])