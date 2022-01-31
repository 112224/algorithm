a = [int(input()) for _ in range(4)]
rise, dive = a[0] < a[1], a[0] > a[1]
flag = True
for i in range(1, 3):
    if rise:
        if a[i] >= a[i+1]:
            flag = False
            break
    elif dive:
        if a[i] <= a[i+1]:
            flag = False
            break
    else:
        if a[i] != a[i+1]:
            flag = False
            break
if not flag:
    print("No Fish")
elif rise:
    print("Fish Rising")
elif dive:
    print("Fish Diving")
else:
    print("Fish At Constant Depth")