input = __import__('sys').stdin.readline

n, m = map(int,input().split())

known = list(map(int,input().split()))
know = set()
for ele in known[1:]:
    know.add(ele)

ans = 0
parties = []
for i in range(m):
    party = list(map(int, input().split()))
    party = party[1:]
    parties.append(party)
visit = [False] * m

def find(visit, know, parties, idx):
    if visit[idx]:
        return
    is_true = False
    for ele in parties[idx]:
        if ele in know:
            is_true = True
            break
    if is_true:
        visit[idx] = True
        know.update(set(parties[idx]))
        for i in range(idx):
            find(visit, know, parties, i)

for i in range(m):
    find(visit, know, parties, i)

for party in parties:
    is_true = False
    for ele in party:
        if ele in know:
            is_true = True
            break
    if not is_true:
        ans += 1

print(ans)