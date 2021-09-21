input = __import__('sys').stdin.readline

ary = list(map(int, input().split()))
ans = 0
for ele in ary:
    val = ele ** 2
    val %= 10
    ans += val
ans %= 10
print(ans)