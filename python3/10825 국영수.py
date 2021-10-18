input = __import__('sys').stdin.readline

n = int(input())
ary = [input().split() for _ in range(n)]
ary = [(-int(x), int(y), -int(z), k) for k, x, y, z in ary]
ary.sort()
for ele in ary:
    print(ele[3])