import sys
input = sys.stdin.readline

from collections import deque

s = int(input())
visit = [[False]*3000 for _ in range(3000)]

visit[1][0] = True
q = deque()
q.append((1,0,0))

ans = 0
while q:
    val, cnt, clip = q.popleft()
    if val == s:
        ans = cnt
        break
    if not visit[val][val]:
        visit[val][val] = True
        q.append((val,cnt+1,val))
    if val+clip < 3000 and clip>0:
        if not visit[val+clip][clip]:
            visit[val+clip][clip] = True
            q.append((val+clip, cnt+1, clip))
    if 0<val-1:
        if not visit[val-1][clip]:
            visit[val-1][clip] = True
            q.append((val-1, cnt +1, clip))
print(ans)