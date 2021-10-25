input = __import__('sys').stdin.readline
from collections import defaultdict as dt

di = [(0,1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
n, m, k = map(int, input().split())
board = [[5]* n for _ in range(n)]
s2d2 = [list(map(int, input().split())) for _ in range(n)]
table = [[dt(int) for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    table[x-1][y-1][age] += 1

year, alive = 0, m
while year < k and alive:
    year += 1
    # 봄, 여름
    nut = [[0] * n for _ in range(n)]
    fall = []
    for i in range(n):
        for j in range(n):
            if not table[i][j]: continue
            temp, dead = dt(int), 0
            for age in sorted(table[i][j].keys()):
                val = table[i][j][age]
                if board[i][j] >= age * val:
                    board[i][j] -= age * val
                    temp[age+1] = val
                else:
                    survive = board[i][j] // age
                    if not survive:
                        dead += val * (age//2)
                        alive -= val
                        continue
                    temp[age + 1] = survive
                    board[i][j] -= survive * age
                    alive -= (val - survive)
                    dead += (val - survive) * (age // 2)
            table[i][j] = temp
            nut[i][j] = dead
    # 가을
    for i in range(n):
        for j in range(n):
            if not table[i][j]: continue
            cnt = 0
            for age in table[i][j]:
                if age % 5 == 0:
                    cnt += table[i][j][age]
            if cnt:
                for dx, dy in di:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        alive += cnt
                        table[nx][ny][1] += cnt

    # 겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += s2d2[i][j] + nut[i][j]
print(alive)