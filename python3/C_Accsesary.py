input = __import__('sys').stdin.readline

p, n = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()
i = -1

while i < n:
    i += 1
    if p >= 200 or i == n: break
    p += ary[i]

print(i)