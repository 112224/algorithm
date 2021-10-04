input = __import__('sys').stdin.readline

n = int(input())
word = list(input().rstrip())
ans = word[0::n]
print(''.join(ans))