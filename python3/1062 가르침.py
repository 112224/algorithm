import sys
input = sys.stdin.readline

n, k = map(int, input().split())
word = []
requ = list('antic')
requ = [ord(x)-ord('a') for x in requ]

for _ in range(n):
    tmp = list(input().strip())
    ret = 0
    for ele in tmp:
        ret |= (1<<(ord(ele)-ord('a')))
    word.append(ret)

def solve(idx, bit, k):
    if idx == 26 or k <= 0:
        ret = 0
        for ele in word:
            if ele & ((1<<26)-1 - bit) == 0:
                ret += 1
        return ret
    ret = 0
    if idx not in requ:
        ret = solve(idx+1,bit,k)
    ret = max(ret, solve(idx+1, bit | (1<<idx), k-1))
    return ret

print(solve(0,0,k))
