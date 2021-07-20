import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    v1.sort()
    v2.sort(reverse=True)
    if sum(v2[:n - n//4]) < sum(v1[n//4:]):
        print(0)
    else:
        i = (sum(v2[:n - n//4]) - sum(v1[n//4:])) // 100 - 1
        while True:
            total = n + i
            if sum(v1[total//4:]) + 100 * i >= sum(v2[:total - total//4]):
                break
            i += 1
        print(i)