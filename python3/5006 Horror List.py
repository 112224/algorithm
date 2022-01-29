input = __import__('sys').stdin.readline
from collections import deque
n, h, l = map(int, input().split())

rank = [-1] * n
ary = list(map(int, input().split()))
adj = [[] for _ in range(n)]

q = deque()
for ele in ary:
    rank[ele] = 0
    q.append(ele)
for _ in range(l):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

while q:
    cur = q.popleft()
    for ele in adj[cur]:
        if rank[ele] == -1 or rank[ele] > rank[cur] + 1:
            rank[ele] = rank[cur] + 1
            q.append(ele)

M = -2
ans = -1
for i in range(n):
    if M != -1 and (rank[i] == -1 or M < rank[i]):
        ans = i
        M = rank[i]
print(ans)