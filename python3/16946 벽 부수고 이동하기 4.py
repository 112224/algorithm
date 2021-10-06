input = __import__('sys').stdin.readline
from collections import deque

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(n)]
can_go = [[0]* m for _ in range(n)]

group = []
for i in range(n):
    for j in range(m):
        if ary[i][j] == '0' and can_go[i][j] == 0:
            tmp = []
            gr_num = len(group) + 1
            cnt = 1
            q = deque()
            q.append((i, j))
            can_go[i][j] = 1
            while q:
                x, y = q.popleft()
                tmp.append((x, y))
                for dx, dy in di:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<n and 0<=ny<m and ary[nx][ny] == '0' and can_go[nx][ny] == 0:
                        cnt += 1
                        can_go[nx][ny] = 1
                        q.append((nx, ny))
            group.append(cnt)
            for x, y in tmp:
                can_go[x][y] = gr_num

for i in range(n):
    for j in range(m):
        if ary[i][j] == '1':
            adj_gr = set()
            for dx, dy in di:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    adj_gr.add(can_go[nx][ny])
            val = 1
            for ele in adj_gr:
                if ele == 0: continue
                val += group[ele - 1]
            val %= 10
            ary[i][j] = str(val)
for ele in ary:
    print(''.join(ele))