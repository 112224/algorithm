import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
inf = 987654321
dist = [[inf]*n for _ in range(n)]
nxt = [[-1]*n for i in range(n)]



for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if dist[a][b] > c:
        dist[a][b] = c
        nxt[a][b] = b


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(n):
    for j in range(n):
        if dist[i][j] == inf:
            dist[i][j] = 0
    print(' '.join(map(str, dist[i])) + '\n')


def path(st, ed):
    if nxt[st][ed] == -1:
        return [0]
    ret = [st+1]
    while ed != st:
        st = nxt[st][ed]
        ret.append(st + 1)

    return [len(ret)] + ret


for i in range(n):
    for j in range(n):
        print(' '.join(map(str, path(i,j))) + '\n')