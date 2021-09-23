input = __import__('sys').stdin.readline
import heapq
tc = int(input())

def pops(ary, visit, opt, opt2):
    while ary:
        val, _id = heapq.heappop(ary)
        val *= opt
        if not visit[_id]:
            if opt2: visit[_id] = True
            return val
    return None
for _ in range(tc):
    k = int(input())
    visit = [False] * 1000010
    mh, Mh = [], []
    for i in range(k):
        cmd, val = input().split()
        val = int(val)
        if cmd == 'I':
            heapq.heappush(mh, (val, i))
            heapq.heappush(Mh, (-val, i))
        else:
            if val == -1:
                pops(mh, visit, 1, True)
            else:
                pops(Mh, visit, -1, True)
    M, m = pops(Mh, visit, -1, False), pops(mh, visit, 1, False)
    if not M or not m:
        print("EMPTY")
    else:
        print(M, m)
    