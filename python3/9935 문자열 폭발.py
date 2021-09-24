input = __import__('sys').stdin.readline

ori = list(input().rstrip())
boom = list(input().rstrip())
n = len(boom)
ans = []
for ele in ori:
    ans.append(ele)
    while len(ans) >= n and ans[-n:] == boom:
        for _ in range(n):
            ans.pop()
ans = ans if ans else list('FRULA')
print(''.join(ans))