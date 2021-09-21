input = __import__('sys').stdin.readline

n = int(input())
m = int(input())
ary = input().rstrip()

i = 0
matched = 0

ans = 0
while i < m-2:
    if ary[i] == ary[i+2] == 'I' and ary[i+1] == 'O':
        matched += 1
        if matched == n:
            ans += 1
            matched -= 1
        i += 1
    else:
        matched = 0
    i += 1
print(ans)

