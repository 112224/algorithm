input = __import__('sys').stdin.readline

r = 31
M = 1234567891

n = int(input())
ary = list(input().rstrip())
ary = [ord(x) - ord('a') + 1 for x in ary]

ans = 0
mul = 1
for ele in ary:
    ans += ele * mul
    ans %= M
    mul *= r
print(ans)