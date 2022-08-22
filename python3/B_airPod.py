input = __import__('sys').stdin.readline

n = int(input())
ary = list(map(int, input().split()))
prev = -1
cur = 0
bat = 0

for ele in ary:
    if ele == prev:
        bat *= 2
    else:
        prev = ele
        bat = 2
    cur += bat
    if cur >= 100:
        prev = -1
        cur = 0
        bat = 0
print(cur)