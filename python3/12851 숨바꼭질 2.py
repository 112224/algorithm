input = __import__('sys').stdin.readline
from collections import deque

n, k = map(int, input().split())
M = 100010
q = deque()
visit = [[-1, -1] for _ in range(M)]
visit[n] = [0, 1] # 방문 시간, 방문 횟수
q.append(n) # 현재 위치, 방문 시간

while q:
    cur = q.popleft()
    cur_cnt = visit[cur][0]
    for x in [2*cur, cur + 1, cur - 1]:
        if 0<=x<M:
            if visit[x][0] == -1:
                visit[x][0] = cur_cnt + 1
                visit[x][1] = visit[cur][1]
                q.append(x)
            elif visit[x][0] == cur_cnt + 1:
                visit[x][1] += visit[cur][1]


print(visit[k][0])
print(visit[k][1])