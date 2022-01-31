s = input()
s1 = list(map(int ,list('00000' + s)))
s2 = list(map(int, list('0' + s + '0000')))
l = len(s2)
for i in range(l):
    s2[i] += s1[i]
for i in range(l-1,0,-1):
    if s2[i] >= 2:
        s2[i] -= 2
        s2[i-1] += 1
if s2[0] == 0:
    print(''.join(map(str, s2[1:])))
else:
    print(''.join(map(str, s2)))
