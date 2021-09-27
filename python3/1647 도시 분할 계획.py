import heapq
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append((b, c))
    adj[b].append((a, c))

visit = [False] * n
heap = [(0, 0)]
ans = []
while heap:
    cost, cur = heapq.heappop(heap)
    if visit[cur]: continue
    visit[cur] = True
    ans.append(cost)
    for v, c in adj[cur]:
        if not visit[v]:
            heapq.heappush(heap, (c, v))

ans.sort(reverse=True)
print(sum(ans[1:]))