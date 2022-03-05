from collections import deque


def bfs(info, n, visit, adj):
    visit[1] = True
    q = deque([(1, 0, 1)])

    ret = 1
    while q:
        sheep, wolf, route = q.popleft()
        if sheep > ret:
            ret = sheep
        for i in range(n):
            if not route & (1 << i): continue
            for ele in adj[i]:
                next_route = route | (1 << ele)
                if visit[next_route]: continue
                if info[ele] == -1 and sheep <= wolf + 1: continue
                visit[next_route] = True
                ns, nw = sheep, wolf
                if info[ele] == 1:
                    ns += 1
                else:
                    nw += 1
                q.append((ns, nw, next_route))

    return ret


def solution(info, edges):
    answer = 0
    n = len(info)
    info = [1 - 2 * ele for ele in info]
    visit = [False] * (1 << n)
    adj = [[] for _ in range(n)]
    for x, y in edges:
        adj[x].append(y)

    return bfs(info, n, visit, adj)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
