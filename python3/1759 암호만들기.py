import sys
input = sys.stdin.readline

l, c = map(int, input().split())
ary = list(input().split())
ans = []

def check(ret):
    c1, c2 = 0, 0
    for ch in ret:
        if ch in list('aeiou'):
            c1 += 1
        else:
            c2 += 1
        if c1 >=1 and c2 >= 2:
            return True
    return False


def go(idx, ret, length):
    if length == l:
        if check(ret):
            ans.append(ret)
        return
    if idx >= c:
        return
    go(idx + 1, ret + ary[idx], length + 1)
    go(idx + 1, ret, length)


ary.sort()
go(0,'',0)
print('\n'.join(ans))