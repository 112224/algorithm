n = int(input())
a, r = divmod(n, 2)
if r == 0:
    print((a+1)**2)
else:
    print((a+1)**2 + a + 1)