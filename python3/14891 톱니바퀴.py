input = __import__('sys').stdin.readline

tobni = [list(map(int, list(input().rstrip()))) for _ in range(4)]
k = int(input())
def rotate(idx, wise):
    if wise == 1:
        return [tobni[idx][-1]]+tobni[idx][:-1]
    return tobni[idx][1:] + [tobni[idx][0]]
for _ in range(k):
    idx, wise = map(int, input().split())
    wise = 1 if wise == 1 else 0
    idx -= 1
    candi = [(idx, wise)]
    t1 = 1 - wise
    for i in range(idx-1, -1, -1):
        if tobni[i][2] == tobni[i+1][6]: break
        candi.append((i, t1))
        t1 ^= 1
    t2 = 1 - wise
    for i in range(idx + 1, 4):
        if tobni[i-1][2] == tobni[i][6]: break
        candi.append((i, t2))
        t2 ^= 1
    for i, wise in candi:
        tobni[i] = rotate(i, wise)
ans = 0
for i in range(4):
    if tobni[i][0] == 1:
        ans += (1<<i)
print(ans)