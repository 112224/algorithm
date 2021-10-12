input = __import__('sys').stdin.readline
import bisect

n, m, k = map(int, input().split())
card = list(map(int, input().split()))
chul = list(map(int, input().split()))
card.sort()
pare = [i for i in range(m)]

def find(a):
    if a == pare[a]: return a
    pare[a] = find(pare[a])
    return pare[a]

def union(a, b):
    if b == m: return
    pa, pb = find(a), find(b)
    if pa != pb:
        pare[pa] = pb
        find(a)
for ch in chul:
    idx = bisect.bisect_right(card, ch)
    idx = find(idx)
    print(card[idx])
    union(idx, idx + 1)