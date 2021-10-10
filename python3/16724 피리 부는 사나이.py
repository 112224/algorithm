input = __import__('sys').stdin.readline
from collections import deque
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
pare = [i for i in range(n*m)]

di = dict()
di['U'] = -m
di['L'] = -1
di['D'] = m
di['R'] = 1
def find(a):
    if a == pare[a]:
        return a
    pare[a] = find(pare[a])
    return pare[a]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        if pa > pb: pa, pb = pb, pa
        pare[pb] = pa
        find(b)

for i in range(n*m):
    x, y = divmod(i, m)
    union(i, i + di[board[x][y]])

ans = set()
for i in range(n*m):
    ans.add(find(i))
print(len(ans))