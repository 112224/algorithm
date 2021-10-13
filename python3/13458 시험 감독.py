input = __import__('sys').stdin.readline

n = int(input())
ary = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for ele in ary:
    ele -= b
    ans += 1
    if ele > 0:
        ret, rem = divmod(ele, c)
        if rem != 0:
            ret += 1
        ans += ret
print(ans)