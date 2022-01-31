x, k = map(int,input().split())
x *= 1000
k *= 1000
if x >= 7*k:
    print(7*k)
elif 2*x >= 7*k:
    print(7*k//2)
elif 4*x >= 7*k:
    print(7*k//4)
else:
    print(0)