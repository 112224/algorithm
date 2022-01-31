a = [list(map(int, input().split())) for _ in range(3)]


def to_time(ary):
    h = ary[3] - ary[0]
    m = ary[4] - ary[1]
    s = ary[5] - ary[2]
    if s < 0:
        m -= 1
        s += 60
    if m < 0:
        h -= 1
        m += 60
    print(f'{h} {m} {s}')

for ary in a:
    to_time(ary)