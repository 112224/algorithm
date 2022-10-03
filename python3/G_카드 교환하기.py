from collections import deque

def bfs(visit, card, adj, cur):
    visit[cur] = True
    q = deque([cur])
    cards = [card[cur]]
    member = [cur]

    while q:
        cur = q.popleft()

        for ele in adj[cur]:
            if not visit[ele]:
                visit[ele] = True
                cards.append(card[ele])
                member.append(ele)
                q.append(ele)
    ret = 0
    cards.sort()
    member.sort()
    for i in range(len(cards)):
        ret += abs(member[i] - cards[i] + 1)

    return ret

def solution():
    n, m = map(int, input().split())
    card = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    visit = [False] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        adj[a].append(b)
        adj[b].append(a)
    ret = 0

    for i in range(n):
        if not visit[i]:
            ret += bfs(visit, card, adj, i)

    return ret

print(solution())