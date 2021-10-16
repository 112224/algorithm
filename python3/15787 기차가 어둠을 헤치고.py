input = __import__('sys').stdin.readline

n, m = map(int, input().split())
ary = [0] * n
for _ in range(m):
    cmd, *ele = map(int, input().split())
    ele[0] -= 1
    if cmd == 1:
        ele[1] -= 1
        ary[ele[0]] |= (1<<ele[1])
        ary[ele[0]] &= ~(1<<20)
    elif cmd == 2:
        ele[1] -= 1
        ary[ele[0]] &= ~(1<<ele[1])
    elif cmd == 3:
        ary[ele[0]] <<= 1
        ary[ele[0]] &= ~(1<<20)
    elif cmd == 4:
        ary[ele[0]] >>= 1

visit = set()
for ele in ary:
    visit.add(ele)
print(len(visit))