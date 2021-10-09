input = __import__('sys').stdin.readline

n = int(input())
board = [0] * n
di = [(0, 0), (0,1), (1,0), (0,-1),(-1, 0)]
# 같은 지역은 최대 한 번만
# 그럼 윗줄, 오른쪽은? => 끄고 지나가야함 무조건
for i in range(n):
    cur = map(int, input().split())
    for j, ch in enumerate(cur):
        if ch == 1:
            board[i] |= (1<<j)

def switch(tboard, x, y):
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            tboard[nx] ^= (1<<ny)

ans = -1
for cur in range(1<<n):
    tboard = [0] * n
    for i in range(n):
        tboard[i] = board[i]
    ret = 0
    for i in range(n):
        if cur & (1<<i):
            switch(tboard, 0, i)
            ret += 1
    for i in range(1, n):
        for j in range(n):
            if tboard[i-1] & (1<<j):
                switch(tboard, i, j)
                ret += 1
    if tboard[n-1] == 0:
        if ans == -1 or ans > ret:
            ans = ret
print(ans)