import sys
input = sys.stdin.readline

n = int(input())
equ = input().split()

check = [False]*10

ans = []
def go(idx, ret, last):
    if idx == n:
        ans.append(ret)
        return
    for i in range(10):
        if not check[i]:
            if equ[idx] == '<' and last < i:
                check[i] = True
                go(idx+1, ret+str(i), i)
                check[i] = False
            elif equ[idx] == '>' and last > i:
                check[i] = True
                go(idx + 1, ret + str(i), i)
                check[i] = False

for i in range(10):
    check[i] = True
    go(0, str(i), i)
    check[i] = False

ans.sort()
ans = [ans[-1],ans[0]]
print('\n'.join(ans))