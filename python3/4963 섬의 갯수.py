import sys
input = sys.stdin.readline
from collections import deque


di = [(0,1),(1,0),(-1,0),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    ary = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    candi = []
    for i in range(h):
        for j in range(w):
            if ary[i][j] == 1:
                candi.append((i,j))

    while True:
        q = deque()
        flag = False
        for i, j in candi:
            if ary[i][j] == 1:
                q.append((i,j))
                ary[i][j] = 0
                flag = True
                break

        while q:
            i, j = q.popleft()
            for dx, dy in di:
                ni, nj = i + dx, j+dy
                if 0<=ni<h and 0<=nj<w:
                    if ary[ni][nj] == 1:
                        ary[ni][nj] = 0
                        q.append((ni,nj))
        if not flag:
            break
        else:
            ans += 1
    print(ans)