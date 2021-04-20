import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit = [False] * (n)


def dfs(idx, cnt, pre):
    if cnt == 5:
        return True
    for ele in adj[idx]:
        if not visit[ele]:
            visit[ele] = True
            if dfs(ele, cnt + 1, idx):
                return True
            visit[ele] = False
    return False


flag = False
for i in range(n):
    visit[i] = True
    if dfs(i, 1, -1):
        flag = True
        break
    visit[i] = False

if flag:
    print(1)
else:
    print(0)