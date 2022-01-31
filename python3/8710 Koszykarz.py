k, w, m = map(int, input().split())
a = w - k
if a <= 0:
    print(0)
else:
    ans, r = divmod(a, m)
    if r != 0:
        ans += 1
    print(ans)