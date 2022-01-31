a, b = map(int, input().split())
s1, r1 = divmod(a+b, 2)
if r1 != 0 or a - s1<0:
    print(-1)
else:
    ary = [s1, a - s1]
    ary.sort(reverse=True)
    print(*ary)
