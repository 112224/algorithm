input = __import__('sys').stdin.readline
import heapq

def to_int(time):
    time = time.replace('.', '')
    time = time.split(':')
    val = int(time[0]) * 3600 * 1000 + int(time[1]) * 60 *1000 + int(time[2])
    return val

n = int(input())
heap = []
for _ in range(n):
    st, ed = input().split()
    st, ed = to_int(st), to_int(ed)
    heap.append((st, 1))
    heap.append((ed, 0))

heapq.heapify(heap)
ans = 0
cur = 0
while heap:
    ti, fl = heapq.heappop(heap)
    if fl == 0:
        cur -= 1
    else:
        cur += 1
        ans = max(ans, cur)
print(ans)