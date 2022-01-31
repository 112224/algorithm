a = list(map(int, input().split()))
a.sort()
if a[2]**2 == a[0]**2 + a[1]**2:
    print(1)
elif a[0] == a[1] and a[1] == a[2]:
    print(2)
else:
    print(0)