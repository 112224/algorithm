ret = []
v = 1
# (a + k)^2 - a^2 = 2ka + k^2 <= 100000
while v**2 <= 100000:
    ret.append(v**2)
    v += 1
g = int(input())
ans = []

# 위 식에서 k
for i in range(1, v):
    if g - ret[i-1] <= 0:
        break
    val, rm = divmod(g - ret[i-1], 2*i)
    if rm == 0:
        ans.append(val + i)
if not ans:
    print(-1)
else:
    ans.reverse()
    print('\n'.join(map(str, ans)))
