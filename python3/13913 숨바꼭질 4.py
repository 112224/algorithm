import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
visit = [False]*300000

visit[n] = True
q = deque()
q.append((n,0))

ans = 0
while q:
    now, cnt = q.popleft()
    if now == k:
        ans = cnt
        break
    if now-1 >=0:
        if not visit[now-1]:
            visit[now-1] = 1
            q.append((now-1,cnt+1))
    if now +1 < 300000:
        if not visit[now+1]:
            visit[now+1] = 2
            q.append((now + 1, cnt + 1))
    if now*2 < 300000:
        if not visit[now*2]:
            visit[now*2] = 3
            q.append((now *2, cnt + 1))
print(ans)
val = k
path = [n]
st = []
while val != n:
    st.append(val)
    if visit[val] == 1:
        val += 1
    elif visit[val] == 2:
        val -= 1
    elif visit[val] == 3:
        val //= 2
while st:
    path.append(st.pop())
print(' '.join(map(str, path)))